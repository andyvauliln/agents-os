"""The items of the tree and their metadata files, read from the repository on disk (docs/metadata.md).

An item is a file that git keeps (`git ls-files --cached --others --exclude-standard`), a folder that holds one,
or a local keys file (`.env`) that is on disk. Its id is its path from the top of the repository; the top itself
is `agent-os`. The old planning folder (SKIP) is left out.

A file's metadata files are named after it without its last extension and sit next to it: `vision.md` has
`vision.index.md` (How it works) and `vision.meta.json` (Details). A folder `f/` has `f/f.index.md` and
`f/f.meta.json` inside it; the top has `agent-os.index.md`. A name with no extension stays whole
(`.gitignore.index.md`). Where two files in one folder, or a file and its folder, would share a name
(`server/server.py` and `server/`), the file keeps its extension (`server.py.index.md`).

Each How it works file:

    ---
    about: agent-os/agents/system/docs/README.md     # what it describes
    basis: 1a2b3c4d5e6f                               # hash of what it was written from (build_map.py)
    written: 2026-10-05T07:31:00Z
    by: knowledge-base-agent
    confirmed: 2026-10-05T09:40:00Z                   # optional: checked and still right
    ---
    # README.md

    ## What it is            (the fixed headings of docs/metadata.md section 5)
    ...
    ## Keep in mind
    - When you ..., ...

build_map.py, enrich.py and materialize.py read the items and their metadata files through this module.
"""
import json, os, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = "agent-os"
SKIP = ("vision",)   # the old planning area is not part of the tree
FIXED = ["What it is", "Who looks after it", "When and how it changes", "Who uses it, and when", "Where it is mentioned", "Related knowledge"]
KEEP = "Keep in mind"
META_KEYS = ["about", "basis", "written", "by", "confirmed"]
# metadata and tab files have no metadata files of their own (docs/metadata.md section 3, rule 4)
META_ENDS = (".index.md", ".meta.json", ".example.md", ".questions.md", ".view.html", ".gitkeep", ".env.example")
STAGE_TWO = "agents/trading/prediction-market/"   # stage two (owner, 2026-10-12): nothing is made inside ...
PM_DOCS = STAGE_TWO + "docs"                      # ... except its docs, which have metadata like any item (owner, 2026-10-14)
# Kept data: the earlier metadata files of the prediction-market domain, kept as records when its old files left the
# tree. Everything inside this folder is a plain file: it has no metadata files of its own, a ".index.md" or
# ".meta.json" in it is data (shown with its text, never as a tab), and none of it counts as an orphan.
# The folder itself has its metadata like any folder.
KEPT = "apps/project-IDE/data/sources/prediction-market/metadata/"


