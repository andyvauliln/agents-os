#!/usr/bin/env python3
"""Makes every planned item of the tree a real file or folder in the repository (owner, 2026-10-12: "all what was
planned should be already real files"). Run it after enrich.py, then run enrich.py again so the page sees them.

    REPO_DIR=/path/to/repo python3 materialize.py file-tree.data.json

- A planned file with a draft (src_file under vision/) gets the draft's text. The draft stays the source while we
  plan: every build copies it again, and the owner's server writes an edit into both.
- Any other planned file is created empty ("{}" for a .json file), to be filled when the work reaches it.
- Placeholder names such as [skill-name] are created as they are written: they are the templates.
- A folder with nothing in it gets a .gitkeep, because git does not keep empty folders.
- The keys folder (.secrets/) is never created here: it is git-ignored and holds real keys only on the machine.
"""
import json, os, sys

REPO = os.path.abspath(os.environ.get("REPO_DIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def disk(rel):
    """The name on disk: '|' is not allowed in Windows file names (same rule as the server)."""
    return rel.replace("|", "-")


def main(data_file):
    nodes = json.load(open(data_file, encoding="utf-8"))["nodes"]
    nodes = nodes.values() if isinstance(nodes, dict) else nodes
    made, copied, folders = 0, 0, set()
    for n in nodes:
        path = n.get("path") or ""
        if not path.startswith("agent-os/") or n.get("scanned") or ".secrets" in path:
            continue
        rel = disk(path[len("agent-os/"):])
        full = os.path.join(REPO, rel.rstrip("/"))
        if n["type"] == "folder":
            if rel:
                os.makedirs(full, exist_ok=True)
                folders.add(full)
            continue
        os.makedirs(os.path.dirname(full), exist_ok=True)
        folders.add(os.path.dirname(full))
        src = n.get("src_file") or ""
        if src.startswith("vision/") and os.path.isfile(os.path.join(REPO, src)):
            text = open(os.path.join(REPO, src), encoding="utf-8").read()
            if not os.path.isfile(full) or open(full, encoding="utf-8").read() != text:
                with open(full, "w", encoding="utf-8") as f:
                    f.write(text)
                copied += 1
        elif not os.path.exists(full):
            with open(full, "w", encoding="utf-8") as f:
                f.write("{}\n" if full.endswith(".json") else "")
            made += 1
    kept = 0
    for d in folders:
        if os.path.isdir(d) and not os.listdir(d):
            open(os.path.join(d, ".gitkeep"), "w").close()
            kept += 1
    print(f"materialize: {copied} files copied from drafts, {made} empty files made, {kept} .gitkeep files")


if __name__ == "__main__":
    main(sys.argv[1])
