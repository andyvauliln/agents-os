# Handoff: continue the Agent OS planning in Claude Code

Updated 2026-10-12. Nothing of the system is built yet; this repository is the plan in its final shape. Every planned file and folder exists on disk: files with a draft carry its text, the rest are empty, and every item's How it works (`.index.md`) and Details (`.meta.json`) file sits next to it. The planning sources are still in `vision/`.

## Start here

1. `git pull` on `main`, then start Claude Code in `agents/system/`. It loads `agents/system/CLAUDE.md`, which says the project is at stage one and gives the reading order: `docs/vision.md`, `docs/README.md`, `agents/system/docs/vision.md` and `README.md`, `docs/file-tree.md`, `apps/project-IDE/docs/README.md`. Every README has an ASD-STE100 twin, `README.asd.md`.
2. The project IDE: `python3 vision/server/server.py` from the repo top serves the File Tree page with edits written back to the files (see `vision/server/README.md`). The request box needs `claude-agent-sdk` and a signed-in Claude Code; the mic needs `GROQ_API_KEY` in `.secrets/test/.env`. The same page is on claude.ai: https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs (version 62).
3. Rebuild after any change, from `vision/tools/` (see its README and the `ide-build` skill), with `S` a scratch folder and `R` the repo:
   - `python3 parse.py $S/parsed.json`
   - `REPO_DIR=$R DATA_VERSION=N python3 enrich.py $S/parsed.json $S/ftd.json`, then copy it to `vision/file-tree.data.json` and `vision/explorer/`, and `$S/real-files.json` to `vision/explorer/`
   - `REPO_DIR=$R python3 materialize.py ../file-tree.data.json` (puts planned items, drafts and metadata files onto disk; run enrich again if it made new files)
   - `python3 build_map.py --stale` until it is clean (`--confirm <ids>` for each stale one), and `node check_page.js <page folder> -` must print "page ok"
   - Check: the page tree must list exactly the files in git (`git ls-files --cached --others --exclude-standard`), plus the two local-only `.env` files.

## Where things stand

- Done: the name Agent OS; trading lives in the prediction-market domain (`agents/trading/prediction-market/`); the system vision, README and rebuild prompt in general terms; all How it works files fresh.
- Done 2026-10-09: the page lists every real file; edit in the Read view (double-click a paragraph); the inputs vision (D-062); the project IDE runs from `vision/`.
- Done 2026-10-12: the page tree is exactly the files in git; every planned item is a real file (`materialize.py`); each item's metadata files sit next to it on disk; `.secrets/` and its metadata are in git, and only the `.env` files with the keys stay out (D-063).
- Done 2026-10-12 (D-064): stage one set up: `agents/system/CLAUDE.md`, the docs at five levels with their metadata, prediction-market emptied to folders (files in `vision/archive/2026-10-12/`).
- Waiting for the owner: the stage-one defaults (keep `rebuild-prompt.md`, keep the prediction-market folder names, project docs in `docs/`); merge PR #5 (keys folder, metadata on disk, stage one). Open questions: scheduler machine (D-029), symlinks or rebuild for link files (D-031), v[N] placement (D-032), model defaults, jobs, D-058 defaults.
- Not done (optional): make the real files the source and retire the drafts in `vision/` (the "full layout" move into `apps/project-IDE/` and `agents/system/`). Until then, edit the draft in `vision/`; the build copies it into place.

## Rules to keep

- Never write a key value anywhere; key names only. `.env` files never go in git, and the page never reads or shows them.
- Every owner input goes into `vision/docs/inputs/` word for word (skill `knowledge-intake`); decisions into `vision/docs/decisions.md`; plan every change first (skill `change-plan`).
- The page tree must always equal the real file tree on disk.
- Call the owner "the owner" (they/them); docs for people are plain prose without ids or codes.
- Ask the owner before restructuring beyond what they asked, and before merging into `main`.
