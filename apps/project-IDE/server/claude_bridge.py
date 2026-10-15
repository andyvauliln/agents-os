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

import notes as notes_mod
from worktrees import GitError

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

    def __init__(self, rid, text, node, session, delete=None, root=None, cwd=None, notes=None, options=None, worktree=None):
        self.id, self.text, self.node, self.session = rid, text, node, session
        self.delete = delete         # repo path the owner deleted with the Delete button, or None
        self.root, self.cwd = root, cwd   # the checkout the run works in (its worktree, or the repository) and where Claude Code starts
        self.notes = notes or []     # the note records this run carries
        self.options = options or {}
        self.worktree = worktree     # {branch, path, base} when the run works on its own branch
        self.status, self.cancelled, self.record = "working", False, None
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
    def __init__(self, cfg, repo, env=None, jobs=None, worktrees=None, data_file=None, summarize=None):
        self.cfg = cfg.get("claude", {})
        self.repo = os.path.realpath(repo)
        self.cwd = os.path.join(self.repo, self.cfg.get("cwd", "agents/system"))
        self.env = env or {}
        self.jobs, self.worktrees, self.data_file = jobs, worktrees, data_file
        self.summarize = summarize   # called with a finished run record, in the background
        self.log_dir = os.path.join(self.repo, cfg.get("log_dir", "agents/system/logs/subagents/project-ide-agent"))
        self.store_dir = cfg.get("store_dir", "apps/project-IDE/data/page-store")
        self.runs = {}

    @property
    def available(self):
        return SDK_ERROR is None

    # ---------- the page's side ----------
    def start(self, text, node, session=None, input_id=None, delete=None, notes=None, options=None, kind=None):
        """One Claude Code run. With notes, it works on its own branch in a worktree (or the one its
        conversation already has), and its notes follow its status."""
        if SDK_ERROR:
            raise RuntimeError(SDK_ERROR)
        rid = time.strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:6]
        options = {**notes_mod.DEFAULT_OPTIONS, **(self.jobs.defaults if self.jobs else {}), **(options or {})}
        root, worktree, prev = self.repo, None, None
        if notes and self.worktrees and not delete:
            prev = self.jobs.run_by_session(session) if (session and self.jobs) else None
            if prev and prev.get("worktree") and self.worktrees.exists(prev["id"]) and prev.get("status") not in ("in main", "cancelled"):
                worktree, rid = prev["worktree"], prev["id"]      # a follow-up continues on the same branch
            else:
                session = None if prev else session               # its branch is gone: a new conversation
                worktree = self.worktrees.create(rid, notes[0]["text"])
            root = worktree["path"]
        cwd = os.path.join(root, self.cfg.get("cwd", "agents/system"))
        text = notes_mod.Jobs.combine(notes, options) if notes else text
        run = Run(rid, text, node or {}, session, delete, root=root, cwd=cwd, notes=notes, options=options, worktree=worktree)
        self.runs[rid] = run
        try:
            run.record = self._record(run, prev, kind or ("notes" if notes else "delete" if delete else "request"))
            threading.Thread(target=lambda: asyncio.run(self._run(run, input_id)), daemon=True).start()
        except Exception as e:   # nothing runs: leave no branch and no run that looks busy
            self.runs.pop(rid, None)
            if worktree and not prev:
                self.worktrees.remove(rid, worktree["branch"], delete_branch=True)
            if self.jobs and run.record is not None:
                run.record.update(status="failed", status_detail=f"The run did not start: {e}", worktree=None)
                self.jobs.save_run(run.record)
            raise
        return run

    # ---------- the run record and the notes' statuses ----------
    def versions(self, cwd=None):
        commit = (self._git("rev-parse", "--short", "HEAD") or "").strip() or None
        try:
            with open(self.data_file, encoding="utf-8") as f:
                dv = json.load(f).get("data_version")
        except (OSError, ValueError, TypeError):
            dv = None
        return {"at": now(), "commit": commit, "data_version": dv}

    def _record(self, run, prev, kind):
        if not self.jobs:
            return None
        rec = dict(prev or {})
        sent = self.versions()
        rec.update({"id": run.id, "origin": "page", "kind": kind, "session": run.session, "status": "working",
                    "request": run.text[:4000], "node": run.node, "notes": sorted(set((rec.get("notes") or []) + [n["id"] for n in run.notes])),
                    "options": run.options if run.notes else None, "worktree": run.worktree, "started": rec.get("started") or now(),
                    "sent": rec.get("sent") or sent, "ended": None, "error": None})
        self.jobs.save_run(rec)
        for n in run.notes:
            try:
                self.jobs.update_note(n["id"], {"status": "working", "run": run.id, "sent": sent, "error": None, "fixed": None}, force=True)
            except ValueError:   # deleted on the page meanwhile
                pass
        return rec

    def set_status(self, run, status, detail=None, **extra):
        run.status = status
        run.emit("status", status=status, detail=detail)
        if self.jobs and run.record is not None:
            run.record.update(status=status, status_detail=detail, **extra)
            self.jobs.save_run(run.record)
            self.jobs.set_run_notes(run.record, status, **({"error": detail} if status in ("failed", "need human") else {}))

    def merge(self, rid):
        """Merge a finished run's branch into main here, then mark it and its notes "in main"."""
        rec = self.jobs.run(rid) if self.jobs else None
        if not rec or not rec.get("worktree"):
            raise ValueError("This run has no branch to merge.")
        if rec.get("status") in ("working", "planning", "sending"):
            raise ValueError("The run is still working.")
        try:
            got = self.worktrees.merge(rid)
        except GitError as e:
            rec.update(status="need human", status_detail=str(e))
            self.jobs.save_run(rec)
            self.jobs.set_run_notes(rec, "need human", error=str(e))
            raise ValueError(str(e))
        fixed = self.versions()
        self.worktrees.remove(rid, rec["worktree"]["branch"], delete_branch=True)
        rec.update(status="in main", status_detail=None, merged=got, fixed=fixed)
        self.jobs.save_run(rec)
        self.jobs.set_run_notes(rec, "in main", fixed=fixed)
        return rec

    def discard(self, rid):
        """Remove a run's worktree and branch without merging."""
        rec = self.jobs.run(rid) if self.jobs else None
        if not rec or not rec.get("worktree"):
            raise ValueError("This run has no branch.")
        run = self.runs.get(rid)
        if run and not run.done:
            raise ValueError("Stop the run first.")
        self.worktrees.remove(rid, rec["worktree"]["branch"], delete_branch=True)
        rec.update(status="cancelled", status_detail="The branch was discarded.")
        self.jobs.save_run(rec)
        self.jobs.set_run_notes(rec, "cancelled")
        return rec

    def answer(self, rid, aid, allow):
        run = self.runs.get(rid)
        fut = run and run.pending.pop(aid, None)
        if not fut:
            return False
        run.loop.call_soon_threadsafe(lambda: fut.done() or fut.set_result(bool(allow)))
        return True

    def stop(self, rid):
        run = self.runs.get(rid)
        if not run or run.done:
            return False
        run.cancelled = True        # a run still connecting stops as soon as it is connected
        if run.client and run.loop:
            asyncio.run_coroutine_threadsafe(run.client.interrupt(), run.loop)
        return True

    # ---------- checks before every step ----------
    def _inside(self, path, run=None):
        root = os.path.realpath(run.root) if run is not None and run.root else self.repo
        p = os.path.realpath(path if os.path.isabs(path) else os.path.join(run.cwd if run is not None and run.cwd else self.cwd, path))
        return p == root or p.startswith(root + os.sep)

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
        if key and args.get(key) and not self._inside(args[key], run):
            return "ask", "This is outside the run's checkout." if run is not None and run.worktree else "This is outside the repository."
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
            was = run.status
            self.set_status(run, "need human", f"Allow or refuse: {tool} {short(what, 100)}")
            try:
                allow = await asyncio.wait_for(fut, self.cfg.get("approval_timeout_s", 600))
            except asyncio.TimeoutError:
                allow = False
            run.pending.pop(aid, None)
            run.asked.append({"tool": tool, "what": str(what)[:2000], "reason": (verdict or (None, ""))[1], "allow": allow})
            run.emit("answered", id=aid, allow=allow, summary=short(f"{tool}: {what}"))
            if not run.pending:
                self.set_status(run, was if was != "need human" else "working")
            if allow:
                return PermissionResultAllow()
            return PermissionResultDeny(message="The owner did not allow this step.")

        return ClaudeAgentOptions(
            cwd=run.cwd or self.cwd,
            add_dirs=[run.root or self.repo],
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
        label = n.get("name", "")
        lines = ([run.text, ""] if run.notes else [f"The owner wrote this on the File Tree page, on {where} ({label}):", "", run.text, ""])
        if run.worktree:
            lines.append(f"You work in a git worktree on the branch {run.worktree['branch']}, made from main for this run; "
                         f"its top is {run.root}. Paths in the docs are relative to that top. Commit there; the server merges into main.")
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
                if run.cancelled:
                    raise asyncio.CancelledError()
                await client.query(self._prompt(run, input_id))
                async for msg in client.receive_response():
                    sid = getattr(msg, "session_id", None)
                    if not sid and isinstance(getattr(msg, "data", None), dict):
                        sid = msg.data.get("session_id")
                    if sid and sid != run.session:
                        run.session = sid
                        if run.record is not None:
                            run.record["session"] = sid
                            self.jobs.save_run(run.record)
                    if isinstance(msg, AssistantMessage):
                        for b in msg.content:
                            if isinstance(b, TextBlock) and b.text.strip():
                                run.emit("text", text=b.text)
                            elif isinstance(b, ToolUseBlock):
                                arg = b.input.get("command") or b.input.get(FILE_ARGS.get(b.name, ""), "") or b.input.get("skill", "") or b.input.get("description", "")
                                run.emit("tool", tool=b.name, summary=short(f"{b.name} {arg}".strip()))
                                if b.name == "Skill" and b.input.get("skill") == "change-plan" and run.status == "working":
                                    self.set_status(run, "planning")
                                elif run.status == "planning" and b.name in ("Edit", "Write", "MultiEdit") and "/data/plans/" not in str(b.input.get("file_path", "")):
                                    self.set_status(run, "working")
                    elif isinstance(msg, ResultMessage):
                        run.session = msg.session_id or run.session
                        run.result = {"text": msg.result or "", "cost_usd": msg.total_cost_usd, "duration_ms": msg.duration_ms,
                                      "turns": msg.num_turns, "session": run.session, "is_error": msg.is_error, "subtype": msg.subtype}
                        run.emit("result", **run.result)
        except asyncio.CancelledError:
            pass
        except Exception as e:
            run.emit("error", text=short(f"{type(e).__name__}: {e}", 400))
            run.result = {**(run.result or {}), "is_error": True, "error": short(f"{type(e).__name__}: {e}", 400)}
        if run.worktree and self.worktrees:
            try:
                changed = self.worktrees.status(run.id).get("changed") or []
            except Exception:
                changed = []
        else:
            changed = self._changed(snap)
        self._finish(run, changed)
        run.emit("end", changed=changed, seconds=round(time.time() - run.started, 1), status=run.status)
        run.finish()
        self._log(run, changed)
        if self.summarize and run.record is not None:
            threading.Thread(target=self._summarize, args=(dict(run.record),), daemon=True).start()

    def _summarize(self, rec):
        try:
            self.summarize(rec)
        except Exception as e:
            import sys
            import traceback
            print(f"summary of run {rec.get('id')} failed: {type(e).__name__}: {e}", file=sys.stderr, flush=True)
            traceback.print_exc()
            got = self.jobs.run(rec["id"]) if self.jobs else None
            if got:
                got["summary_error"] = f"{type(e).__name__}: {e}"[:400]
                self.jobs.save_run(got)

    def _finish(self, run, changed):
        """The run's last status: from the owner's Stop, an error, or the STATUS line of its answer; then auto merge."""
        res = run.result or {}
        status, detail = notes_mod.read_status(res.get("text"))
        if run.cancelled:
            status, detail = "cancelled", "Stopped by the owner."
        elif res.get("is_error") or not res:
            status, detail = "failed", res.get("error") or res.get("subtype") or "The run ended without an answer."
        elif not status:
            status = "done"
        extra = {"result": {k: res.get(k) for k in ("cost_usd", "duration_ms", "turns", "subtype", "is_error")},
                 "answer": (res.get("text") or "")[-20000:], "changed": changed, "ended": now()}
        if run.worktree and self.worktrees:
            try:
                extra["branch_state"] = {k: v for k, v in self.worktrees.status(run.id).items() if k in ("head", "commits", "dirty")}
            except Exception:
                pass
        self.set_status(run, status, detail, **extra)
        if run.worktree and status == "done" and run.options.get("merge") == "auto":
            try:
                rec = self.merge(run.id)
                run.status = rec["status"]
                run.emit("status", status=rec["status"], detail=f"Merged into main at {rec['merged']['commit']}.")
            except ValueError as e:
                run.status = "need human"
                run.emit("status", status="need human", detail=str(e))

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