def repo_dir():
    """The top of the repository: REPO_DIR, else the git checkout these scripts sit in."""
    if os.environ.get("REPO_DIR"):
        return os.path.realpath(os.environ["REPO_DIR"])
    try:
        return subprocess.run(["git", "-C", HERE, "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return os.path.realpath(os.path.join(HERE, *[".."] * 5))


REPO = repo_dir()


def kept_data(rel):
    """Whether the path is inside the kept-data folder (KEPT): plain data, no metadata of its own."""
    return rel.rstrip("/").startswith(KEPT)


def is_meta_file(name, rel=""):
    """Whether a file is a metadata or tab file. Pass `rel` so a file inside KEPT counts as plain data."""
    return not kept_data(rel) and name.rstrip("/").endswith(META_ENDS)


def stage_two(rel):
    rel = rel.rstrip("/")
    return rel.startswith(STAGE_TWO) and not (rel == PM_DOCS or rel.startswith(PM_DOCS + "/"))


def git_files(repo=None):
    """Every path git keeps or would keep (tracked, or untracked and not ignored), without the old planning folder."""
    repo = repo or REPO
    out = subprocess.run(["git", "-c", "core.quotepath=off", "-C", repo, "ls-files", "--cached", "--others", "--exclude-standard"],
                         capture_output=True, text=True, check=True).stdout.split("\n")
    return sorted({f for f in out if f and f.split("/")[0] not in SKIP and os.path.lexists(os.path.join(repo, f))})


def family(name, keep_ext=False):
    """The family name of a file or folder: a file's name without its last extension, a folder's whole name."""
    nm = name.rstrip("/")
    if keep_ext or name.endswith("/"):
        return nm
    base, ext = os.path.splitext(nm)
    return base if base and ext else nm


def load_items(repo=None):
    """-> list of items, the top first, every folder before what is inside it.
    An item: {id, rel, name, type, parent, children, link}. `rel` is the path from the top ("" for the top)."""
    repo = repo or REPO
    files = git_files(repo)
    # a keys file is never in git; it is on the machine only and is listed, never read (docs/metadata.md section 14)
    folders = {""}
    for f in files:
        parts = f.split("/")
        for i in range(1, len(parts)):
            folders.add("/".join(parts[:i]))
    envs = sorted(os.path.join(d, ".env") if d else ".env" for d in folders if os.path.isfile(os.path.join(repo, d, ".env")))
    paths = set(files) | set(envs)
    items = {"": {"id": ROOT, "rel": "", "name": ROOT + "/", "type": "folder", "parent": None, "children": [], "link": False}}
    for d in sorted(folders - {""}):
        items[d] = {"id": d, "rel": d, "name": os.path.basename(d) + "/", "type": "folder", "parent": None, "children": [], "link": False}
    for f in sorted(paths):
        full = os.path.join(repo, f)
        isdir = os.path.isdir(full) and not os.path.islink(full)
        items[f] = {"id": f, "rel": f, "name": os.path.basename(f) + ("/" if isdir else ""), "type": "folder" if isdir else "file",
                    "parent": None, "children": [], "link": os.path.islink(full)}
    for rel, it in items.items():
        if rel:
            par = os.path.dirname(rel)
            it["parent"] = items[par]["id"]
            items[par]["children"].append(rel)
    for it in items.values():
        it["children"] = order_children(it, [items[c] for c in it["children"]])
    for it in items.values():
        if it["type"] == "file":
            it["fam"] = file_family(it, items)
        else:
            it["fam"] = family(it["name"]) if it["rel"] else ROOT
    out, st = [], [""]
    while st:
        r = st.pop()
        out.append(items[r])
        st += [items_rel(c) for c in reversed(items[r]["children"])]
    return out


def items_rel(item_id):
    return "" if item_id == ROOT else item_id


def file_family(it, items):
    """A file's family name; it keeps its extension when a sibling file or its folder has the same family."""
    par = items[os.path.dirname(it["rel"])]
    own = family(it["name"])
    if par["rel"] and family(par["name"]) == own:
        return it["name"]
    same = [c for c in par["children"] if c != it["rel"] and items[c]["type"] == "file" and not is_meta_file(items[c]["name"], c)
            and family(items[c]["name"]) == own]
    if same and not is_meta_file(it["name"], it["rel"]):
        return it["name"]
    return own


def order_children(folder, kids):
    """The folder's own metadata files first, then its folders, then each file followed by its own metadata files."""
    fam_folder = family(folder["name"]) if folder["rel"] else ROOT
    own_meta = [k for k in kids if k["type"] == "file" and is_meta_file(k["name"], k["rel"]) and _meta_owner(k["name"]) == fam_folder]
    rest = [k for k in kids if k not in own_meta]
    sub = sorted((k for k in rest if k["type"] == "folder"), key=lambda k: k["name"].lower())
    files = [k for k in rest if k["type"] == "file"]
    plain = sorted((k for k in files if not is_meta_file(k["name"], k["rel"])), key=lambda k: k["name"].lower())
    metas = [k for k in files if is_meta_file(k["name"], k["rel"])]
    out, used = [], set()
    for f in plain:
        out.append(f)
        fams = {f["name"], family(f["name"])}
        for m in sorted(metas, key=lambda k: k["name"].lower()):
            if m["rel"] not in used and (_meta_owner(m["name"]) in fams or (f["name"] == ".env" and m["name"] == ".env.example")):
                out.append(m); used.add(m["rel"])
    out += [m for m in sorted(metas, key=lambda k: k["name"].lower()) if m["rel"] not in used]
    order = sorted(own_meta, key=lambda k: k["name"].lower()) + sub + out
    return [k["id"] for k in order]


def _meta_owner(name):
    for end in (".index.md", ".meta.json", ".example.md", ".questions.md"):
        if name.endswith(end):
            return name[:-len(end)]
    return None


def meta_home(item):
    """The folder an item's metadata files sit in: inside a folder, beside a file (relative to the top)."""
    return item["rel"] if item["type"] == "folder" else os.path.dirname(item["rel"])


def family_rel(item, ending):
    home = meta_home(item)
    name = item["fam"] + ending
    return os.path.join(home, name) if home else name


def index_file(item):
    return family_rel(item, ".index.md")


def meta_file(item):
    return family_rel(item, ".meta.json")


def index_path(item):
    return os.path.join(REPO, index_file(item))


def meta_path(item):
    return os.path.join(REPO, meta_file(item))


def has_meta(item):
    """Whether the item has (or must have) its How it works and Details files: every item but a metadata file,
    outside stage two; in stage two only where they already exist; never inside the kept-data folder (KEPT)."""
    if kept_data(item["rel"]):
        return False
    if item["type"] == "file" and is_meta_file(item["name"]):
        return False
    if stage_two(item["rel"]):
        return os.path.isfile(index_path(item))
    return True


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


def title_of(item):
    return item["name"]


def make_body(item, rec):
    out = [f"# {title_of(item)}", ""]
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


def load(item):
    """The item's How it works file as a record, or None when it has none."""
    f = index_path(item)
    if not os.path.isfile(f):
        return None
    text = open(f, encoding="utf-8").read()
    meta, body = split_front(text)
    rec = parse_body(body)
    rec.update({"basis": meta.get("basis", ""), "at": meta.get("written", ""), "by": meta.get("by", ""), "body": body,
                "file": index_file(item), "front": bool(meta)})
    if meta.get("confirmed"):
        rec["confirmed"] = meta["confirmed"]
    return rec


def load_all(items):
    return {it["id"]: r for it in items if has_meta(it) for r in [load(it)] if r is not None}


def about(item):
    return ROOT + "/" + item["rel"] + ("/" if item["type"] == "folder" and item["rel"] else "")


def save(item, rec, body=None):
    """Write the item's How it works file. body=None renders it from rec (text, sections, keep)."""
    f = index_path(item)
    os.makedirs(os.path.dirname(f), exist_ok=True)
    meta = {"about": about(item), "basis": rec.get("basis", ""), "written": rec.get("at", ""), "by": rec.get("by", ""),
            "confirmed": rec.get("confirmed", "")}
    front = "---\n" + "".join(f"{k}: {meta[k]}\n" for k in META_KEYS if meta.get(k)) + "---\n"
    text = front + (body if body is not None else make_body(item, rec))
    tmp = f + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.replace(tmp, f)
    return f


def load_meta(item):
    try:
        return json.load(open(meta_path(item), encoding="utf-8"))
    except (OSError, ValueError):
        return None


def orphans(items):
    """How it works and Details files whose item is gone (renamed or removed): remove them or archive them.
    The files inside the kept-data folder (KEPT) are data, not orphans."""
    want = {p(it) for it in items if has_meta(it) for p in (index_file, meta_file)}
    return sorted(it["rel"] for it in items if it["type"] == "file" and it["name"].endswith((".index.md", ".meta.json"))
                  and not kept_data(it["rel"]) and it["rel"] not in want)


def missing(items):
    """Items that must have metadata files and lack one: -> [(item, path)]."""
    return [(it, p(it)) for it in items if has_meta(it) for p in (index_file, meta_file) if not os.path.isfile(os.path.join(REPO, p(it)))]
