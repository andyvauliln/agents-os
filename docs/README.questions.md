# Questions: README.md

## Open questions for the owner

- **Do the records move from `vision/docs/` into `apps/project-IDE/data/`?** The records are the inputs, the decisions, the changelog, the tree notes and the plans. The README tells about both locations. The answer decides which location is the source.
- **Does `docs/file-tree.md` also list the metadata files, or only the items?** If it lists each `.index.md` and `.meta.json`, the file becomes approximately two times longer. Without them, the map is cleaner.
- **Must git ignore the logs and the data of the agents again?** The current `.gitignore` does not have these rules now. The rules kept the runtime `logs/` and `data/` and the research clones in `apps/temp/` out of git. The owner asked for them before.
- **Do we still need `HANDOFF.md` when `agents/system/CLAUDE.md` is the entry point?** Both files tell a new session where to start. Two start points can disagree.

## The owner's questions

### 2026-10-05: The layout of the repository

> i think we should have something like this what do you think?

The layout was agreed: the repository itself is the tree. Today the top of the repository holds these items:

1. `README.md`, `HANDOFF.md`, `.gitignore` and `.secrets/`.
2. `docs/`, the project docs.
3. `agents/`, the system and trading.
4. `apps/`, the project IDE, `trading-ui/`, `temp/` and the docs of the apps.
5. The planning area `vision/`.

This changed later: there is no `CLAUDE.md` and no `researches/` at the top. `CLAUDE.md` is in `agents/system/`. The research studies are in `agents/trading/researches/`. `trading-ui/` and the project IDE are in `apps/`.

Docs improved: none, the answer was already in docs/README.md (how the repository is laid out).

### 2026-10-06: What is the difference between the vision and the README?

> i am a bit confused what suppose to be difference between vision and readme?

The vision is the top-level doc. It tells what we build and why, the concept, how it must work, the business logic and examples.

The README is the full and exact description of each part of its level. It gives the path to the docs of each part. It has no logic of the agents.

Each level has both docs. It also has `README.asd.md` and the rebuild prompt. The rebuild prompt is the specification that an AI follows to build the level again.

This changed later: at the time of the question, the two docs had much of the same content. Then the owner set these jobs.

Docs improved: docs/README.md, docs/README.asd.md.

### 2026-10-06: Do we put the detailed logic in separate files or in the README?

> and if it's part of documentation where in another knowledges and which way we store it there, because it looks like there a lot of knowledge of how it works and i am not sure should we in such cases have separate files for some logic or add it in a README and vision and such files and reference there, or just have short view on it there

The details go in their own doc or skill. The README gives a short summary with the path to that doc. The vision keeps only the idea.

The metadata logic is an example of this rule:

1. `docs/metadata.md` has the full logic.
2. This README has a short part that refers to it.
3. The `file-index` skill has the steps.

Docs improved: docs/README.md, docs/README.asd.md.

### 2026-10-09: Where is vision/ now?

> before we had folder vision where is it right now?

It did not move. `vision/` is the planning area at the top of the repository. While we plan the project, it holds the records, the plans, the build tools, the page source and the server.

The File Tree page now shows it as all other folders.

A plan is written to make the real files the only source and to remove `vision/` from the repository. This plan waits for the approval of the owner.

Docs improved: none, the answer was already in docs/README.md (the planning area).

### 2026-10-13: What do we need to work without vision/?

> i need kind of go out of the vision folder what we still would need in a current system to live without it and move forward

The real files must become the only source. The main work is the tree notes. The ids, numbers and decisions of each item move into its Details file. Then the build reads only the disk and the metadata.

The other work is:

1. Move the records to `apps/project-IDE/data/`.
2. Move the build scripts into the `ide-build` skill.
3. Move the page to `apps/project-IDE/current-ui/`.
4. Correct the server settings.
5. Stop the copy of drafts and metadata.

The plan is `apps/project-IDE/data/plans/2026-10-13-leave-vision.md`. It waits for the approval of the owner.

Docs improved: docs/README.md, docs/README.asd.md.
