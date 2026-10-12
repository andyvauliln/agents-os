# Agent OS

You are working in the repository of the Agent OS, the owner's personal system that runs AI agents of any kind; trading on prediction markets is its first domain. This file sits in the system's own Claude Code folder, `agents/system/.claude/`, and there is no other CLAUDE.md at the top of the repository. Claude Code loads it by itself when it starts in `agents/system/`, as it does on the owner's server. If you started at the top of the repository instead, read this file first by hand. Paths below are from the top of the repository.

The system is in its planning phase: none of the agents is built yet. The repository already has its final shape, and every file and folder of the plan is in it: written files are real, and a file nobody has written yet exists only as its How it works file.

## What this project is for

The owner builds the Agent OS by vibecoding: they say what they want in plain words, and AI writes the plans, the docs and later the code. The project IDE is the owner's window on that work: the File Tree page (a clickable map of every folder and file) and plain docs that explain how everything works, so they can understand the project, watch it change, steer it and analyse how the system is doing. Everything you do keeps that window true and easy to read.

The same window is your context. Before you change a file, know what it is for, how it works, what depends on it and what holds for it from every level above; after you change it, bring everything that depends on it in line in the same round.

## Read first, in this order

1. `agents/system/docs/vision.md`: what we are building and why, the concept, how it should work and the business logic.
2. `agents/system/docs/README.md`: every part of the system exactly, how the parts connect, and where each part's own docs are.
3. `agents/system/.claude/agents/knowledge-base-agent.md`: how knowledge is kept and docs are written. Its rules apply to you.
4. `agents/system/.claude/agents/project-ide-agent.md`: how the File Tree page is built and how what the owner leaves on it comes back.
5. `apps/project-IDE/data/memory/`: working notes on how the owner wants us to work and what is open.
6. The newest entries of `apps/project-IDE/data/changelog.md` and `git log --oneline -20`: what changed since your last round, on either side.
7. `apps/project-IDE/data/decisions.md`: every decision. Decided means the owner decided.

Before you touch a file or folder, read its How it works file: `vision.index.md` next to `vision.md` (the file's name without its extension), `f/f.index.md` inside a folder. Its section in `apps/project-IDE/data/file-tree.md` has the details, and `python3 agents/system/.claude/skills/ide-build/scripts/build_map.py --context <its node>` prints everything that applies to it, the levels above included.

## Where things are

| What | Where |
|---|---|
| All agents: every domain, the system included, each with its agent, settings, scripts, logs, data, tests and research | `agents/` |
| The docs: vision, README, the rebuild prompt for AI, more for people one by one | `agents/system/docs/` |
| The knowledge base agent, the project IDE agent and their skills | `agents/system/.claude/agents/`, `agents/system/.claude/skills/` |
| The topic notes agents read while they work: architecture, conventions, safety, flows, schemas, how-to, the index; each domain adds its own, such as the prediction-market domain's `trading-` notes | `agents/system/docs/`, `agents/trading/prediction-market/docs/` |
| Research, kept by the level it serves: the system's own and each domain's | `agents/system/research/`, `agents/trading/prediction-market/research/` |
| The File Tree page and its data | `apps/project-IDE/current-ui/` |
| The same page on the owner's server, with Claude Code behind its request box | `apps/project-IDE/server/` |
| This project's records: every input word for word, decisions, changelog, the tree notes, the knowledge map, the notes behind each doc, page edits, working notes, plans, retired files | `apps/project-IDE/data/` |
| The page build scripts | `agents/system/.claude/skills/ide-build/scripts/` |
| The prediction-market domain's dashboard, empty for now and maybe never needed | `apps/trading-ui/` |
| Keys | `.secrets/` on the machine only, never in git |

## Every round

1. **Pull.** On the owner's server: `git pull` on `main`. In the cloud project: bring `origin/main` into your branch first.
2. **Plan every change.** A request that changes the system, its structure, code or docs gets a plan first, with the `change-plan` skill, stored in `apps/project-IDE/data/plans/`; build it only after the owner has seen it, then move its knowledge into the files it belongs to and archive the plan. Small fixes (a typo, a broken link, a rebuild) need none.
3. **File every input.** Every owner message, every answer you give to the owner's question and every change to the plan goes through the knowledge base agent: `knowledge-intake` stores it word for word in `apps/project-IDE/data/inputs/`, then the docs it touches, decisions, changelog, the How it works files (`file-index`), then the vision, the README and the rebuild prompt, in that order.
4. **Rebuild the page** with the project IDE agent's `ide-build`: the build must report every How it works file fresh and no orphans, and the page check must pass. If the owner asked for a sync, `ide-sync` comes first.
5. **Commit and push**, with a message that says what changed and which input caused it. Cloud: open or update the pull request into `main`.

## Rules

- Decided only on the owner's word. Your own ideas are "proposed" until the owner says yes.
- Never write a secret value anywhere: no keys, passwords or wallet details. Key names only.
- Docs for people are plain and book-like, with no reference numbers, ids or decision codes. The notes for agents keep the ids.
- Never change the owner's words in a stored input. Never drop the owner's words from a How it works file they edited on the page.
- Generated files are rebuilt, never merged by hand: `apps/project-IDE/current-ui/file-tree.data.json`, `apps/project-IDE/data/knowledge-map.json` and the `basis` line of each How it works file.
- Ask the owner before anything hard to undo: deleting, rewriting history, merging into `main` unless the owner allowed it, anything that acts live in the outside world. A Delete the owner pressed on the page is that ask, for that one item.
- The tree lists only real files and folders, never examples of names.
- One job per code file: one function, endpoint, script or worker with one purpose, parameters allowed, never several jobs in one file. Group related ones in a folder, each with its own How it works.
- Before a big rewrite, show the owner the plan and one example first.
- What you learn about the system, from the owner or from your own work, goes into the docs before the round ends. Every question the owner asks gets its answer written into the docs, where they should have found it.
- Call the owner "the owner", and "they" when a pronoun is needed.

## The File Tree page

The page is published at https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs from `apps/project-IDE/current-ui/file-tree-explorer.html` with `file-tree.data.json` next to it. Messages, edits and deletions the owner leaves on the page wait in the page's own store, and the page marks each touched item "changed". When the owner presses Apply changes on the page, or says "sync the file tree", the project IDE agent runs `ide-sync` (every waiting message, edit and deletion saved word for word and carried into the files, the knowledge handed to the knowledge base agent), then `ide-build` (rebuild, check, republish), and the round is committed and pushed.

## The system manager

When you run as the system's own agent rather than as a helper on the project, you are the system manager. You oversee every domain, the health of the whole system and its development, plan each new domain before it is built, and answer the owner's questions about the whole system. The common prompt every level shares comes first; this part adds the system's own job. Both are proposals until the owner confirms them. A hard limit on any outside action goes in code, never only in a prompt.
