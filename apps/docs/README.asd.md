# Apps (ASD-STE100)

This file is the ASD-STE100 Simplified Technical English version of `apps/docs/README.md`. `README.md` is the source. If the two files do not agree, `README.md` is correct.

## In short

Apps are programs that help people and agents to use the Agent OS. There are three kinds of app: our own apps, forks of outside apps that we use, and research clones of outside code. Each app has its own vision, README and rebuild prompt. Now, `apps/` has one app that operates: the project IDE of the owner. The dashboard of the prediction-market domain is an empty folder. No outside code is in the project now.

This document gives a full description of the `apps/` folder. It gives each app, the layout of the folder, the rules for outside code and the location of the docs of each app. The vision tells why the system has apps. The vision is at `apps/docs/vision.md`.

## The apps at a glance

| App | Kind | Function | Location | Condition |
|---|---|---|---|---|
| Project IDE | ours | It shows the project to the owner: the File Tree page, its server and the knowledge of the project | `apps/project-IDE/` | It is complete and the owner uses it |
| Prediction-market dashboard | ours | It shows the trading agents of that domain and controls them | `apps/trading-ui/` | Empty folder; stage two; possibly not necessary |
| Research clones | research clone | Copies of outside repositories, only for study | `apps/temp/<name>/` | None now |
| Apps we use | fork | Outside programs that the project uses, kept as our fork | `apps/<name>/` | None now |

The connections between the apps and the system:

1. The owner uses the page of the project IDE.
2. The page writes the changes of the owner into the files of the repository.
3. On the server, the page sends each request to Claude Code. Claude Code starts in `agents/system/`.
4. The project IDE agent and its skills build the page again from the files.
5. Each AI reads the same files before it makes a change.
6. A research clone goes into `apps/temp/<name>/repo/`. After the study, the clone is deleted. The results go into the research folder of the agent that did the study.
7. An app that we use is a fork on GitHub. The fork goes into `apps/<name>/repo/`. The branch `main` is ours. The branch `upstream` follows the source.

## How the folder is laid out

```
apps/
├── apps.index.md            How it works of the apps folder
├── apps.meta.json           Details of the apps folder
├── docs/                    the docs for all apps (this folder)
│   ├── vision.md            why the system has apps; the function of each kind
│   ├── README.md            each app and the path to its docs
│   ├── README.asd.md        this file
│   └── rebuild-prompt.md    the instructions for an AI to build apps/ again
├── project-IDE/             the IDE of the owner (our app)
│   ├── docs/                its vision, README, README.asd.md and rebuild prompt
│   ├── current-ui/          the File Tree page and its data, published on claude.ai
│   ├── server/              the same page on the server of the owner, with Claude Code
│   └── data/                the knowledge of the project and the records for the page
├── temp/                    research clones: <name>/repo/ is not committed; <name>/docs/ only on request
└── trading-ui/              the dashboard of the prediction-market domain: empty now
```

An outside app that we use gets its own folder at this level: `apps/<name>/`. This folder has `docs/` and `repo/`. No such folder is in the project now. The tree shows no example.

Each file and each folder of our own apps has a How it works file (`x.index.md`) and a Details file (`x.meta.json`). Each folder of `apps/` also has these two files. The four docs in `apps/docs/` also have an Example file (`x.example.md`) and a Questions file (`x.questions.md`). An outside app is different. Its three docs are its only metadata now. The files in its `repo/` folder get no metadata.

## The parts

### The apps docs

`apps/docs/` describes the apps folder as one unit. It has this README, the vision, the rebuild prompt and `README.asd.md`. `README.asd.md` has the same content as the README in Simplified Technical English. Thus, you can compare the two files.

The facts come from the notes of the system in `apps/project-IDE/data/`. The facts also come from the docs of each app. The knowledge base agent writes these docs. The agent uses the skills `vision-doc`, `readme-doc` and `rebuild-prompt-doc`, in that sequence. The agent writes them again when an app is added, changed or removed. The details of an app stay in the docs of that app. This folder gives only a summary.

