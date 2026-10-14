# Working on the plan from two places through GitHub

Status: the layout is decided by the owner. Nothing is pushed yet: the owner gives the GitHub project next, and the first sync follows.

## The problem

Today the whole planning project lives in the cloud project's shared folder. Only the Claudes inside this project can see it, and part of what they know sits in the project's memory, which nothing outside the project can read. A Claude Code started on the owner's server would begin blind. And if both worked on their own copies, one would silently overwrite the other, or the two copies would drift apart.

## The idea

The GitHub repository becomes the one place where the project lives, and the repository is the file tree itself: every folder and file the File Tree page shows is in it. Every Claude, in the cloud or on the server, starts each round by pulling the latest version and ends it by committing and pushing. A `CLAUDE.md` in the system's own Claude Code folder, `agents/system/.claude/`, tells any Claude what the project is for, what to read first, the rules and how to sync, so it has the full context within a minute of starting.

Nothing about the way of working changes: every input still goes through the knowledge base agent, the docs are still written the same way, and the File Tree page still shows everything. Only the place the files live changes, from a shared folder to a repository both sides can reach.

## The layout

```text
trading-os/
├── README.md            the front page for people
├── agents/              the whole tree as the page shows it, agreed by the owner as it stands
│   └── system/
│       ├── .claude/
│       │   ├── CLAUDE.md  read first: what this is, where to start, the rules, how a round works
│       │   ├── agents/  knowledge-base-agent, project-ide-agent
│       │   └── skills/  knowledge-intake, file-index, the doc skills, ide-build (with the build scripts), ide-sync
│       ├── docs/        the docs for people (README, vision, more one by one) and the topic notes agents read while they work
│       └── research/    the system's research, with two of the earlier studies
└── apps/                our own apps, and outside code projects later
    ├── project-IDE/     the owner's IDE
    │   ├── current-ui/  the File Tree page and its data
    │   ├── server/      the same page on the owner's server, with Claude Code behind it
    │   └── data/        this project's knowledge and what the page is built from: every input, decisions,
    │                    changelog, the tree notes, the knowledge map, the notes behind each doc,
    │                    the owner's page edits, working notes, plans, retired files
    └── trading-ui/      the trading dashboard, empty for now
```

- Every file and folder is created with its How it works file next to it. A file nobody has written yet exists only as its How it works file. A placeholder such as `[agent-name]/` is a folder holding only its How it works file, and scripts skip names in brackets.
- The keys folder stays on the machine and never goes into git.
- The project IDE agent looks after the page: it builds the page from the repository and brings back the owner's notes and edits. The knowledge base agent keeps the knowledge and the docs.
- Later the page data can be built by walking the repository and its How it works files instead of reading the tree notes, and the tree notes can be generated from the repository.

## The first sync

The planning folder in the cloud project is laid out differently, so the first sync copies each part to its place in the tree:

| In the planning folder `vision/` | Goes to |
|---|---|
| `.claude/CLAUDE.md` | `agents/system/.claude/CLAUDE.md` |
| `.claude/agents/`, `.claude/skills/` | `agents/system/.claude/agents/`, `agents/system/.claude/skills/` |
| `.claude/docs/` (README, vision) | `agents/system/docs/` |
| `tools/` (the scripts) | `agents/system/.claude/skills/ide-build/scripts/` |
| `explorer/` (the page and its data) | `apps/project-IDE/current-ui/` |
| `server/` (the page's service on the owner's server) | `apps/project-IDE/server/` |
| `docs/` inputs, decisions, changelog, file tree notes, the map, the knowledge guide | `apps/project-IDE/data/` |
| `docs/` topic notes (overview, architecture, conventions, safety, flows, schemas, metrics, glossary, roadmap, feature map, how-to, common, index) | `agents/system/docs/` |
| `.claude/knowledge/sources/`, the earlier vision notes | `apps/project-IDE/data/sources/` |
| `tools/overrides.json`, `.claude/memory/`, `plans/`, `archive/` | `apps/project-IDE/data/` |
| in the repository today: `researches/prediction-market-research/`; `researches/self-improving-agents/` and `researches/trding-agents-arhiteches/` | `agents/trading/prediction-market/research/`; `agents/system/research/` (the root `researches/` goes away) |
| every How it works file (next to the drafts, or in `tree/trading-os/...`) | next to its file or inside its folder |

The scripts' paths are switched to the repository layout in the same step, and the build must report every How it works file fresh with no orphans before the first commit. After the first sync, the cloud project works from a clone of the repository, so both sides have the same layout.

## How a round works, on either side

1. **Pull** the latest `main`.
2. **Catch up:** read the newest changelog entries and the commits since your last round, so you know what the other side did.
3. **Work:** every input from the owner goes through the knowledge base agent, exactly as now.
4. **Rebuild:** the knowledge map, the How it works files and the page. The build must report nothing out of date.
5. **Commit and push**, with a message that says what changed and which input caused it.

## The two sides

**The cloud project.** A Claude in a thread pushes only to its own branch, so each round becomes a pull request into `main`. At the start of every round it brings `main` into its branch first. A pull request is merged by the owner, or by Claude when the owner allows that for planning-only changes.

**The owner's server.** Claude Code works in a clone of the repository, on `main` directly (it is the owner's own machine and credentials), or on its own branch if the owner wants to review that side too. It is started in `agents/system/`, so it loads the system's `CLAUDE.md`, agents and skills by itself.

## Keeping the two from fighting

- Pull before every round and push right after it; small commits.
- Generated files are never merged by hand: after any merge, run the build again. They are the page data, the knowledge map and the line of each How it works file that records what it was written from.
- When both sides changed the same doc, the knowledge base agent merges the two by meaning, like any other input, and asks the owner when they contradict each other.
- The project's memory stops being the only copy: the working notes live in `apps/project-IDE/data/memory/`, and the cloud memory only points to them.

## The File Tree page

The page stays on claude.ai, where the owner opens it. Its source and data are in the repository, so either side can rebuild and republish it. Messages and edits left on the page wait in the page's own store until a sync. Whichever Claude does the sync brings them back with the project IDE agent, commits, pushes and republishes. Claude Code on the server can do this too when it is signed in with the owner's claude.ai account; that still has to be checked on the server.

The two files also open on the server itself, served by any web server: the same page, but view only, because saving and asking Claude come from claude.ai. The page says so in its header. Editing the files does not change the claude.ai link until they are published to it again.

The owner wants the page on the server too, with Claude Code behind its request box, so that notes and edits go straight into the files and requests run right away. The design is in `server-ide.md`, next to this plan.

## What the owner decides

1. Which GitHub project the tree goes into (next step).
2. Who merges the pull requests: the owner, or Claude for planning-only changes.
3. On the server: install Claude Code, clone the repository, give it a way to push (an SSH key or a GitHub token, kept out of the repository), sign it in, and start it at the top of the repository.

## Still open

- Whether the server works on `main` directly or on its own branch.
- Whether the page's waiting messages can be read from the server.
