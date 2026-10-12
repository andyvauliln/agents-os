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
import voice  # noqa: E402

CONFIG = os.environ.get("IDE_CONFIG", os.path.join(HERE, "server.config.json"))
COLLECTIONS = {"nodes", "changes", "inputs"}       # what the page keeps (same as on claude.ai)
SAFE_ID = re.compile(r"^[A-Za-z0-9_.:@+~-]{1,200}$")


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

    def __init__(self, repo, data_file, never, planning=None):
        self.repo, self.data_file, self.never = repo, data_file, never
        self.planning = planning   # while we plan, the folder that holds the drafts and How it works files ("vision")
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
        if node.get("src_file"):             # the file the page showed: a draft, a repository file or a real file found on disk
            return self._safe(node["src_file"])
        if self.planning:                    # a planned file nobody has written: the edit waits in the page store for the sync
            return None
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
        if self.planning:                    # How it works files sit in the planning folder (next to a draft, or in its mirror tree)
            return self._safe(os.path.join(self.planning, node["how_file"])) if node.get("how_file") else None
        return self.metadata_of(node, ".index.md")

    def apply(self, node_id, doc, before=None):
        """Writes what this save changed. A field the page saved before is not written again: the same
        document is saved again for a comment or a mark, and that must not undo what Claude Code wrote since."""
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
            meta = {"about": n.get("path"), "node": n["id"]}
            if os.path.isfile(p):
                m = re.match(r"^---\n(.*?)\n---[ \t]*\n?", open(p, encoding="utf-8").read(), re.S)
                for line in (m.group(1).split("\n") if m else []):
                    k, _, v = line.partition(":")
                    if k.strip():
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
        self.write = WriteThrough(self.repo, os.path.join(self.page_dir, self.data), never, self.cfg.get("planning_dir")) if self.cfg.get("write_through", True) else None
        secrets = load_secrets(self.cfg, self.repo)
        self.voice = voice.Voice(self.cfg, secrets)
        # Claude Code gets only its own keys, never the voice key
        vkey = self.voice.cfg["key"]
        self.bridge = claude_bridge.Bridge(self.cfg, self.repo, {k: v for k, v in secrets.items() if k != vkey})

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
                                    "voice": a.voice.available, "voice_max_seconds": a.voice.cfg["max_seconds"]})
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
            if parts == ["api", "agent"] and method == "POST":
                text = (body.get("text") or "").strip()
                if not text:
                    return self._send(400, {"error": "empty request"})
                node = {k: body.get(k) for k in ("node_id", "path", "name", "num")}
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
