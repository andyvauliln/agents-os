"""Checks the How it works files of every item against the item itself (docs/metadata.md sections 9 and 10).

The items are the files in git and their folders (index_files.py); an item's id is its path from the top of the
repository, and the top itself is `agent-os`. Every item outside stage two, except a metadata file, has a How it
works file. Its "basis" is a hash of:
  - the content of the item (a file's bytes; nothing for a folder, a local keys file or a built output),
  - for a folder, the names of its items and the text of their How it works files.
A file whose front matter holds the same basis is fresh; another basis is stale; no file is missing; a file with
nothing in it yet is empty (written later, by the knowledge base agent's file-index skill).

  python3 build_map.py                      # the report: "how it works files: N fresh, M missing or stale, K orphans ..."
  python3 build_map.py --stale              # the missing or stale ones, children first: path, state
  python3 build_map.py --empty              # the empty ones (nothing written yet)
  python3 build_map.py --context <path>     # everything needed to write one item's How it works
  python3 build_map.py --set <file.json>    # write {path: text} or {path: {text, keep: [...], sections: [{title, text}]}} (by = $BY or "knowledge-base-agent")
  python3 build_map.py --confirm <path>...  # the file is right (also after editing it by hand): store the new basis, keep the text
  python3 build_map.py --confirm -          # the same for every path read from stdin (first column), e.g. from --stale
  python3 build_map.py --orphans            # metadata files whose item is gone (remove them, or move them to an archive)

enrich.py imports states() to show each How it works file's state on the page.
"""
import datetime, fcntl, hashlib, json, os, sys
import index_files as IF

LOCK_PATH = os.path.join(IF.REPO, ".git", "ide-build.index.lock")
# outputs of the build itself: they change every round, so their content is not part of the basis
BUILT = {"apps/project-IDE/current-ui/file-tree.data.json", "apps/project-IDE/current-ui/real-files.json", "docs/file-tree.md"}


def h(s):
    return hashlib.sha1(s.encode("utf-8") if isinstance(s, str) else s).hexdigest()[:12]


def content_hash(item):
    if item["type"] != "file" or item["name"] == ".env" or item["rel"] in BUILT:   # a keys file is never read
        return ""
    try:
        with open(os.path.join(IF.REPO, item["rel"]), "rb") as f:
            return h(f.read())
    except OSError:
        return ""


def body_of(rec):
    return (rec or {}).get("body", "").strip()


def bases(items, summaries):
    byid = {it["id"]: it for it in items}
    out = {}
    for it in items:
        if not IF.has_meta(it):
            continue
        kids = [byid[c] for c in it["children"] if IF.has_meta(byid[c])] if it["type"] == "folder" else []
        out[it["id"]] = h(json.dumps([content_hash(it), [[k["name"], h(body_of(summaries.get(k["id"])))] for k in kids]]))
    return out


def state_of(rec, basis):
    if rec is None:
        return "missing"
    if not body_of(rec) and not rec.get("basis"):
        return "empty"
    return "fresh" if rec.get("basis") == basis else "stale"


def states(items, summaries=None):
    """-> {id: {"basis", "state"}} for every item that has a How it works file."""
    summaries = IF.load_all(items) if summaries is None else summaries
    return {i: {"basis": b, "state": state_of(summaries.get(i), b)} for i, b in bases(items, summaries).items()}


def find(items, key):
    key = key.strip()
    k = key[len(IF.ROOT) + 1:] if key.startswith(IF.ROOT + "/") else key
    k = k.rstrip("/")
    for it in items:
        if key == it["id"] or k == it["rel"] or (not k and it["rel"] == ""):
            return it
    return None


def post_order(items):
    byid = {it["id"]: it for it in items}
    out, st = [], [(items[0]["id"], False)]
    while st:
        x, done = st.pop()
        if done:
            out.append(x); continue
        st.append((x, True))
        for c in reversed(byid[x]["children"]):
            st.append((c, False))
    return out


