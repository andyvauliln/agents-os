"""Knowledge map for the Agent OS knowledge base (D-032).

Reads every doc in vision/docs/ (knowledge tags, see docs/README.md) plus the node list of
file-tree.data.json and works out which knowledge applies to which file or folder.

  python3 build_map.py                      # rebuild docs/index/knowledge-map.json, print problems + stale count
  python3 build_map.py --stale              # list nodes whose "How it works" summary is missing or stale, children first
  python3 build_map.py --context <node>     # everything needed to write one node's summary (node = id, [n] or path)
  python3 build_map.py --set <file.json>    # write {node: text} or {node: {text, keep: [...], sections: [{title, text}]}} into each node's index file (by = $BY or "knowledge-agent")
  python3 build_map.py --confirm <node>...  # the index file is right (also after editing it by hand): store the new basis, keep the text
  python3 build_map.py --orphans            # index files whose file or folder is gone (move them to archive/<date>/tree/)

The How it works of every node lives in its own Markdown file, `{name}.index.md` (tools/index_files.py),
in the mirror tree vision/tree/ while we plan. docs/index/summaries.json is retired (archive/2026-10-05/).

enrich.py imports build() to bake the map and the summaries into the explorer data.
"""
import json, re, os, sys, hashlib, datetime, fnmatch
import index_files as IF

HERE = os.path.dirname(os.path.abspath(__file__))
VISION = os.path.dirname(HERE)
DOCS = os.path.join(VISION, "docs")
INDEX = os.path.join(DOCS, "index")
MAP_PATH = os.path.join(INDEX, "knowledge-map.json")
LOCK_PATH = os.path.join(IF.TREE, ".index.lock")
DATA_PATH = os.path.join(VISION, "file-tree.data.json")

TAG = re.compile(r"<!--\s*k:\s*(.*?)\s*-->")
HEAD = re.compile(r"^(#{1,6})\s+(.*)$")


def h(s):
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:12]


def rel(path):
    return path[len("agent-os/"):] if path.startswith("agent-os/") else ("" if path == "agent-os" else path)


def glob_rx(pat):
    out, i = "", 0
    while i < len(pat):
        if pat.startswith("**", i):
            out += ".*"; i += 2
            if i < len(pat) and pat[i] == "/":
                out = out[:-2] + "(?:.*/)?"; i += 1
        elif pat[i] == "*":
            out += "[^/]*"; i += 1
        elif pat[i] == "?":
            out += "[^/]"; i += 1
        else:
            out += re.escape(pat[i]); i += 1
    return re.compile("^" + out + "/?$")


def parse_attrs(s):
    a = {}
    for part in s.split():
        if "=" in part:
            k, v = part.split("=", 1)
            a[k.strip()] = v.strip()
    return a


def doc_files():
    for root, dirs, files in os.walk(DOCS):
        dirs[:] = sorted(d for d in dirs if d not in ("inputs",))
        for f in sorted(files):
            if f.endswith(".md"):
                yield os.path.relpath(os.path.join(root, f), DOCS)


def read_doc(relpath):
    """-> (title, [entries]) for a topic doc; entries carry raw applies."""
    text = open(os.path.join(DOCS, relpath), encoding="utf-8").read()
    lines = text.split("\n")
    title = next((l.lstrip("# ").strip() for l in lines if l.startswith("# ")), relpath)
    heads = []  # (line_no, level, heading, attrs or None)
    fence = False
    for i, ln in enumerate(lines):
        if ln.strip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = HEAD.match(ln)
        if not m:
            continue
        attrs = None
        for j in range(i + 1, min(i + 3, len(lines))):
            t = TAG.search(lines[j])
            if t:
                attrs = parse_attrs(t.group(1)); break
            if lines[j].strip() and not lines[j].strip().startswith("<!--"):
                break
        heads.append((i, len(m.group(1)), m.group(2).strip(), attrs))
    entries = []
    for k, (i, lvl, head, attrs) in enumerate(heads):
        if attrs is None:
            continue
        end = len(lines)
        for (j, l2, _, a2) in heads[k + 1:]:
            if l2 <= lvl or a2 is not None:
                end = j; break
        body = "\n".join(l for l in lines[i + 1:end] if not TAG.search(l)).strip()
        entries.append({"id": attrs.get("id"), "doc": relpath, "heading": head, "level": lvl, "line": i + 1,
                        "applies_raw": [x for x in attrs.get("applies", "").split(",") if x],
                        "sources": [x for x in attrs.get("sources", "").split(",") if x],
                        "status": attrs.get("status", "decided"), "text": body, "hash": h(head + "\n" + body)})
    return title, entries, h(text)


