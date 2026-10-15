"""Runs: every Claude Code session in this repository, read from Claude Code's own transcripts.

Claude Code writes each session, from a terminal or from the page, to
$CLAUDE_CONFIG_DIR/projects/<folder>/<session>.jsonl: every message, every tool call with its input and
output, the token use of every step, and each subagent's own transcript in <session>/subagents/.
This module turns them into runs for the page: a short row for the list, and the full run with its
steps for the run page. It copies nothing and writes nothing; the run records (status, notes,
versions, summary, tags) are kept by the server and merged in by the caller.
"""
import json
import os
import re
import subprocess
import threading
import time

READ = {"Read", "Glob", "Grep", "LS", "NotebookRead"}
EDIT = {"Edit", "Write", "MultiEdit", "NotebookEdit"}
WEB = {"WebFetch", "WebSearch"}
CHECKS = re.compile(r"(build_map\.py|check_tree\.py|check_page\.js|rebuild\.py)(\s|$)|\bpytest\b|-m unittest|npm (run )?test|node --test|\./start\.sh")
PLANS = re.compile(r"apps/project-IDE/data/plans/[^/]+(?<!\.index)(?<!\.questions)\.md$")
SAFE_ID = re.compile(r"^[0-9a-f-]{8,64}$")


def kind_of(tool):
    if tool in READ:
        return "read"
    if tool in EDIT:
        return "edit"
    if tool == "Bash":
        return "command"
    if tool == "Skill":
        return "skill"
    if tool in ("Agent", "Task"):
        return "subagent"
    if tool.startswith("mcp__"):
        return "mcp"
    if tool in WEB:
        return "web"
    if tool == "Workflow":
        return "workflow"
    return "tool"


def text_of(content):
    """The text of a message or tool result: a string, or a list of blocks."""
    if isinstance(content, str):
        return content
    out = []
    for b in content or []:
        if isinstance(b, dict):
            if b.get("type") == "text":
                out.append(b.get("text", ""))
            elif b.get("type") == "image":
                out.append("[image]")
            elif b.get("type") == "tool_reference":
                out.append(f"[tool {b.get('tool_name', '')}]")
    return "\n".join(out)


def clip(text, n):
    text = text if isinstance(text, str) else json.dumps(text, ensure_ascii=False, indent=1)
    return (text, False) if len(text) <= n else (text[:n], True)


def one_line(text, n=140):
    text = " ".join(str(text).split())
    return text if len(text) <= n else text[:n - 1] + "…"


def summary_of(tool, inp):
    """A one-line description of a tool call."""
    inp = inp or {}
    if tool == "Bash":
        return inp.get("description") or one_line(inp.get("command", ""))
    if tool in ("Agent", "Task"):
        return f"{inp.get('subagent_type') or 'agent'}: {inp.get('description', '')}"
    if tool == "Skill":
        return f"{inp.get('skill', '')} {inp.get('args', '') or ''}".strip()
    for k in ("file_path", "notebook_path", "path", "pattern", "url", "query", "description", "skill"):
        if inp.get(k):
            return f"{inp[k]}" + (f"  ({inp['pattern']})" if k == "path" and inp.get("pattern") else "")
    return one_line(json.dumps(inp, ensure_ascii=False))


def context_of(usage):
    """The tokens the model had in view for one step, and what it wrote."""
    u = usage or {}
    return (u.get("input_tokens") or 0) + (u.get("cache_read_input_tokens") or 0) + (u.get("cache_creation_input_tokens") or 0), u.get("output_tokens") or 0


