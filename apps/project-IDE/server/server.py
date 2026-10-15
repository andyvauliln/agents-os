#!/usr/bin/env python3
"""The project IDE server: the File Tree page on the owner's own machine, with Claude Code behind it.

It serves the same page that is published on claude.ai, from the repository, and gives
it what claude.ai gives it there:
- a store for the owner's notes, edits and messages, kept as JSON files in the
  repository (store_dir), so nothing waits on claude.ai;
- write-through: an edit to a file's text goes straight into that file, and an edit to
  How it works into the item's How it works file (vision.md has vision.index.md);
- the request box: each request runs as a Claude Code session (claude_bridge.py) and
  streams its progress to the page;
- voice input for the request boxes: a recording goes to Groq and comes back as text
  (voice.py).

Start it from the top of the repository:
    python3 apps/project-IDE/server/server.py
and open http://127.0.0.1:8765/ through an SSH tunnel. Never open the port to the
internet: whoever reaches the page can make Claude Code change files and run commands.
Settings are in server.config.json next to this file. Standard library only, plus
claude-agent-sdk for the request box.
"""
import json
import os
import re
import sys
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, unquote, urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True   # no __pycache__ in the repository
import claude_bridge  # noqa: E402
import notes  # noqa: E402
import run_summary  # noqa: E402
import runs  # noqa: E402
import voice  # noqa: E402
import worktrees  # noqa: E402

CONFIG = os.environ.get("IDE_CONFIG", os.path.join(HERE, "server.config.json"))
COLLECTIONS = {"nodes", "changes", "inputs"}       # what the page keeps (same as on claude.ai)
SAFE_ID = re.compile(r"^[A-Za-z0-9_.:@+~-]{1,600}$")   # a nodes document is keyed by its item's path with "/" and other signs as ~XX


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def load_config():
    cfg = json.load(open(CONFIG, encoding="utf-8"))
    repo = os.path.realpath(os.path.join(HERE, cfg.get("repo", "../../..")))
    return cfg, repo


def load_secrets(cfg, repo):
    """Only the key names the config lists, read from the keys file on this machine. Values are never logged."""
    s = cfg.get("secrets") or {}
    path, names, env = os.path.join(repo, s.get("file", ".secrets/test/.env")), s.get("keys", []), {}
    if names and os.path.isfile(path):
        for line in open(path, encoding="utf-8"):
            k, sep, v = line.strip().partition("=")
            if sep and k.strip() in names:
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


class Store:
    """The page's store as files: <store_dir>/<collection>/<id>.json, one document per file."""

    def __init__(self, root):
        self.root, self.lock = root, threading.Lock()

    def _path(self, coll, doc_id):
        if coll not in COLLECTIONS or not SAFE_ID.match(doc_id):
            raise ValueError("bad collection or id")
        return os.path.join(self.root, coll, doc_id + ".json")

    def list(self, coll):
        if coll not in COLLECTIONS:
            raise ValueError("bad collection")
        d, out = os.path.join(self.root, coll), []
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.endswith(".json"):
                    try:
                        out.append({"id": f[:-5], "data": json.load(open(os.path.join(d, f), encoding="utf-8"))})
                    except (OSError, ValueError):
                        pass
        return out

    def get(self, coll, doc_id):
        p = self._path(coll, doc_id)
        return json.load(open(p, encoding="utf-8")) if os.path.isfile(p) else None

    def set(self, coll, doc_id, data):
        p = self._path(coll, doc_id)
        with self.lock:
            os.makedirs(os.path.dirname(p), exist_ok=True)
            tmp = p + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=1, ensure_ascii=False)
            os.replace(tmp, p)
        return data

    def update(self, coll, doc_id, patch):
        with self.lock:
            cur = self.get(coll, doc_id) or {}
        cur.update(patch)
        return self.set(coll, doc_id, cur)


