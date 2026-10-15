# Apps

## In short

Apps are the programs that sit next to the agents of the Agent OS and help people and agents work with it: our own apps, outside apps we adopt as a fork, and outside code we copy only to study it. Every app explains itself with its own vision, README and rebuild prompt. Today `apps/` holds one working app, the owner's project IDE; a dashboard for the prediction-market domain is kept as an empty folder; no outside code has come in yet. This document describes the `apps/` folder exactly: every app, how the folder is laid out, the rules for outside code, and where each app's own docs are. Why the system has apps and how they should work for us is in the vision, `apps/docs/vision.md`.

## The apps at a glance

| App | Kind | What it is for | Where it lives | State |
|---|---|---|---|---|
| Project IDE | ours | the owner's window on the project: the File Tree page, its server and the project's knowledge | `apps/project-IDE/` | built and in use |
| Prediction-market dashboard | ours | that domain's screen to watch and control its trading agents | `apps/trading-ui/` | empty folder; stage two; maybe never needed |
| Research copies | research clone | outside repositories copied only to study them | `apps/temp/<name>/` | none yet |
| Apps we use | fork | outside programs we rely on, kept as our own fork | `apps/<name>/` | none yet |

How the apps connect to the rest of the system:

```
 owner ──► project IDE page ──► files of the repository ◄── every AI reads them
                │                        ▲
                │ requests               │ builds the page, folds edits back
                ▼                        │
     Claude Code in agents/system/ ──────┘   (the system's project IDE agent and skills)

 outside code ──► apps/temp/<name>/repo/   study, then delete   ──► findings in the studying agent's research folder
 outside code ──► fork on GitHub ──► apps/<name>/repo/  (main: ours, upstream: the source)
```

## How the folder is laid out

```
apps/
├── apps.index.md            How it works of the apps folder
├── apps.meta.json           Details of the apps folder
├── docs/                    the docs for all apps (this folder)
│   ├── vision.md            why the system has apps and what each kind is for
│   ├── README.md            this file: every app and the path to its docs
│   ├── README.asd.md        this README again in ASD-STE100 Simplified Technical English
│   └── rebuild-prompt.md    how an AI builds apps/ again
├── project-IDE/             the owner's IDE (our own app)
│   ├── docs/                its vision, README, README.asd.md and rebuild prompt
│   ├── current-ui/          the File Tree page and its data, as published on claude.ai
│   ├── server/              the same page on the owner's server, with Claude Code behind it
│   └── data/                the project's knowledge and the records the page is built from
├── temp/                    research clones: <name>/repo/ never committed, <name>/docs/ only when asked
└── trading-ui/              the prediction-market domain's dashboard: empty for now
```

An app we adopt from outside would get its own folder at the same level, `apps/<name>/`, holding `docs/` and `repo/`. None exists yet, and the tree shows no example of one.

