# Plan: live without the vision/ folder

- Input: in-20261013-leave-vision (2026-10-13), the owner: "i need kind of go out of the vision folder what we still would need in a current system to live without it and move forward"
- Status: proposed, waiting for the owner's go
- Paths are from the top of the repository.
- Note (owner, 2026-10-14): the moved notes in `apps/project-IDE/data/sources/` and the prediction-market trading notes in `agents/trading/prediction-market/docs/` are kept but not referenced by any doc, skill, agent or metadata file; whether to use them is decided later.

## The idea

Today `vision/` is the source for most things and the build copies them into the real places. After this plan the real files are the only source: you edit a file where it lives, the IDE builds the page from the files on disk and their metadata, and `vision/` is gone from the repository (its history stays in git).

## What vision/ holds today, and where it goes

| In vision/ | What it does now | Where it goes | Work needed |
|---|---|---|---|
| `tools/` (parse, enrich, build_map, index_files, materialize, tabs, check_page, overrides.json) | Builds the page data, checks the page | `agents/system/.claude/skills/ide-build/scripts/` (copies already there, `materialize.py` missing) | Point every path at the real places. Drop the parts that read the old tree notes and drafts (see "The tree notes" below). `materialize.py` shrinks to: write `docs/file-tree.md`, keep `.gitkeep`, give new files empty metadata. |
| `explorer/` (the page, its data, real-files.json) | The page itself | `apps/project-IDE/current-ui/` (a copy is there; its data file is still `{}`) | Build writes the data and real-files.json there; publish from there. |
| `server/` | The page on your server | `apps/project-IDE/server/` (a copy is there) | Fix `server.config.json`: `repo` must be `../../..`, page folder `apps/project-IDE/current-ui`, store `apps/project-IDE/data/page-store`, logs in `agents/system/logs/`, `planning_dir` empty (then an edit to How it works goes into the `x.index.md` next to the item; the code already has this path), Claude Code starts in `agents/system/`. Drop the planning words from `server.py` and `claude_bridge.py`. |
| `.claude/skills/`, `.claude/agents/` | Drafts of the system's skills and the two helper agents | `agents/system/.claude/skills/`, `agents/system/.claude/agents/` (copies already there, the same text) | Make the real files the source: drop the draft lists in the build (DRAFTS, CLAUDE_DRAFTS, VISION_FILES). Fix the paths inside the skills that still say `vision/`. |
| `tree/agent-os/...` (481 How it works and Details files) | The source of every item's metadata; the build copies them next to items | Already next to every item on disk | Make the files next to items the source; stop copying. `build_map.py` and `index_files.py` read and write them there. |
| `docs/inputs/` (116 inputs + index.json) | Every owner input word for word | `apps/project-IDE/data/inputs/` | Move; the knowledge-intake skill writes there. |
| `docs/decisions.md`, `docs/changelog.md` | Decisions D-001 to D-065, the change log | `apps/project-IDE/data/` (older copies there) | Move, replacing the old copies. |
| `docs/index/knowledge-map.json` | Links knowledge to items | `apps/project-IDE/data/knowledge-map.json` | Rebuild there from the docs that stay. |
| `plans/` | Change plans | `apps/project-IDE/data/plans/` | Move. |
| `.claude/memory/` | The project memory notes | Nowhere (D-066) | Nearly all is in the docs already. Owner wishes go into CLAUDE.md rules, the "system text general" rule into `agents/trading/docs/README.md`, open questions into the `x.questions.md` of their items; cloud-only facts stay in the cloud project memory. Then delete. |
| `docs/file-tree.md` (the tree notes, with [n] numbers, decisions, rules per item) | Gives every item its id, number, decisions and notes | Nowhere as one file: each item's own metadata | See "The tree notes". |
| Topic notes `docs/*.md`, `docs/common/`, `docs/how-to/`, `docs/index/*.md`, `docs/prediction-market-agents/`, `.claude/docs/`, `.claude/knowledge/` | The old knowledge base | Already folded into the docs at five levels; the how-to guides and the prediction-market notes are still needed later | Move `how-to/` to `agents/system/docs/how-to/` and the prediction-market notes to `agents/trading/prediction-market/docs/` for stage two; the rest goes to the archive. |
| `archive/` (1,001 files) | Old versions | Nowhere in the tree | Remove from the repository; git history keeps it. |
| `file-tree.data.json`, the four "Moved:" stubs (`vision.md`, `overview.md`, `feature-map.md`, `file-tree.md`) | Old copies and pointers | Nowhere | Remove. |

## The tree notes: the one real change

The page still gets each item's id, its [n] number, decisions, rules and notes from the tree block in `vision/docs/file-tree.md`. Without it the build must take these from the item itself:

- The id is the item's path. The [n] numbers and the `n-` ids are removed (owner, 2026-10-14): the `tree_number` field is already gone from every Details file; the move removes `node:` from the How it works front matter, the numbers from the knowledge tags, and the numbers from the page.
- Decisions, notes and open questions come from the Details file and the Questions file.
- `parse.py` is no longer needed; `enrich.py` walks the disk and reads each item's metadata. The build no longer reads the topic notes, the feature map or the trading notes (owner, 2026-10-14: kept, not referenced), and `build_map.py` checks each How it works against its item and children only.

This is the biggest step. Everything else is moving files and changing paths.

## Steps

1. Move the records (inputs, decisions, changelog, plans) to `apps/project-IDE/data/` and point knowledge-intake, change-plan and CLAUDE.md at them. Put the few missing memory parts into CLAUDE.md, the trading README and the system README questions (D-066).
2. Make the real skills, agents and metadata files the source: drop the draft lists and the metadata copying in the build.
3. Move the build tools into `ide-build/scripts/` with paths to the real places; the page source and its data into `apps/project-IDE/current-ui/`; fix the server settings.
4. Teach `enrich.py` to build the tree from disk plus each item's metadata, without the tree notes, the numbers or the topic notes; carry the decisions of every item into its Details file first.
5. Move `how-to/` and the prediction-market notes to their real docs; archive the rest.
6. Rebuild, check the page against git, publish. Then test the server from `apps/project-IDE/server/` on a copy of the repository, the same tests as on 2026-10-05: the page opens, an edit goes into the file and a How it works edit into its `x.index.md`, a request runs with Allow and Refuse, a delete and a bring-back, and the microphone with the key present.
7. Remove `vision/` from the repository, update CLAUDE.md, every README, HANDOFF.md, and remove `apps/project-IDE/data/memory/`.

## Open for the owner

- Remove `vision/archive/` from the repository (it stays in git history)? Proposed: yes. The topic notes move to `apps/project-IDE/data/sources/` and stay, not referenced (owner, 2026-10-14).
- Do it in one pull request, or step by step (records first)? Proposed: one pull request, built in the order above.
