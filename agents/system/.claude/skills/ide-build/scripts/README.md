# scripts: build the File Tree page data

These are the scripts of the `ide-build` skill (`agents/system/.claude/skills/ide-build/SKILL.md`, the project IDE agent's). They build the page data from the repository on disk: the files are the only source. The page and its data are in `apps/project-IDE/current-ui/`, the records in `apps/project-IDE/data/`. All are Python with the standard library only, except `check_page.js`, which needs Node and Playwright with Chromium.

## One build, from the top of the repository

`N` is the next data version: one more than `data_version` in the current `apps/project-IDE/current-ui/file-tree.data.json`.

```bash
S=agents/system/.claude/skills/ide-build/scripts
python3 $S/materialize.py                       # empty metadata files for new items, .gitkeep, docs/file-tree.md
python3 $S/build_map.py --stale                 # How it works files that are missing or stale, children first
# write each stale one again (file-index skill), or, when it is still right:
python3 $S/build_map.py --confirm <path> ...    # or: python3 $S/build_map.py --stale | python3 $S/build_map.py --confirm -
DATA_VERSION=N python3 $S/enrich.py             # apps/project-IDE/current-ui/file-tree.data.json and real-files.json
python3 $S/materialize.py                       # if it made files (a new built file), run build_map.py and enrich.py again
python3 $S/build_map.py                         # must say "... fresh, 0 missing or stale, 0 orphans ..."
python3 $S/check_tree.py                        # must say "tree ok"
node $S/check_page.js apps/project-IDE/current-ui - agent-os docs/README.md <the items this round changed>   # must say "page ok"
```

To start the IDE on the owner's server, `./start.sh` at the top of the repository runs `rebuild.py` instead of these steps: the same data, without a new version when nothing changed, and without writing How it works files or publishing.

`REPO_DIR` points every script at another checkout (default: the checkout the scripts sit in). `enrich.py` takes another data file as its argument, for a test build in a scratch folder; `real-files.json` is written next to it. `check_page.js` takes a screenshot folder instead of `-`.

## The items and their ids

An item is a file git keeps (`git ls-files --cached --others --exclude-standard`), a folder that holds one, or a local keys file (`.env`), which is listed but never read. The old planning folder is left out. An item's id is its path from the top of the repository, `docs/README.md` or `apps/project-IDE`; the top itself is `agent-os`. The page opens an item from its address: `file-tree-explorer.html#docs/README.md`.

## The scripts

| Script | What it does |
|---|---|
| `index_files.py` | Lists the items from git. Knows each item's metadata files: a file's are named after it without its last extension and sit beside it (`vision.md`: `vision.index.md`, `vision.meta.json`), a folder's sit inside it (`configs/configs.index.md`), the top has `agent-os.index.md`; a file whose name it shares with a sibling or its folder keeps its extension (`server.py.index.md`). Reads and writes How it works files, finds missing and orphan metadata files. |
| `enrich.py` | Writes the page data. For each item: its text into `real-files.json` (the page loads it when a file is opened; a file over 200 KB, a non-text file, a keys file and the built files are not put there), its How it works and Details files with the state of the How it works file, its Example (`x.example.md`, `.env.example` beside a `.env`), Questions (`x.questions.md`) and ASD-STE100 twin (`README.asd.md` beside `README.md`) when they exist, and the extra tabs from `tabs.py`. It applies the owner's kept edits of those tabs from `apps/project-IDE/data/overrides.json` (keyed by path), reads the decisions from `apps/project-IDE/data/decisions.md` for the page's pop-ups, and marks the empty files (0 bytes, or only `{}` or `[]`). |
| `tabs.py` | The field guides and extra tables by path or kind of file: settings fields, jobs, links, routes, tests, capabilities, key names (never values). |
| `materialize.py` | Gives every item outside stage two that has none an empty `x.index.md` and `x.meta.json` (a metadata file has none of its own; in the prediction-market domain only its `docs/` gets them). Keeps a `.gitkeep` in every empty folder and removes it once the folder holds a file. Writes `docs/file-tree.md`, every path in git without the metadata files. It copies nothing. |
| `build_map.py` | Checks the How it works files (below). `--stale`, `--empty`, `--context <path>`, `--set <file.json>`, `--confirm <path>...` (or `-` to read the paths from stdin), `--orphans`. Without an option it prints the report. |
| `check_tree.py` | Checks that the items of the page data are exactly the files in git, the folders that hold them and the top, with the path as each id; the local `.env` files are the only extra items. |
| `rebuild.py` | The rebuild for a start of the IDE, run by `start.sh` at the top of the repository. Runs `materialize.py`, builds the data into a scratch folder with the current data version and compares it with the data next to the page (without the `generated` time) and with `real-files.json`; only when something differs does it build in place with the next data version, so a restart with no change leaves git clean. Then it prints the `build_map.py` report and runs `check_tree.py`. Exit 0 when the tree check passes. It never writes How it works files and never publishes: a stale one is only reported. |
| `check_page.js` | Opens the page at a desktop and a phone width with a stand-in for the artifact runtime, opens each item it is given by its path in the address and its How it works and File tabs, and fails on a page error, a missing tab, an address that does not open its item, or a page wider than the phone. `PLAYWRIGHT`, `CHROMIUM` and `PLAYWRIGHT_LIBS` (a folder of libraries the browser needs and the system lacks) override the module, browser and library paths; when they are not set, it reads them from `.playwright.env` at the top of the repository, which `./init.sh` writes on each machine (git ignores it). |

## How it works files and their basis

Every item but a metadata file has a How it works file (docs/metadata.md, sections 5 and 9). Its front matter holds `about`, `written`, `by`, and the `basis` and `confirmed` that `build_map.py` writes. The basis is a hash of the item's own content (nothing for a folder, a keys file or a built file: the page data, `real-files.json`, `docs/file-tree.md`) and, for a folder, the names and How it works texts of the items inside it. A file with the same basis is fresh, another basis is stale, no file is missing, and a file with nothing written yet is empty: it is counted on its own and written later with the `file-index` skill.

When a child's How it works text changes, its folder becomes stale, so a change goes up from the bottom. `--confirm` writes the new basis and the `confirmed` time without touching the text, so the folder above does not become stale because of it. `--set` takes `{path: text}` or `{path: {text, keep: [...], sections: [{title, text}]}}` and writes the files (writer from `BY`, default `knowledge-base-agent`).

The build reads no knowledge notes and no tree notes: an item is described only by its own files.

One folder is plain data: `apps/project-IDE/data/sources/prediction-market/metadata/` (`KEPT` in `index_files.py`) holds the earlier metadata files of the prediction-market domain, kept as records. Nothing inside it gets metadata files, its `.index.md` and `.meta.json` files show as plain files with their text, and none of them is an orphan; the folder itself has its own metadata like any folder.

## Where the page lives

The page source is `apps/project-IDE/current-ui/file-tree-explorer.html`, with `file-tree.data.json` and `real-files.json` next to it. Publish it with the Artifact tool by url (https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs) with `files: {"file-tree.data.json": ..., "real-files.json": ...}`. The page shows its own source on its File tab, so put the finished page in place before you build. On the owner's server, `apps/project-IDE/server/server.py` serves the same folder.

## How page saves reach the files ("sync the file tree")

The page saves at once into its store, not into these files (on the owner's server the store is `apps/project-IDE/data/page-store/` and file and How it works edits are also written straight into their files):

- `nodes/<key>`: one document per item the owner touched, `{fields: {field: new value}, qa: [{q, a, at}], comments, deleted, new_node: {...}, updated_at, by}`. The key is the item's id (its path) with `/` and every other sign but letters, digits, `.`, `_` and `-` written as `~XX` (`docs/README.md` is `docs~2FREADME.md`); decode it by turning `~` back into `%` and URL-decoding. `fields.content` is the file's text as edited on the File tab, `fields.how_md` the How it works text.
- `changes/<auto id>`: the history `{at, by, title, instruction, kind, items: [{node_id, path, kind, fields: {k: {before, after}}}], undone}`; `node_id` there is the path itself.
- `inputs/<auto id>`: every message sent on the page, with `node_id` and `path`.

The `ide-sync` skill folds them in: each edited text into its file, each How it works edit into the item's `x.index.md` word for word (`by: owner`), then `build_map.py --confirm <path>`, then a new build. Old documents keyed `n-...` or `r-...` belong to ids that no longer exist; read their `path` from the matching `changes` and `inputs` documents.
