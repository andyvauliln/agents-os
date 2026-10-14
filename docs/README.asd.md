This is the ASD-STE100 version of `docs/README.md`. `README.md` is the source. If the two documents are different, `README.md` is correct.

# The Agent OS project

## In short

The Agent OS is a personal system of the owner. It operates AI agents of different kinds. Examples are agents that trade, agents that work on social media and agents that help with management.

The system operates many small agents at the same time. Each agent has one clear task. The system tests each idea safely first. It keeps the ideas that work. The first area of work is trading on prediction markets.

The owner builds the system by vibecoding. The owner tells the AI what to do in plain words. The AI writes the plans, the docs and, later, the code. The owner monitors and controls all the work through the project IDE.

The system does not operate yet. The project is in stage one. In stage one, we complete the project IDE and we make all metadata correct. We also write the docs of the project, the system, trading and the apps. The prediction-market domain is in stage two.

This document gives a full and exact description of the repository. It tells each part, the contents of each part and the connections between the parts. It tells the steps of a round of work. It gives the location of the docs of each part. The vision, `docs/vision.md`, tells why the project exists, its concept and its rules.

## The repository at a glance

The project is one GitHub repository, `andyvauliln/trading-oss`. The docs use the name `agent-os/` for the top folder. The repository keeps its old name for now.

```text
                         the owner
                 (chat, voice, the File Tree page)
                              │ inputs
                              ▼
   vision/  ──── planning area: records, plans, build tools, page source ────┐
      │ build copies drafts and metadata into place                           │ builds
      ▼                                                                       ▼
   agents/            apps/                 docs/            apps/project-IDE/current-ui/
   system/            project-IDE/          (project level)  the File Tree page
   trading/           temp/  trading-ui/                         │
      │                  │                                       │ shows every file
      └──── .secrets/ (key names in git; .env values never) ─────┘ and its metadata
```

| Part | Purpose | Location |
|---|---|---|
| The front page | The first page that GitHub shows | `README.md` |
| The handoff | It tells how to continue the planning in a new session | `HANDOFF.md` |
| The project docs | They describe the full repository and the method of work | `docs/` |
| Agents | All domains. The system is the first domain | `agents/` |
| The system | The system agent, the shared parts and the entry point for Claude Code | `agents/system/` |
| Trading | The folder of trading domains, with its docs and its research | `agents/trading/` |
| Apps | Our apps, outside apps that we use, and research clones | `apps/` |
| The project IDE | The File Tree page, its server and its data | `apps/project-IDE/` |
| Keys | All private keys. The keys stay on the machine | `.secrets/` |
| Git ignore rules | Keys files, dependencies, caches and editor files | `.gitignore` |
| Metadata files | How it works, Details and other files for each item | Next to each item |
| The planning area | All the material that we use to plan the project | `vision/` |

The parts connect in these steps:

1. The owner gives an input in a chat, by voice or on the File Tree page.
2. The knowledge base agent keeps the input word for word in the planning area.
3. The knowledge base agent writes a plan.
4. The owner approves the plan. Then the knowledge base agent updates the docs and metadata files of each level that the change touches.
5. The project IDE agent builds the page again from the repository.
6. The build reads the tree notes and the knowledge in the planning area.
7. The build copies the drafts and the metadata files to their locations in the tree.
8. The build makes sure that each How it works file is current.
9. The build writes the data file of the page next to the page.
10. The page shows each file and each folder of the repository. It shows the metadata of each item as tabs.
11. At the next sync, the AI puts the changes from the page into the files.

The keys stay in `.secrets/` on the machine. Only the names of the keys go to other files.

## How the repository is laid out

This is the top of the tree:

```text
agent-os/
├── README.md                    the front page for people
├── HANDOFF.md                   how to continue the planning in a new session
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
└── vision/                      the planning area
```

These are the levels and the location of the docs of each level:

```text
project            docs/
├── system         agents/system/docs/
├── trading        agents/trading/docs/
│   └── prediction-market (stage two)   agents/trading/prediction-market/docs/
└── apps           apps/docs/
    └── project IDE                     apps/project-IDE/docs/
```

The docs folder of each level has the same four docs: `vision.md`, `README.md`, `README.asd.md` and `rebuild-prompt.md`. The project level also has `file-tree.md`. This file is a plain list of all paths.

A level does not repeat the text of its parent level. It gives a short summary of the parent level in one or two sentences. Then it describes only its own parts.

