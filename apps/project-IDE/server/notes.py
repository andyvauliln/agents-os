"""Notes and run records: the rows of the page's "Notes and runs" panel.

A note is anything the owner says or types to Claude Code on the page. It is one file,
<store_dir>/notes/<id>.json (git ignores the folder; a note's words are filed as an owner input by
the run that takes it). A run record is one file, <log_dir>/runs/<run>.json, for every run started
from the page and for every terminal run once it has a summary; it holds what Claude Code's
transcript does not: status, notes, options, branch, versions, summary, tags, the report.
Statuses: transcribing, ready, queued, sending, planning, working, need human, need manual test,
done, in main, failed, cancelled.
"""
import json
import os
import re
import threading
import time
import uuid

NOTE_STATUSES = ("transcribing", "ready", "queued", "sending", "planning", "working", "need human",
                 "need manual test", "done", "in main", "failed", "cancelled")
ACTIVE = ("transcribing", "queued", "sending", "planning", "working")
SAFE = re.compile(r"^[0-9A-Za-z-]{6,64}$")
DEFAULT_OPTIONS = {"where": "local", "merge": "auto", "tests": "related", "bug_check": True, "report": True}
EDITABLE = ("text", "include", "send_after_transcript", "status")


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


class Jobs:
    def __init__(self, store_dir, log_dir, cfg=None):
        self.notes_dir = os.path.join(store_dir, "notes")
        self.runs_dir = os.path.join(log_dir, "runs")
        self.defaults = {**DEFAULT_OPTIONS, **{k: v for k, v in ((cfg or {}).get("send_options") or {}).items() if not k.startswith("_")}}
        self.lock = threading.RLock()
        self.listeners = []          # called with ("note"|"run", record) after every change

    # ---------- files ----------
    def _path(self, folder, rid):
        if not SAFE.match(rid or ""):
            raise ValueError("bad id")
        return os.path.join(folder, rid + ".json")

    @staticmethod
    def _load(path):
        try:
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        except (OSError, ValueError):
            return None

    def _save(self, folder, rec):
        os.makedirs(folder, exist_ok=True)
        p = self._path(folder, rec["id"])
        tmp = p + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(rec, f, indent=1, ensure_ascii=False)
        os.replace(tmp, p)

    def _all(self, folder):
        out = []
        if os.path.isdir(folder):
            for f in os.listdir(folder):
                if f.endswith(".json"):
                    r = self._load(os.path.join(folder, f))
                    if r:
                        out.append(r)
        return out

    def _tell(self, kind, rec):
        for fn in self.listeners:
            try:
                fn(kind, rec)
            except Exception:
                pass

    # ---------- notes ----------
    def notes(self):
        return self._all(self.notes_dir)

    def note(self, nid):
        return self._load(self._path(self.notes_dir, nid))

    def add_note(self, body):
        text = str(body.get("text") or "")
        recording = bool(body.get("recording"))
        if not text.strip() and not recording:
            raise ValueError("empty note")
        ctx = body.get("context") or {}
        rec = {"id": time.strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:6], "text": text,
               "status": "transcribing" if recording else "ready", "include": body.get("include", True) is not False,
               "send_after_transcript": bool(body.get("send_after_transcript")),
               "context": {k: ctx.get(k) for k in ("where", "path", "node_id", "name", "tab", "selection", "line", "page_version") if ctx.get(k) is not None}
               | {"recorded": recording, "at": now()},
               "created": now(), "updated": now(), "run": None, "error": None,
               "sent": None, "fixed": None}
        with self.lock:
            self._save(self.notes_dir, rec)
        self._tell("note", rec)
        return rec

    def update_note(self, nid, patch, force=False):
        with self.lock:
            rec = self.note(nid)
            if not rec:
                raise ValueError("no such note")
            for k, v in patch.items():
                if force or k in EDITABLE:
                    if k == "status" and v not in NOTE_STATUSES:
                        raise ValueError("bad status")
                    rec[k] = v
            rec["updated"] = now()
            self._save(self.notes_dir, rec)
        self._tell("note", rec)
        return rec

    def delete_note(self, nid):
        with self.lock:
            rec = self.note(nid)
            if rec and rec["status"] in ("sending", "planning", "working"):
                raise ValueError("Cancel the run first.")
            try:
                os.remove(self._path(self.notes_dir, nid))
            except OSError:
                pass

    def sendable(self, ids):
        """The notes in `ids` that can go out now, in the order they were made."""
        out = []
        for nid in ids:
            n = self.note(nid)
            if n and n["status"] in ("ready", "failed", "cancelled", "done", "need manual test", "need human") and n["text"].strip():
                out.append(n)
        return sorted(out, key=lambda n: n["created"])

    # ---------- run records ----------
    def runs(self):
        return self._all(self.runs_dir)

    def run(self, rid):
        return self._load(self._path(self.runs_dir, rid))

    def run_by_session(self, session):
        for r in self.runs():
            if r.get("session") == session or r.get("id") == session:
                return r
        return None

    def save_run(self, rec):
        rec["updated"] = now()
        with self.lock:
            self._save(self.runs_dir, rec)
        self._tell("run", rec)
        return rec

    def set_run_notes(self, run, status, **extra):
        """Every note of a run follows the run's status."""
        for nid in run.get("notes") or []:
            try:
                self.update_note(nid, {"status": status, "run": run["id"], **extra}, force=True)
            except ValueError:
                pass

    def recover(self, live_runs):
        """After a restart: whatever was on its way or at work, and is not running any more, failed."""
        for n in self.notes():
            if n["status"] in ("sending", "planning", "working") and n.get("run") not in live_runs:
                self.update_note(n["id"], {"status": "failed", "error": "The server restarted while the run was working."}, force=True)
            elif n["status"] == "transcribing":
                self.update_note(n["id"], {"status": "failed", "error": "The server restarted while the note was transcribing."}, force=True)
        for r in self.runs():
            if r.get("status") in ("sending", "planning", "working", "need human") and r["id"] not in live_runs and r.get("origin") == "page":
                r.update(status="failed", error="The server restarted while the run was working.")
                self.save_run(r)

    # ---------- one request from many notes ----------
    @staticmethod
    def combine(notes, options):
        """The request Claude Code gets for a batch of notes: each note with where it came from."""
        lines = [f"The owner sent {len(notes)} note{'s' if len(notes) != 1 else ''} from the File Tree page. "
                 "Handle every one of them in this run. File each note word for word as an owner input (knowledge-intake), "
                 "then do what it asks or answer it.", ""]
        for i, n in enumerate(notes, 1):
            c = n.get("context") or {}
            where = c.get("path") or "the whole repository"
            head = f"Note {i} (id {n['id']}), {'recorded by voice' if c.get('recorded') else 'typed'} on {where}"
            if c.get("tab"):
                head += f", {c['tab']} tab"
            if c.get("where"):
                head += f", from the {c['where']}"
            lines.append(head + ":")
            if c.get("selection"):
                sel = c["selection"]
                at = f" (line {c['line']})" if c.get("line") else ""
                lines += [f"The owner selected this text{at}:", "~~~text", str(sel)[:4000], "~~~"]
            lines += ["~~~text", n["text"].strip(), "~~~", ""]
        return "\n".join(lines) + "\n" + Jobs.instructions(options)

    @staticmethod
    def instructions(options):
        o = {**DEFAULT_OPTIONS, **(options or {})}
        tests = {"related": "Run the checks of the build and the tests that cover the files you changed.",
                 "all": "Run every check and test the repository has.",
                 "none": "Run no tests beyond what the build itself does."}[o.get("tests", "related")]
        lines = ["How to work this run:",
                 f"- {tests}"]
        if o.get("bug_check"):
            lines.append("- Before you finish, review your whole diff for bugs (use the code-review skill if you have it), fix what you find, and list what you did not fix.")
        if o.get("report"):
            lines.append("- End your answer with a short report under the heading \"Report\": what was asked, what you changed, the checks and their results, what is left.")
        lines += ["- Commit your work on the current branch. Never push and never merge into main: the server does that.",
                  "- The very last line of your answer is exactly one of these:",
                  "  STATUS: done",
                  "  STATUS: need manual test: <what a person must try, in one line>",
                  "  STATUS: need human: <what you need from the owner, in one line>"]
        return "\n".join(lines)


STATUS_LINE = re.compile(r"^\s*STATUS:\s*(done|need manual test|need human)\s*(?::\s*(.*))?$", re.I | re.M)


def read_status(text):
    """The STATUS line at the end of a run's answer: (status, detail), or (None, None)."""
    found = STATUS_LINE.findall(text or "")
    if not found:
        return None, None
    status, detail = found[-1]
    return status.lower(), (detail or "").strip() or None
