#!/usr/bin/env python3
"""Makes every planned item of the tree a real file or folder in the repository (owner, 2026-10-12: "all what was
planned should be already real files"). Run it after enrich.py, then run enrich.py again so the page sees them.

    REPO_DIR=/path/to/repo python3 materialize.py file-tree.data.json

- A planned file with a draft (src_file under vision/) gets the draft's text. The draft stays the source while we
  plan: every build copies it again, and the owner's server writes an edit into both.
- Any other planned file is created empty ("{}" for a .json file), to be filled when the work reaches it.
- Placeholder names such as [skill-name] are created as they are written: they are the templates.
- A folder with nothing in it gets a .gitkeep, because git does not keep empty folders.
- Each item's How it works (.index.md) and Details (.meta.json) files are copied next to it (inside a folder,
  beside a file), so the disk shows them like the page does. The copy in vision/ stays the source while we plan.
- The keys folder .secrets/ and its notes are created and go in git (owner, 2026-10-12). A .env keys file is
  created empty only when it is missing, is never read or overwritten, and git ignores it.
"""
import json, os, sys

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


def main(data_file):
    nodes = json.load(open(data_file, encoding="utf-8"))["nodes"]
    nodes = nodes.values() if isinstance(nodes, dict) else nodes
    made, copied, metas, folders = 0, 0, 0, set()
    for n in nodes:
        path = n.get("path") or ""
        if not path.startswith("agent-os/") or n.get("scanned"):
            continue
        rel = disk(path[len("agent-os/"):])
        full = os.path.join(REPO, rel.rstrip("/"))
        metas += copy_meta(n, rel)
        if n["type"] == "folder":
            if rel:
                os.makedirs(full, exist_ok=True)
                folders.add(full)
            continue
        os.makedirs(os.path.dirname(full), exist_ok=True)
        folders.add(os.path.dirname(full))
        if os.path.basename(full) == ".env":   # a keys file: created empty when missing, never read or written over
            if not os.path.exists(full):
                open(full, "w").close(); made += 1
            continue
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
        if not os.path.isdir(d):
            continue
        other = [f for f in os.listdir(d) if f not in (".env", ".gitkeep")]
        if not other and not os.path.exists(os.path.join(d, ".gitkeep")):   # git keeps no empty folder, and ignores .env
            open(os.path.join(d, ".gitkeep"), "w").close()
            kept += 1
        elif other and os.path.exists(os.path.join(d, ".gitkeep")):   # not needed once the folder holds a file
            os.remove(os.path.join(d, ".gitkeep"))
    print(f"materialize: {copied} files copied from drafts, {made} empty files made, {kept} .gitkeep files, {metas} metadata files copied")


if __name__ == "__main__":
    main(sys.argv[1])