Each of the four docs has a different purpose. The vision tells what the level is for and why. It tells the concept, how the level must operate, the business rules and examples. The README gives an exact description of each part of the level. It tells what each part contains and how the parts connect. It gives the path to the docs of each part. It does not tell the logic in the agents. `README.asd.md` is the README in ASD-STE100. The rebuild prompt is the specification that an AI uses to build the level again. Detailed logic is not in these four docs. It is in its own doc or skill. The README gives a short summary and the path to it. The vision keeps only the idea. Example: the full metadata logic is in `docs/metadata.md`. This README has a short part with a link to it. The `file-index` skill has the steps.

## The parts

### The front page and the handoff

`README.md` at the top of the repository is the front page that GitHub shows. It must tell in a few lines what the project is. It must tell where to start: the project vision and the project README in `docs/`. The front page is empty now. Its content is an open subject.

`HANDOFF.md` is a file for the planning time. It tells how to continue the planning in a new Claude Code session. It tells the current status, the build commands and the rules. A person writes it at the end of a period of planning. The next person or AI reads it.

Each of these two files has its How it works file and its Details file next to it: `README.index.md`, `README.meta.json`, `HANDOFF.index.md` and `HANDOFF.meta.json`. The root has `agent-os.index.md` and `agent-os.meta.json`.

Its docs: `README.index.md` and `HANDOFF.index.md`.

### The project docs

`docs/` describes the full repository and the method of work. People and AI sessions read it first.

- `docs/vision.md` tells what the project is and why. It tells the method of work, the rules, examples, the stages and the open questions.
- `docs/README.md` is the source of this document.
- `docs/README.asd.md` is this document. It has the same content and the same section order as `README.md`. It uses ASD-STE100 Simplified Technical English. The owner can compare the two documents.
- `docs/rebuild-prompt.md` gives the instructions to an AI coding agent. With these instructions, the agent builds the top level of the repository again. Then it builds each level with the rebuild prompt of that level.
- `docs/file-tree.md` is a plain list of all paths in the repository, one path on each line. It has no metadata. The IDE build writes it in each round. Do not write it by hand.
- `docs/metadata.md` tells all of the metadata logic, in ASD-STE100. It tells which metadata files each item has and how they get their names. It tells the content of each file, when a file becomes stale and how the build finds it. It tells how an agent updates the files after a change, how the build and the page use them, and the rules. It tells how the status (decided, proposed, idea, open), the owner inputs, the decisions and the questions work. It tells the true state of each Details field, and the parts that are not built yet.

Each doc has its How it works file and its Details file next to it. The four written docs also have two more files:

- `x.example.md` gives the outline of the doc: the headings and one line about the content of each heading.
- `x.questions.md` gives the open questions for the owner about the doc.

The knowledge base agent writes these docs with its doc skills: `vision-doc`, `readme-doc`, `readme-asd-doc` and `rebuild-prompt-doc`. The docs change when an input changes the full project. Examples are a change to the levels, the folders, the method of work or the stage.

Its docs: `docs/docs.index.md`.

### Agents

`agents/` contains all domains, one folder for each domain. The system is also a domain.

Each agent at each level has the same standard folder. The standard folder contains:

- `.claude/`, the Claude Code setup of the agent. It contains `CLAUDE.md` or the prompt, `settings.json`, `rules/`, `skills/`, `commands/`, `agents/` for sub-agents, `workflows/`, `output-styles/` and `agent-memory/`.
- `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/` and `research/`.
- The level files `package.json`, `requirements.txt`, `init.sh` and `start.sh`.

Each content folder contains the files of its own level. It also contains a `subagents.link/` folder with one link for each child agent. The files that all agents need are in the folder of the system. The files that one domain needs are in that domain. The system README gives the exact description.

Its docs: `agents/agents.index.md`.

### The system

`agents/system/` is the folder of the system agent. The system agent manages the full Agent OS. The folder contains all parts that all agents share, in all domains.

- `agents/system/CLAUDE.md` is the entry point for Claude Code for the full project. When Claude Code starts in `agents/system/`, it reads this file first. Claude Code starts there on the owner's server.
- `CLAUDE.md` tells what the project is and its current stage.
- `CLAUDE.md` tells which files to read and in which order. The order is: the project vision and README, the system vision and README, `docs/file-tree.md` and the README of the project IDE.
- `CLAUDE.md` also gives the rules, the steps after each input, and when and how to update each doc.
- There is no `CLAUDE.md` at the top of the repository.
- `agents/system/.claude/` contains the Claude Code setup of the system: `settings.json`, the helper agents in `agents/` and the skills in `skills/`.
- The helper agents are the knowledge base agent, the project IDE agent and the self-improvement helper of the system.
- The skills are `knowledge-intake`, `change-plan`, `file-index`, `vision-doc`, `readme-doc`, `readme-asd-doc`, `rebuild-prompt-doc`, `claude-md-doc`, `ide-build` and `ide-sync`. The skills `readme-asd-doc` and `claude-md-doc` are new in this stage. The build scripts are in `ide-build/scripts/`.
- `agents/system/configs/` contains the settings of the system: `system.config.json`, `system.workers.json`, `models.config.json` and `system.links.json`. `system.workers.json` lists all jobs of the system. All jobs are off now.
- `agents/system/docs/` contains the four docs of the system.
- `scripts/`, `logs/`, `data/`, `tests/` and `research/` follow the standard folder. Most of their files are planned and empty.

