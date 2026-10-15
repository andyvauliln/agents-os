"""Worktrees: each run from the page works on its own branch, in its own git worktree.

    .worktrees/<run>/        a full checkout of branch ide/<date>-<subject>, made from main
                             (git ignores .worktrees/, so the page tree never lists it)

Several runs can work at the same time, and none of them touches the files the server shows.
When a run is done, its branch is brought up to date with main and merged into main here on
the server (a fast-forward). The built files (the page data and the plain file tree) differ on
every branch, so a conflict in them alone is solved by building them again; any other conflict
stops the merge and waits for the owner.
"""
import os
import re
import shutil
import subprocess
import sys
import time

GENERATED = ("apps/project-IDE/current-ui/file-tree.data.json", "apps/project-IDE/current-ui/real-files.json", "docs/file-tree.md")
REBUILD = "agents/system/.claude/skills/ide-build/scripts/rebuild.py"
SAFE_RUN = re.compile(r"^[0-9A-Za-z-]{6,64}$")


class GitError(RuntimeError):
    pass


def slug(text, n=40):
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return (s[:n].rstrip("-") or "run")


class Worktrees:
    def __init__(self, repo, cfg=None):
        cfg = cfg or {}
        self.repo = os.path.realpath(repo)
        self.root = os.path.join(self.repo, cfg.get("folder", ".worktrees"))
        self.main = cfg.get("main", "main")

    def git(self, *args, cwd=None, check=True):
        p = subprocess.run(["git", "-c", "core.quotepath=off", *args], cwd=cwd or self.repo, capture_output=True, text=True, timeout=120)
        if check and p.returncode:
            raise GitError((p.stderr or p.stdout).strip()[:600] or f"git {' '.join(args)} failed")
        return p.stdout

    def path(self, run_id):
        if not SAFE_RUN.match(run_id or ""):
            raise ValueError("bad run id")
        return os.path.join(self.root, run_id)

    def head(self, cwd=None, short=True):
        return self.git("rev-parse", *(["--short"] if short else []), "HEAD", cwd=cwd).strip()

    # ---------- make and remove ----------
    def create(self, run_id, subject):
        """A new branch from main and its worktree. Returns {branch, path, base}."""
        path = self.path(run_id)
        branch = f"ide/{time.strftime('%Y%m%d-%H%M')}-{slug(subject)}"
        stem, n = branch, 2
        while self.git("branch", "--list", branch).strip():
            branch, n = f"{stem}-{n}", n + 1
        base = self.git("rev-parse", self.main).strip()
        os.makedirs(self.root, exist_ok=True)
        self.git("worktree", "add", "-q", "-b", branch, path, base)
        return {"branch": branch, "path": path, "base": base[:7]}

    def remove(self, run_id, branch=None, delete_branch=False):
        path = self.path(run_id)
        if os.path.isdir(path):
            self.git("worktree", "remove", "--force", path, check=False)
            if os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)
        self.git("worktree", "prune", check=False)
        if branch and delete_branch:
            self.git("branch", "-D", branch, check=False)

    def exists(self, run_id):
        try:
            return os.path.isdir(self.path(run_id))
        except ValueError:
            return False

    # ---------- state of a branch ----------
    def status(self, run_id):
        """Uncommitted files in the worktree, and the commits of its branch that main does not have."""
        path = self.path(run_id)
        if not os.path.isdir(path):
            return {"exists": False}
        dirty = [l[3:] for l in self.git("status", "--porcelain", cwd=path).splitlines()]
        commits = [dict(zip(("commit", "subject"), l.split("\t", 1))) for l in
                   self.git("log", "--format=%h\t%s", f"{self.main}..HEAD", cwd=path).splitlines()]
        branch = self.git("rev-parse", "--abbrev-ref", "HEAD", cwd=path).strip()
        changed = self.git("diff", "--name-only", f"{self.main}...HEAD", cwd=path).splitlines()
        return {"exists": True, "branch": branch, "head": self.head(path), "dirty": dirty, "commits": commits, "changed": changed}

    # ---------- bring up to date and merge ----------
    def update(self, run_id):
        """Merge main into the run's branch. Built files that conflict are built again; any other conflict raises."""
        path = self.path(run_id)
        if self.git("status", "--porcelain", "--untracked-files=no", cwd=path).strip():
            self.git("add", "-A", cwd=path)
            self.git("commit", "-q", "-m", "Work left uncommitted by the run", cwd=path)
        p = subprocess.run(["git", "merge", "-q", "--no-edit", self.main], cwd=path, capture_output=True, text=True, timeout=120)
        if p.returncode == 0:
            return {"rebuilt": False}
        conflicts = self.git("diff", "--name-only", "--diff-filter=U", cwd=path).splitlines()
        if not conflicts or any(c not in GENERATED for c in conflicts):
            self.git("merge", "--abort", cwd=path, check=False)
            raise GitError("The branch conflicts with main in: " + ", ".join(c for c in conflicts if c not in GENERATED))
        self.git("checkout", "--theirs", "--", *conflicts, cwd=path)
        self.rebuild(path)
        self.git("add", "--", *GENERATED, cwd=path)
        self.git("commit", "-q", "--no-edit", cwd=path)
        return {"rebuilt": True}

    def rebuild(self, path):
        p = subprocess.run([sys.executable, os.path.join(path, REBUILD)], cwd=path, capture_output=True, text=True, timeout=600,
                           env={**os.environ, "REPO_DIR": path})
        if p.returncode:
            raise GitError("The page rebuild failed: " + (p.stdout + p.stderr).strip()[-600:])
        return p.stdout

    def merge(self, run_id):
        """Bring the branch up to date with main, then fast-forward main to it in the repository the server shows.
        Returns {commit, from}. The owner's uncommitted edits on main stay; git refuses if the branch changes one of them."""
        path = self.path(run_id)
        self.update(run_id)
        branch = self.git("rev-parse", "--abbrev-ref", "HEAD", cwd=path).strip()
        if self.git("rev-parse", "--abbrev-ref", "HEAD").strip() != self.main:
            raise GitError(f"The repository the server shows is not on {self.main}.")
        before = self.head()
        self.git("checkout", "-q", "--", *GENERATED, check=False)   # built again below; a local build never blocks the merge
        p = subprocess.run(["git", "merge", "-q", "--ff-only", branch], cwd=self.repo, capture_output=True, text=True, timeout=120)
        if p.returncode:
            raise GitError("main could not take the branch: " + (p.stderr or p.stdout).strip()[:400])
        self.rebuild(self.repo)
        return {"commit": self.head(), "from": before, "branch": branch}
