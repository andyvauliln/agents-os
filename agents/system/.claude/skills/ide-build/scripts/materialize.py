#!/usr/bin/env python3
"""Keeps the metadata files and the plain tree in step with the files on disk (docs/metadata.md section 11).
The real files are the only source: nothing is copied from anywhere. Run it after enrich.py, then run enrich.py
again if it made anything.

    python3 materialize.py          # REPO_DIR overrides the repository (default: the checkout these scripts sit in)

- Every file and folder outside stage two that has no How it works (x.index.md) or Details (x.meta.json) file
  gets an empty one (owner, 2026-10-12: metadata for all files). A metadata file has none of its own, and a
  local keys file (.env) is never made, read or written. The prediction-market domain is stage two: nothing is
  made inside it, except in its docs/. Nothing is made inside the kept-data folder (index_files.KEPT): the earlier
  prediction-market metadata files kept there are plain data.
- A folder with nothing in it keeps a .gitkeep, because git keeps no empty folder; the
  .gitkeep goes once the folder holds a file.
- docs/file-tree.md is written again: every path in git, plain, without metadata files.
"""
import os

import index_files as IF

REPO = IF.REPO


def empty_meta(items):
    """An empty x.index.md and x.meta.json for every item that must have them and has none."""
    made = 0
    for it, rel in IF.missing(items):
        f = os.path.join(REPO, rel)
        if os.path.basename(f) == ".env" or not os.path.isdir(os.path.dirname(f) or REPO):
            continue
        with open(f, "w", encoding="utf-8") as fh:
            fh.write("{}\n" if rel.endswith(".meta.json") else "")
        made += 1
    return made


def gitkeep(items):
    """A .gitkeep in every empty folder (a keys file does not count); none once the folder holds a file."""
    kept = removed = 0
    for it in items:
        if it["type"] != "folder" or not it["rel"] or IF.stage_two(it["rel"] + "/"):
            continue
        d = os.path.join(REPO, it["rel"])
        own = [f for f in os.listdir(d) if f not in (".env", ".gitkeep")]
        keep = os.path.join(d, ".gitkeep")
        if not own and not os.path.exists(keep):
            open(keep, "w").close(); kept += 1
        elif own and os.path.exists(keep):
            os.remove(keep); removed += 1
    return kept, removed


def plain_tree(items):
    """docs/file-tree.md: every path in the repository, plain, without metadata files (owner, 2026-10-12)."""
    paths = set()
    for it in items:   # the files, and the folders that hold them
        if it["type"] != "file" or IF.is_meta_file(it["name"], it["rel"]) or it["name"] == ".env":   # kept data (IF.KEPT) is listed
            continue
        parts = it["rel"].split("/")
        paths.update("/".join(parts[:i]) + "/" for i in range(1, len(parts)))
        paths.add(it["rel"])
    lines = ["# File tree", "",
             "Every file and folder in the repository, one path per line, folders ending with `/`. The metadata files",
             "(`.index.md`, `.meta.json`, `.example.md`, `.questions.md`, `.gitkeep`) are left out. Built by the IDE build",
             "every round; never edit it by hand.", "", "```text"]
    lines += sorted(paths, key=lambda p: [s.lower() for s in p.rstrip("/").split("/")])
    lines += ["```", ""]
    text = "\n".join(lines)
    f = os.path.join(REPO, "docs", "file-tree.md")
    if not os.path.isfile(f) or open(f, encoding="utf-8").read() != text:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(text)
    return len(paths)


def main():
    items = IF.load_items()
    made = empty_meta(items)
    kept, removed = gitkeep(items)
    listed = plain_tree(IF.load_items())
    print(f"docs/file-tree.md: {listed} paths")
    print(f"materialize: {made} empty metadata files, {kept} .gitkeep files added, {removed} removed")


if __name__ == "__main__":
    main()