The system level is general. Do not write about money, markets or orders at the system level.

Its docs: `agents/system/docs/README.md`.

### Trading

`agents/trading/` is the folder of trading domains. It is not an agent. It has no prompt, no settings and no jobs.

- `agents/trading/docs/` contains the four docs of trading. They tell the purpose of trading, the relation between the trading domains and how to build them.
- `agents/trading/researches/` contains the research studies.
- `prediction-market-research/` contains 42 studies about methods to make money on prediction markets. It also contains their evidence and the pipeline that wrote them.
- `self-improving-agents/` contains a study about agents that improve themselves.
- `trding-agents-arhiteches/` contains a study about the structure of trading agents.
- `agents/trading/prediction-market/` is the first trading domain. It is in stage two.
- In the prediction-market domain, the folders exist. Each empty folder contains a `.gitkeep` file.
- Its `docs/` folder contains earlier notes. They are kept for stage two.
- The folders include the first strategy agent `strategy-1-agent/` and its first trading agent `pm-strategy-1.momentum-v1.opus55-test/`.
- The old files of the domain are in the archive of the planning area. The build does not make files in the domain until stage two.

The next trading domain is copy trading. We make it as a copy of the prediction-market domain when the owner asks.

Its docs: `agents/trading/docs/README.md`.

### Apps

`apps/` contains applications. These are our own apps, outside apps that we use, and repositories that we clone only for study. Each app has its own `docs/` folder with the four docs.

- `apps/docs/` contains the docs for all apps. They tell the purpose of apps, each app and the location of its docs.
- `apps/project-IDE/` is the IDE of the owner. The next part describes it.
- `apps/temp/` is for repositories that we clone only for study. Each clone is in its own `repo/` folder. Do not put a clone in git. The folder is empty now.
- `apps/trading-ui/` is the planned dashboard of the prediction-market domain. It is empty. Possibly it is not necessary, because the project IDE can do its work.

When we use an outside app, we fork it. Our `main` branch contains our changes. An `upstream` branch follows the source. From time to time, we merge `upstream` into `main`. We do not use an outside app yet.

Its docs: `apps/docs/README.md`.

### The project IDE

`apps/project-IDE/` is the window of the owner on the project. It also gives the context to each AI.

- `current-ui/` contains the File Tree page, `file-tree-explorer.html`, and its data file, `file-tree.data.json`. The page is on claude.ai at https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs.
- `server/` operates the same page on the owner's server. Claude Code operates behind the request box of the page.
- The server files are `server.py`, `claude_bridge.py`, `voice.py`, `server.config.json` and `README.md`. `voice.py` changes speech to text with Groq.
- `data/` is the planned location of the project records: inputs, decisions, changelog, tree notes, knowledge map, plans, working notes, the page store and the archive.
- During the planning, the records are in the planning area. The build copies them into `data/`.
- `docs/` contains the four docs of the IDE. Its README is the full documentation of the IDE.

The page shows each file and each folder of the repository:

- The File tab shows the text of a file. The owner can read and edit the text.
- The metadata files show as tabs: How it works, Details, Example, Questions and the ASD-STE100 version of a README.
- Some kinds of file have custom views. An example is the table of key names for a `.env` file.
- A tab shows only when its file exists.
- A "metadata" switch shows or hides the metadata files in the tree.
- Each item has a request box for questions and changes.
- On the owner's server, a voice button records the owner.
- Each item has a Delete button.
- The "Apply changes" button at the top puts all changes from the page into the files.

During the planning, start the page on the owner's server from the top of the repository with `python3 vision/server/server.py`. The server listens only on the machine, at `127.0.0.1:8765`. Use an SSH tunnel to open it.

Its docs: `apps/project-IDE/docs/README.md`.

### Keys and secrets

`.secrets/` at the top of the repository is the one location for all private keys. It is outside `agents/`. Thus no agent folder and no link can get to it.