Its docs: `apps/docs/docs.index.md`

### The project IDE

`apps/project-IDE/` is the IDE of the owner. It is our most important app. The owner builds the Agent OS with plain words, and AI writes the plans, docs and code. The IDE helps the owner to understand the result.

The IDE shows the project as a tree. Each file and each folder has tabs: the file, How it works, Details, and Example and Questions when these files exist. Some kinds of file have more tabs. The owner can edit, comment, ask questions and delete items. The button Apply changes moves all changes into the files. Each AI uses the same tree. The tree tells the function of a file, the files that depend on it and the files that must change with it.

The IDE has four folders:

- `current-ui/` has the page `file-tree-explorer.html`, its data `file-tree.data.json` and `real-files.json`, the text of each file. The build makes the two data files. Do not edit them manually. The page is published on claude.ai.
- `server/` has `server.py`, `claude_bridge.py`, `voice.py`, `server.config.json` and `README.md`. These files operate the same page on the server of the owner. On the server, notes and edits go directly into the files. A request on the page operates as a Claude Code session. The session starts in `agents/system/`. The service accepts connections only from the same machine. The owner connects through an SSH tunnel. Push, delete, install, live actions and access to `.secrets/` need the approval of the owner, or the server refuses them.
- `data/` has the records of the project: `inputs/` (each input of the owner, word for word), `decisions.md`, `changelog.md`, `plans/`, `archive/`, `overrides.json` and, on the server, `page-store/`.
- `docs/` has the docs of the IDE: `vision.md`, `README.md` (the full documentation of the IDE), `README.asd.md` and `rebuild-prompt.md`.

The logic of the IDE is not in its folder. The project IDE agent and its skills `ide-build` and `ide-sync` are in `agents/system/.claude/`. The build scripts are in the skill `ide-build`. Claude Code starts in `agents/system/`, thus it loads this agent and these skills. The IDE reads all the repository. It gives the page, writes the edits of the owner into files, and keeps a record of each request.

Stage one is to complete the IDE. Do these tasks: examine each file and each folder, write custom views for the different kinds of file, and make each How it works file and each Details file correct. We propose a folder `apps/project-IDE/views/` for the shared views. This folder does not exist now.

Its docs: `apps/project-IDE/docs/README.md`

### The prediction-market dashboard

`apps/trading-ui/` is for the dashboard of the prediction-market domain. The dashboard is a Next.js API and web app. With it, the owner can monitor the trading agents of that domain: their parts, logs, performance, data, decisions and the improvements in test. The owner can also create an agent from a plain description, approve a new strategy version or a live account, stop or delete agents, and ask questions to agents. Each action with live money needs the approval of the owner.

The folder is empty. It has only its How it works file and its Details file. It is part of stage two, with all the prediction-market domain. Possibly the project IDE does this function, and the dashboard is not necessary. The dashboard has no `docs/` folder now. The docs come when the design of the dashboard starts.

These questions are open: Does the dashboard read the files of the domain directly or through an API layer? How does the owner get access to it: only on the machine, or with a sign-in?

Its docs: `apps/trading-ui/trading-ui.index.md`

### Research clones

`apps/temp/` has repositories from GitHub that we copy only for study. Each repository gets a folder `apps/temp/<name>/`. The clone goes into `repo/`. Our `vision.md`, `README.md` and `rebuild-prompt.md` go into `docs/` only when the owner asks for them.

Do not commit the clone. `.gitignore` must ignore `apps/temp/*/repo/`. The agent that does the research writes the results in its own research folder. When the research is complete, delete the clone. If we decide to use the program, we make a fork. The fork goes into its own folder, not into `temp/`. Now, there are no clones. The folder has only its How it works file and its Details file.

Its docs: `apps/temp/temp.index.md`

### Apps we use from outside

We make a fork on GitHub of each outside program that the project uses. The fork goes into `apps/<name>/`:

