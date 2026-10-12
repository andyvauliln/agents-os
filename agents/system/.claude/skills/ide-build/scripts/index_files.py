"""How it works and metadata of every file and folder, one file each (owner, 2026-10-05; names 2026-10-07, D-057).

A file's metadata files are named after it without its last extension and sit next to it: `vision.md` has
`vision.index.md` (How it works) and `vision.meta.json` (metadata). A folder `f/` has `f/f.index.md` and
`f/f.meta.json` inside it. A name with no extension stays whole (`.gitignore.index.md`). Where two files in one
folder, or a file and its folder, would share a name (`server/server.py` and `server/`), the file keeps its
extension (`server.py.index.md`). While we plan, the real files do not exist yet, so these files sit in a mirror
of the planned tree: vision/tree/agent-os/... Files and folders that already exist as drafts in this folder
(DRAFTS, DRAFT_DIRS: the people docs, the agents, the skills) keep theirs next to the draft, e.g.
vision/.claude/docs/README.index.md. When the repo is built they all move next to the real files.

Each index file:

    ---
    about: agent-os/agents/system/docs/README.md     # what it describes
    node: n-2.1                                       # its node on the File Tree page
    basis: 1a2b3c4d5e6f                               # hash of what it was written from (build_map.py)
    written: 2026-10-05T07:31:00Z
    by: knowledge-base-agent
    confirmed: 2026-10-05T09:40:00Z                   # optional: checked and still right
    ---
    # README.md

    ## What it is            (fixed headings, D-036) ... or ## Summary for files not moved yet
    ...
    ## Keep in mind
    - When you ..., ...

Each metadata file is JSON with the fields of the file-set plan (vision/plans/file-set.md), empty for now.

build_map.py reads and writes the index files through load_all() and save(); enrich.py reads the metadata files.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
VISION = os.path.dirname(HERE)
TREE = os.path.join(VISION, "tree")
ROOT = "agent-os"
FIXED = ["What it is", "Who looks after it", "When and how it changes", "Who uses it, and when", "Where it is mentioned", "Related knowledge"]
KEEP = "Keep in mind"
META_KEYS = ["about", "node", "basis", "written", "by", "confirmed"]
# nodes whose draft already exists in vision/ (by [n]): their index file sits next to the draft, not in the mirror
DRAFTS = {"2.1": ".claude/docs/README.md",
          "2.2": ".claude/docs/vision.md",
          "10.1.1.2": ".claude/agents/knowledge-base-agent.md",
          "10.1.1.3": ".claude/agents/project-ide-agent.md",
          "10.1.2.5.1": ".claude/skills/ide-build/SKILL.md",
          "10.1.2.6": ".claude/skills/ide-sync/SKILL.md",
          "10.1.5": ".claude/CLAUDE.md",
          "10.1.2.1": ".claude/skills/knowledge-intake/SKILL.md",
          "10.1.2.2": ".claude/skills/file-index/SKILL.md",
          "10.1.2.3": ".claude/skills/vision-doc/SKILL.md",
          "10.1.2.4": ".claude/skills/readme-doc/SKILL.md",
          "2.22": ".claude/docs/rebuild-prompt.md",
          "2.23": ".claude/docs/inputs-vision.md",
          "10.1.2.7": ".claude/skills/rebuild-prompt-doc/SKILL.md",
          "10.1.2.8": ".claude/skills/change-plan/SKILL.md"}
DRAFT_DIRS = {"10.1": ".claude/", "10.1.1": ".claude/agents/", "10.1.2": ".claude/skills/",
              "10.1.2.5": ".claude/skills/ide-build/"}


def _safe(seg):
    return re.sub(r",\s*", "+", seg.replace("|", "-"))


CLASH = set()   # ids of files that keep their extension: another family in the same folder has the same name


def family(name, keep_ext=False):
    """The family name of a file or folder: a file's name without its last extension, a folder's whole name."""
    nm = name.rstrip("/")
    if keep_ext or name.endswith("/"):
        return nm
    base, ext = os.path.splitext(nm)
    return base if base and ext else nm


def prepare(nodes):
    """Find the files whose family name is shared in their folder (with a sibling or with the folder itself)."""
    groups = {}
    for n in nodes:
        name = n.get("name") or ""
        if n.get("type") == "folder":
            groups.setdefault((n["id"], _safe(name.rstrip("/"))), []).append(None)
        elif n.get("parent") and not name.endswith(".index.md"):
            groups.setdefault((n["parent"], family(_safe(name))), []).append(n["id"])
    CLASH.clear()
    for ids in groups.values():
        if len(ids) > 1:
            CLASH.update(i for i in ids if i)


def family_rel(node, ending):
    """Path of one of the node's metadata files (ending ".index.md" or ".meta.json"), relative to vision/tree/."""
    p = node.get("path") or ROOT + "/"
    segs = [_safe(s) for s in p.rstrip("/").split("/") if s]
    if node.get("type") == "folder":
        return "/".join(segs + [segs[-1] + ending])
    if segs[-1].endswith(".index.md"):  # an index file has none of its own; (the retired pattern node [51] was its own example)
        return "/".join(segs)
    return "/".join(segs[:-1] + [family(segs[-1], node.get("id") in CLASH) + ending])


def index_rel(node):
    return family_rel(node, ".index.md")


