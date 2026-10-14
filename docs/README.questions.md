# Questions: README.md

## Open questions for the owner

- **Should the records (inputs, decisions, changelog, tree notes, plans) move from `vision/docs/` into `apps/project-IDE/data/`?** The README describes both places; it decides which one is the source.
- **Should `docs/file-tree.md` list the metadata files too, or only the items?** Listing every `.index.md` and `.meta.json` roughly doubles the file; leaving them out makes it a cleaner map.
- **Should the logs and data of agents be ignored by git again?** The current `.gitignore` no longer has the rules that keep runtime `logs/` and `data/` and research clones in `apps/temp/` out of git, which the owner asked for earlier.
- **Is `HANDOFF.md` still needed once `agents/system/CLAUDE.md` is the entry point?** Both tell a new session where to start, and two starting points can disagree.

## The owner's questions

### 2026-10-05: The layout of the repository

> i think we should have something like this what do you think?

The layout was agreed: the repository itself is the tree. Today the top holds `README.md`, `HANDOFF.md`, `.gitignore`, `.secrets/`, `docs/` (the project docs), `agents/` (the system and trading), `apps/` (the project IDE, `trading-ui/`, `temp/` and the apps' docs) and the planning area `vision/`. This changed later: there is no `CLAUDE.md` or `researches/` at the top; `CLAUDE.md` is in `agents/system/`, the research studies are in `agents/trading/researches/`, and `trading-ui/` and the project IDE are in `apps/`.

Docs improved: none, the answer was already in docs/README.md (how the repository is laid out).

### 2026-10-06: The difference between the vision and the README

> i am a bit confused what suppose to be difference between vision and readme?

The vision is the top-level doc: what we build and why, the concept, how it should work, the business logic and examples. The README is the full and exact description of every part of its level, with the path to each part's own docs and no logic inside the agents. Every level has both, plus `README.asd.md` and the rebuild prompt, the spec an AI follows to build the level again. This changed later: when the owner asked, the two overlapped a lot, and the owner then set these jobs.

Docs improved: docs/README.md, docs/README.asd.md.

### 2026-10-06: Separate files for detailed logic, or in the README?

> and if it's part of documentation where in another knowledges and which way we store it there, because it looks like there a lot of knowledge of how it works and i am not sure should we in such cases have separate files for some logic or add it in a README and vision and such files and reference there, or just have short view on it there

Detail lives in its own doc or skill, the README gives a short view with the path to it, and the vision keeps only the idea. The metadata logic shows the rule: its full logic is `docs/metadata.md`, this README has a short part that points to it, and the `file-index` skill holds the steps.

Docs improved: docs/README.md, docs/README.asd.md.

### 2026-10-09: Where did vision/ go?

> before we had folder vision where is it right now?

It has not moved: `vision/` is the planning area at the top of the repository, with the records, plans, build tools, page source and server while the project is planned. The File Tree page now shows it like every other folder. A plan to make the real files the only source and take `vision/` out of the repository is written and waits for the owner's go.

Docs improved: none, the answer was already in docs/README.md (the planning area).

### 2026-10-13: What is needed to live without vision/?

> i need kind of go out of the vision folder what we still would need in a current system to live without it and move forward

The real files must become the only source. The main work is the tree notes: each item's ids, numbers and decisions move into its Details file, and the build reads only the disk and the metadata. The rest is moving the records to `apps/project-IDE/data/`, the build scripts into the `ide-build` skill and the page to `apps/project-IDE/current-ui/`, fixing the server settings, and stopping the copying of drafts and metadata. The plan is `apps/project-IDE/data/plans/2026-10-13-leave-vision.md`, and it waits for the owner's go.

Docs improved: docs/README.md, docs/README.asd.md.
