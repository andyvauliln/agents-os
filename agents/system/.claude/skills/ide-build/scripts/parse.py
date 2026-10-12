"""Parse vision/docs/file-tree.md (+ feature-map.md, decisions.md) into a node list. Enrichment lives in enrich.py."""
import re, json, sys

VISION = "/mnt/project-files/vision"
DOCS = f"{VISION}/docs"      # knowledge base (D-033); file-tree.md and feature-map.md moved here
md = open(f"{DOCS}/file-tree.md", encoding="utf-8").read()
fm = open(f"{DOCS}/feature-map.md", encoding="utf-8").read()
lines = md.split("\n")

version = re.search(r"# Agent OS: File tree \((v[\d.]+)\)", md).group(1)

# ---------- 1. tree block ----------
start = lines.index("```text", lines.index("## 1. Tree"))
end = lines.index("```", start + 1)
tree_lines = lines[start + 1:end]

nodes = []
stack = []  # (depth, node)
for raw in tree_lines:
    if not raw.strip():
        continue
    m = re.search(r"[├└]── ", raw)
    if m:
        depth = m.start() // 4
        rest = raw[m.end():]
    else:
        depth = -1
        rest = raw
    if "#" in rest:
        # a '#' inside a name never happens in this tree
        name, comment = rest.split("#", 1)
    else:
        name, comment = rest, ""
    name, comment = name.strip(), comment.strip()
    num = None
    nm = re.match(r"^\[([\d.]+)\]\s*", comment)
    if nm:
        num = nm.group(1)
        comment = comment[nm.end():]
    while stack and stack[-1][0] >= depth:
        stack.pop()
    parent = stack[-1][1] if stack else None
    if parent is None:
        path = name
    else:
        path = parent["path"].rstrip("/") + "/" + name
    is_folder = name.endswith("/")
    ntype = "folder" if is_folder else "file"
    node = {
        "id": None,
        "num": num,
        "name": name,
        "path": path,
        "type": ntype,
        "is_link": (bool(re.search(r"\.link(\.|/|$)", name)) and name != "subagents.link/") or bool(parent and parent["name"] == "subagents.link/"),  # *.links.json is a real file
        "is_placeholder": "[" in name,
        "parent": parent["id"] if parent else None,
        "children": [],
        "summary": comment,
    }
    # stable id: number if unique, otherwise path-based
    node["_depth"] = depth
    nodes.append(node)
    if parent:
        parent["children"].append(node)
    stack.append((depth, node))

# ids: "n-<num>" when that number appears once; otherwise path slug
from collections import Counter
cnt = Counter(n["num"] for n in nodes if n["num"])
def slug(p):
    s = re.sub(r"[^A-Za-z0-9._-]+", "-", p).strip("-")
    return s[:180]
for n in nodes:
    if n["num"] and cnt[n["num"]] == 1:
        n["id"] = "n-" + n["num"]
    else:
        n["id"] = "p-" + slug(n["path"])
seen = Counter()
for n in nodes:
    seen[n["id"]] += 1
    if seen[n["id"]] > 1:
        n["id"] += f"-{seen[n['id']]}"
for n in nodes:
    n["children"] = [c["id"] for c in n["children"]]
byid = {n["id"]: n for n in nodes}
for n in nodes:
    if n["parent"] and not isinstance(n["parent"], str):
        pass
# parent was set to parent's id before ids existed -> fix
tmp = {}
for n in nodes:
    for cid in n["children"]:
        tmp[cid] = n["id"]
for n in nodes:
    n["parent"] = tmp.get(n["id"])