class WriteThrough:
    """Writes the owner's page edits of a file's text or its How it works into the repository."""

    def __init__(self, repo, data_file, never):
        self.repo, self.data_file, self.never = repo, data_file, never
        self._nodes, self._mtime = {}, None

    def nodes(self):
        try:
            m = os.path.getmtime(self.data_file)
        except OSError:
            return {}
        if m != self._mtime:
            data = json.load(open(self.data_file, encoding="utf-8"))
            self._nodes, self._mtime = {n["id"]: n for n in data.get("nodes", [])}, m
        return self._nodes

    @staticmethod
    def _segs(node):
        segs = [s for s in (node.get("path") or "agent-os/").rstrip("/").split("/") if s]
        return [re.sub(r",\s*", "+", s.replace("|", "-")) for s in segs]

    def _safe(self, rel):
        p = os.path.realpath(os.path.join(self.repo, rel))
        inside = p.startswith(self.repo + os.sep)
        return p if inside and not any(b in rel for b in self.never) else None

    def file_of(self, node):
        if node.get("src_file"):             # the file the page showed, by its path in the repository
            return self._safe(node["src_file"])
        segs = self._segs(node)[1:]          # drop the root name "agent-os"
        if node.get("type") != "file" or not segs or any("[" in s for s in segs):
            return None
        return self._safe("/".join(segs))

    @staticmethod
    def family(node, last):
        """The name an item's metadata files share: a file's name without its extension, a folder's own name.
        The build sets it on each item ("fam"); there a file whose name would clash keeps its extension."""
        if node.get("fam"):
            return node["fam"]
        if node.get("type") == "folder":
            return last
        base, ext = os.path.splitext(last)
        return base if base and ext else last

    def metadata_of(self, node, ending):
        """An item's metadata file (ending ".index.md" or ".meta.json"): next to a file, inside a folder."""
        segs = self._segs(node)
        where = segs[1:] if node.get("type") == "folder" else segs[1:-1]
        return self._safe("/".join(where + [self.family(node, segs[-1]) + ending]))

    def index_of(self, node):
        if node.get("how_file"):             # the build names it: x.index.md beside a file, f/f.index.md inside a folder
            return self._safe(node["how_file"])
        return self.metadata_of(node, ".index.md")

    def apply(self, doc_id, doc, before=None):
        """Writes what this save changed. A field the page saved before is not written again: the same
        document is saved again for a comment or a mark, and that must not undo what Claude Code wrote since.
        The document id is the item's id (its path) with "/" and other signs written as ~XX."""
        node_id = unquote(doc_id.replace("~", "%"))
        n, fields, done = self.nodes().get(node_id), (doc or {}).get("fields") or {}, []
        old = (before or {}).get("fields") or {}
        if not n:
            return done
        text = fields.get("content")
        cut = isinstance(text, str) and "…(cut for the page" in text   # never write back a text the page only showed in part
        p = self.file_of(n) if isinstance(text, str) and not cut and text != old.get("content") else None
        if p and (not os.path.isfile(p) or open(p, encoding="utf-8").read() != text):
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8") as f:
                f.write(text)
            done.append(os.path.relpath(p, self.repo))
        how = fields.get("how_md")
        p = self.index_of(n) if isinstance(how, str) and how.strip() and how != old.get("how_md") else None
        if p:
            meta = {"about": n.get("path")}
            if os.path.isfile(p):
                m = re.match(r"^---\n(.*?)\n---[ \t]*\n?", open(p, encoding="utf-8").read(), re.S)
                for line in (m.group(1).split("\n") if m else []):
                    k, _, v = line.partition(":")
                    if k.strip() and k.strip() != "node":   # items have no node ids any more: the path is the id
                        meta[k.strip()] = v.strip()
            meta.update({"written": now(), "by": "owner"})
            body = "---\n" + "".join(f"{k}: {v}\n" for k, v in meta.items() if v) + "---\n" + how.strip() + "\n"
            if not os.path.isfile(p) or open(p, encoding="utf-8").read().split("---\n", 2)[-1].strip() != how.strip():
                os.makedirs(os.path.dirname(p), exist_ok=True)
                with open(p, "w", encoding="utf-8") as f:
                    f.write(body)
                done.append(os.path.relpath(p, self.repo))
        return done


