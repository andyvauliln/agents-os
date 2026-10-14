---
name: ide-build
description: Build the File Tree page (the owner's IDE) from the repository, check it, test it and publish it at the same link. Use it after every round that changed the tree notes, a doc, a draft or a How it works file, after a pull that brought changes, and as the last step of ide-sync.
---

# IDE build: from the repository to the page

The File Tree page shows the owner every folder and file of the Agent OS, with its How it works, its text, its example and its extra tabs. The page reads one data file. This skill rebuilds that file from the repository, checks that every How it works file is current, tests the page and publishes it. The scripts it uses sit next to this file in `scripts/`.

## What the page is built from

| Input | Where in the repository | While we plan (`vision/`) |
|---|---|---|
| The tree notes: the numbered tree and one section per file and folder | `apps/project-IDE/data/file-tree.md` | `docs/file-tree.md` |
| The knowledge: topic notes with knowledge tags, decisions, inputs | `agents/system/docs/`, `apps/project-IDE/data/` | `docs/` |
| The drafts: docs for people, agents, skills, scripts | their own places in the tree | `.claude/` (with `CLAUDE.md`), `tools/` |
| How it works of every file and folder | `vision.index.md` next to `vision.md` (the name without its extension), `f/f.index.md` inside each folder; the Details files the same with `.meta.json` | next to the drafts, otherwise `tree/agent-os/...` |
| The owner's page edits kept in the data | `apps/project-IDE/data/overrides.json` | `tools/overrides.json` |
| What already exists in the repository | the repository itself | a checkout in `REPO_DIR` |

The output is `apps/project-IDE/current-ui/file-tree.data.json` (while we plan: `vision/file-tree.data.json`, copied to `vision/explorer/`), next to the page `file-tree-explorer.html`.

## The scripts

| Script | What it does |
|---|---|
| `parse.py` | Reads the tree notes into a list of items with their sections, the decisions and the feature map. |
| `enrich.py` | Adds drafts, examples, knowledge, How it works and tabs, applies the overrides, and writes the page data. Set `DATA_VERSION` to the next number. |
| `materialize.py` | Keeps files on disk in step with vision/: drafts copied over their real files, metadata copied next to items, empty metadata for the rest, .gitkeep in empty folders, docs/file-tree.md. Makes nothing from the plan (owner, 2026-10-13). |
| `tabs.py` | The field guides and extra tabs: settings fields, jobs, links, tests, key names. Used by `enrich.py`. |
| `build_map.py` | Builds the knowledge map, and checks the How it works files: `--stale`, `--orphans`, `--context <id>`, `--confirm <id> ...`, `--set <file.json>`. |
| `index_files.py` | Knows where each How it works (`.index.md`) and Details (`.meta.json`) file lives; reads and writes them; `ensure_meta` makes the empty Details files. |
| `check_page.js` | Opens the page on a desktop and a phone width with a stand-in for the artifact runtime; fails on a page error, a missing tab or a page wider than the phone. |

All but `check_page.js` are Python with the standard library only. `check_page.js` needs Node and Playwright with Chromium.

## Steps

While we plan, in the cloud project (`T` is a scratch folder outside the shared folder, `N` the next data version, one more than the `data_version` in the current data file):

```bash
cd /mnt/project-files/vision/tools
python3 parse.py $T/parsed.json
DATA_VERSION=N python3 enrich.py $T/parsed.json ../file-tree.data.json
python3 materialize.py ../file-tree.data.json   # drafts and metadata onto the files on disk (run enrich again if it changed anything)
cp ../file-tree.data.json ../explorer/file-tree.data.json
python3 build_map.py                  # must end "... fresh, 0 missing or stale, 0 orphans"
node check_page.js ../explorer $T/shots n-0 n-2.1 <the items this round changed>
```

1. **Parse and enrich** with the next data version.
2. **Check the How it works files.** `python3 build_map.py --stale` lists the missing or stale ones, children first, and `--orphans` lists index files whose item is gone. Hand the stale ones to the knowledge base agent's `file-index` skill (or follow it yourself), move orphans to the archive with their date, and run the build again until nothing is stale and nothing is orphaned.
3. **Copy** the data next to the page.
4. **Test.** Run `check_page.js` on the root, the README and every item the round changed. Look at the screenshots of anything you changed on the page itself. Nothing is published while a check fails.
5. **Publish** the page by its link, https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs, with the data file next to it (`files: {"file-tree.data.json": <path>}`). It keeps the same link, so the owner's notes and edits waiting on the page stay where they are.
6. **Report** in plain words what the owner will see changed: new or moved items, items whose status changed, docs that read differently.

In the repository the steps are the same, run from `agents/system/.claude/skills/ide-build/scripts/` with the paths in the table above.

## When you change the page itself

The page source is `file-tree-explorer.html`. The page shows its own source on its File tab, read from `explorer/` when the data is built, so put the finished page in `explorer/` before you build. The data file shows itself as the page loaded it, read-only. Keep a copy of the version before your change, change it in small steps, run `check_page.js` after each, and look at a desktop and a phone screenshot in both light and dark. A Markdown file always opens as a readable page; How it works always shows its file name and an Edit button; nothing on the page may be wider than a phone screen.

## Rules

- The page data is built, never edited or merged by hand. After a merge, build again.
- The status an item shows comes from its notes: decided unless its section or tree line says proposed, placeholder for names in brackets, example for the example agent. Anything new you add is marked proposed until the owner agrees.
- No secret values in the data, ever: a keys file shows only key names.
- A new draft for an item (a doc, an agent, a skill) is added to the drafts list in `index_files.py` so its How it works file sits next to it and the page shows its text.

## Checks

- `build_map.py` reports every How it works file fresh, none missing, no orphans.
- `check_page.js` prints "page ok".
- The page tree lists exactly the files in git (`git ls-files --cached --others --exclude-standard`), plus the two local-only `.env` files. This is how the page stays in step with the disk.
- The data version on the page is the new one, and the items the round changed show what the round changed.
