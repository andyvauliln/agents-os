# The Agent OS project

## In short

The Agent OS is the owner's personal system for running AI agents of any kind: agents that trade, that work on social media or that help with management. It runs many small agents side by side, each with one clear job, tries every idea safely first and keeps what works. Trading on prediction markets is its first area of work. The owner builds it by vibecoding: they say what they want in plain words, and AI writes the plans, the docs and later the code, while the owner follows and steers everything through the project IDE.

Nothing of the system runs yet. The project is in stage one: finishing the project IDE, making every file's metadata correct, and writing the docs at the project, system, trading and apps levels. The prediction-market domain is stage two.

This document is the full and exact description of the whole repository: every part, what it holds, how the parts connect, how a round of work goes, and where each part's own docs are. Why the project exists, its concept and the rules it follows are in the vision, `docs/vision.md`.

## The repository at a glance

The repository is one GitHub repository, `andyvauliln/trading-oss`. In the docs its top folder is called `agent-os/`, the system's name; the repository keeps its old name for now.

```text
                         the owner
                 (chat, voice, the File Tree page)
                              │ inputs, kept word for word in apps/project-IDE/data/
                              ▼
   agents/            apps/                 docs/
   system/            project-IDE/          (project level)
   trading/           temp/  trading-ui/
      │                  │                     │
      └──────────────────┴─────────────────────┘
                         │ the IDE build reads every file and its metadata
                         ▼
          apps/project-IDE/current-ui/: the File Tree page

   .secrets/: key names in git; the .env values never leave the machine
```

| Part | What it is for | Where it lives |
|---|---|---|
| The front page | The first page anyone sees on GitHub | `README.md` |
| The handoff | How to pick the planning work up in a new session | `HANDOFF.md` |
| The start scripts | Set up the owner's server once, and start or restart the project IDE | `init.sh`, `start.sh` |
| The project docs | The whole repository and the way it is worked on | `docs/` |
| Agents | Every domain, the system first | `agents/` |
| The system | The system agent, everything every agent shares, and Claude Code's entry point | `agents/system/` |
| Trading | The folder of trading domains, its docs and its research | `agents/trading/` |
| Apps | Our own apps, outside apps we use, research clones | `apps/` |
| The project IDE | The owner's window on the project: the File Tree page, its server, its data | `apps/project-IDE/` |
| Keys | Every private key, kept on the machine | `.secrets/` |
| What git ignores | Keys files, dependencies, caches, editor noise | `.gitignore` |
| Metadata files | How it works, Details and more, next to every file and folder | beside each item |
| The records | Every owner input word for word, decisions, changelog, plans | `apps/project-IDE/data/` |

How the parts connect, step by step. The owner's words arrive in a chat, by voice or on the File Tree page. The knowledge base agent keeps them word for word in the records, `apps/project-IDE/data/`, writes a plan, and after the owner's go brings the docs of every level touched and their metadata files in line. Every file is its own source and is edited where it is. The project IDE agent then rebuilds the page from the files on disk: it gives new items their empty metadata files, checks that every How it works note is current, and writes the page's data file next to the page. The page shows every file and folder of the repository with its metadata as tabs. What the owner leaves on the page comes back into the files at the next sync. Keys stay in `.secrets/` on the machine; only their names travel.

## How the repository is laid out

The top of the tree:

```text
agent-os/
├── README.md                    the front page for people
├── HANDOFF.md                   how to continue the planning in a new session
├── init.sh                      sets up the owner's server once: tools, .venv/, the service that starts the IDE at boot
├── start.sh                     starts the project IDE: sync, stop the old server, rebuild, start, check
├── .gitignore                   what git leaves out: .env files, dependencies, caches
├── .secrets/                    keys: test/.env and live/.env stay on the machine
├── docs/                        the project docs: vision, README, README.asd, rebuild prompt, file tree
├── agents/
│   ├── system/                  the system agent and the shared parts; CLAUDE.md
│   └── trading/                 the folder of trading domains
│       ├── docs/                trading's own docs
│       ├── researches/          the research studies
│       └── prediction-market/   the first trading domain: folders and earlier notes, stage two
├── apps/
│   ├── docs/                    the docs for all apps
│   ├── project-IDE/             the File Tree page, its server and its data
│   ├── temp/                    repositories cloned only to study them
│   └── trading-ui/              the prediction-market domain's dashboard, empty
```