- `.secrets/test/.env` contains all test keys.
- `.secrets/live/.env` will contain the live keys, with the same names. Only the owner writes this file.
- The two `.env` files stay on the machine. Do not put them in git.
- `.secrets/secrets.index.json` lists the key names and the files that use them. It does not contain values.
- The folder, `test/`, `live/`, the index and all How it works and Details files are in git. They show in the tree.

The page shows each `.env` file as local-only. The page does not read, show or edit the text of a `.env` file.

Settings and docs give the names of keys. They do not give the values. Two of the key names are `ANTHROPIC_API_KEY`, for Claude Code on the server, and `GROQ_API_KEY`, for voice input.

`.gitignore` keeps all `.env` files out of git. An `.env.example` file is the exception, because it contains only names. `.gitignore` keeps the How it works, Details and Questions files of a keys file in git. It also keeps these items out of git:

- dependencies and build output: `node_modules/`, `dist/`, `build/`, `.venv/` and `venv/`
- Python caches
- OS files and editor files
- the local state of Cursor

Each entry in `.gitignore` has a comment that tells why.

Its docs: `.secrets/.secrets.index.md` and `.gitignore.index.md`.

### Metadata files

Each file and each folder outside the planning area has metadata files next to it. The name of a metadata file is the name of the item without its extension.

| Metadata file | Tab on the page | Content |
|---|---|---|
| `x.index.md` | How it works | What the item is, who keeps it, when and how it changes, who uses it, where other files mention it, related knowledge, and a maximum of four "keep in mind" lines, in plain words |
| `x.meta.json` | Details | The facts about the item: its kind, its state, git or secret, who writes it, who reads it, when it changes, related files, sources, what must change with it, and what applies from the levels above |
| `x.example.md` | Example | The outline of the item: its sections and the content of each section |
| `x.questions.md` | Questions | Two parts. Part 1: the open questions for the owner. Plans and the `make-questions` skill write them. Part 2: each question that the owner asked about the item, word for word, with its answer |
| `x.{type}.{name}.view.html` | A custom view | A view for one kind of item. It is planned |

- A folder `f/` keeps its metadata files inside it, as `f/f.index.md` and `f/f.meta.json`.
- A file without an extension keeps its full name, for example `.gitignore.index.md`.
- The metadata files of the root are `agent-os.index.md` and `agent-os.meta.json`.
- A metadata file has no metadata files.
- Now, only the main docs and the two `.env` files have Example files and Questions files. The example of a `.env` file is `.env.example`. It contains only key names.

During the planning, the source of each How it works file and each Details file is in the mirror tree of the planning area, `vision/tree/agent-os/`. The build copies each file next to its item. The knowledge base agent writes these files with the `file-index` skill. It writes the children before their folders.

`docs/metadata.md` tells all of the logic, step by step, in ASD-STE100.

Its docs: `docs/metadata.md`, `agent-os.index.md` and the `file-index` skill, `agents/system/.claude/skills/file-index/SKILL.md`.

### The planning area

`vision/` contains all the material that we use to plan the project. It is the workshop. The other parts of the repository are the system as we design it.

- `vision/docs/` is the knowledge base.
- `vision/docs/inputs/` keeps each owner input word for word, with its answer. It also has `index.json`.
- `vision/docs/decisions.md` keeps all decisions.
- `vision/docs/changelog.md` records the changes. The newest change is first.
- `vision/docs/file-tree.md` contains the tree notes: the planned tree and one section for each file and each folder.
- `vision/docs/` also contains the knowledge map.
- `vision/docs/` also contains earlier knowledge notes. They are kept. They are not used now.
- `vision/plans/` contains one plan for each change request, and `index.json`.
- `vision/.claude/` contains the planning copies of the helper agents, the skills and the working memory (`memory/`). It also contains earlier notes behind the docs. They are kept. They are not used now.
- `vision/tools/` contains the build scripts: `parse.py`, `enrich.py`, `materialize.py`, `tabs.py`, `build_map.py`, `index_files.py` and `check_page.js`. It also contains `overrides.json`, which keeps the owner's page edits in the data.
- `vision/explorer/` contains the page source, its data and the texts of the real files that the page shows.
- `vision/server/` contains the server of the page. During the planning, the server operates from here.
- `vision/tree/agent-os/` is the mirror tree of all How it works files and Details files.
- `vision/archive/` keeps old texts, by date. It includes the old drafts of the docs and the files of the prediction-market domain for stage two.

The build copies the drafts, records and metadata files from `vision/` to their locations in the tree. We write the docs of each level in their own folders.