class App:
    def __init__(self):
        self.cfg, self.repo = load_config()
        self.page_dir = os.path.join(self.repo, self.cfg.get("page_dir", "apps/project-IDE/current-ui"))
        self.page = self.cfg.get("page", "file-tree-explorer.html")
        self.data = self.cfg.get("data", "file-tree.data.json")
        self.store = Store(os.path.join(self.repo, self.cfg.get("store_dir", "apps/project-IDE/data/page-store")))
        never = self.cfg.get("claude", {}).get("never", [".secrets"])
        self.write = WriteThrough(self.repo, os.path.join(self.page_dir, self.data), never) if self.cfg.get("write_through", True) else None
        secrets = load_secrets(self.cfg, self.repo)
        self.voice = voice.Voice(self.cfg, secrets)
        # Claude Code gets only its own keys, never the voice key
        vkey = self.voice.cfg["key"]
        log_dir = os.path.join(self.repo, self.cfg.get("log_dir", "agents/system/logs/subagents/project-ide-agent"))
        self.jobs = notes.Jobs(self.store.root, log_dir, self.cfg)
        self.worktrees = worktrees.Worktrees(self.repo, self.cfg.get("worktrees"))
        self.transcripts = runs.Transcripts(self.repo, self.cfg.get("runs"))
        self.summarizer = run_summary.Summarizer(self.cfg.get("runs"))
        self.bridge = claude_bridge.Bridge(self.cfg, self.repo, {k: v for k, v in secrets.items() if k != vkey}, jobs=self.jobs,
                                           worktrees=self.worktrees, data_file=os.path.join(self.page_dir, self.data), summarize=self.summarize)
        self.jobs.recover(set())
        self.worktrees.git("worktree", "prune", check=False)
        self.summary_queue, self.summary_busy, self.summary_lock = [], set(), threading.Lock()

    # ---------- notes and runs ----------
    def send(self, ids, options=None, session=None, node=None):
        """Send notes as one run. Notes still transcribing wait and go out by themselves."""
        waiting = [i for i in ids if (self.jobs.note(i) or {}).get("status") in ("transcribing", "queued")]
        for i in waiting:
            self.jobs.update_note(i, {"status": "queued", "send_after_transcript": True, "options": options or {}}, force=True)
        ready = self.jobs.sendable([i for i in ids if i not in waiting])
        if not ready:
            if waiting:
                return {"queued": waiting}
            raise ValueError("No note to send.")
        for n in ready:
            self.jobs.update_note(n["id"], {"status": "sending"}, force=True)
        first = (ready[0].get("context") or {})
        node = node or {"node_id": first.get("node_id"), "path": first.get("path"), "name": first.get("name")}
        try:
            run = self.bridge.start(None, node, session, notes=ready, options=options)
        except Exception as e:
            for n in ready:
                try:
                    self.jobs.update_note(n["id"], {"status": "failed", "error": str(e)}, force=True)
                except ValueError:
                    pass
            raise
        return {"run": run.id, "queued": waiting}

    def transcribe(self, nid, audio, ctype):
        """Turn a note's recording into its text, in the background; send it when it was queued."""
        def work():
            try:
                got = self.voice.transcribe(audio, ctype)
                text = (got.get("text") or "").strip()
                n = self.jobs.note(nid)
                if not n or n["status"] == "cancelled":
                    return
                if not text:
                    self.jobs.update_note(nid, {"status": "failed", "error": "Nothing was heard in the recording."}, force=True)
                    return
                both = ((n.get("text") or "").rstrip() + " " + text).strip()
                queued = n["status"] == "queued" or n.get("send_after_transcript")
                self.jobs.update_note(nid, {"text": both, "status": "ready", "error": None, "model": got.get("model")}, force=True)
                if queued and (self.jobs.note(nid) or {}).get("status") == "ready":   # not cancelled or deleted meanwhile
                    self.send([nid], n.get("options"), None)
            except Exception as e:
                try:
                    self.jobs.update_note(nid, {"status": "failed", "error": str(e)}, force=True)
                except ValueError:
                    pass
        threading.Thread(target=work, daemon=True).start()

    def run_view(self, rid):
        """One run for its page: the record and the transcript together, with the branch and git state."""
        rec = self.jobs.run(rid) if notes.SAFE.match(rid or "") else None
        rec = rec or self.jobs.run_by_session(rid)
        session = (rec or {}).get("session") or (None if rec else rid)
        t = self.transcripts.get(session) if session else None
        if not rec and not t:
            return None
        live = self.bridge.runs.get((rec or {}).get("id"))
        out = {**(t or {}), **{k: v for k, v in (rec or {}).items() if v is not None}}
        out["id"] = (rec or {}).get("id") or session
        out["session"] = session
        out["record"] = bool(rec)
        out["status"] = (rec or {}).get("status") or ("working" if (t or {}).get("live") else "done")
        out["active"] = bool(live and not live.done)
        if t:
            out["request_full"] = next((s.get("input") for s in t["steps"] if s["kind"] == "prompt"), "")
            out["answer_full"] = next((s.get("output") for s in reversed(t["steps"]) if s["kind"] == "text"), "")
        if (rec or {}).get("worktree") and self.worktrees.exists(rec["id"]):
            out["branch_now"] = self.worktrees.status(rec["id"])
        out["git"] = {"branch": (self.worktrees.git("rev-parse", "--abbrev-ref", "HEAD", check=False) or "").strip(),
                      "head": (self.worktrees.git("rev-parse", "--short", "HEAD", check=False) or "").strip(),
                      "status": self.worktrees.git("status", "--short", check=False).splitlines()[:200]}
        out["notes_full"] = [n for n in (self.jobs.note(i) for i in (rec or {}).get("notes") or []) if n]
        return out

    def summarize(self, rec_or_session):
        """Write the summary and tags of a run into its record (a terminal run gets one now)."""
        rec = rec_or_session if isinstance(rec_or_session, dict) else (self.jobs.run_by_session(rec_or_session) or {})
        session = rec.get("session") or (rec_or_session if isinstance(rec_or_session, str) else None)
        view = self.run_view(rec.get("id") or session)
        if not view:
            raise ValueError("no such run")
        got = self.summarizer.write(view)
        rec = self.jobs.run(view["id"]) if notes.SAFE.match(view["id"]) else None
        rec = rec or self.jobs.run_by_session(session) or {"id": session, "session": session, "origin": "terminal"}
        rec.update(summary=got["summary"], tags=got["tags"], summary_cost_usd=got.get("cost_usd"), summary_at=notes.now())
        self.jobs.save_run(rec)
        return rec

    def queue_summaries(self, sessions):
        """Summaries for finished runs that have none, one after another in the background."""
        if not self.summarizer.available:
            return
        with self.summary_lock:
            new = [x for x in sessions if x not in self.summary_busy]
            self.summary_busy.update(new)
            self.summary_queue += new
            if not new or len(self.summary_queue) > len(new):
                return
        def work():
            while True:
                with self.summary_lock:
                    if not self.summary_queue:
                        return
                    sid = self.summary_queue[0]
                try:
                    self.summarize(sid)
                except Exception:
                    pass
                with self.summary_lock:
                    self.summary_queue.pop(0)
        threading.Thread(target=work, daemon=True).start()

    def job_rows(self, offset=0, limit=10, show="all"):
        """The rows of the panel: notes and runs, those that need the owner first, then those at work, then the newest."""
        rows = []
        if show in ("all", "notes"):
            for n in self.jobs.notes():
                rows.append({"type": "note", **n})
        if show in ("all", "runs"):
            recs = self.jobs.runs()
            by_session = {r["session"]: r for r in recs if r.get("session")}
            seen, todo = set(), []
            trows, _ = self.transcripts.list(0, 200)
            for t in trows:
                rec = by_session.get(t["id"])
                if rec:
                    seen.add(rec["id"])
                elif not t["live"]:
                    todo.append(t["id"])
                rows.append(self._run_row(t, rec))
            for r in recs:
                if r["id"] not in seen and r.get("origin") == "page":
                    rows.append(self._run_row(None, r))
            self.queue_summaries(todo[:limit + offset])
        order = {"need human": 0, "transcribing": 1, "queued": 1, "sending": 1, "planning": 1, "working": 1}
        rows.sort(key=lambda r: r.get("updated") or "", reverse=True)
        rows.sort(key=lambda r: order.get(r.get("status"), 2))
        return {"rows": rows[offset:offset + limit], "total": len(rows), "offset": offset}

    def _run_row(self, t, rec):
        rec, t = rec or {}, t or {}
        status = rec.get("status") or ("working" if t.get("live") else "done")
        if t.get("live") and status in ("done", "failed"):
            status = "working"
        return {"type": "run", "id": rec.get("id") or t.get("id"), "session": rec.get("session") or t.get("id"),
                "title": t.get("title") or (rec.get("request") or "")[:90], "status": status, "detail": rec.get("status_detail"),
                "origin": rec.get("origin") or t.get("origin") or "terminal", "kind": rec.get("kind"), "tags": rec.get("tags") or [],
                "summary": bool(rec.get("summary")), "notes": rec.get("notes") or [], "branch": (rec.get("worktree") or {}).get("branch") or t.get("branch"),
                "cwd": t.get("cwd"), "steps": t.get("steps"), "cost_usd": (rec.get("result") or {}).get("cost_usd"),
                "max_context": t.get("max_context"), "start": t.get("start") or rec.get("started"), "end": t.get("end") or rec.get("ended"),
                "updated": max(filter(None, [t.get("end"), rec.get("updated")]), default=""), "live": t.get("live", False),
                "sent": rec.get("sent"), "fixed": rec.get("fixed")}

    def real_files(self):
        """id -> text of every real file the build found on disk ("scanned"), read now, so the page shows what is on disk."""
        out, never = {}, self.cfg.get("claude", {}).get("never", [".secrets"])
        try:
            nodes = json.load(open(os.path.join(self.page_dir, self.data), encoding="utf-8")).get("nodes", [])
        except (OSError, ValueError):
            return out
        for n in nodes:
            if not n.get("content_lazy") or not str(n.get("path", "")).startswith("agent-os/"):
                continue
            rel = n["path"][len("agent-os/"):]
            p = os.path.realpath(os.path.join(self.repo, rel))
            if not p.startswith(self.repo + os.sep) or any(b in rel for b in never) or not os.path.isfile(p):
                continue
            try:
                out[n["id"]] = open(p, encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                pass
        return out


class Handler(BaseHTTPRequestHandler):
    app = None
    server_version = "ProjectIDE/1"

    def log_message(self, fmt, *args):  # quiet: one line per request on stderr only with -v
        if "-v" in sys.argv:
            super().log_message(fmt, *args)

    # ---------- helpers ----------
    def _send(self, code, body, ctype="application/json; charset=utf-8", extra=None):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-cache")
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def _body(self):
        n = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(n) or b"{}") if n else {}

    def _local(self):
        """Only this machine's own address: stops other sites in the browser from talking to the server."""
        host = (self.headers.get("Host") or "").split(":")[0]
        if host not in ("127.0.0.1", "localhost", "[::1]"):
            return False
        origin = self.headers.get("Origin")
        return not origin or urlparse(origin).hostname in ("127.0.0.1", "localhost", "::1")

    def _route(self):
        u = urlparse(self.path)
        return [unquote(p) for p in u.path.strip("/").split("/") if p], parse_qs(u.query)

    # ---------- GET ----------
    def do_GET(self):
        if not self._local():
            return self._send(403, {"error": "local only"})
        parts, q = self._route()
        a = self.app
        if not parts:
            return self._send(302, b"", extra={"Location": "/" + a.page})
        if parts[0] != "api":
            if parts == ["real-files.json"]:   # the texts of the real files, read fresh from the repository
                return self._send(200, json.dumps(a.real_files(), ensure_ascii=False).encode(), "application/json; charset=utf-8")
            if len(parts) == 1 and parts[0] in (a.page, a.data):
                ctype = "text/html; charset=utf-8" if parts[0].endswith(".html") else "application/json; charset=utf-8"
                return self._send(200, open(os.path.join(a.page_dir, parts[0]), "rb").read(), ctype)
            return self._send(404, {"error": "not found"})
        if parts[1:] == ["health"]:
            b = a.bridge
            return self._send(200, {"ok": True, "server": "project-ide", "agent": b.available, "agent_error": claude_bridge.SDK_ERROR,
                                    "repo": os.path.basename(a.repo), "claude_cwd": os.path.relpath(b.cwd, a.repo), "write_through": bool(a.write),
                                    "voice": a.voice.available, "voice_max_seconds": a.voice.cfg["max_seconds"],
                                    "jobs": True, "send_options": a.jobs.defaults, "summaries": a.summarizer.available})
        if parts[1:] == ["jobs"]:
            off, lim = int((q.get("offset") or ["0"])[0]), min(int((q.get("limit") or ["10"])[0]), 100)
            return self._send(200, a.job_rows(off, lim, (q.get("show") or ["all"])[0]))
        if parts[1:] == ["notes"]:
            return self._send(200, {"notes": a.jobs.notes()})
        if len(parts) == 3 and parts[1] == "runs":
            v = a.run_view(parts[2])
            return self._send(200, v) if v else self._send(404, {"error": "no such run"})
        if len(parts) == 5 and parts[1] == "runs" and parts[3] == "steps":
            v = a.run_view(parts[2])
            st = a.transcripts.step(v["session"], parts[4]) if v and v.get("session") else None
            return self._send(200, st) if st else self._send(404, {"error": "no such step"})
        if len(parts) == 3 and parts[1] == "store":
            try:
                return self._send(200, {"docs": a.store.list(parts[2])})
            except ValueError as e:
                return self._send(400, {"error": str(e)})
        if len(parts) == 4 and parts[1] == "agent" and parts[3] == "events":
            return self._events(parts[2], q)
        return self._send(404, {"error": "not found"})

    def _events(self, rid, q):
        run = self.app.bridge.runs.get(rid)
        if not run:
            return self._send(404, {"error": "no such run"})
        after = int(self.headers.get("Last-Event-ID", "-1")) + 1 if self.headers.get("Last-Event-ID") else int((q.get("after") or ["0"])[0])
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        try:
            while True:
                events, done = run.wait(after)
                for e in events:
                    self.wfile.write(f"id: {e['n']}\ndata: {json.dumps(e, ensure_ascii=False)}\n\n".encode("utf-8"))
                after += len(events)
                if not events:
                    self.wfile.write(b": still working\n\n")
                self.wfile.flush()
                if done and after >= len(run.events):
                    break
        except (BrokenPipeError, ConnectionResetError):
            pass

    # ---------- writes ----------
    def _write(self, method):
        if not self._local():
            return self._send(403, {"error": "local only"})
        parts, _ = self._route()
        a = self.app
        if parts == ["api", "voice"] and method == "POST":
            return self._voice()
        if len(parts) == 4 and parts[:2] == ["api", "notes"] and parts[3] == "audio" and method == "POST":
            n = int(self.headers.get("Content-Length") or 0)
            if n > a.voice.cfg["max_bytes"]:
                return self._send(413, {"error": "recording too large"})
            if not a.voice.available:
                return self._send(503, {"error": "Voice input is off: no Groq key on this server."})
            audio = self.rfile.read(n) if n else b""
            try:
                a.jobs.update_note(parts[2], {"status": "transcribing"}, force=True)
            except ValueError as e:
                return self._send(404, {"error": str(e)})
            a.transcribe(parts[2], audio, self.headers.get("Content-Type"))
            return self._send(200, {"ok": True})
        try:
            body = self._body()
        except ValueError:
            return self._send(400, {"error": "bad JSON"})
        try:
            if len(parts) in (3, 4) and parts[:2] == ["api", "store"]:
                coll = parts[2]
                if method == "POST" and len(parts) == 3:
                    doc_id = time.strftime("%Y%m%d%H%M%S") + uuid.uuid4().hex[:6]
                    a.store.set(coll, doc_id, body)
                    return self._send(200, {"id": doc_id})
                doc_id = parts[3]
                before = a.store.get(coll, doc_id) if coll == "nodes" else None
                doc = a.store.set(coll, doc_id, body) if method == "PUT" else a.store.update(coll, doc_id, body)
                written = a.write.apply(doc_id, doc, before) if (a.write and coll == "nodes") else []
                return self._send(200, {"ok": True, "written": written})
            if parts == ["api", "notes"] and method == "POST":
                return self._send(200, a.jobs.add_note(body))
            if parts == ["api", "notes", "send"] and method == "POST":
                return self._send(200, a.send(body.get("ids") or [], body.get("options"), body.get("session"), body.get("node")))
            if len(parts) == 3 and parts[:2] == ["api", "notes"] and method in ("PATCH", "PUT"):
                return self._send(200, a.jobs.update_note(parts[2], body))
            if len(parts) == 4 and parts[:2] == ["api", "notes"] and method == "POST":
                nid, act = parts[2], parts[3]
                n = a.jobs.note(nid)
                if not n:
                    return self._send(404, {"error": "no such note"})
                if act == "delete":
                    a.jobs.delete_note(nid)
                    return self._send(200, {"ok": True})
                if act == "cancel":
                    if n["status"] in ("planning", "working", "need human", "sending") and n.get("run"):
                        return self._send(200, {"ok": a.bridge.stop(n["run"])})
                    return self._send(200, a.jobs.update_note(nid, {"status": "cancelled"}, force=True))
            if len(parts) == 4 and parts[:2] == ["api", "runs"] and method == "POST":
                rid, act = parts[2], parts[3]
                if act == "summary":
                    return self._send(200, a.summarize(rid))
                if act == "merge":
                    return self._send(200, a.bridge.merge(rid))
                if act == "discard":
                    return self._send(200, a.bridge.discard(rid))
                if act == "stop":
                    return self._send(200, {"ok": a.bridge.stop(rid)})
            if parts == ["api", "agent"] and method == "POST":
                text = (body.get("text") or "").strip()
                if not text:
                    return self._send(400, {"error": "empty request"})
                node = {k: body.get(k) for k in ("node_id", "path", "name")}
                known = (a.write.nodes().get(node["node_id"]) if a.write else None) or {}
                node.update({k: known[k] for k in ("type", "fam") if known.get(k)})
                # the Delete button: Claude Code may delete exactly this item without a second click
                target = a.bridge.delete_target(body["delete"]) if body.get("delete") else None
                run = a.bridge.start(text, node, body.get("session"), body.get("input_id"), delete=target)
                return self._send(200, {"run": run.id})
            if len(parts) == 4 and parts[1] == "agent" and parts[3] == "answer":
                return self._send(200, {"ok": a.bridge.answer(parts[2], body.get("id"), body.get("allow"))})
            if len(parts) == 4 and parts[1] == "agent" and parts[3] == "stop":
                return self._send(200, {"ok": a.bridge.stop(parts[2])})
        except ValueError as e:
            return self._send(400, {"error": str(e)})
        except RuntimeError as e:
            return self._send(503, {"error": str(e)})
        return self._send(404, {"error": "not found"})

    def _voice(self):
        """The raw recording in the body; its text back. The audio is not kept."""
        n = int(self.headers.get("Content-Length") or 0)
        if n > self.app.voice.cfg["max_bytes"]:
            return self._send(413, {"error": "recording too large"})
        audio = self.rfile.read(n) if n else b""
        try:
            return self._send(200, self.app.voice.transcribe(audio, self.headers.get("Content-Type")))
        except ValueError as e:
            return self._send(400, {"error": str(e)})
        except RuntimeError as e:
            return self._send(503, {"error": str(e)})

    def do_POST(self):
        self._write("POST")

    def do_PUT(self):
        self._write("PUT")

    def do_PATCH(self):
        self._write("PATCH")


def main():
    app = App()
    Handler.app = app
    host, port = app.cfg.get("host", "127.0.0.1"), int(os.environ.get("IDE_PORT") or app.cfg.get("port", 8765))
    if host not in ("127.0.0.1", "localhost", "::1"):
        sys.exit("Refusing to listen on " + host + ": the page can run Claude Code, so it stays on this machine. Use an SSH tunnel.")
    srv = ThreadingHTTPServer((host, port), Handler)
    print(f"Project IDE on http://{host}:{port}/  (repo {app.repo}; Claude Code in {os.path.relpath(app.bridge.cwd, app.repo)}"
          + ("" if app.bridge.available else f"; request box off: {claude_bridge.SDK_ERROR}") + ")", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