The levels and where each level's docs are:

```text
project            docs/
├── system         agents/system/docs/
├── trading        agents/trading/docs/
│   └── prediction-market (stage two)   agents/trading/prediction-market/docs/
└── apps           apps/docs/
    └── project IDE                     apps/project-IDE/docs/
```

Every level's docs folder holds the same four docs: `vision.md`, `README.md`, `README.asd.md` and `rebuild-prompt.md`. The project level adds `file-tree.md`, the plain list of every path. A level never repeats its parent; it sums the parent up in a sentence and describes only its own parts.

Each of the four has its own job. The vision says what the level is for and why: the concept, how it should work, its business rules and examples. The README describes every part of the level exactly, what it holds and how the parts connect, with the path to each part's own docs and no logic inside the agents. `README.asd.md` is the README again in ASD-STE100. The rebuild prompt is the spec an AI follows to build the level again. Detailed logic does not go into any of them: it lives in its own doc or skill, the README gives a short view with the path to it, and the vision keeps only the idea. The metadata logic shows the rule: the full logic is `docs/metadata.md`, this README has a short part that points to it, and the `file-index` skill holds the steps.

## The parts

### The front page, the handoff and the start scripts

`README.md` at the top of the repository is the front page GitHub shows. It is meant to say in a few lines what the project is and where to start: the project vision and README in `docs/`. It is still empty; what it says is open.

`HANDOFF.md` is a planning-time file: how to continue the planning in a new Claude Code session, where things stand, the build commands, and the rules to keep. It is written by hand at the end of a planning stretch and read by whoever picks the work up.

`init.sh` and `start.sh` run the project IDE on the owner's server. `./init.sh` is run once: it checks the tools, makes `.venv/` (which git ignores) with the Python package the request box needs, installs a service that starts the IDE when the machine boots, and starts it. `./start.sh` starts or restarts the IDE: it brings in new commits from GitHub when that is a clean move forward, stops the old server, rebuilds the page data and starts the server again. They are not the system's own `agents/system/init.sh` and `agents/system/start.sh`, which belong to the agents and are not written yet.

Each of these files has its How it works and Details files beside it (`README.index.md`, `HANDOFF.index.md`, `init.index.md`, `start.index.md`, each with its `.meta.json`), and the root itself has `agent-os.index.md` and `agent-os.meta.json`.

Its docs: `README.index.md`, `HANDOFF.index.md`, and for the start scripts `apps/project-IDE/server/README.md`.

### The project docs

`docs/` describes the whole repository and the way it is worked on. It is the first thing to read, for people and for every AI session.

- `docs/vision.md`: what the Agent OS project is and why, the way of working, the rules the project follows, examples, the stages and the open questions.
- `docs/README.md`: this document.
- `docs/README.asd.md`: this document again in ASD-STE100 Simplified Technical English, with the same content and section order, so the two can be compared. `README.md` is its source.
- `docs/rebuild-prompt.md`: the instructions an AI coding agent follows to build the repository's top level again, then each level in order through that level's own rebuild prompt.
- `docs/file-tree.md`: a plain list of every path in the repository, one per line, with no metadata. It is written by the IDE build every round, never by hand.
- `docs/metadata.md`: the full logic of the metadata files, in ASD-STE100: which files every item has and how they are named, what each one holds, when one goes stale and how the build finds it, how an agent updates them after a change, how the build and the page use them, the rules, how status (decided, proposed, idea, open), owner inputs, decisions and questions work, the true state of each Details field, and what is not built yet.

Every doc has its How it works and Details files beside it. The four written docs also have `x.example.md`, the outline of the doc (its headings and one line on what goes under each), and `x.questions.md`, the open questions for the owner about it.

The knowledge base agent writes them with its doc skills: `vision-doc`, `readme-doc`, `readme-asd-doc` and `rebuild-prompt-doc`. They change whenever an input changes the project as a whole: its levels, its folders, its way of working, its stage.

Its docs: `docs/docs.index.md`.

### Agents

`agents/` holds every domain, one folder each. The system is a domain too.

