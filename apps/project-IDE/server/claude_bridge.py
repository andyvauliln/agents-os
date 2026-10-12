"""Runs the owner's requests from the File Tree page as Claude Code sessions.

One request is one run. Claude Code starts in the system folder (agents/system/),
so the system's CLAUDE.md, agents and skills in agents/system/.claude/ load as its
own (there is no CLAUDE.md at the top of the repository). A follow-up passes the
previous session id and continues the same conversation.

Every step Claude Code wants to take is checked first:
- anything that touches the keys folder is refused;
- when the owner pressed Delete on the page, deleting exactly that item (and its How it
  works file) goes ahead without a second click;
- a file outside the repository waits for the owner's click on the page;
- a tool or command that is not on the allow list in server.config.json waits for
  the owner's click too (push, delete, installs, network tools ...).

A run streams events to the page (text, steps, approval requests, the result with its
cost and time) and is logged as one JSON file in the project IDE agent's log folder.
"""
import asyncio
import hashlib
import json
import os
import shlex
import subprocess
import threading
import time
import uuid

try:
    from claude_agent_sdk import (AssistantMessage, ClaudeAgentOptions, ClaudeSDKClient, HookMatcher,
                                  PermissionResultAllow, PermissionResultDeny, ResultMessage, TextBlock,
                                  ToolUseBlock)
    SDK_ERROR = None
except ImportError as e:  # the page still works without it, only the request box is off
    SDK_ERROR = f"claude-agent-sdk is not installed ({e})"

FILE_ARGS = {"Read": "file_path", "Edit": "file_path", "Write": "file_path", "MultiEdit": "file_path",
             "NotebookEdit": "notebook_path", "Glob": "path", "Grep": "path", "LS": "path"}

APPEND = """You are working for the owner through the project IDE page on their own server.
Their request comes from the File Tree page, about one file or folder of the repository.
- Follow the system's CLAUDE.md: file the request with knowledge-intake like any owner message, and finish a round that changed files as it says (rebuild the page with ide-build, commit).
- Never push: pushing waits for the owner's click. Never open the keys folder.
- Answer in plain, short words, as you would in a chat with the owner. Say what you changed."""


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def short(text, n=160):
    text = " ".join(str(text).split())
    return text if len(text) <= n else text[:n - 1] + "…"


class Run:
    """One request: its events, its open approval questions and its result."""

    def __init__(self, rid, text, node, session, delete=None):
        self.id, self.text, self.node, self.session = rid, text, node, session
        self.delete = delete         # repo path the owner deleted with the Delete button, or None
        self.events, self.done, self.result = [], False, None
        self.cond = threading.Condition()
        self.pending = {}            # approval id -> asyncio future
        self.asked = []              # every step that waited for the owner, in full, for the log
        self.loop = self.client = None
        self.started = time.time()

    def emit(self, kind, **data):
        with self.cond:
            self.events.append({"n": len(self.events), "type": kind, "at": now(), **data})
            self.cond.notify_all()

    def wait(self, after, timeout=15.0):
        """Events after the first `after` ones, waiting up to `timeout` seconds for new ones."""
        with self.cond:
            if len(self.events) <= after and not self.done:
                self.cond.wait(timeout)
            return self.events[after:], self.done

    def finish(self):
        with self.cond:
            self.done = True
            self.cond.notify_all()


