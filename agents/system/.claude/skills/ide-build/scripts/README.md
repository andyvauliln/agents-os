# tools: build file-tree.data.json

These are the scripts of the `ide-build` skill (`.claude/skills/ide-build/SKILL.md`, the project IDE agent's). In the repository they live in `agents/system/.claude/skills/ide-build/scripts/`, the page in `apps/project-IDE/current-ui/` and the records in `apps/project-IDE/data/` (D-041); while we plan they are here, in `vision/explorer/` and in `vision/docs/`.

Before publishing, run the page check: `node check_page.js ../explorer <screenshot dir or -> <node ids...>` opens the page on a desktop and a phone width with a stand-in for the artifact runtime and prints "page ok" or what failed (needs Playwright; `PLAYWRIGHT` and `CHROMIUM` override the module and browser paths).

`file-tree.data.json` (the File Tree explorer's data) is built from `../file-tree.md` plus hand-written knowledge:

```bash
cd /mnt/project-files/vision/tools
python3 parse.py /tmp/parsed.json                       # tree + [n] sections + decisions + feature map
DATA_VERSION=<next> python3 enrich.py /tmp/parsed.json ../file-tree.data.json
```

- `enrich.py` adds concepts, rules and example file contents, then the tab data from `tabs.py` (field guides, custom tables such as the .env Variables table, fake-value .env examples), reads real file contents from the repo checkout (`REPO_DIR`, read only; clone the latest repo first, or the real files are missing from the page), lists every real file under a folder that exists in the repo as a "scanned" item with no How it works of its own (D-061; only `.git/` and `.secrets/` are left out; their texts go to `real-files.json` next to the data, which the page loads when one is opened and which is published with it; `build_map.py` skips scanned items), and finally applies `overrides.json`.
- `overrides.json` holds owner edits folded in from the explorer page, keyed by `[n]` (fields replace the parsed ones). Keep it: rebuilding without it loses those edits.

## Where the page lives

The page source is `vision/explorer/file-tree-explorer.html`, with `vision/explorer/file-tree.data.json` (a copy of `../file-tree.data.json`) next to it. Publish it with the Artifact tool by url (https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs) with `files: {"file-tree.data.json": ...}`. Copy the source back here whenever you change it in a scratchpad.

## How it works files (D-039)

Every node's How it works is its own Markdown file, built and read by `index_files.py`: a file has one named after it without its extension (`vision.md`: `vision.index.md`; `.gitignore`: `.gitignore.index.md`; a file whose name would clash with a sibling's or its folder's keeps its extension, today only `server.py.index.md`), a folder `f/` has `f/f.index.md`. Next to each sits an empty Details file with the same name ending in `.meta.json` (`meta_path(node)`; `ensure_meta(nodes)` makes the missing ones; `enrich.py` puts it in each node's `meta` and its path in `meta_file`). Drafts that already exist in `vision/` (`index_files.DRAFTS`, `DRAFT_DIRS`: the people docs, the agent, the skills) keep theirs next to the draft, e.g. `vision/.claude/docs/README.index.md`; everything else is in the mirror tree `vision/tree/agent-os/...`. `enrich.py` takes `CLAUDE_DRAFTS` from `index_files.DRAFTS`; `VISION_FILES` in `enrich.py` shows other drafts in `vision/` (the scripts, `overrides.json`, the page source, the server files in `vision/server/`) on the File tab while their index files stay in the mirror. `enrich.py` puts the body in each node's `how_md` and the path in `how_file`; the page shows it and edits it (db `nodes/<id>.fields.how_md`). At a sync, write each edited `how_md` into the node's index file word for word (`by: owner`), then `python3 build_map.py --confirm <id>`. `build_map.py --orphans` lists index and Details files whose node is gone. The skill is `.claude/skills/file-index/SKILL.md`.

## How page saves reach the files ("sync the file tree")

The explorer saves instantly into its artifact db, not into these files:
- `nodes/<node id>`: `{fields: {field: new value}, qa: [{q, a, at}], plain: {text, basis, at}, deleted, new_node: {...}, updated_at, by}`. `fields` is the latest full value per field; `new_node` marks a node added on the page (id `new-...`, no [n] yet).
- `nodes/<node id>.fields.content`: the file's text as edited on the File tab. `nodes/<node id>.comments`: `[{id, line (null = whole file/folder), snippet (the line's text, used to re-anchor), text, at, by, resolved}]`.
- `changes/<auto id>`: history `{at, by, title, instruction, kind: edit|qa|ripple (ripple = related updates Claude saved automatically after an edit), items: [{node_id, path, kind: set|remove|new|qa, fields: {k: {before, after}}}], undone}`.

To fold them into the files: ArtifactData list `nodes` and `changes` → for each node with `fields`/`deleted`/`new_node`, change `file-tree.md` (bump version, changelog, give new nodes a [n], record decisions as D-0xx in the [2.6] seed list) → put the node's final `fields` (and `qa` if worth keeping) in `overrides.json` → rebuild with the next DATA_VERSION → republish the explorer with the new data file → delete the folded `nodes` docs (keep `plain` explanations by re-writing them as docs holding only `plain`, or let the page regenerate them). Leave `changes` as the history.

File content edited on the page goes into `overrides.json` as `content` (and, for the docs drafted in this folder, into that draft file). It is not written into the git repo until the owner asks for that. Open comments are applied if the owner says so, otherwise carried over as open questions.

## People docs on the page (D-034, D-036)

- Every `.md` file's File tab opens in Read view (D-038): `mdDoc()` in the page renders the Markdown (headings with ids, nested lists, tables, code, quotes, a skill's frontmatter as properties; `<!-- -->` tags dropped), `readerHTML()` wraps it with the white/black switch (`ftx-rtheme` in localStorage) and a full-screen mode. Source (`ftx-mdmode`) is the old line view with line comments.

- `enrich.py` `CLAUDE_DRAFTS` maps a node to its planning copy in `vision/.claude/` (agent, skills, `docs/README.md` for [2.1], `docs/vision.md` for [2.2]); the File tab shows that text. When a new doc is written, add its node here and in `DOC_SKILLS`.
- `enrich.py` `DOC_SKILLS` maps a doc node to its skill; the first ```` ```markdown ```` block under `## Outline` in the skill becomes the node's Example (`kind: "outline"`).
- `build_map.py --set` also takes `sections: [{title, text}]`. A node with sections shows only those headings, its keep lines, and the owner's waiting messages and page changes on How it works. Headings: What it is, Who looks after it, When and how it changes, Who uses it and when, Where it is mentioned, Related knowledge.