def file_tree_sections():
    """file-tree.md object sections -> {heading: entry}; the file docs layer."""
    p = os.path.join(DOCS, "file-tree.md")
    if not os.path.exists(p):
        p = os.path.join(VISION, "file-tree.md")
    lines = open(p, encoding="utf-8").read().split("\n")
    out, cur, buf = {}, None, []
    try:
        start = lines.index("## 2. Objects")
    except ValueError:
        start = 0

    def flush():
        if cur:
            body = "\n".join(buf).strip()
            nums = re.findall(r"\[([\d.]+)\]", re.match(r"^((?:\[[\d.]+\][, ]*)+)", cur).group(1)) if re.match(r"^\[", cur) else []
            retired = bool(re.search(r"\((retired|moved to|moved:|merged into)", cur))
            out[cur] = {"id": "ft-" + (nums[0] if nums else h(cur)), "doc": "file-tree.md", "heading": cur, "nums": nums,
                        "status": "retired" if retired else "file-doc", "text": body, "hash": h(cur + "\n" + body)}
    for ln in lines[start + 1:]:
        if ln.startswith("## "):
            break
        if ln.startswith("### "):
            flush(); cur, buf = ln[4:].strip(), []
        elif cur is not None:
            buf.append(ln)
    flush()
    return out


def load_json(p, default):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return default


def build(nodes, summaries=None):
    """nodes: explorer node dicts (id, num, name, path, type, parent, children, summary, purpose, section_heading)."""
    summaries = IF.load_all(nodes) if summaries is None else summaries
    byid = {n["id"]: n for n in nodes}
    bynum = {}
    for n in nodes:
        if n.get("num"):
            bynum.setdefault(n["num"], []).append(n["id"])
    problems = []

    def subtree(nid):
        out, st = [], [nid]
        while st:
            x = st.pop(); out.append(x); st += byid[x].get("children") or []
        return out

    def resolve(item):
        """-> (direct ids, inherited ids)"""
        m = re.fullmatch(r"\[([\d.]+)\](/\*\*)?", item)
        if m:
            ids = bynum.get(m.group(1), [])
            if not m.group(2):
                return ids, []
            inh = [d for i in ids for d in subtree(i)[1:]]
            return ids, inh
        if item.startswith("path:"):
            rx = glob_rx(item[5:])
            return [n["id"] for n in nodes if rx.match(rel(n["path"]))], []
        if item.startswith("name:"):
            rx = glob_rx(item[5:])
            return [n["id"] for n in nodes if rx.match(n["name"])], []
        if item in ("none", "root"):
            return [], []
        return None, None

    # topic docs
    docs, entries = {}, {}
    for rp in doc_files():
        if rp == "file-tree.md":
            continue
        title, ents, dh = read_doc(rp)
        docs[rp] = {"title": title, "hash": dh, "entries": []}
        for e in ents:
            if not e["id"]:
                problems.append(f"{rp}:{e['line']} tag without id"); continue
            if e["id"] in entries:
                problems.append(f"{rp}:{e['line']} duplicate id {e['id']} (also {entries[e['id']]['doc']})"); continue
            direct, inh = set(), set()
            for it in e["applies_raw"]:
                d, i = resolve(it)
                if d is None:
                    problems.append(f"{rp}:{e['line']} {e['id']}: bad applies item {it!r}"); continue
                if not d and it not in ("none", "root"):
                    problems.append(f"{rp}:{e['line']} {e['id']}: applies {it!r} matches nothing")
                direct |= set(d); inh |= set(i)
            e["nodes"], e["inherited_by"] = sorted(direct), sorted(inh - direct)
            entries[e["id"]] = e
            docs[rp]["entries"].append(e["id"])
    # file docs
    ft = file_tree_sections()
    file_docs = {}
    for head, s in ft.items():
        file_docs[s["id"]] = s
    node_fd = {}
    for n in nodes:
        sh = n.get("section_heading")
        if sh and sh in ft:
            node_fd[n["id"]] = ft[sh]["id"]
        elif n.get("num") and ("ft-" + n["num"]) in file_docs and file_docs["ft-" + n["num"]]["status"] != "retired":
            node_fd[n["id"]] = "ft-" + n["num"]
    # per node
    nmap = {}
    for n in nodes:
        nmap[n["id"]] = {"num": n.get("num"), "path": rel(n["path"]), "name": n["name"], "type": n["type"],
                         "parent": n.get("parent"), "children": n.get("children") or [],
                         "file_doc": node_fd.get(n["id"]), "same_as": n.get("same_as"), "direct": [], "inherited": []}
    for eid, e in entries.items():
        for nid in e["nodes"]:
            nmap[nid]["direct"].append(eid)
        for nid in e["inherited_by"]:
            nmap[nid]["inherited"].append(eid)
    for nid, x in nmap.items():
        n = byid[nid]
        fd = file_docs.get(x["file_doc"]) if x["file_doc"] else None
        kids = [h((summaries.get(c) or {}).get("text", "")) for c in x["children"]]
        basis_src = json.dumps([n.get("summary") or "", n.get("purpose") or "", fd["hash"] if fd else "",
                                sorted(entries[e]["hash"] for e in x["direct"]), kids])
        x["basis"] = h(basis_src)
        s = summaries.get(nid)
        x["summary_state"] = "missing" if not s else ("fresh" if s.get("basis") == x["basis"] else "stale")
        if not x["file_doc"] and not x["direct"] and not x["inherited"] and not x["same_as"]:
            problems.append(f"node {nid} ({x['path']}) has no file doc and no knowledge")
    # inputs
    inputs = load_json(os.path.join(DOCS, "inputs", "index.json"), {"inputs": []})
    inp = {}
    for i in inputs.get("inputs", []):
        inp[i["id"]] = {k: i.get(k) for k in ("at", "where", "file", "categories", "summary", "processed_into")}
        inp[i["id"]]["entries"] = []
    for eid, e in entries.items():
        for s in e["sources"]:
            if s.startswith("in-"):
                if s in inp:
                    inp[s]["entries"].append(eid)
                else:
                    problems.append(f"{e['doc']}:{e['line']} {eid}: unknown input {s}")
    return {
        "schema_version": 1,
        "built": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "docs": docs,
        "entries": {k: {kk: v for kk, v in e.items() if kk not in ("text",)} | {"chars": len(e["text"])} for k, e in entries.items()},
        "file_docs": {k: {kk: v for kk, v in s.items() if kk != "text"} for k, s in file_docs.items()},
        "nodes": nmap,
        "inputs": inp,
        "problems": problems,
    }, entries, file_docs