Every file and folder of our own apps, and every folder of `apps/` itself, has its How it works file (`x.index.md`) and its Details file (`x.meta.json`) next to it; the four docs in `apps/docs/` also have an Example file (`x.example.md`, the doc's outline) and a Questions file (`x.questions.md`, open questions for the owner). An outside app is the exception: its three docs are all its metadata for now, and the files inside its `repo/` get none.

## The parts

### The apps docs

`apps/docs/` explains the apps folder as a whole: this README, its ASD-STE100 twin `README.asd.md` (the same content in Simplified Technical English, so the two can be compared), the vision and the rebuild prompt. It takes its facts from the system's notes (the tree notes, the decisions and the conventions for apps in `apps/project-IDE/data/`) and from each app's own docs, and gives every reader one place that lists every app. The knowledge base agent in `agents/system/.claude/agents/` writes it with the `vision-doc`, `readme-doc` and `rebuild-prompt-doc` skills, in that order, whenever an app is added, changed or removed. Each app's details stay in that app's own docs; this folder only sums them up.

Its docs: `apps/docs/docs.index.md`

### The project IDE

`apps/project-IDE/` is the owner's IDE and our main app. The owner builds the Agent OS by describing what they want in plain words while AI writes the plans, docs and code; the IDE keeps that understandable. It shows the whole project as a clickable tree where every file and folder has tabs: the file itself, its How it works, its Details, its Example and Questions where they exist, and extra tabs for some kinds of file. The owner can edit, comment, ask questions and delete items, and an Apply changes button carries every change into the files. Every AI uses the same map to find what a file is for, what depends on it and what must change with it.

It holds four folders:

- `current-ui/`: `file-tree-explorer.html`, the page, `file-tree.data.json`, everything the page shows, and `real-files.json`, the text of every file, both generated by the build and never edited by hand. The page is published on claude.ai.
- `server/`: `server.py`, `claude_bridge.py`, `voice.py`, `server.config.json` and a `README.md`. They run the same page on the owner's server, where notes and edits go straight into the files and a request typed on the page runs as a Claude Code session started in `agents/system/`. The service listens only on the machine itself and is reached through an SSH tunnel; pushing, deleting, installing and anything touching `.secrets/` or live actions wait for the owner's click or are refused.
- `data/`: the project's records: every owner input word for word in `inputs/`, `decisions.md`, `changelog.md`, `plans/`, `archive/`, `overrides.json` and, on the server, `page-store/`.
- `docs/`: its own `vision.md`, `README.md` (the IDE's full documentation), `README.asd.md` and `rebuild-prompt.md`.

The IDE's logic does not live in its folder. The project IDE agent and its skills `ide-build` (with the build scripts) and `ide-sync` are in `agents/system/.claude/`, next to the knowledge base agent, so that Claude Code started in `agents/system/` loads them as its own. The IDE takes the whole repository as its input and gives back the page, the owner's edits written into files, and a record of every request.

Finishing the IDE is the main work of stage one: going through every file and folder, writing custom views for the different kinds of file, and making every How it works and Details file correct. Shared views are proposed to live in the IDE itself, in a `views/` folder that does not exist yet.

Its docs: `apps/project-IDE/docs/README.md`

### The prediction-market dashboard

`apps/trading-ui/` is kept for the prediction-market domain's own dashboard: a Next.js API and web app where the owner would watch that domain's trading agents in full (parts, logs, performance, data, decisions and improvements under test), create an agent from a plain description, approve a new strategy version or a live account, stop or delete agents, and ask them questions. Any action that touches live money would need the owner's approval there. The folder is empty apart from its How it works and Details files. It belongs to stage two, together with the rest of the prediction-market domain, and it may never be needed if the project IDE does this job. It has no `docs/` yet; they come when the dashboard is designed.

Still open: whether it would read the domain's files directly or through an API layer, and how it would be reached (only on the machine, or with sign-in).

Its docs: `apps/trading-ui/trading-ui.index.md`

### Research clones

`apps/temp/` holds repositories copied from GitHub only to study them. Each gets `apps/temp/<name>/`, with the clone in `repo/` and, only when the owner asks, our `vision.md`, `README.md` and `rebuild-prompt.md` in `docs/`. The clone is never committed: `.gitignore` must ignore `apps/temp/*/repo/`. The agent or session doing the research writes its findings in its own research folder, and the clone is deleted when the research is done. A program we decide to rely on is not kept here; it is forked and moves to its own folder. Nothing has been cloned yet, so the folder holds only its How it works and Details files.

Its docs: `apps/temp/temp.index.md`

### Apps we use from outside

An outside program the project relies on is forked on GitHub and kept in `apps/<name>/`:

- `docs/` holds our `vision.md` (why this app, and what we changed or plan to change), `README.md` (the source, our fork, its branches and the commit we use, its parts, how to start and test it, how it is updated) and `rebuild-prompt.md` (how to fork it again, the commit to start from and every change we made). For now these docs are all its metadata.
- `repo/` holds our fork. The plan is to keep it as a git submodule, so the repository records the exact commit in use; this is a proposal.

In the fork, `main` is ours: every change we make goes there, and it is what we run. `upstream` follows the source's main branch and is never changed by us. To update: fetch the source, bring `upstream` up to it, merge `upstream` into `main`, run the app's tests, then record the new commit in the app's docs and in the list of apps.

Later, on the owner's request, a skill (`adopt-app`, a proposed name) will turn an app fully into the system's way: a How it works and Details file for every file, one job per file, its features and the other docs. It is not written yet.

No app has come in this way yet. The earlier Polymarket tools are the likely first one, which is still open.

Its docs: each app's own `apps/<name>/docs/README.md`, once it exists

### The list of apps

Every app has one row in the list of apps: its name, its kind (`ours`, `fork` or `research`), its source, our fork and its branches, the commit in use, its last update from the source, and who uses it. The list has no file of its own at the moment. We propose that, until the owner decides where it lives, the table below is that list.

| App | Kind | Source | Fork and branches | Commit in use | Last update from source | Used by |
|---|---|---|---|---|---|---|
| `project-IDE` | ours | this repository | none | this repository's | not applicable | the owner, every AI working on the project |
| `trading-ui` | ours | this repository | none | none (empty) | not applicable | the prediction-market domain, later |

Its docs: this file

## What apps take from and give to the system

- **They take** the repository's files: the project IDE reads every file, How it works and Details file and the knowledge in `apps/project-IDE/data/`; a research clone gives findings to the agent that studies it; an adopted app may later be called by agents as a tool.
- **They give** the owner a way to see and steer the project, every AI the context for a precise change, and the owner's edits and requests back into the files.
- **They follow** the system's rules: no key value is ever stored or shown (key names only; values stay in `.secrets/` on the machine), nothing acts live without the owner's approval, and every change is planned with the `change-plan` skill first.

## Where each part's docs are

| Part | Its docs | What they add |
|---|---|---|
| The apps folder | `apps/docs/vision.md`, `apps/docs/README.md`, `apps/docs/rebuild-prompt.md` | why apps exist, every app, how to build the folder |
| The project IDE | `apps/project-IDE/docs/README.md` | the page, the server and the data in full, and how to rebuild them |
| The IDE's server | `apps/project-IDE/server/README.md` | what the server needs, how to start and reach it, every setting |
| The IDE's knowledge | `apps/project-IDE/data/README.md` | how the knowledge is kept: layers, tags, the flow |
| The IDE's build | `agents/system/.claude/skills/ide-build/scripts/README.md` | how the page is built and checked |
| The dashboard | `apps/trading-ui/trading-ui.index.md` | what it would do, and what is open |
| Research clones | `apps/temp/temp.index.md` | the rules for a clone |
| An app we use | `apps/<name>/docs/README.md` | its source, fork, branches, commit and changes |

## Still open in the design

- **Forks:** submodule (proposed) or a clone that git ignores for `repo/`; where the forks live on GitHub (the owner's account is proposed); how often to update from the source (on request for now; a scheduled check is an idea).
- **Research clones:** whether agents may clone a repository on their own.
- **First outside app:** whether the earlier Polymarket tools come in as a fork.
- **The list of apps:** where it lives: in this README, as now proposed, or in a file of its own.
- **The dashboard:** whether it is needed at all; if so, files or an API layer, and how it is reached; when it gets its own `docs/`.
- **Shared views:** the proposed `apps/project-IDE/views/` folder and its `views.json`.