Every agent at every level has the same standard folder: `.claude/` (its Claude Code setup: `CLAUDE.md` or its prompt, `settings.json`, `rules/`, `skills/`, `commands/`, `agents/` for its sub-agents, `workflows/`, `output-styles/`, `agent-memory/`), then `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/`, and the level files `package.json`, `requirements.txt`, `init.sh` and `start.sh`. Each content folder holds the level's own files and a `subagents.link/` folder with one link per child agent. What every agent needs lives in the system's folder; what one domain needs lives in that domain. The system README describes all of this exactly.

Its docs: `agents/agents.index.md`.

### The system

`agents/system/` is the system agent's folder: it looks after the whole Agent OS and holds everything every agent shares, whatever its domain.

- `agents/system/CLAUDE.md` is Claude Code's entry point for the whole project. Claude Code started in `agents/system/`, as it is on the owner's server, loads it first. It says what the project is and which stage it is in, what to read and in which order (the project vision and README, the system vision and README, `docs/file-tree.md`, the project IDE's README), the rules, what to do after every input, and when and how each doc is updated. There is no `CLAUDE.md` at the top of the repository.
- `agents/system/.claude/` holds the system's Claude Code setup: `settings.json`, the helper agents in `agents/` (the knowledge base agent, the project IDE agent and the system's self-improvement helper) and the skills in `skills/` (`knowledge-intake`, `change-plan`, `file-index`, `vision-doc`, `readme-doc`, `readme-asd-doc`, `rebuild-prompt-doc`, `claude-md-doc`, `ide-build` with its build scripts in `ide-build/scripts/`, and `ide-sync`; `readme-asd-doc` and `claude-md-doc` are new this stage).
- `agents/system/configs/` holds the system's settings: `system.config.json`, `system.workers.json` (every job the system runs, all switched off for now), `models.config.json` and `system.links.json`.
- `agents/system/docs/` holds the system's four docs.
- `scripts/`, `logs/`, `data/`, `tests/` and `research/` follow the standard folder; most of their files are planned and still empty.

The system level stays general: nothing about money, markets or orders is written there.

Its docs: `agents/system/docs/README.md`.

### Trading

`agents/trading/` is the folder of trading domains. It is not an agent itself: it has no prompt, settings or jobs of its own.

- `agents/trading/docs/` holds trading's four docs: what trading as a whole is for, how its domains relate, and how they are built.
- `agents/trading/researches/` holds the research studies: 42 studies of ways to make money on prediction markets with their evidence and the pipeline that wrote them (`prediction-market-research/`), a study of agents that improve themselves (`self-improving-agents/`), and a study of how trading agents are built (`trding-agents-arhiteches/`).
- `agents/trading/prediction-market/` is the first trading domain. It is stage two: only its folders exist, each empty folder holding a `.gitkeep`, including its first strategy agent `strategy-1-agent/` and that strategy's first trading agent `pm-strategy-1.momentum-v1.opus55-test/`. Its `docs/` holds earlier notes kept for stage two. Its other earlier files are in git history. The build creates nothing else inside it until stage two.

The next trading domain, copy trading, will be copied from the prediction-market domain when the owner asks.

Its docs: `agents/trading/docs/README.md`.

### Apps

`apps/` holds applications: our own, outside ones we use, and repositories cloned only to study them. Every app has its own `docs/` with the four docs.

- `apps/docs/` holds the docs for all apps: what apps are for, every app, and where its docs are.
- `apps/project-IDE/` is the owner's IDE, described in the next part.
- `apps/temp/` is for repositories cloned only to study them; each clone sits in its own `repo/` folder, which is never committed. It is empty.
- `apps/trading-ui/` is the planned dashboard of the prediction-market domain. It is empty, and may never be needed if the project IDE does the job.

An outside app we decide to use is forked: our `main` branch holds our changes, and an `upstream` branch follows the source and is merged in from time to time. None is brought in yet.

Its docs: `apps/docs/README.md`.

### The project IDE

`apps/project-IDE/` is the owner's window on the project and the context every AI works from.

