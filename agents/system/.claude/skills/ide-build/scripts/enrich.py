"""Builds the File Tree page data from the repository on disk (docs/metadata.md section 11).

    DATA_VERSION=<next> python3 enrich.py [data file]
    # default data file: apps/project-IDE/current-ui/file-tree.data.json; real-files.json is written next to it

The items are the files git keeps (`git ls-files --cached --others --exclude-standard`), the folders that hold
them and the local keys files (.env, listed but never read), without the old planning folder (index_files.py). Each item's id is
its path from the top of the repository; the top is `agent-os`. For each item it reads:
  - its text, into real-files.json (the page loads it the first time a file is opened);
  - its How it works file (x.index.md) and Details file (x.meta.json), with the state of the How it works
    file from build_map.py;
  - its Example (x.example.md, or .env.example beside a .env), Questions (x.questions.md) and ASD-STE100 twin
    (README.asd.md beside README.md), when they exist;
  - the extra tabs that come from the kind of file (tabs.py): field guides, jobs, links, key names, tests;
  - the owner's page edits kept for the extra tabs (apps/project-IDE/data/overrides.json, keyed by path).
It also reads the decisions (apps/project-IDE/data/decisions.md) so the page can show one when it is named.
REPO_DIR overrides the repository (default: the checkout these scripts sit in). Standard library only.
"""
import datetime, json, os, re, sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import index_files as IF
import build_map
import tabs

REPO = IF.REPO
UI = "apps/project-IDE/current-ui"
DATA = "apps/project-IDE/data"
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(REPO, UI, "file-tree.data.json")
DATA_FILE = UI + "/file-tree.data.json"     # the page data shows itself as the page loaded it
REAL_FILE = UI + "/real-files.json"         # the texts of the files; it cannot hold itself
MAX = 200000                                # a bigger file is not put on the page
STATUSES = ("decided", "proposed", "idea")


def read_text(rel):
    try:
        return open(os.path.join(REPO, rel), encoding="utf-8").read()
    except (OSError, UnicodeDecodeError):
        return None


def decisions():
    """D-0xx: the title and the decision line of each decision in decisions.md, for the page's pop-ups."""
    text = read_text(DATA + "/decisions.md") or ""
    lines, out = text.split("\n"), {}
    for i, ln in enumerate(lines):
        hm = re.match(r"^#{2,4}\s+(D-\d{3})\s*[:.\-–]?\s*(.*)$", ln)
        if not hm:
            continue
        body = []
        for l2 in lines[i + 1:]:
            if l2.startswith("#"):
                break
            if l2.strip() and not l2.strip().startswith("<!--"):
                body.append(l2.strip().lstrip("- "))
        first = next((b for b in body if re.match(r"(\*\*)?Decision", b)), body[0] if body else "")
        first = re.sub(r"^\*\*Decision:?\*\*:?\s*", "", first)
        out[hm.group(1)] = (hm.group(2).strip() + ": " + first).strip(": ") if first else hm.group(2).strip()
    return [{"id": k, "text": v} for k, v in sorted(out.items())]


def is_empty(it):
    """Nothing written yet: 0 bytes, or only {} or [] (a file over 64 bytes never is; .gitkeep and .env never are)."""
    if it["type"] != "file" or it["name"] in (".gitkeep", ".env"):
        return False
    f = os.path.join(REPO, it["rel"])
    try:
        size = os.path.getsize(f)
    except OSError:
        return False
    if size == 0:
        return True
    if size > 64:
        return False
    t = read_text(it["rel"])
    return t is not None and t.strip() in ("", "{}", "[]")


