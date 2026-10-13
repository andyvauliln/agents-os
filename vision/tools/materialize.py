#!/usr/bin/env python3
"""Keeps the files on disk in step with their sources in vision/ (owner, 2026-10-13: the tree is the files on disk;
nothing is made from the plan any more). Run it after enrich.py, then run enrich.py again if it changed anything.

    REPO_DIR=/path/to/repo python3 materialize.py file-tree.data.json

- A file on disk whose source is a draft in vision/ (src_file) gets the draft's text again. The draft stays the
  source while we plan, and the owner's server writes an edit into both.
- Each item's How it works (.index.md) and Details (.meta.json) files are copied from vision/ next to it (inside
  a folder, beside a file). The copy in vision/ stays the source while we plan.
- Every other file and folder outside vision/ gets an empty x.index.md and x.meta.json when it has none
  (owner, 2026-10-12: metadata for all files). The prediction-market domain is stage two: nothing is made inside.
- A folder with nothing in it keeps a .gitkeep, because git does not keep empty folders; it goes once the folder
  holds a file. A .env keys file is never made, read or written.
- docs/file-tree.md is written again: every path in git, plain.
"""
import json, os, sys
from collections import Counter

STAGE_TWO = "agents/trading/prediction-market/"   # stage two (owner, 2026-10-12): only its folders exist, nothing is made inside
META_ENDS = (".index.md", ".meta.json", ".gitkeep", ".example.md", ".questions.md", ".env.example")   # metadata and tab files have none of their own

REPO = os.path.abspath(os.environ.get("REPO_DIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def disk(rel):
    """The name on disk: '|' is not allowed in Windows file names (same rule as the server)."""
    return rel.replace("|", "-")


def meta_home(n, rel):
    """Where an item's metadata files go on disk: inside a folder, beside a file."""
    return os.path.join(REPO, rel.rstrip("/")) if n["type"] == "folder" else os.path.dirname(os.path.join(REPO, rel))


def copy_meta(n, rel):
    """Copies the item's .index.md and .meta.json from vision/ next to the item; returns how many changed."""
    changed = 0
    for key in ("how_file", "meta_file"):
        src = os.path.join(REPO, "vision", n[key]) if n.get(key) else None
        if not src or not os.path.isfile(src):
            continue
        dst = os.path.join(meta_home(n, rel), os.path.basename(src))
        if os.path.realpath(dst) == os.path.realpath(src):
            continue
        text = open(src, encoding="utf-8").read()
        if not os.path.isfile(dst) or open(dst, encoding="utf-8").read() != text:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with open(dst, "w", encoding="utf-8") as f:
                f.write(text)
            changed += 1
    return changed


def scanned_meta(nodes):
    """An empty .index.md and .meta.json for every found file and folder outside vision/ that has none."""
    made = 0
    found = [n for n in nodes if n.get("scanned")]
    by_dir = {}
    for n in found:
        rel = n["path"][len("agent-os/"):].rstrip("/")
        if rel.startswith(("vision/", STAGE_TWO)) or rel == "vision" or n["name"].rstrip("/").endswith(META_ENDS) or n["name"] == ".env":
            continue
        by_dir.setdefault(os.path.dirname(rel), []).append((n, rel))
    for d, items in by_dir.items():
        fams = Counter(os.path.splitext(os.path.basename(r))[0] for n, r in items if n["type"] == "file")
        for n, rel in items:
            base = os.path.basename(rel)
            if n["type"] == "folder":
                home, fam = os.path.join(REPO, rel), base
            else:
                stem = os.path.splitext(base)[0] or base
                home, fam = os.path.dirname(os.path.join(REPO, rel)), (base if fams[stem] > 1 else stem)
            for ext, text in ((".index.md", ""), (".meta.json", "{}\n")):
                f = os.path.join(home, fam + ext)
                if not os.path.exists(f):
                    with open(f, "w", encoding="utf-8") as fh:
                        fh.write(text)
                    made += 1
    return made


def plain_tree():
    """docs/file-tree.md: every path in the repository, plain, without metadata files (owner, 2026-10-12).
    vision/ is the planning area and shows as one line."""
    import subprocess
    out = subprocess.run(["git", "-C", REPO, "ls-files", "--cached", "--others", "--exclude-standard"], capture_output=True, text=True).stdout.split("\n")
    paths = set()
    for f in out:
        f = f.strip()
        if not f or not os.path.exists(os.path.join(REPO, f)) or os.path.basename(f).endswith(META_ENDS):
            continue
        if f.startswith("vision/"):
            paths.add("vision/"); continue
        parts = f.split("/")
        for i in range(1, len(parts)):
            paths.add("/".join(parts[:i]) + "/")
        paths.add(f)
    lines = ["# File tree", "",
             "Every file and folder in the repository, one path per line, folders ending with `/`. The metadata files",
             "(`.index.md`, `.meta.json`, `.example.md`, `.questions.md`, `.gitkeep`) are left out, and `vision/`, the planning",
             "area, is one line. Built by the IDE build every round; never edit it by hand.", "", "```text"]
    lines += sorted(paths, key=lambda p: [s.lower() for s in p.rstrip("/").split("/")])
    lines += ["```", ""]
    text = "\n".join(lines)
    f = os.path.join(REPO, "docs", "file-tree.md")
    if not os.path.isfile(f) or open(f, encoding="utf-8").read() != text:
        os.makedirs(os.path.dirname(f), exist_ok=True)
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(text)
    return len(paths)


def main(data_file):
    nodes = json.load(open(data_file, encoding="utf-8"))["nodes"]
    nodes = nodes.values() if isinstance(nodes, dict) else nodes
    copied, metas, folders = 0, 0, set()
    for n in nodes:
        path = n.get("path") or ""
        if not path.startswith("agent-os/") or n.get("scanned"):
            continue
        rel = disk(path[len("agent-os/"):])
        full = os.path.join(REPO, rel.rstrip("/"))
        if not os.path.exists(full) or rel.startswith(STAGE_TWO):   # only what is on disk; stage two stays as it is
            continue
        metas += copy_meta(n, rel)
        if n["type"] == "folder":
            folders.add(full)
            continue
        src = n.get("src_file") or ""
        if os.path.basename(full) != ".env" and src.startswith("vision/") and os.path.isfile(os.path.join(REPO, src)):
            text = open(os.path.join(REPO, src), encoding="utf-8").read()
            if open(full, encoding="utf-8").read() != text:
                with open(full, "w", encoding="utf-8") as f:
                    f.write(text)
                copied += 1
    empty = scanned_meta(nodes)
    kept = 0
    for d in folders:
        other = [f for f in os.listdir(d) if f not in (".env", ".gitkeep")]
        if not other and not os.path.exists(os.path.join(d, ".gitkeep")):   # git keeps no empty folder, and ignores .env
            open(os.path.join(d, ".gitkeep"), "w").close()
            kept += 1
        elif other and os.path.exists(os.path.join(d, ".gitkeep")):   # not needed once the folder holds a file
            os.remove(os.path.join(d, ".gitkeep"))
    listed = plain_tree()
    print(f"docs/file-tree.md: {listed} paths")
    print(f"materialize: {copied} files copied from drafts, {kept} .gitkeep files, {metas} metadata files copied, {empty} empty metadata files for found files")


if __name__ == "__main__":
    main(sys.argv[1])