class Transcripts:
    def __init__(self, repo, cfg=None):
        cfg = cfg or {}
        self.repo = os.path.realpath(repo)
        base = cfg.get("claude_config_dir") or os.environ.get("CLAUDE_CONFIG_DIR") or os.path.expanduser("~/.claude")
        self.projects = os.path.join(os.path.expanduser(base), "projects")
        self.live_seconds = cfg.get("live_seconds", 90)
        self.since = cfg.get("since") or ""    # sessions that started before this time are not listed
        self.max_text = cfg.get("max_text", 1200)
        self._rows = {}      # path -> (mtime, size, row)
        self.lock = threading.Lock()

    # ---------- finding the sessions of this repository ----------
    def folders(self):
        """Transcript folders whose sessions started inside this repository."""
        slug = re.sub(r"[^A-Za-z0-9]", "-", self.repo)
        out = []
        try:
            names = os.listdir(self.projects)
        except OSError:
            return out
        for name in names:
            if name == slug or name.startswith(slug + "-"):
                d = os.path.join(self.projects, name)
                cwd = self._first_cwd(d)
                if cwd is None or cwd == self.repo or cwd.startswith(self.repo + os.sep):
                    out.append(d)
        return out

    @staticmethod
    def _first_cwd(folder):
        for f in sorted(os.listdir(folder)):
            if f.endswith(".jsonl"):
                try:
                    with open(os.path.join(folder, f), encoding="utf-8") as fh:
                        for i, line in enumerate(fh):
                            if '"cwd"' in line:
                                return os.path.realpath(json.loads(line).get("cwd") or "")
                            if i > 200:
                                break
                except (OSError, ValueError):
                    pass
        return None

    def path_of(self, session):
        if not SAFE_ID.match(session or ""):
            return None
        for d in self.folders():
            p = os.path.join(d, session + ".jsonl")
            if os.path.isfile(p):
                return p
        return None

    # ---------- the list ----------
    def list(self, offset=0, limit=10):
        files = []
        for d in self.folders():
            for f in os.listdir(d):
                if f.endswith(".jsonl"):
                    p = os.path.join(d, f)
                    try:
                        files.append((os.path.getmtime(p), p))
                    except OSError:
                        pass
        files.sort(reverse=True)
        if self.since:   # a session's start is in its file; files changed before the cut-off cannot have started after it
            files = [(m, p) for m, p in files if time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(m)) >= self.since[:19]]
            files = [(m, p) for m, p in files if (self.row(p).get("start") or "") >= self.since]
        return [self.row(p) for _, p in files[offset:offset + limit]], len(files)

    def row(self, path):
        """The short form of one session for the list, cached until its file changes."""
        st = os.stat(path)
        with self.lock:
            hit = self._rows.get(path)
            if hit and hit[0] == st.st_mtime and hit[1] == st.st_size:
                row = dict(hit[2])
                row["live"] = time.time() - st.st_mtime < self.live_seconds
                return row
        title = first = last_text = branch = cwd = model = start = end = entry = None
        steps = tokens_out = context = 0
        for o in self._read(path):
            t = o.get("type")
            ts = o.get("timestamp")
            if ts:
                start = start or ts
                end = ts
            if t == "ai-title":
                title = o.get("aiTitle") or title
            elif t == "user" and not o.get("isMeta") and isinstance(o.get("message", {}).get("content"), str):
                if o.get("promptSource") != "system" and first is None:
                    first = o["message"]["content"]
                cwd, branch, entry = o.get("cwd") or cwd, o.get("gitBranch") or branch, o.get("entrypoint") or entry
            elif t == "assistant":
                m = o.get("message") or {}
                model = m.get("model") or model
                c, w = context_of(m.get("usage"))
                context, tokens_out = max(context, c), tokens_out + w
                for b in m.get("content") or []:
                    if isinstance(b, dict) and b.get("type") == "tool_use":
                        steps += 1
                    elif isinstance(b, dict) and b.get("type") == "text" and b.get("text", "").strip():
                        last_text = b["text"]
        sid = os.path.basename(path)[:-6]
        row = {"id": sid, "title": title or one_line(clean_prompt(first or ""), 90) or sid[:8],
               "request": one_line(clean_prompt(first or ""), 240), "answer": one_line(last_text or "", 240),
               "origin": "page" if entry and entry.startswith("sdk") else "terminal",
               "cwd": os.path.relpath(cwd, self.repo) if cwd and cwd.startswith(self.repo) else cwd,
               "branch": branch, "model": model, "start": start, "end": end, "steps": steps,
               "max_context": context, "output_tokens": tokens_out}
        with self.lock:
            self._rows[path] = (st.st_mtime, st.st_size, row)
        return {**row, "live": time.time() - st.st_mtime < self.live_seconds}

    @staticmethod
    def _read(path):
        try:
            with open(path, encoding="utf-8") as f:
                for line in f:
                    try:
                        yield json.loads(line)
                    except ValueError:
                        continue
        except OSError:
            return

    # ---------- one run in full ----------
    def get(self, session):
        path = self.path_of(session)
        if not path:
            return None
        run = self.row(path)
        steps, totals = self._steps(path, os.path.join(os.path.dirname(path), session, "subagents"), "")
        run.update(steps=steps, totals=totals)
        run["checks"] = [s for s in walk(steps) if s["kind"] == "command" and CHECKS.search(s.get("command") or "")]
        run["plans"] = sorted({s["file"] for s in walk(steps) if s["kind"] == "edit" and PLANS.search(s.get("file") or "")})
        run["commits"] = self.commits(run.get("start"), run.get("end"), run.get("live"))
        return run

    def step(self, session, sid):
        """One step with its full input and output."""
        path = self.path_of(session)
        if not path:
            return None
        steps, _ = self._steps(path, os.path.join(os.path.dirname(path), session, "subagents"), "", full=True)
        for s in walk(steps):
            if s["id"] == sid:
                return s
        return None

    def _steps(self, path, sub_dir, prefix, full=False):
        n = self.max_text * 1000 if full else self.max_text
        steps, by_tool = [], {}
        totals = {"tools": {}, "read": [], "edited": [], "skills": {}, "subagents": [], "mcp": {}, "plugins": {}, "workflows": [], "web": []}
        read, edited = [], []
        for o in self._read(path):
            t = o.get("type")
            if o.get("isSidechain") and prefix == "":
                continue
            ts = o.get("timestamp")
            if t == "user":
                m = o.get("message") or {}
                c = m.get("content")
                if isinstance(c, str) and not o.get("isMeta"):
                    body, more = clip(clean_prompt(c), n)
                    steps.append({"id": f"{prefix}{len(steps) + 1}", "kind": "prompt" if o.get("promptSource") != "system" else "notification",
                                  "at": ts, "summary": one_line(clean_prompt(c)), "input": body, "more": more})
                    continue
                for b in c if isinstance(c, list) else []:
                    if isinstance(b, dict) and b.get("type") == "tool_result" and b.get("tool_use_id") in by_tool:
                        s = by_tool[b["tool_use_id"]]
                        res = o.get("toolUseResult")
                        out = text_of(b.get("content"))
                        if isinstance(res, dict) and res.get("persistedOutputPath") and full:
                            out = self._persisted(res["persistedOutputPath"]) or out
                        s["output"], s["more"] = clip(out, n)
                        s["more"] = s["more"] or (isinstance(res, dict) and bool(res.get("persistedOutputPath")))
                        s["error"] = bool(b.get("is_error"))
                        s["ms"] = ms_between(s.get("at"), ts)
                        if s["kind"] == "subagent" and isinstance(res, dict) and res.get("agentId"):
                            s["agent_id"] = res["agentId"]
                            sp = os.path.join(sub_dir, f"agent-{res['agentId']}.jsonl")
                            if os.path.isfile(sp):
                                s["steps"], s["sub_totals"] = self._steps(sp, sub_dir, s["id"] + ".", full)
                                merge_totals(totals, s["sub_totals"])
            elif t == "assistant":
                m = o.get("message") or {}
                ctx, out_tokens = context_of(m.get("usage"))
                for b in m.get("content") or []:
                    if not isinstance(b, dict):
                        continue
                    if b.get("type") == "text" and b.get("text", "").strip():
                        prev = steps[-1] if steps else None
                        if prev and prev["kind"] == "text" and prev.get("msg") == m.get("id"):
                            prev["output"] += "\n" + b["text"]
                            continue
                        body, more = clip(b["text"], n)
                        steps.append({"id": f"{prefix}{len(steps) + 1}", "kind": "text", "at": ts, "msg": m.get("id"),
                                      "summary": one_line(b["text"]), "output": body, "more": more, "context": ctx, "out_tokens": out_tokens})
                    elif b.get("type") == "tool_use":
                        tool, inp = b.get("name", ""), b.get("input") or {}
                        k = kind_of(tool)
                        body, more = clip(inp, n)
                        s = {"id": f"{prefix}{len(steps) + 1}", "kind": k, "tool": tool, "at": ts, "summary": summary_of(tool, inp),
                             "input": body, "more": more, "context": ctx, "out_tokens": out_tokens}
                        if k == "command":
                            s["command"] = inp.get("command", "")
                        if k in ("read", "edit"):
                            s["file"] = self.rel(inp.get("file_path") or inp.get("notebook_path") or inp.get("path") or "")
                        steps.append(s)
                        by_tool[b.get("id")] = s
                        bump(totals["tools"], tool)
                        if k == "read" and s["file"] and tool == "Read":
                            read.append(s["file"])
                        elif k == "edit" and s["file"]:
                            edited.append(s["file"])
                        elif k == "skill":
                            name = inp.get("skill", "")
                            bump(totals["skills"], name)
                            if ":" in name:
                                bump(totals["plugins"], name.split(":")[0])
                        elif k == "subagent":
                            totals["subagents"].append({"type": inp.get("subagent_type") or "general-purpose", "description": inp.get("description", ""), "step": s["id"]})
                        elif k == "mcp":
                            server = tool.split("__")[1] if tool.count("__") >= 2 else tool
                            bump(totals["mcp"], server)
                            if server.startswith("plugin_"):
                                bump(totals["plugins"], server.split("_")[1])
                        elif k == "workflow":
                            totals["workflows"].append(inp.get("name") or "script")
                        elif k == "web":
                            totals["web"].append(inp.get("url") or inp.get("query") or "")
        totals["read"] = sorted(set(totals["read"]) | set(read))
        totals["edited"] = sorted(set(totals["edited"]) | set(edited))
        return steps, totals

    def rel(self, p):
        p = str(p)
        if p.startswith(self.repo + os.sep):
            return os.path.relpath(p, self.repo)
        return p

    def _persisted(self, p):
        p = os.path.realpath(p)
        if not p.startswith(os.path.realpath(self.projects) + os.sep):
            return None
        try:
            with open(p, encoding="utf-8", errors="replace") as f:
                return f.read(self.max_text * 1000)
        except OSError:
            return None

    def commits(self, start, end, live):
        """The commits made in the repository while the session ran."""
        if not start:
            return []
        args = ["git", "-C", self.repo, "log", "--all", "--format=%h%x09%an%x09%aI%x09%s", f"--since={start}"]
        if end and not live:
            args.append(f"--until={end}")
        try:
            out = subprocess.run(args, capture_output=True, text=True, timeout=20).stdout
        except Exception:
            return []
        rows = []
        for line in out.splitlines()[:50]:
            h, who, at, subject = (line.split("\t") + ["", "", "", ""])[:4]
            rows.append({"commit": h, "author": who, "at": at, "subject": subject})
        return rows


def clean_prompt(text):
    """The owner's words, without the tags the terminal wraps around pasted text and commands."""
    text = re.sub(r"<pasted_content[^>]*>|</pasted_content[^>]*>", "", text or "")
    text = re.sub(r"<command-(name|message|args)>(.*?)</command-\1>", r"\2 ", text, flags=re.S)
    text = re.sub(r"<local-command-stdout>.*?</local-command-stdout>", "", text, flags=re.S)
    return text.strip()


def walk(steps):
    for s in steps:
        yield s
        yield from walk(s.get("steps") or [])


def bump(d, k):
    d[k] = d.get(k, 0) + 1


def merge_totals(into, add):
    for k in ("tools", "skills", "mcp", "plugins"):
        for name, n in add.get(k, {}).items():
            into[k][name] = into[k].get(name, 0) + n
    for k in ("read", "edited"):
        into[k] = sorted(set(into[k]) | set(add.get(k, [])))
    for k in ("subagents", "workflows", "web"):
        into[k] = into[k] + add.get(k, [])


def ms_between(a, b):
    try:
        from datetime import datetime
        f = lambda s: datetime.fromisoformat(s.replace("Z", "+00:00"))
        return int((f(b) - f(a)).total_seconds() * 1000)
    except Exception:
        return None
