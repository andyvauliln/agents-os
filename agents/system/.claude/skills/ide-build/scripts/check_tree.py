#!/usr/bin/env python3
"""Checks that the page tree equals the files in git (ide-build, the last check before publishing).

    python3 check_tree.py [data file]     # default: apps/project-IDE/current-ui/file-tree.data.json

The items of the page data must be exactly the paths `git ls-files --cached --others --exclude-standard` lists,
without the old planning folder, plus the folders that hold them and the top (`agent-os`). The local keys files
(.env) are the only items allowed on top of that: git ignores them, and the page lists them without reading them.
Every id must be the item's path. Prints "tree ok" or what differs, and exits 1 when something differs.
"""
import json, os, sys

import index_files as IF


def main():
    data_file = sys.argv[1] if len(sys.argv) > 1 else os.path.join(IF.REPO, "apps/project-IDE/current-ui/file-tree.data.json")
    nodes = json.load(open(data_file, encoding="utf-8"))["nodes"]
    files = IF.git_files()
    want = {IF.ROOT} | set(files)
    for f in files:
        parts = f.split("/")
        want.update("/".join(parts[:i]) for i in range(1, len(parts)))
    have = {n["id"] for n in nodes}
    bad_ids = [n["id"] for n in nodes if n["id"] != IF.ROOT and n["path"].rstrip("/") != IF.ROOT + "/" + n["id"]]
    extra = sorted(have - want)
    keys = [x for x in extra if os.path.basename(x) == ".env"]
    extra = [x for x in extra if x not in keys]
    lacking = sorted(want - have)
    numbered = [n["id"] for n in nodes if n["id"].startswith(("n-", "r-", "p-")) or n.get("num")]
    print(f"{len(nodes)} items on the page; {len(want)} paths in git with their folders; {len(keys)} local keys files: {', '.join(keys) or 'none'}")
    for title, lst in (("on the page, not in git", extra), ("in git, not on the page", lacking), ("id is not the path", bad_ids), ("old numbered id", numbered)):
        if lst:
            print(f"{title} ({len(lst)}): " + ", ".join(lst[:20]) + (" ..." if len(lst) > 20 else ""))
    ok = not (extra or lacking or bad_ids or numbered)
    print("tree ok" if ok else "tree differs from git")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