def context(items, it, summaries, st):
    byid = {x["id"]: x for x in items}
    meta = IF.load_meta(it) or {}
    print(f"# {IF.about(it)}  ({it['type']}, how it works: {st.get(it['id'], {}).get('state', 'none')})")
    print(f"how it works file: {IF.index_file(it)}\ndetails file: {IF.meta_file(it)}")
    if meta.get("about"):
        print(f"about: {meta['about']}")
    if it["type"] == "file" and it["name"] != ".env":
        try:
            text = open(os.path.join(IF.REPO, it["rel"]), encoding="utf-8").read()
            print(f"\n## Content ({len(text)} characters; first 60 lines)\n" + "\n".join(text.split("\n")[:60]))
        except (OSError, UnicodeDecodeError):
            print("\n## Content: not a text file")
    if it["children"]:
        print("\n## Inside")
        for c in it["children"]:
            x = byid[c]
            if not IF.has_meta(x):
                continue
            s = summaries.get(c)
            print(f"- {x['name']}: {(s or {}).get('text') or '(no How it works yet)'}")
    if it["id"] in summaries:
        rec = summaries[it["id"]]
        print(f"\n## Current How it works\n{body_of(rec) or '(empty)'}")


def main():
    args = sys.argv[1:]
    items = IF.load_items()
    summaries = IF.load_all(items)
    st = states(items, summaries)
    byid = {it["id"]: it for it in items}
    if "--context" in args:
        it = find(items, args[args.index("--context") + 1])
        if not it:
            sys.exit("unknown item")
        context(items, it, summaries, st)
        return
    if "--set" in args or "--confirm" in args:
        lock = open(LOCK_PATH, "w"); fcntl.flock(lock, fcntl.LOCK_EX)   # several workers may save at once
        summaries = IF.load_all(items)
        rendered = set()
        by = os.environ.get("BY", "knowledge-base-agent")
        at = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        ids = []
        if "--set" in args:
            new = json.load(open(args[args.index("--set") + 1], encoding="utf-8"))
            for k, t in new.items():
                it = find(items, k)
                if not it or not IF.has_meta(it):
                    print("unknown item", k); continue
                rec = t if isinstance(t, dict) else {"text": t}
                keep = [x.strip() for x in rec.get("keep") or [] if x.strip()]
                secs = [{"title": x["title"].strip(), "text": x["text"].strip()} for x in rec.get("sections") or [] if x.get("title") and x.get("text")]
                text = next((x["text"] for x in secs if x["title"].lower() == "what it is"), None) or rec.get("text", "").strip()
                r = {"text": text, "basis": "", "at": at, "by": by} | ({"keep": keep} if keep else {}) | ({"sections": secs} if secs else {})
                r["body"] = IF.make_body(it, r)
                summaries[it["id"]] = r
                ids.append(it["id"]); rendered.add(it["id"])
        else:
            keys = args[args.index("--confirm") + 1:]
            if keys == ["-"]:
                keys = [l.split("\t")[0].split()[0] for l in sys.stdin if l.strip()]
            for k in keys:
                it = find(items, k)
                if not it or not IF.has_meta(it):
                    print("unknown item", k); continue
                ids.append(it["id"])
        # bases depend on the children's texts: compute them after all texts are in, children first
        order = [i for i in post_order(items) if i in set(ids)]
        new_bases = bases(items, summaries)
        for i in order:
            rec = summaries.setdefault(i, {"text": "", "at": "", "by": "", "body": ""})
            rec["basis"] = new_bases[i]
            if "--confirm" in args:
                rec["confirmed"] = at
            IF.save(byid[i], rec, rec.get("body", ""))
        fcntl.flock(lock, fcntl.LOCK_UN); lock.close()
        summaries = IF.load_all(items)
        st = states(items, summaries)
        print(f"{'set' if '--set' in args else 'confirmed'} {len(order)}; missing or stale now: {sum(1 for x in st.values() if x['state'] in ('missing', 'stale'))}")
    order = [i for i in post_order(items) if i in st]
    if "--orphans" in args:
        for f in IF.orphans(items):
            print(f)
        return
    if "--stale" in args:
        for i in order:
            if st[i]["state"] in ("missing", "stale"):
                print(f"{i}\t{st[i]['state']}")
        return
    if "--empty" in args:
        for i in order:
            if st[i]["state"] == "empty":
                print(i)
        return
    count = lambda *s: sum(1 for i in order if st[i]["state"] in s)
    print(f"items {len(items)}, with a How it works file {len(st)}")
    print(f"how it works files: {count('fresh')} fresh, {count('missing', 'stale')} missing or stale, {len(IF.orphans(items))} orphans (--orphans); "
          f"{count('empty')} empty, not written yet (--empty)")
    lacking = IF.missing(items)
    if lacking:
        print(f"{len(lacking)} metadata files missing (materialize.py makes them): " + ", ".join(p for _, p in lacking[:10]) + (" ..." if len(lacking) > 10 else ""))


if __name__ == "__main__":
    main()
