# Agent OS

You are working in the repository of the Agent OS: the owner's personal system that runs AI agents of any kind. Trading on prediction markets is its first domain. Claude Code loads this file when it starts in `agents/system/`, which is how the owner starts it. If you started at the top of the repository, read this file first by hand. All paths below are from the top of the repository.

## Where the project is now: stage one

Nothing of the system runs yet. The files on disk are the tree: what exists is the project, files with nothing written yet are empty (the page's "empty" filter lists them), and every item's metadata files sit next to it.

**Stage one, the current work:**

1. Finish the project IDE (the File Tree page and its server).
2. Go through every file and folder: write custom views for each kind of file, and make every metadata file correct.
3. Finish the docs at four levels: the project (`docs/`), the system domain (`agents/system/docs/`), trading in general (`agents/trading/docs/`) and the apps (`apps/docs/`, `apps/project-IDE/docs/`).

**Stage two, not now:** the prediction-market domain and everything under it (`agents/trading/prediction-market/`, its strategy and variant folders). Only its folders exist, and its `docs/` holds all the trading notes the project has (each with its metadata files). Its other old files are in `vision/archive/2026-10-12/prediction-market/`. Do not add, write or plan anything else there until the owner starts stage two. Keep the trading notes in its `docs/` up to date when trading knowledge changes.

## Read first, in this order

1. `docs/vision.md`: the project vision. What the Agent OS is, why, how it should work, where it stands.
2. `docs/README.md`: the project README. Every part of the repository and where its docs are.
3. `agents/system/docs/vision.md`: the system vision.
4. `agents/system/docs/README.md`: the system README.
5. `docs/file-tree.md`: every path in the repository, plain, without metadata. The IDE build writes it every round.
6. `docs/metadata.md`: the full logic of the metadata files, in ASD-STE100. Read it before you write or change any metadata file.
7. `apps/project-IDE/docs/README.md`: the IDE, in full: the page, its modes and tabs, how it is built and checked, the server, how the owner's edits come back.
8. The newest entries of `vision/docs/changelog.md` and `git log --oneline -20`: what changed since your last round.

Every `README.md` has an ASD-STE100 twin, `README.asd.md`, next to it. Read the README; the twin is for the owner to compare. Before you change a file or folder, read its How it works file: `x.index.md` beside a file `x.md`, or `f/f.index.md` inside a folder `f/`.

## Where things are

| What | Where |
|---|---|
| The project docs: vision, README, README.asd, rebuild prompt, the plain file tree | `docs/` |
| The system domain: its agent, shared configs, scripts, logs, data, tests, research, and this file | `agents/system/` |
| The system's helpers: the knowledge base agent, the project IDE agent, their skills | `agents/system/.claude/agents/`, `agents/system/.claude/skills/` |
| Trading in general, its docs and research; its domains (stage two) | `agents/trading/` |
| The apps and their docs; the project IDE; the trading dashboard (empty); research clones (never committed) | `apps/`, `apps/project-IDE/`, `apps/trading-ui/`, `apps/temp/` |
| The planning area: every owner input word for word, decisions, changelog, the tree notes, the knowledge base, plans, archive, memory, the build tools, the page source, the server | `vision/` |
| Keys: the folder and its notes are in git; the `.env` files with the values never are | `.secrets/` |

**Where to edit while we plan.** The docs at the four levels and this file are real files: edit them where they are. Everything else that came from a draft has its source in `vision/`, and the build copies it into place, so edit the source: skills and agents in `vision/.claude/`, tools in `vision/tools/`, the page in `vision/explorer/`, the server in `vision/server/`, records in `vision/docs/`, How it works and Details files in the mirror `vision/tree/agent-os/`.

## Rules

These are the lasting rules for every session. The new version keeps no memory folder: agents work from the docs and the metadata, and the planning copy of the memory notes, `vision/.claude/memory/`, is deleted, not moved, when `vision/` goes.

- Decided means the owner decided. Your own ideas are "proposed" until the owner says yes.
- Never write a key value anywhere: no keys, passwords or wallet details. Key names only. Never read a `.env` file.
- Docs for people are plain and book-like, with no reference numbers, ids or decision codes. The notes for agents keep the ids.
- Never change the owner's words in a stored input, and never drop their words from a How it works file they edited on the page.
- Plan every change that alters the system, its structure, code or docs (skill `change-plan`), show the plan to the owner, then build it. Small fixes need no plan.
- The page tree always equals the files on disk. There is no separate plan of files: to add a file or folder, create it.
- Every file and folder outside `vision/` has an `x.index.md` and an `x.meta.json` (all the rules are in `docs/metadata.md`). The extra tab files (`x.example.md`, `x.questions.md`, `README.asd.md`) exist only where they are written; the page shows a tab only when its file exists.
- One job per code file. Group related ones in a folder, each with its own How it works.
- Generated files are rebuilt, never merged by hand: the page data, the knowledge map, `docs/file-tree.md`.
- Ask the owner before anything hard to undo: deleting, rewriting history, merging into `main`, anything that acts in the outside world. A Delete the owner pressed on the page is that ask for that one item.
- What you learn goes into the docs before the round ends. Every question the owner asks gets its answer written where they should have found it.
- Answer in ASD-STE100 when the owner asks for it, and keep token use low: read what the task needs, not everything.
- Call the owner "the owner", and "they" when a pronoun is needed.

## After every input or update

1. **Pull.** On the owner's server, `git pull` on `main`. In the cloud project, bring `origin/main` into your branch first.
2. **File the input** word for word in `vision/docs/inputs/` with its row in `index.json` (skill `knowledge-intake`). Your answers to the owner and every change to the plan are filed too.
   When the owner asked a question, record it with its answer in the item's Questions file, and improve the docs that should have answered it (skill `knowledge-intake`, step 6).
3. **Plan** the change if it alters the system (skill `change-plan`).
4. **Record** decisions in `vision/docs/decisions.md` and the change in `vision/docs/changelog.md`.
5. **Update the docs it touches**, level by level, in this order inside each level: vision, README, README.asd, rebuild prompt. Then this file, if the stage, the reading list or a rule changed.
6. **Update the metadata** of every file you changed: its How it works and Details, and its Example and Questions where they exist (skill `file-index`).
7. **Rebuild and check the page** (skill `ide-build`): the build reports every How it works fresh and no orphans, the page check passes, and the page tree equals the files in git.
8. **Commit and push**, with a message that says what changed and which input caused it. Cloud: open or update the pull request into `main`; merge only on the owner's word.

## When and how to update each doc

| A change to… | Makes stale… | Written with |
|---|---|---|
| goals, the concept, how the system should behave, business rules, the stage | the vision at that level and every level above it that mentions it | `vision-doc` |
| a part: a folder, an agent, an app, a config, a job, how parts connect | the README at that level, and the README of the level above if the part is listed there | `readme-doc` |
| any README | its `README.asd.md`, right after | `readme-asd-doc` |
| names, formats, the tree, the build order or checks | the rebuild prompt at that level | `rebuild-prompt-doc` |
| a file's purpose, content or links | its How it works, Details, Example and Questions | `file-index` |
| a question the owner asked about an item | that item's Questions file, part "The owner's questions", with the answer | `knowledge-intake` |
| a choice only the owner can make (in a plan, or found by checking) | that item's Questions file, part "Open questions for the owner" | `change-plan`, `make-questions` |
| the stage, the reading list, the rules, the round | this file | `claude-md-doc` |
| any file or folder added, moved or removed | `docs/file-tree.md` and the page | `ide-build` |

Levels from the top: the project (`docs/`), then the system (`agents/system/docs/`), trading (`agents/trading/docs/`) and the apps (`apps/docs/`), then each app (`apps/project-IDE/docs/`). Write the lowest level that changed first, then each level above it.

## The File Tree page

The page is published at https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs, and the owner's server serves the same page with `python3 vision/server/server.py`. Messages, edits and deletions the owner leaves on it wait in the page's store, marked "changed". When the owner presses Apply changes, or says "sync the file tree", run `ide-sync` (everything saved word for word and carried into the files), then `ide-build` (rebuild, check, publish), and commit.

## The system manager

When you run as the system's own agent rather than as a helper on the project, you are the system manager. You oversee every domain, the health of the whole system and its development, plan each new domain before it is built, and answer the owner's questions about the whole system. This part is proposed until the owner confirms it. A hard limit on any outside action goes in code, never only in a prompt.