- `docs/` has our `vision.md`, `README.md` and `rebuild-prompt.md`. The vision tells why we use this app and what we changed. The README gives the source, our fork, its branches, the commit in use, its parts, how to start and test it, and how to update it. The rebuild prompt tells how to make the fork again, the start commit and each change that we made. Now, these three docs are the only metadata of the app.
- `repo/` has our fork. We propose to keep it as a git submodule. Then the repository records the exact commit in use.

The fork has two branches. The branch `main` is ours. All our changes go into `main`, and we operate `main`. The branch `upstream` follows the main branch of the source. We do not change `upstream`.

To update the app, do these steps:

1. Get the changes from the source.
2. Move `upstream` to the new source commit.
3. Merge `upstream` into `main`.
4. Do the tests of the app.
5. Record the new commit in the docs of the app and in the list of apps.

Later, the owner can ask for a skill that changes an app fully to the system format. The proposed name of the skill is `adopt-app`. The skill gives a How it works file and a Details file to each file of the app, one job to each file, its features and the other docs. This skill does not exist now.

Now, there is no app of this kind. Possibly the first is the old Polymarket tools. This question is open.

Its docs: `apps/<name>/docs/README.md` of each app, when it exists

### The list of apps

Each app has one row in the list of apps. The row gives the name, the kind (`ours`, `fork` or `research`), the source, our fork and its branches, the commit in use, the last update from the source, and the users. Now, the list has no file. We propose that this table is the list until the owner decides its location.

| App | Kind | Source | Fork and branches | Commit in use | Last update from source | Users |
|---|---|---|---|---|---|---|
| `project-IDE` | ours | this repository | none | the commit of this repository | not applicable | the owner, each AI that works on the project |
| `trading-ui` | ours | this repository | none | none (empty) | not applicable | the prediction-market domain, later |

Its docs: this file

## What apps take from and give to the system

- **Apps take** the files of the repository. The project IDE reads each file, each How it works file, each Details file and the knowledge in `apps/project-IDE/data/`. A research clone gives results to the agent that does the study. Later, agents can use an outside app as a tool.
- **Apps give** the owner a method to see and control the project. They give each AI the context for a correct change. They write the edits and requests of the owner into the files.
- **Apps obey** the rules of the system. An app does not keep or show the value of a key. An app uses only key names. The values stay in `.secrets/` on the machine. No action is live without the approval of the owner. Each change starts with a plan from the skill `change-plan`.

## Where each part's docs are

| Part | Its docs | Content |
|---|---|---|
| The apps folder | `apps/docs/vision.md`, `apps/docs/README.md`, `apps/docs/rebuild-prompt.md` | why apps exist, each app, how to build the folder |
| The project IDE | `apps/project-IDE/docs/README.md` | the page, the server and the data, and how to build them again |
| The server of the IDE | `apps/project-IDE/server/README.md` | the server requirements, how to start it and connect to it, each setting |
| The knowledge of the IDE | `apps/project-IDE/data/README.md` | how the system keeps the knowledge: layers, tags, the flow |
| The build of the IDE | `agents/system/.claude/skills/ide-build/scripts/README.md` | how the build makes and checks the page |
| The dashboard | `apps/trading-ui/trading-ui.index.md` | its function and the open questions |
| Research clones | `apps/temp/temp.index.md` | the rules for a clone |
| An app we use | `apps/<name>/docs/README.md` | its source, fork, branches, commit and changes |

## Still open in the design

- **Forks:** Is `repo/` a submodule (proposed) or a clone that git ignores? Where are the forks on GitHub (proposed: the account of the owner)? How frequently do we update from the source (now: only on request; a scheduled check is an idea)?
- **Research clones:** Can agents make a clone without a request from the owner?
- **First outside app:** Do the old Polymarket tools come in as a fork?
- **The list of apps:** Where is the list: in this README (proposed now) or in a separate file?
- **The dashboard:** Is it necessary? If yes, does it use files or an API layer, and how does the owner get access? When does it get its `docs/` folder?
- **Shared views:** the proposed folder `apps/project-IDE/views/` and its file `views.json`.