- `current-ui/` holds the File Tree page, `file-tree-explorer.html`, its data file, `file-tree.data.json`, and `real-files.json`, the text of every file, loaded when one is opened. The page is published on claude.ai at https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs.
- `server/` runs the same page on the owner's server, with Claude Code behind its request box: `server.py`, `claude_bridge.py`, `voice.py` (voice input through Groq), `server.config.json` and its own `README.md`.
- `data/` holds the project's records: `inputs/` with every owner input word for word and its answer (and `index.json`), `decisions.md`, `changelog.md` (newest first), `plans/` with one plan per change request (and `index.json`), `overrides.json` with the owner's kept edits of the extra tables, the page's store on the server, and the archive.
- `docs/` holds the IDE's four docs; its README is the full documentation of the IDE.

The page shows every file and folder of the repository. A file opens on its File tab, readable or editable; its metadata files show as tabs: How it works, Details, Example, Questions, the ASD-STE100 version of a README, and custom views for some kinds of file, such as the table of key names for a `.env` file. A tab shows only when its file exists. A "metadata" switch shows or hides the metadata files in the tree. Each item has a request box for questions and changes, a voice button on the owner's server, and a Delete button; "Apply changes" at the top carries everything the owner left on the page into the files.

On the owner's server the IDE is started from the top of the repository with `./start.sh`, and a service starts it when the machine boots; `./init.sh` sets this up once. The server listens only on the machine itself, at `127.0.0.1:8765`, reached through an SSH tunnel.

Its docs: `apps/project-IDE/docs/README.md`.

### Keys and secrets

`.secrets/` at the top of the repository is the one store for every private key, outside `agents/`, so no agent folder or link reaches it.

- `.secrets/test/.env` holds every test key; `.secrets/live/.env` will hold the live keys with the same names, written only by the owner. Both stay on the machine and never go into git.
- `.secrets/secrets.index.json` lists key names and what uses them, never values.
- The folder itself, `test/`, `live/`, the index and every How it works and Details file are in git and show in the tree.

The page lists each `.env` file as local-only and never reads, shows or edits its text. Settings and docs name keys, never their values; today the named keys include `ANTHROPIC_API_KEY` for Claude Code on the server and `GROQ_API_KEY` for voice input.

`.gitignore` keeps every `.env` file out of git (except an `.env.example`, which holds names only), while keeping the How it works, Details and Questions files of a keys file. It also leaves out dependencies and build output (`node_modules/`, `dist/`, `build/`, `.venv/`, `venv/`), Python caches, OS and editor files, Cursor's local state, each person's Claude Code `settings.local.json` and `agent-memory-local/` contents, and what agents write at run time into `logs/` and `data/` under `agents/` (the folders and their metadata files stay). Each entry carries a comment saying why.

Its docs: `.secrets/.secrets.index.md` and `.gitignore.index.md`.

### Metadata files

Every file and folder has its metadata files beside it. Their names are the item's name without its extension:

| Metadata file | Tab on the page | What it holds |
|---|---|---|
| `x.index.md` | How it works | What the item is, who looks after it, when and how it changes, who uses it, where it is mentioned, related knowledge, and up to four "keep in mind" lines, in plain words |
| `x.meta.json` | Details | The facts about the item: what kind it is, its state, whether it is in git or secret, who writes and reads it, when it changes, related files, sources, what must change with it, what applies from above |
| `x.example.md` | Example | The outline of the item: its sections and what goes in each |
| `x.questions.md` | Questions | Two parts: the open questions for the owner, made by plans and by the `make-questions` skill; and every question the owner asked about the item, word for word, with its answer |
| `x.{type}.{name}.view.html` | a custom view | A view for one kind of item; planned |

A folder `f/` keeps its own as `f/f.index.md` and `f/f.meta.json` inside it. A file without an extension keeps its whole name (`.gitignore.index.md`). The root's are `agent-os.index.md` and `agent-os.meta.json`. A metadata file has no metadata files of its own. For now only the main docs and the two `.env` files have Example and Questions files; the `.env` files' example is `.env.example`, with key names only.

Each metadata file is its own source and is edited where it sits; the build only gives a new item its empty How it works and Details files. The knowledge base agent writes them with the `file-index` skill, children before their folders.

The full logic, step by step in ASD-STE100, is in `docs/metadata.md`.

Its docs: `docs/metadata.md`, `agent-os.index.md` and the `file-index` skill, `agents/system/.claude/skills/file-index/SKILL.md`.

