---
name: ide-build
description: Build the File Tree page (the owner's IDE) from the repository, check it, test it and publish it at the same link. Use it after every round that changed a file, a folder or a metadata file, after a pull that brought changes, and as the last step of ide-sync.
---

# IDE build: from the repository to the page

The File Tree page shows the owner every folder and file of the Agent OS, with its How it works, its text, its Details and its other tabs. The page reads one data file. This skill rebuilds that file from the repository, checks that every How it works file is current, tests the page and publishes it. The scripts it uses sit next to this file in `scripts/`; `scripts/README.md` tells each script's options.

## What the page is built from

The files on disk are the only source. There is no tree plan, no number and no knowledge note in the build.

| Input | Where in the repository |
|---|---|
| The items: every file git keeps, the folders that hold them, the local keys files (`.env`, listed, never read) | the repository itself (`git ls-files --cached --others --exclude-standard`), without the old planning folder |
| Each item's text | the file itself |
| How it works and Details of every item | `x.index.md` and `x.meta.json` beside a file `x.md`, `f/f.index.md` and `f/f.meta.json` inside a folder `f/`, `agent-os.index.md` at the top |
| The other tabs | `x.example.md` (`.env.example` beside a `.env`), `x.questions.md`, `README.asd.md` beside `README.md`; the extra tables come from the kind of file (`scripts/tabs.py`) |
| The owner's kept edits of the extra tables | `apps/project-IDE/data/overrides.json`, keyed by path |
| The decisions the page shows when one is named | `apps/project-IDE/data/decisions.md` |

An item's id is its path from the top of the repository (`docs/README.md`, `apps/project-IDE`); the top is `agent-os`. The output is `apps/project-IDE/current-ui/file-tree.data.json` and `real-files.json` (the text of every file, loaded by the page when one is opened), next to the page `file-tree-explorer.html`.

## The scripts

| Script | What it does |
|---|---|
| `enrich.py` | Reads every item and its metadata files and writes the page data and `real-files.json`. Set `DATA_VERSION` to the next number. |
| `materialize.py` | Gives new items their empty `x.index.md` and `x.meta.json` (outside stage two), keeps `.gitkeep` in empty folders, writes `docs/file-tree.md`. Copies nothing. |
| `tabs.py` | The field guides and extra tabs: settings fields, jobs, links, tests, key names. Used by `enrich.py`. |
| `build_map.py` | Checks the How it works files: `--stale`, `--empty`, `--orphans`, `--context <path>`, `--confirm <path> ...` (or `-` for paths on stdin), `--set <file.json>`. |
| `index_files.py` | Lists the items and knows where each How it works and Details file lives; reads and writes them. |
| `check_tree.py` | Checks that the page tree equals the files in git, with paths as ids. |
| `rebuild.py` | The rebuild for a start of the IDE (`./start.sh`): materializes, builds in a scratch folder, and builds in place with the next data version only when the data changed; then the How it works report and the tree check. Writes no How it works file, never publishes. |
| `check_page.js` | Opens the page on a desktop and a phone width with a stand-in for the artifact runtime; fails on a page error, a missing tab, an address that does not open its item, or a page wider than the phone. |

All but `check_page.js` are Python with the standard library only. `check_page.js` needs Node and Playwright with Chromium.

## Steps

From the top of the repository. `N` is the next data version: one more than `data_version` in `apps/project-IDE/current-ui/file-tree.data.json`.

```bash
S=agents/system/.claude/skills/ide-build/scripts
python3 $S/materialize.py
python3 $S/build_map.py --stale
python3 $S/build_map.py --confirm <path> ...     # each stale file that is still right; write the others first
DATA_VERSION=N python3 $S/enrich.py
python3 $S/materialize.py                        # made anything? then build_map.py --stale and enrich.py again
python3 $S/build_map.py                          # must end "... fresh, 0 missing or stale, 0 orphans ..."
python3 $S/check_tree.py                         # must say "tree ok"
node $S/check_page.js apps/project-IDE/current-ui $T/shots agent-os docs/README.md <the items this round changed>
```

1. **Metadata for new items.** `materialize.py` gives every new file and folder its empty How it works and Details files and writes the plain tree.
2. **Check the How it works files.** `build_map.py --stale` lists the missing or stale ones, children first. A stale file is out of date with its item, or, for a folder, with what is inside. Hand the ones that are wrong to the knowledge base agent's `file-index` skill (or follow it yourself), confirm the ones that are still right with `--confirm <path>`, and remove orphans (`--orphans`: metadata files whose item is gone). `--empty` lists the How it works files nobody has written yet; they are not an error, and filling them is stage one work.
3. **Build the data** with the next data version. `enrich.py` writes the data and `real-files.json` next to the page.
4. **Check the tree.** `check_tree.py`: the page lists exactly the files in git and their folders, plus the local `.env` files.
5. **Test.** Run `check_page.js` on the top, the README and every item the round changed (`$T` is a scratch folder; use `-` for no screenshots). Look at the screenshots of anything you changed on the page itself. Nothing is published while a check fails.
6. **Publish** the page by its link, https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs, with the data files next to it (`files: {"file-tree.data.json": <path>, "real-files.json": <path>}`). It keeps the same link, so the owner's notes and edits waiting on the page stay where they are.
7. **Report** in plain words what the owner will see changed: new, moved or removed items, How it works files written again, docs that read differently.

## When you change the page itself

The page source is `apps/project-IDE/current-ui/file-tree-explorer.html`. The page shows its own source on its File tab, read when the data is built, so put the finished page in place before you build. The data file shows itself as the page loaded it, read-only. Keep a copy of the version before your change, change it in small steps, run `check_page.js` after each, and look at a desktop and a phone screenshot in both light and dark. A Markdown file always opens as a readable page; How it works always shows its file name and an Edit button; nothing on the page may be wider than a phone screen. The page keys its store documents for items by the path written with `~XX` for `/` and other signs (`scripts/README.md`).

## Rules

- The page data is built, never edited or merged by hand. After a merge, build again.
- The status an item shows comes from the `status` field of its Details file (`decided`, `proposed` or `idea`), and `decided` when the field is empty; a name in brackets is a placeholder. Anything new you add is proposed until the owner agrees.
- No secret values in the data, ever: a keys file shows only key names, and the build never opens it.
- A new file or folder needs no list anywhere: create it, and the build finds it and gives it its metadata files.

## Checks

- `build_map.py` reports every How it works file fresh, none missing or stale, no orphans.
- `check_tree.py` prints "tree ok": the page tree lists exactly the files in git (`git ls-files --cached --others --exclude-standard`) and their folders, plus the local-only `.env` files.
- `check_page.js` prints "page ok".
- The data version on the page is the new one, and the items the round changed show what the round changed.
