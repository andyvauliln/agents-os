# Handoff: continue the Agent OS planning in Claude Code

Updated 2026-10-14. Nothing of the system is built yet; this repository is the plan in its final shape. The files on disk are the tree (nothing is shown or made from a plan any more, 2026-10-13): files with a draft carry its text, empty files are marked on the page, and every item's How it works (`.index.md`) and Details (`.meta.json`) file sits next to it. Every file is its own source; the planning folder `vision/` was removed on 2026-10-14 (git history keeps it).

## Start here

1. `git pull` on `main`, then start Claude Code in `agents/system/`. It loads `agents/system/CLAUDE.md`, which says the project is at stage one and gives the reading order: `docs/vision.md`, `docs/README.md`, `agents/system/docs/vision.md` and `README.md`, `docs/file-tree.md`, `apps/project-IDE/docs/README.md`. Every README has an ASD-STE100 twin, `README.asd.md`.
2. The project IDE: `python3 apps/project-IDE/server/server.py` from the repo top serves the File Tree page with edits written back to the files (see `apps/project-IDE/server/README.md`). The request box needs `claude-agent-sdk` and a signed-in Claude Code; the mic needs `GROQ_API_KEY` in `.secrets/test/.env`. The same page is on claude.ai: https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs.
3. Rebuild after any change, from the repo top, as the `ide-build` skill says (`agents/system/.claude/skills/ide-build/SKILL.md`), with `S=agents/system/.claude/skills/ide-build/scripts`:
   - `python3 $S/materialize.py` (empty metadata files for new items, `.gitkeep`, `docs/file-tree.md`)
   - `python3 $S/build_map.py --stale` until it is clean (`--confirm <paths>` for each stale one that is still right)
   - `DATA_VERSION=N python3 $S/enrich.py` (writes the page data and `real-files.json` into `apps/project-IDE/current-ui/`)
   - `python3 $S/check_tree.py` must print "tree ok", and `node $S/check_page.js apps/project-IDE/current-ui -` must print "page ok"

## Where things stand

- Done: the name Agent OS; trading lives in the prediction-market domain (`agents/trading/prediction-market/`); the system vision, README and rebuild prompt in general terms; all How it works files fresh.
- Done 2026-10-09: the page lists every real file; edit in the Read view (double-click a paragraph); the inputs vision (D-062); the project IDE ran from `vision/` until 2026-10-14.
- Done 2026-10-12: the page tree is exactly the files in git; every planned item is a real file (`materialize.py`); each item's metadata files sit next to it on disk; `.secrets/` and its metadata are in git, and only the `.env` files with the keys stay out (D-063).
- Done 2026-10-12 (D-064): stage one set up: `agents/system/CLAUDE.md`, the docs at five levels with their metadata, prediction-market emptied to folders (its earlier files are in git history).
- Waiting for the owner: the stage-one defaults (keep `rebuild-prompt.md`, keep the prediction-market folder names, project docs in `docs/`); merge PR #5 (keys folder, metadata on disk, stage one). Open questions: scheduler machine (D-029), symlinks or rebuild for link files (D-031), v[N] placement (D-032), model defaults, jobs, D-058 defaults.
- Done 2026-10-14: the move out of `vision/`. The records (inputs, decisions, changelog, plans) are in `apps/project-IDE/data/`, the build scripts in `agents/system/.claude/skills/ide-build/scripts/`, the page in `apps/project-IDE/current-ui/`, the how-to guides in `agents/system/docs/how-to/`. Edit every file where it is.

## Rules to keep

- Never write a key value anywhere; key names only. `.env` files never go in git, and the page never reads or shows them.
- Every owner input goes into `apps/project-IDE/data/inputs/` word for word (skill `knowledge-intake`); decisions into `apps/project-IDE/data/decisions.md`; plan every change first (skill `change-plan`).
- The page tree must always equal the real file tree on disk.
- Call the owner "the owner" (they/them); docs for people are plain prose without ids or codes.
- Ask the owner before restructuring beyond what they asked, and before merging into `main`.