def post_order(nmap, root):
    out, st = [], [(root, False)]
    while st:
        x, done = st.pop()
        if done:
            out.append(x); continue
        st.append((x, True))
        for c in reversed(nmap[x]["children"]):
            st.append((c, False))
    return out


def find_node(nodes, key):
    key = key.strip()
    for n in nodes:
        if key in (n["id"], f"[{n.get('num')}]", n.get("num"), n["path"], rel(n["path"])):
            return n
    return None


def main():
    args = sys.argv[1:]
    data = load_json(DATA_PATH, None)
    _scanned = {n["id"] for n in data["nodes"] if n.get("scanned")}   # real files found by the scan have no index file (D-061)
    nodes = [dict(n, children=[c for c in n.get("children") or [] if c not in _scanned]) for n in data["nodes"] if n["id"] not in _scanned]
    summaries = IF.load_all(nodes)
    m, entries, file_docs = build(nodes, summaries)
    byid = {n["id"]: n for n in nodes}
    root = data.get("root") or nodes[0]["id"]
    if "--context" in args:
        n = find_node(nodes, args[args.index("--context") + 1])
        x = m["nodes"][n["id"]]
        print(f"# {x['path'] or 'agent-os/'}  ({n['id']}, [{n.get('num') or '-'}], {n['type']}, status {n.get('status')})")
        print(f"tree comment: {n.get('summary') or ''}\npurpose: {n.get('purpose') or ''}")
        if x["file_doc"]:
            fd = file_docs[x["file_doc"]]
            print(f"\n## File doc: file-tree.md / {fd['heading']}\n{fd['text']}")
        elif x["same_as"]:
            print(f"\n## Same layout as {x['same_as']} ({byid[x['same_as']]['path']})")
        for eid in x["direct"]:
            e = entries[eid]
            print(f"\n## Knowledge {eid} ({e['doc']} / {e['heading']}, {e['status']})\n{e['text']}")
        if x["inherited"]:
            print("\n## From folders above: " + "; ".join(f"{e} ({entries[e]['heading']})" for e in x["inherited"]))
        if x["children"]:
            print("\n## Children")
            for c in x["children"]:
                s = summaries.get(c, {}).get("text") or "(no summary yet) " + (byid[c].get("summary") or "")
                print(f"- {byid[c]['name']} [{byid[c].get('num') or '-'}]: {s}")
        if n["id"] in summaries:
            print(f"\n## Current summary ({x['summary_state']})\n{summaries[n['id']]['text']}")
            for sec in summaries[n["id"]].get("sections") or []:
                print(f"- {sec['title']}: {sec['text']}")
            for k in summaries[n["id"]].get("keep") or []:
                print(f"- keep in mind: {k}")
        return
    if "--set" in args or "--confirm" in args:
        # several workers may save at once: hold a lock and re-read the file inside it
        import fcntl
        os.makedirs(IF.TREE, exist_ok=True)
        lock = open(LOCK_PATH, "w"); fcntl.flock(lock, fcntl.LOCK_EX)
        summaries = IF.load_all(nodes)
        rendered = set()
        by = os.environ.get("BY", "knowledge-agent")
        at = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        if "--set" in args:
            new = load_json(args[args.index("--set") + 1], {})
            ids = []
            for k, t in new.items():
                n = find_node(nodes, k)
                if not n:
                    print("unknown node", k); continue
                rec = t if isinstance(t, dict) else {"text": t}
                keep = [k.strip() for k in rec.get("keep") or [] if k.strip()]
                secs = [{"title": x["title"].strip(), "text": x["text"].strip()} for x in rec.get("sections") or [] if x.get("title") and x.get("text")]
                # the six-heading files are read back with "What it is" as their text: store the same, so parents' bases hold
                text = next((x["text"] for x in secs if x["title"].lower() == "what it is"), None) or rec.get("text", "").strip()
                summaries[n["id"]] = {"text": text, "basis": "", "at": at, "by": by} | ({"keep": keep} if keep else {}) | ({"sections": secs} if secs else {})
                ids.append(n["id"]); rendered.add(n["id"])
        else:
            ids = [find_node(nodes, k)["id"] for k in args[args.index("--confirm") + 1:]]
        # bases depend on children's texts: recompute after all texts are in
        m, _, _ = build(nodes, summaries)
        for i in ids:
            rec = summaries.setdefault(i, {"text": "", "at": at, "by": by})
            rec["basis"] = m["nodes"][i]["basis"]
            if "--confirm" in args:
                rec["confirmed"] = at
            IF.save(byid[i], rec, None if i in rendered or not rec.get("body") else rec["body"])
        fcntl.flock(lock, fcntl.LOCK_UN); lock.close()
        m, _, _ = build(nodes, summaries)
        print(f"set {len(ids)}; stale now: {sum(1 for x in m['nodes'].values() if x['summary_state'] != 'fresh')}")
    os.makedirs(INDEX, exist_ok=True)
    json.dump(m, open(MAP_PATH, "w"), indent=1, ensure_ascii=False)
    order = post_order(m["nodes"], root)
    stale = [i for i in order if m["nodes"][i]["summary_state"] != "fresh"]
    if "--orphans" in args:
        for f in IF.orphans(nodes):
            print("tree/" + f)
        return
    if "--stale" in args:
        for i in stale:
            print(f"{i}\t{m['nodes'][i]['summary_state']}\t{m['nodes'][i]['path'] or 'agent-os/'}")
        return
    print(f"docs {len(m['docs'])}, entries {len(m['entries'])}, file docs {len(m['file_docs'])}, nodes {len(m['nodes'])}, inputs {len(m['inputs'])}")
    print(f"how it works files: {sum(1 for x in m['nodes'].values() if x['summary_state'] == 'fresh')} fresh, {len(stale)} missing or stale, {len(IF.orphans(nodes))} orphans (--orphans)")
    for p in m["problems"][:80]:
        print("problem:", p)
    if len(m["problems"]) > 80:
        print(f"... {len(m['problems']) - 80} more problems")


if __name__ == "__main__":
    main()