class Bridge:
    def __init__(self, cfg, repo, env=None):
        self.cfg = cfg.get("claude", {})
        self.repo = os.path.realpath(repo)
        self.cwd = os.path.join(self.repo, self.cfg.get("cwd", "agents/system"))
        self.env = env or {}
        self.log_dir = os.path.join(self.repo, cfg.get("log_dir", "agents/system/logs/subagents/project-ide-agent"))
        self.store_dir = cfg.get("store_dir", "apps/project-IDE/data/page-store")
        self.runs = {}

    @property
    def available(self):
        return SDK_ERROR is None

    # ---------- the page's side ----------
    def start(self, text, node, session=None, input_id=None, delete=None):
        if SDK_ERROR:
            raise RuntimeError(SDK_ERROR)
        rid = time.strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:6]
        run = Run(rid, text, node or {}, session, delete)
        self.runs[rid] = run
        threading.Thread(target=lambda: asyncio.run(self._run(run, input_id)), daemon=True).start()
        return run

    def answer(self, rid, aid, allow):
        run = self.runs.get(rid)
        fut = run and run.pending.pop(aid, None)
        if not fut:
            return False
        run.loop.call_soon_threadsafe(lambda: fut.done() or fut.set_result(bool(allow)))
        return True

    def stop(self, rid):
        run = self.runs.get(rid)
        if not run or run.done or not run.client:
            return False
        asyncio.run_coroutine_threadsafe(run.client.interrupt(), run.loop)
        return True

    # ---------- checks before every step ----------
    def _inside(self, path):
        p = os.path.realpath(path if os.path.isabs(path) else os.path.join(self.cwd, path))
        return p == self.repo or p.startswith(self.repo + os.sep)

    def delete_target(self, rel):
        """The repository path of an item deleted on the page, checked: inside the repository, not the top, never the keys folder."""
        rel = str(rel or "").strip().lstrip("/")
        rel = rel[len("agent-os/"):] if rel.startswith("agent-os/") else rel
        p = os.path.realpath(os.path.join(self.repo, rel))
        if not rel or any(b in rel for b in self.cfg.get("never", [".secrets"])) or not p.startswith(self.repo + os.sep) or "[" in rel:
            raise ValueError("This item cannot be deleted from the page.")
        return os.path.relpath(p, self.repo)

    def metadata_files(self, rel, node=None):
        """The metadata files that sit next to a deleted file: its How it works and Details files, named without
        the file's extension (the build gives the name as "fam"). A folder keeps its own inside, so none."""
        rel = rel.rstrip("/")
        node = node or {}
        if os.path.isdir(os.path.join(self.repo, rel)) or node.get("type") == "folder" or str(node.get("name") or "").endswith("/"):
            return []
        base, ext = os.path.splitext(os.path.basename(rel))
        fam = node.get("fam") or (base if base and ext else os.path.basename(rel))
        return [os.path.join(os.path.dirname(rel), fam + e) for e in (".index.md", ".meta.json")]

    def _only_deletes(self, cmd, rel, node=None):
        """True when the command is one rm or git rm of the deleted item or its metadata files, by absolute path."""
        if any(ch in cmd for ch in ";&|`$<>()\n"):
            return False
        try:
            words = shlex.split(cmd)
        except ValueError:
            return False
        if words[:2] == ["git", "rm"]:
            words = words[2:]
        elif words[:1] == ["rm"]:
            words = words[1:]
        else:
            return False
        flags = [w for w in words if w.startswith("-")]
        paths = [w for w in words if not w.startswith("-")]
        if not paths or any(f not in ("-r", "-R", "-f", "-rf", "-fr", "-q", "--quiet", "--cached", "--ignore-unmatch", "--") for f in flags):
            return False
        root = os.path.join(self.repo, rel).rstrip(os.sep)
        extra = [os.path.join(self.repo, m) for m in self.metadata_files(rel, node)]
        for w in paths:
            if not os.path.isabs(w):
                return False
            p = os.path.normpath(w)
            if not (p == root or p in extra or p.startswith(root + os.sep)):
                return False
        return True

    def check(self, tool, args, run=None):
        """None to let the permission rules decide, or (decision, reason) with decision deny, allow or ask."""
        key = FILE_ARGS.get(tool)
        target = str(args.get(key) or "") if key else str(args.get("command") or "") if tool == "Bash" else ""
        for bad in self.cfg.get("never", [".secrets"]):
            if bad in target:   # the path or the command, not the text being written: docs may name the keys folder
                return "deny", f"Nothing from the page may touch {bad}."
        if tool == "Bash" and run is not None and run.delete and self._only_deletes(str(args.get("command") or ""), run.delete, run.node):
            return "allow", "The owner deleted this with the Delete button on the page."
        if key and args.get(key) and not self._inside(args[key]):
            return "ask", "This is outside the repository."
        if tool == "Bash":
            cmd = args.get("command", "")
            for word in self.cfg.get("ask_owner", []):
                if word in cmd:
                    return "ask", f"'{word.strip()}' waits for the owner."
        return None

    def _options(self, run):
        async def guard(inp, tool_use_id, ctx):
            verdict = self.check(inp.get("tool_name", ""), inp.get("tool_input") or {}, run)
            if not verdict:
                return {}
            decision, why = verdict
            return {"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                           "permissionDecision": decision, "permissionDecisionReason": why}}

        async def ask_owner(tool, args, ctx):
            verdict = self.check(tool, args, run)
            if verdict and verdict[0] == "deny":
                return PermissionResultDeny(message=verdict[1])
            if verdict and verdict[0] == "allow":
                return PermissionResultAllow()
            aid = uuid.uuid4().hex[:8]
            fut = asyncio.get_running_loop().create_future()
            run.pending[aid] = fut
            what = args.get("command") or args.get(FILE_ARGS.get(tool, ""), "") or json.dumps(args)[:200]
            run.emit("approval", id=aid, tool=tool, summary=short(what), reason=(verdict or (None, ""))[1])
            try:
                allow = await asyncio.wait_for(fut, self.cfg.get("approval_timeout_s", 600))
            except asyncio.TimeoutError:
                allow = False
            run.pending.pop(aid, None)
            run.asked.append({"tool": tool, "what": str(what)[:2000], "reason": (verdict or (None, ""))[1], "allow": allow})
            run.emit("answered", id=aid, allow=allow, summary=short(f"{tool}: {what}"))
            if allow:
                return PermissionResultAllow()
            return PermissionResultDeny(message="The owner did not allow this step.")

        return ClaudeAgentOptions(
            cwd=self.cwd,
            add_dirs=[self.repo],
            setting_sources=["project", "local"],
            skills="all",
            system_prompt={"type": "preset", "preset": "claude_code", "append": APPEND},
            permission_mode="default",
            allowed_tools=self.cfg.get("allow", []),
            can_use_tool=ask_owner,
            hooks={"PreToolUse": [HookMatcher(matcher=None, hooks=[guard])]},
            model=self.cfg.get("model") or None,
            max_turns=self.cfg.get("max_turns") or None,
            max_budget_usd=self.cfg.get("max_budget_usd") or None,
            resume=run.session or None,
            env=dict(self.env),
        )

    def _prompt(self, run, input_id):
        n = run.node
        where = n.get("path", "the repository")
        label = f"{n.get('name', '')} [{n['num']}]" if n.get("num") else n.get("name", "")
        lines = [f"The owner wrote this on the File Tree page, on {where} ({label}):", "", run.text, ""]
        if run.delete:
            target = os.path.join(self.repo, run.delete)
            both = " ".join([target] + [os.path.join(self.repo, m) for m in self.metadata_files(run.delete, run.node)])
            lines += ["The owner pressed Delete on the page for this item and confirmed it. Follow \"Deleting an item\" in the ide-sync skill, "
                      "keeping in mind any note the owner wrote above.",
                      f"Delete the item itself with exactly this command, run on its own with nothing before or after it: "
                      f"`git rm -r -q --ignore-unmatch {both}`, and `rm -rf {both}` for what git does not track. "
                      "Those two go ahead without a second click; deleting anything else waits for the owner's click.", ""]
        if input_id:
            lines.append(f"The page saved it as {self.store_dir}/inputs/{input_id}.json. When you have filed it, "
                         "set that file's \"status\" to \"processed\" and \"processed_into\" to what it changed.")
        return "\n".join(lines)

    # ---------- the run ----------
    def _git(self, *args):
        try:
            out = subprocess.run(["git", "-c", "core.quotepath=off", *args], cwd=self.repo, capture_output=True, text=True, timeout=30)
            return out.stdout if out.returncode == 0 else None
        except Exception:
            return None

    def _hash(self, rel):
        try:
            with open(os.path.join(self.repo, rel), "rb") as f:
                return hashlib.sha1(f.read()).hexdigest()
        except OSError:
            return None

    def _dirty(self, head):
        """Files that differ from `head`: changed, deleted or new (committed or not)."""
        names = set((self._git("diff", "--name-only", head) or "").splitlines()) if head else set()
        names |= set((self._git("ls-files", "--others", "--exclude-standard") or "").splitlines())
        return {p for p in names if not any(b in p for b in self.cfg.get("never", [".secrets"]))}

    def _snapshot(self):
        """HEAD and the content of every file that already differed from it, to tell afterwards what a run changed."""
        head = (self._git("rev-parse", "HEAD") or "").strip() or None
        return head, {p: self._hash(p) for p in self._dirty(head)}

    def _changed(self, snap):
        """Files the run changed, also when Claude Code committed them."""
        head, before = snap
        now_dirty = self._dirty(head)
        return sorted({p for p in now_dirty if p not in before or self._hash(p) != before[p]} | (set(before) - now_dirty))

    async def _run(self, run, input_id):
        run.loop = asyncio.get_running_loop()
        snap = self._snapshot()
        run.emit("start", run=run.id, session=run.session)
        try:
            async with ClaudeSDKClient(options=self._options(run)) as client:
                run.client = client
                await client.query(self._prompt(run, input_id))
                async for msg in client.receive_response():
                    if isinstance(msg, AssistantMessage):
                        for b in msg.content:
                            if isinstance(b, TextBlock) and b.text.strip():
                                run.emit("text", text=b.text)
                            elif isinstance(b, ToolUseBlock):
                                arg = b.input.get("command") or b.input.get(FILE_ARGS.get(b.name, ""), "") or b.input.get("skill", "") or b.input.get("description", "")
                                run.emit("tool", tool=b.name, summary=short(f"{b.name} {arg}".strip()))
                    elif isinstance(msg, ResultMessage):
                        run.session = msg.session_id or run.session
                        run.result = {"text": msg.result or "", "cost_usd": msg.total_cost_usd, "duration_ms": msg.duration_ms,
                                      "turns": msg.num_turns, "session": run.session, "is_error": msg.is_error, "subtype": msg.subtype}
                        run.emit("result", **run.result)
        except Exception as e:
            run.emit("error", text=short(f"{type(e).__name__}: {e}", 400))
        changed = self._changed(snap)
        run.emit("end", changed=changed, seconds=round(time.time() - run.started, 1))
        run.finish()
        self._log(run, changed)

    def _log(self, run, changed):
        try:
            day = os.path.join(self.log_dir, run.id[:8])
            os.makedirs(day, exist_ok=True)
            rec = {"run": run.id, "at": now(), "node": run.node, "request": run.text, "delete": run.delete, "result": run.result, "changed": changed,
                   "steps": [e.get("summary") for e in run.events if e["type"] in ("tool", "answered")], "asked": run.asked}
            with open(os.path.join(day, run.id + ".json"), "w", encoding="utf-8") as f:
                json.dump(rec, f, indent=1, ensure_ascii=False)
        except OSError:
            pass
