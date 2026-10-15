"""Run summaries: a short summary in ASD-STE100 and one to four tags for a finished run, by a small model.

It reads what the run page shows (the request, the answer, the steps in one line each, the files
changed) and asks Claude Haiku for JSON {"summary": ..., "tags": [...]}. The call runs from a
folder outside the repository with its own short system prompt, so it loads no project settings
and its own transcript never shows up as a run. Its cost is about one cent.
"""
import asyncio
import json
import os
import re
import tempfile
import threading

try:
    from claude_agent_sdk import AssistantMessage, ClaudeAgentOptions, ResultMessage, TextBlock, query
    SDK_ERROR = None
except ImportError as e:
    SDK_ERROR = f"claude-agent-sdk is not installed ({e})"

TAGS = ("question", "change", "fix", "docs", "ui", "server", "setup", "sync", "plan", "research", "delete", "failed", "waiting")

SYSTEM = """You write the summary of one Claude Code run for its owner. Write in ASD-STE100 (Simplified Technical English):
short sentences (at most 20 words), one statement in each sentence, active voice, simple present or past tense, no -ing forms,
the same word for the same thing. File paths, commands and names stay as they are.
Write 4 to 10 sentences: what the owner asked, what the agent did, what changed, the checks and their results, what is still open.
Then choose 1 to 4 tags. Use tags from this list when they fit: """ + ", ".join(TAGS) + """.
Make a new tag (one short lowercase word) only when no tag in the list fits.
Answer with JSON only: {"summary": "...", "tags": ["..."]}"""


def brief(run, max_steps=160):
    """The text the model reads: a run from runs.Transcripts.get, with the record's answer when there is one."""
    lines = [f"Title: {run.get('title', '')}", f"Started in: {run.get('cwd') or ''} on branch {run.get('branch') or ''}", "",
             "The owner's first request:", (run.get("request_full") or run.get("request") or "")[:6000], ""]
    steps = [s for s in walk(run.get("steps") or []) if s["kind"] not in ("text",)]
    lines.append(f"Steps ({len(steps)}):")
    for s in steps[:max_steps]:
        lines.append(f"- {s['kind']}: {s.get('summary', '')[:160]}" + (" [error]" if s.get("error") else ""))
    if len(steps) > max_steps:
        lines.append(f"- … {len(steps) - max_steps} more steps")
    t = run.get("totals") or {}
    lines += ["", "Files changed: " + ", ".join((run.get("changed") or t.get("edited") or [])[:60]),
              "Commits: " + "; ".join(c["subject"] for c in (run.get("commits") or [])[:10]), "",
              "The last answer:", (run.get("answer_full") or run.get("answer") or "")[-6000:]]
    return "\n".join(lines)


def walk(steps):
    for s in steps:
        yield s
        yield from walk(s.get("steps") or [])


def parse(text):
    m = re.search(r"\{.*\}", text or "", re.S)
    if not m:
        raise ValueError("no JSON in the answer")
    got = json.loads(m.group(0))
    tags = [re.sub(r"[^a-z0-9-]", "", str(t).lower())[:20] for t in got.get("tags") or []]
    return {"summary": str(got.get("summary") or "").strip(), "tags": [t for t in tags if t][:4]}


class Summarizer:
    def __init__(self, cfg=None):
        cfg = cfg or {}
        self.model = cfg.get("summary_model", "haiku")
        self.workdir = os.path.join(tempfile.gettempdir(), "project-ide-summaries")
        self.lock = threading.Lock()     # one summary at a time

    @property
    def available(self):
        return SDK_ERROR is None

    def write(self, run):
        """{summary, tags, cost_usd} for a run, or raises RuntimeError."""
        if SDK_ERROR:
            raise RuntimeError(SDK_ERROR)
        os.makedirs(self.workdir, exist_ok=True)
        with self.lock:
            return asyncio.run(self._ask(brief(run)))

    async def _ask(self, text):
        opts = ClaudeAgentOptions(cwd=self.workdir, model=self.model, system_prompt=SYSTEM, max_turns=1,
                                  allowed_tools=[], setting_sources=[], permission_mode="default")
        out, cost = [], None
        async for msg in query(prompt=text, options=opts):
            if isinstance(msg, AssistantMessage):
                out += [b.text for b in msg.content if isinstance(b, TextBlock)]
            elif isinstance(msg, ResultMessage):
                cost = msg.total_cost_usd
                if msg.is_error:
                    raise RuntimeError(f"The summary failed: {msg.subtype}")
        try:
            got = parse("\n".join(out))
        except (ValueError, json.JSONDecodeError) as e:
            raise RuntimeError(f"The summary was not readable: {e}")
        return {**got, "cost_usd": cost}