def family_path(node, ending):
    num = node.get("num") or ""
    if num in DRAFTS:
        d, b = os.path.split(DRAFTS[num])
        return os.path.join(VISION, d, family(b, node.get("id") in CLASH) + ending)
    if num in DRAFT_DIRS:
        d = DRAFT_DIRS[num].rstrip("/")
        return os.path.join(VISION, d, os.path.basename(d) + ending)
    return os.path.join(TREE, family_rel(node, ending))


def index_path(node):
    return family_path(node, ".index.md")


def meta_path(node):
    return family_path(node, ".meta.json")


def index_file(node):
    """Where the node's index file is, relative to vision/ (shown on the page)."""
    return os.path.relpath(index_path(node), VISION)


def meta_file(node):
    return os.path.relpath(meta_path(node), VISION)


META_FIELDS = {"schema_version": 1, "about": "", "kind": "", "state": "", "status": "", "git": "", "secret": None,
               "generated_by": None, "writers": [], "readers": [], "changes_when": "", "related": [],
               "sources": {"decisions": [], "inputs": [], "notes": []}, "update_with": [], "inherits": [],
               "features": [], "views": [], "how_it_works": {}, "tree_number": ""}


def ensure_meta(nodes):
    """Write an empty metadata file for every node that has none (owner, 2026-10-07: empty for now)."""
    import json
    made = []
    for n in nodes:
        if (n.get("name") or "").endswith(".index.md"):
            continue
        f = meta_path(n)
        if not os.path.isfile(f):
            os.makedirs(os.path.dirname(f), exist_ok=True)
            with open(f, "w", encoding="utf-8") as fh:
                json.dump(META_FIELDS, fh, indent=2)
                fh.write("\n")
            made.append(f)
    return made


def split_front(text):
    m = re.match(r"^---\n(.*?)\n---[ \t]*\n?", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).split("\n"):
        k, _, v = line.partition(":")
        if k.strip():
            meta[k.strip()] = v.strip()
    return meta, text[m.end():]


def parse_body(body):
    """-> text (the main summary), sections [{title, text}] for the fixed format, keep lines."""
    parts = re.split(r"^##[ \t]+(.+?)[ \t]*$", body, flags=re.M)
    secs = [(parts[i].strip(), parts[i + 1].strip()) for i in range(1, len(parts) - 1, 2)]
    keep, rest = [], []
    for t, x in secs:
        if t.lower() == KEEP.lower():
            keep = [re.sub(r"^\s*[-*]\s+", "", l).strip() for l in x.split("\n") if re.match(r"^\s*[-*]\s+", l)]
        else:
            rest.append((t, x))
    summ = [x for t, x in rest if t.lower() == "summary"]
    if summ:
        return {"text": summ[0], "sections": [], "keep": keep}
    if rest:
        first = next((x for t, x in rest if t.lower() == FIXED[0].lower()), rest[0][1])
        return {"text": first, "sections": [{"title": t, "text": x} for t, x in rest], "keep": keep}
    plain = re.sub(r"^#\s+.*$", "", body, flags=re.M).strip()
    return {"text": plain, "sections": [], "keep": keep}


def title_of(node):
    return node.get("name") or ROOT + "/"


def make_body(node, rec):
    out = [f"# {title_of(node)}", ""]
    secs = rec.get("sections") or []
    if secs:
        for s in secs:
            out += [f"## {s['title']}", "", s["text"].strip(), ""]
    else:
        out += ["## Summary", "", (rec.get("text") or "").strip(), ""]
    keep = [k for k in rec.get("keep") or [] if k.strip()]
    if keep:
        out += [f"## {KEEP}", ""] + [f"- {k.strip()}" for k in keep] + [""]
    return "\n".join(out).rstrip() + "\n"


def load(node):
    f = index_path(node)
    if not os.path.isfile(f):
        return None
    text = open(f, encoding="utf-8").read()
    meta, body = split_front(text)
    rec = parse_body(body)
    rec.update({"basis": meta.get("basis", ""), "at": meta.get("written", ""), "by": meta.get("by", ""), "body": body, "file": index_file(node)})
    if meta.get("confirmed"):
        rec["confirmed"] = meta["confirmed"]
    return rec


def load_all(nodes):
    prepare(nodes)
    out = {}
    for n in nodes:
        r = load(n)
        if r is not None:
            out[n["id"]] = r
    return out


def save(node, rec, body=None):
    """Write the node's index file. body=None renders it from rec (text, sections, keep)."""
    f = index_path(node)
    os.makedirs(os.path.dirname(f), exist_ok=True)
    meta = {"about": node.get("path") or ROOT + "/", "node": node["id"], "basis": rec.get("basis", ""),
            "written": rec.get("at", ""), "by": rec.get("by", ""), "confirmed": rec.get("confirmed", "")}
    front = "---\n" + "".join(f"{k}: {meta[k]}\n" for k in META_KEYS if meta.get(k)) + "---\n"
    text = front + (body if body is not None else make_body(node, rec))
    tmp = f + ".tmp"
    open(tmp, "w", encoding="utf-8").write(text)
    os.replace(tmp, f)
    return f


def orphans(nodes):
    """Index files under tree/ whose object is gone (renamed or removed): archive them."""
    prepare(nodes)
    want = {os.path.normpath(p(n)) for n in nodes for p in (index_path, meta_path)}
    out = []
    for d, _, fs in os.walk(TREE):
        out += [os.path.relpath(os.path.join(d, f), TREE) for f in fs if f.endswith((".index.md", ".meta.json")) and os.path.normpath(os.path.join(d, f)) not in want]
    return sorted(out)