items = IF.load_items()
summaries = IF.load_all(items)
states = build_map.states(items, summaries)
ov_path = os.path.join(REPO, DATA, "overrides.json")
OV = json.load(open(ov_path, encoding="utf-8")) if os.path.isfile(ov_path) else {}
REAL_FILES = {}
nodes = []
for it in items:
    rel, name = it["rel"], it["name"]
    meta = IF.load_meta(it) if IF.has_meta(it) else None
    m = meta if isinstance(meta, dict) else {}
    about = (m.get("about") or "").strip()
    status = "placeholder" if "[" in name else (m.get("status") if m.get("status") in STATUSES else "decided")
    sources = m.get("sources") if isinstance(m.get("sources"), dict) else {}
    x = {"id": it["id"], "name": name, "path": IF.about(it), "type": it["type"], "link": bool(it["link"] or re.search(r"\.link(\.|/|$)", name)),
         "placeholder": "[" in name, "parent": it["parent"], "children": list(it["children"]), "status": status,
         "summary": about, "purpose": about or None,
         "link_target": os.readlink(os.path.join(REPO, rel)) if it["link"] else None,
         "decisions": [d for d in sources.get("decisions") or [] if isinstance(d, str)],
         "open_questions": [], "qa": [], "example": None, "exists": True, "content": None}
    # the text of a file: never a keys file; the page data shows itself; everything else from real-files.json
    if it["type"] == "file":
        x["src_file"] = rel
        if name == ".env":
            x.update({"local_only": True, "content_source": "a keys file: it stays on the machine, git ignores it and the page never shows what is in it",
                      "readonly": "Keys are never shown or edited here. Write them in the file on the machine."})
            del x["src_file"]
        elif rel == DATA_FILE:
            x.update({"content_self": True, "content_source": "this page's data file, exactly as the page loaded it",
                      "readonly": "Built by ide-build from the files in the repository and their metadata files. It is rebuilt every round, never edited by hand."})
        elif rel == REAL_FILE:
            x.update({"content_source": "the texts of the files, built next to the page data; open it in the repository",
                      "readonly": "Built by ide-build every round, never edited by hand."})
        elif os.path.getsize(os.path.join(REPO, rel)) > MAX:
            x["content_source"] = f"the repository: {rel} (too large for the page; open it in the repository)"
        else:
            text = read_text(rel)
            if text is None:
                x["content_source"] = f"the repository: {rel} (not a text file)"
            else:
                REAL_FILES[it["id"]] = text
                x.update({"content_lazy": True, "content_source": f"the repository: {rel}"})
    # How it works and Details: every item but a metadata file has them (docs/metadata.md section 3)
    if IF.has_meta(it):
        s = summaries.get(it["id"])
        st = states.get(it["id"], {}).get("state")
        body = (s or {}).get("body", "").strip()
        x["how"] = {"text": s["text"], "keep": s.get("keep") or [], "sections": s.get("sections") or [], "at": s.get("at"),
                    "by": s.get("by"), "state": st} if s and s.get("text") else None
        x["how_md"] = body + "\n" if body else None
        x["how_state"] = st
        x["how_file"] = IF.index_file(it)
        x["meta_file"] = IF.meta_file(it)
        x["meta"] = meta
        x["fam"] = it["fam"]
    # the extra tab files: a tab shows only when its file exists (owner, 2026-10-12)
    home = IF.meta_home(it)
    j = lambda n: os.path.join(home, n) if home else n
    if it["type"] == "file" and not IF.is_meta_file(name, rel):
        ex_rel = j(".env.example") if name == ".env" else j(it["fam"] + ".example.md")
        ex = read_text(ex_rel) if os.path.isfile(os.path.join(REPO, ex_rel)) else None
        if ex is not None:
            x["example"] = {"lang": "dotenv" if name == ".env" else "markdown", "title": os.path.basename(ex_rel), "body": ex, "file": ex_rel}
    if IF.has_meta(it):
        q_rel = j(it["fam"] + ".questions.md")
        q = read_text(q_rel) if os.path.isfile(os.path.join(REPO, q_rel)) else None
        if q is not None:
            x["questions_md"], x["questions_file"] = q, q_rel
    if name == "README.md":
        a_rel = j("README.asd.md")
        a = read_text(a_rel) if os.path.isfile(os.path.join(REPO, a_rel)) else None
        if a is not None:
            x["asd_md"], x["asd_file"] = a, a_rel
    # the tabs that come from the kind of file: field guides, jobs, links, key names, tests, an agent's overview
    x["fields"] = tabs.fields_for(x)
    x["custom_tabs"] = tabs.custom_tabs_for(x)
    x["agent"] = tabs.agent_for(x)
    for k, v in (OV.get(it["id"]) or {}).items():   # the owner's kept page edits of those tabs
        if k in ("custom_tabs", "fields"):
            x[k] = v
    if is_empty(it):
        x["empty"] = True
    nodes.append(x)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(os.path.join(os.path.dirname(OUT), "real-files.json"), "w", encoding="utf-8") as f:
    json.dump(REAL_FILES, f, ensure_ascii=False)
dv = int(os.environ.get("DATA_VERSION", "1"))
data = {
    "schema_version": 2,
    "title": "Agent OS file tree",
    "source": {"repo": "the files in git (without the old planning folder), their folders and the local keys files, with every item's metadata files",
               "doc_version": f"v{dv}"},
    "generated": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    "data_version": dv,
    "sync": "Built by the ide-build scripts from the files on disk and the metadata files next to each item. The page saves straight away into its own store (collections inputs, nodes, changes); at a sync (\"sync the file tree\") the project IDE agent saves them word for word, writes edits into their files and rebuilds this file.",
    "status_legend": {
        "decided": "agreed by the owner",
        "proposed": "an agent's proposal, waiting for the owner",
        "idea": "kept for later",
        "placeholder": "a pattern such as [agent-name]; real names come later",
    },
    "root": items[0]["id"],
    "concepts": [],
    "decisions": decisions(),
    "nodes": nodes,
}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=1, ensure_ascii=False)
print(len(nodes), "items;", sum(1 for x in nodes if x["type"] == "folder"), "folders;", len(REAL_FILES), "texts in real-files.json;",
      sum(1 for x in nodes if x.get("empty")), "empty files")
print("how it works:", dict(Counter(x.get("how_state") for x in nodes if x.get("how_file"))))
print("tabs:", sum(1 for x in nodes if x.get("example")), "examples,", sum(1 for x in nodes if x.get("questions_file")), "questions,",
      sum(1 for x in nodes if x.get("asd_file")), "ASD-STE100,", sum(1 for x in nodes if x.get("custom_tabs") or x.get("fields")), "with extra tabs")