## How a round of work goes

Every round, whether it starts from a chat, the page or the AI's own work, follows the same steps.

1. **Pull.** Bring the latest `main` into the working branch.
2. **File the input.** The knowledge base agent stores the owner's words word for word in `apps/project-IDE/data/inputs/`, with a summary, categories and the answer, using the `knowledge-intake` skill. A question and its answer are one input.
3. **Plan.** A change to the system, its structure, its code or its docs gets a plan in `apps/project-IDE/data/plans/` with the `change-plan` skill, shown to the owner. Work starts on the owner's go. Small fixes need no plan.
4. **Update the docs in order.** At each level the change touches: `vision.md`, then `README.md`, then `README.asd.md`, then `rebuild-prompt.md`. Levels in this order: project, system, apps, project IDE, trading. A change at a lower level is carried up to the levels above it. Decisions go into `apps/project-IDE/data/decisions.md`, a line into `apps/project-IDE/data/changelog.md`.
5. **Update the metadata.** Every stale How it works and Details file is rewritten with `file-index`, children first, until none is stale.
6. **Rebuild the page.** The project IDE agent runs `ide-build` (with `ide-sync` first when the owner pressed Apply changes): give new items their metadata files and write `docs/file-tree.md`, check the How it works notes, build the page data from the files on disk, test the page and publish it at the same link.
7. **Check the page against the disk.** The page tree must list exactly the files in git (`git ls-files --cached --others --exclude-standard`), plus the two local-only `.env` files.
8. **Commit** with a message that says what changed and which input caused it.
9. **Open or update a pull request** into `main`.
10. **Merge only on the owner's word.**

## The stages

**Stage one, now.** Finish the project IDE and its full documentation; go through every file and folder, write the custom views, make all metadata correct; finish the docs at the project, system, trading and apps levels. Nothing inside the prediction-market domain is touched.

**Stage two.** The prediction-market domain: its own docs, its strategies and their trading agents. Its earlier files are in git history.

**Later.** The system's machinery, the first strategy in test mode, more trading domains, agents of other kinds.

## Where each part's docs are

| Part | Its docs | What they add |
|---|---|---|
| The whole project | `docs/vision.md`, `docs/README.md` | Why, the way of working, every part of the repository |
| The front page | `README.index.md` | What the front page is for |
| The handoff | `HANDOFF.index.md` | What the handoff is for |
| Every path | `docs/file-tree.md` | The plain list of the repository |
| Claude Code's entry point | `agents/system/CLAUDE.md` | What to read first, the rules, the round |
| Agents | `agents/agents.index.md` | The domains and the standard folder |
| The system | `agents/system/docs/README.md` | Every shared part of the system exactly |
| Trading | `agents/trading/docs/README.md` | The trading domains and their research |
| The prediction-market domain | `agents/trading/prediction-market/prediction-market.index.md` | its folders; its README in stage two |
| Apps | `apps/docs/README.md` | Every app and how apps are brought in |
| The project IDE | `apps/project-IDE/docs/README.md` | The full documentation of the IDE |
| The IDE server and the start scripts | `apps/project-IDE/server/README.md` | How to set up, start and reach the page on the owner's server |
| Keys | `.secrets/.secrets.index.md` | How keys are kept |
| What git ignores | `.gitignore.index.md` | Each ignore rule |
| Metadata files | `docs/metadata.md`, `agents/system/.claude/skills/file-index/SKILL.md` | The full metadata logic; how every metadata file is written |
| The records | `apps/project-IDE/data/README.md` | The inputs, decisions, changelog and plans |
| The IDE build | `agents/system/.claude/skills/ide-build/SKILL.md`, its `scripts/README.md` | How the page is built and checked |

## Still open in the design

- **Doc names:** whether `rebuild-prompt.md` keeps its name or becomes `reverse-prompt.md`.
- **Repository name:** whether the repository and its top folder are renamed to `agent-os`.
- **Front page:** what `README.md` at the top says; it is empty.
- **The plain file tree:** whether `docs/file-tree.md` later gets a little information on each line.
- **Metadata tabs:** which other files get Example, Questions, Tests and changelog files, and which custom views each kind of item gets.
- **Prediction-market folder names:** whether its strategy and trading agent folders keep their current names.