# ---------- 2. object sections ----------
obj_start = lines.index("## 2. Objects")
obj_end = next(i for i in range(obj_start, len(lines)) if lines[i].startswith("## Changelog"))
sections = {}   # num -> section
retired = []
cur = None
in_code = False
code_buf = []
code_lang = ""
for ln in lines[obj_start + 1:obj_end]:
    if ln.startswith("### "):
        head = ln[4:].strip()
        lead = re.match(r"^((?:\[[\d.]+\][, ]*)+)", head)
        nums = re.findall(r"\[([\d.]+)\]", lead.group(1)) if lead else []
        title_name = re.search(r"`([^`]+)`", head)
        note = re.sub(r"^(\[[\d.]+\][, ]*)+", "", head)
        note = re.sub(r"`[^`]+`", "", note).strip()
        cur = {"nums": nums, "heading": head, "name": title_name.group(1) if title_name else None,
               "note": note.strip("() "), "items": [], "examples": []}
        if re.search(r"\((retired|moved to|moved:|merged into)", head):
            cur["retired"] = True
            retired.append(cur)
        for nnum in nums:
            if not cur.get("retired"):
                sections[nnum] = cur
        continue
    if cur is None:
        continue
    s = ln.strip()
    if s.startswith("```"):
        if not in_code:
            in_code = True
            code_lang = s[3:] or "text"
            code_buf = []
        else:
            in_code = False
            target = cur["items"][-1] if cur["items"] else None
            cur["examples"].append({"lang": code_lang, "body": "\n".join(code_buf),
                                    "after": target["label"] if target else None})
        continue
    if in_code:
        # strip the common 2-space indent used inside bullets
        code_buf.append(ln[2:] if ln.startswith("  ") else ln)
        continue
    if not s or s == "---":
        continue
    indent = len(ln) - len(ln.lstrip())
    if s.startswith("- "):
        body = s[2:]
        lm = re.match(r"^\*\*(.+?)\*\*:?\s*(.*)$", body)
        label, text = None, body
        if lm and (lm.group(1).endswith(":") or body[len(lm.group(0)) - len(lm.group(2)) - 1:].startswith(" ") or True):
            lab = lm.group(1).rstrip(":")
            # only treat as label when bold chunk is at start and followed by ':' (inside or after)
            if lm.group(1).endswith(":") or body.startswith("**" + lm.group(1) + "**:"):
                label, text = lab, lm.group(2).lstrip(": ").strip()
        if indent >= 2 and cur["items"]:
            cur["items"][-1]["sub"].append(text if not label else f"**{label}:** {text}")
        else:
            cur["items"].append({"label": label or "Note", "text": text, "sub": []})
    else:
        if cur["items"]:
            cur["items"][-1]["sub"].append(s)
        else:
            cur["items"].append({"label": "Note", "text": s, "sub": []})

# ---------- 3. decisions: docs/decisions.md (history log, D-033); fallback: the old [2.6] seed list ----------
import os
decisions = {}
if os.path.exists(f"{DOCS}/decisions.md"):
    dl = open(f"{DOCS}/decisions.md", encoding="utf-8").read().split("\n")
    for i, ln in enumerate(dl):
        hm = re.match(r"^#{2,4}\s+(D-\d{3})\s*[:.\-–]?\s*(.*)$", ln)
        if hm:
            body = []
            for l2 in dl[i + 1:]:
                if l2.startswith("#"):
                    break
                if l2.strip() and not l2.strip().startswith("<!--"):
                    body.append(l2.strip().lstrip("- "))
            first = next((b for b in body if re.match(r"(\*\*)?Decision", b)), body[0] if body else "")
            first = re.sub(r"^\*\*Decision:?\*\*:?\s*", "", first)
            decisions[hm.group(1)] = (hm.group(2).strip() + ": " + first).strip(": ") if first else hm.group(2).strip()
if not decisions and "2.6" in sections:
    seed = next((i for i in sections["2.6"]["items"] if i["label"].startswith("Seed entries")), None)
    for part in re.split(r" · ", seed["text"] if seed else ""):
        part = re.sub(r"^\*[^*]+\*\s*", "", part.strip())
        dm = re.match(r"(D-\d{3})\s+(.*)", part, re.S)
        if dm:
            decisions[dm.group(1)] = dm.group(2).strip()
decisions = dict(sorted(decisions.items()))

# ---------- 4. feature map ----------
features = {}  # num -> [ {area, logic, owner} ]
areas = []
area = None
for ln in fm.split("\n"):
    h = re.match(r"^## (\d+)\. (.+)$", ln)
    if h:
        area = h.group(2).strip()
        areas.append(area)
        continue
    if area and ln.startswith("|") and not ln.startswith("|---") and not ln.startswith("| Logic"):
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) < 2:
            continue
        logic, files = cells[0], cells[1]
        owner = cells[2] if len(cells) > 2 else ""
        for nnum in set(re.findall(r"\[([\d.]+)\]", files)):
            features.setdefault(nnum, []).append({"area": area, "logic": logic, "owner": owner})

json.dump({"version": version, "nodes": nodes, "sections": sections, "retired": retired,
           "decisions": decisions, "features": features, "areas": areas},
          open(sys.argv[1], "w"), indent=1, ensure_ascii=False)
print(len(nodes), "nodes;", len(sections), "section nums;", len(retired), "retired;",
      len(decisions), "decisions;", len(features), "feature nums")