It is an open subject when the real files become the only source. After that change, `vision/` becomes an archive. The plan for this change is `apps/project-IDE/data/plans/2026-10-13-leave-vision.md`. It waits for the approval of the owner. In the plan, the identifiers, numbers and decisions of the tree notes go into the Details file of each item. The records go to `apps/project-IDE/data/`. The build scripts go into the `ide-build` skill. The page goes to `apps/project-IDE/current-ui/`. The server settings are corrected. The build stops the copy of drafts and metadata.

Its docs: `vision/docs/README.md` and `vision/tools/README.md`.

## How a round of work goes

Each round has the same steps. The source of the round can be a chat, the page or the work of the AI.

1. Pull the latest `main` into the working branch.
2. Keep the owner's input word for word in `vision/docs/inputs/`. Use the `knowledge-intake` skill. Add a summary, the categories and the answer. Keep a question and its answer as one input.
3. Write a plan in `vision/plans/` with the `change-plan` skill. Show the plan to the owner. Start the work only after the owner approves it. A small fix does not need a plan.
4. Update the docs of each level that the change touches. Use this order in each level: `vision.md`, `README.md`, `README.asd.md`, `rebuild-prompt.md`.
5. Use this order of levels: project, system, apps, project IDE, trading. When a lower level changes, update the levels above it.
6. Write the decisions in `vision/docs/decisions.md`. Write a line in `vision/docs/changelog.md`.
7. Write each stale How it works file and Details file again with `file-index`. Do the children first. Continue until no file is stale.
8. Build the page again with `ide-build`. If the owner pushed "Apply changes", do `ide-sync` first.
9. The build does these steps: parse, enrich, materialize, check the How it works files, write `docs/file-tree.md`, test the page and publish it at the same link.
10. Compare the page tree with the disk. The page tree must list the same files as git (`git ls-files --cached --others --exclude-standard`), and the two local-only `.env` files.
11. Commit the change. The message must tell what changed and which input caused the change.
12. Open or update a pull request into `main`.
13. Merge only when the owner tells you to merge.

## The stages

Stage one is the current stage. In stage one, we do this work:

1. Complete the project IDE and its full documentation.
2. Examine each file and each folder. Write the custom views. Make all metadata correct.
3. Complete the docs of the project, the system, trading and the apps.

In stage one, do not change the contents of the prediction-market domain.

Stage two is the prediction-market domain: its docs, its strategies and their trading agents. The old files of the domain wait in the archive of the planning area.

After stage two, we build the machinery of the system. We start the first strategy in test mode. We add more trading domains and agents of other kinds.

## Where each part's docs are

| Part | Its docs | Content |
|---|---|---|
| The full project | `docs/vision.md`, `docs/README.md` | Why, the method of work and each part of the repository |
| The front page | `README.index.md` | The purpose of the front page |
| The handoff | `HANDOFF.index.md` | The purpose of the handoff |
| All paths | `docs/file-tree.md` | The plain list of the repository |
| The entry point for Claude Code | `agents/system/CLAUDE.md` | What to read first, the rules and the round |
| Agents | `agents/agents.index.md` | The domains and the standard folder |
| The system | `agents/system/docs/README.md` | The exact description of each shared part of the system |
| Trading | `agents/trading/docs/README.md` | The trading domains and their research |
| The prediction-market domain | `agents/trading/prediction-market/prediction-market.index.md` | Its folders. Its README comes in stage two |
| Apps | `apps/docs/README.md` | Each app and how we add apps |
| The project IDE | `apps/project-IDE/docs/README.md` | The full documentation of the IDE |
| The IDE server | `apps/project-IDE/server/README.md` | How to operate the page on the owner's server |
| Keys | `.secrets/.secrets.index.md` | How we keep keys |
| Git ignore rules | `.gitignore.index.md` | Each ignore rule |
| Metadata files | `docs/metadata.md`, `agents/system/.claude/skills/file-index/SKILL.md` | All of the metadata logic, and how to write each metadata file |
| The planning area | `vision/docs/README.md`, `vision/tools/README.md` | The knowledge base and the build |

## Still open in the design

- Doc names: Do we keep the name `rebuild-prompt.md`, or do we change it to `reverse-prompt.md`?
- Repository name: Do we change the name of the repository and its top folder to `agent-os`?
- Front page: What does `README.md` at the top tell? It is empty now.
- Planning area: When do the real files become the only source? When does `vision/` become an archive? Until then, the build copies the drafts to their locations.
- Records: Do the records move from `vision/docs/` to `apps/project-IDE/data/`, as planned?
- Plain file tree: Do we add some information to each line of `docs/file-tree.md` later?
- Metadata tabs: Which other files get Example, Questions, Tests and changelog files? Which custom views does each kind of item get?
- Folder names in the prediction-market domain: Do the strategy folders and the trading agent folders keep their current names?
