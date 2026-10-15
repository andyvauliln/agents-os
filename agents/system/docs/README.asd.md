This is the ASD-STE100 (Simplified Technical English) version of `README.md`. `README.md` is the source. If the two documents do not agree, `README.md` is correct.

# The system domain

## In short

The Agent OS is a personal system of the owner. It operates AI agents of different kinds. Examples are agents that trade, agents that work on social media and agents that help with management. The Agent OS operates many small agents at the same time. Each agent has one clear job. The system tries each idea safely first, and it keeps the ideas that work.

The system domain is the top of the Agent OS. It contains the system agent. The system agent monitors each domain, the health of the full system and the development of the system. The system domain also contains all the parts that each agent uses. These parts include the standard agent folder, the scheduler, the links, the settings, the safety rules and the keys. They also include the helpers that keep the knowledge and the window of the owner on the project.

The project is in its first stage. The design is complete, and real files show it. No part of the system operates yet.

This document gives a full and exact description of each main part of the system domain. It tells how the parts operate together. For each part, it gives the path to the documents of that part. It describes the parts from the outside. It does not describe the logic inside an agent.

It describes only the rules that apply to all agents. One area of work can add its own parts, for example money and orders for trading. The documents of that area describe these parts. The vision tells why the system exists, how it must operate and what its business logic is. The vision is `agents/system/docs/vision.md`.

## The system at a glance

The full Agent OS is one repository of folders and files. Each agent is one folder. All agent folders have the same structure. An agent folder contains the files of the agent and links to files in other locations.

The system domain is in `agents/system/`. It contains the system agent, the shared files and the helpers that look after the project. Some shared parts are outside this folder, for example the keys folder and the File Tree page. These parts serve all agents in the same way.

```text
  outside world: prices, news, events, errors
          │
          ▼
  workers ─────────────────► data files, kept by source
     ▲                             │ file links, read-only
     │                             ▼
  scheduler ── starts runs ──► agents in levels
     ▲                           system agent
     │                           └─► domain agents
     └── every agent's               └─► the levels each domain defines ◄──► self-improvement helpers
         jobs file                           │
                                             ▼
                                 actions, test or live, through scripts
                                 own logs, data and results, read by the level above

keys folder ──► one shared loader ──► only the script that needs a key, at run time
  the owner ──► File Tree page ──► project IDE agent, knowledge base agent ──► files, docs
```

| Part | Purpose | Location |
|---|---|---|
| Agents and their levels | All agents, from the system to the levels of a domain, each in one standard folder | `agents/` |
| The system agent and the shared files | Looks after the full system. Keeps the files that all agents use. | `agents/system/` |
| Domains | One area of work for each domain. A domain agent is responsible for it. | `agents/trading/` and the domains in it |
| Workers and data | Collect information and keep it in files | `agents/system/scripts/workers/`, `agents/system/data/` |
| Jobs and the scheduler | All tasks of an agent, in one list for each agent. One scheduler starts them. | the `configs/` of each agent, `agents/system/scripts/system/` |
| Links between agents | Give each agent the files that it needs, without copies | the `configs/` and content folders of each agent |
| Settings and AI models | The settings that you can control, and the AI model of each part | `agents/system/configs/` |
| Actions: test and live | Each outside action has a test mode and a live mode. One gate controls all actions. | the scripts that do actions, `agents/system/configs/system.config.json` |
| Keys and secrets | The keys to accounts and services, in a separate location | `.secrets/` |
| Logs | The record of all events | `agents/system/logs/`, the `logs/` of each agent |
| Tests | Tests of the instructions, helpers and code of each level | `agents/system/tests/`, the `tests/` of each level |
| Research | The research of each level and its results | `agents/system/research/`, the `research/` of each level |
| Self-improvement helpers | Make better versions at each level | the `.claude/agents/` of each level |
| Each agent's AI setup | The instructions, settings, skills and helpers of each level | the `.claude/` of each level |
| The knowledge base and the docs | Keep all knowledge and write the documents | `agents/system/docs/`, the records in `apps/project-IDE/data/` |
| The project IDE | The window of the owner on the project: the File Tree page | `apps/project-IDE/`, looked after from `agents/system/.claude/` |
| The server | The computer that operates the system, and the page service on it | one server of the owner |

The parts send data to each other in this sequence:

1. Jobs start all work. The scheduler reads the jobs file of each agent. It starts each job at its time. A job can be a worker, the run of an agent or a helper.
2. Workers bring information into the system. A worker gets data from its source and writes a file. A shared worker writes into `agents/system/data/workers/[worker]/`. The worker of a domain or of an agent writes into the `data/` of that level. AI helpers read these files and write their results as files.
3. Links give each agent its files. Each agent lists the files that it needs in its links file. One shared script, relink, makes links in the folders of the agent from this list. The agent reads the files through the links. It does not get copies. A change to an important file starts a new run. Other changes wait for the next run.
4. Agents do actions through scripts. An action in the outside world goes through a script. The script uses the mode from the settings of the agent: test or live. Before the action, the gate checks the mode, the limits and the stop switch. A script that needs a key gets the key from one shared loader. It gets the key when it runs. It gets only the keys that its settings name.
5. Results stay with the agent. Each agent writes its logs and data in its own folder. Each level reads the folders of its children through child links. The system reads each domain. A domain reads the first level below it, and so on.
6. Self-improvement closes the loop. The self-improvement helper of a level reads the results of that level. It also reads research, outside news and the comments of the owner. It writes a short report about a new version. When the owner approves the report, the system makes the version as a new agent in test mode.
7. The words of the owner become files. The owner writes messages in the project chat or on the File Tree page. The knowledge base agent keeps each message word for word. It updates the notes and the documents. It writes each edit from the page into its file.

## How the project is laid out

The system will have hundreds of agents. A person or a tool must find each item without help. Thus the project is one tree, and each level of the tree has the same structure. The repository on the disk is the same as the tree on the File Tree page. This is the top of the repository:

```text
agent-os/
├── README.md               the front page: what this is and where to start
├── .gitignore              keeps the key files, local tool state and build leftovers out of git
├── .secrets/               the keys folder; in git without the .env files that hold the values
├── docs/                   the project docs: the whole repository, read first
├── agents/                 every agent
│   ├── system/             the system domain: the system agent, the shared files, the helpers
│   └── trading/            trading in general, its research and its domains
├── apps/                   our own apps, the outside apps we use, research clones
│   ├── docs/               the docs for all apps
│   └── project-IDE/        the owner's window: the File Tree page, its server, its records
```

This is the folder of the system domain, `agents/system/`:

```text
agents/system/
├── CLAUDE.md          read first by Claude Code started here: the project, its stage, the rules, the round
├── .claude/           the system's AI setup: settings, helpers, skills
├── configs/           system.config.json, models.config.json, system.workers.json, system.links.json
├── scripts/           system/ (the machinery), workers/ (shared collectors)
├── logs/              system/, services/, workers/, subagents/
├── data/              system/, workers/, subagents/
├── docs/              vision.md, README.md, README.asd.md, rebuild-prompt.md; how-to/, the runbooks
├── tests/             agents/, scripts/
├── research/          index.json and one folder per item
├── package.json       the JavaScript packages the shared scripts use
├── requirements.txt   the Python packages the shared scripts use
├── init.sh            sets up the project: git hooks, then relink everywhere
└── start.sh           starts the scheduler and the system's own session
```

The folder of each agent has the same parts at each level:

```text
[agent-name]/
├── .claude/          its AI setup: instructions, settings, skills, helpers and their memory
├── configs/          its settings file, its jobs file and its links file
├── scripts/          its own scripts
├── logs/             what it did: runs, decisions, jobs and test results
├── data/             what it collected and produced
├── docs/             its own docs, starting with its vision, README and rebuild prompt
├── tests/            tests of its instructions and helpers, and of its code
├── research/         its research: a list of every item, and one folder per item
├── package.json      the JavaScript packages its scripts use
├── requirements.txt  the Python packages its scripts use
├── init.sh           sets the agent up, including its links
└── start.sh          does one run
```

The content folders are `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/` and `research/`. Each content folder contains the real files of the agent. It also contains links to files in other locations. At a level with children, it contains one link for each child. All agents have the same structure. Thus the shared tools find the items in the same location at each level.

One rule applies to all code. Each code file contains one item that can run, for example one function, one endpoint, one script or one worker. The item has one purpose. It can accept parameters. Do not put different jobs into one file. Put related items in one folder, with one item in each file.

Each file and each folder has notes next to it. The How it works file explains the item in simple words. The name of this file is the name of the item without its extension, for example `vision.index.md` next to `vision.md`. For a folder, the file is inside the folder, for example `configs/configs.index.md`. The Details file, for example `vision.meta.json`, contains the facts and relations of the item.

These facts include the kind of item, its git state, and its writers and readers. They also include the files that change with it and the sources of its knowledge. Some files also have an Example file, `x.example.md`, with the structure of the file. Some files have a Questions file, `x.questions.md`, with the open questions about the file. These two files exist only where somebody wrote them.

Each planned file and each planned folder already exists on the disk. A file with a draft contains the text of the draft. The other files are empty. A placeholder, for example `[domain-name]/`, is a real folder that contains only its notes.

### How a level reaches its children

If each agent can go into each other agent, a change in one location can cause damage in an unknown location. Also, it is not possible to understand an agent alone. Thus a parent can see its children, but a child cannot see its parent. The system reads each domain.

Each domain reads the first level below it. This continues to the lowest level. A lower level does not go up.

A parent uses child links for this. Each content folder of a level with children contains a folder `subagents.link/`. This folder has one folder link for each direct child. The link has the name of the child. It points to the folder of the same kind in the child:

```text
agents/system/docs/subagents.link/[domain-name]/      → that domain's docs/
agents/system/configs/subagents.link/[domain-name]/   → that domain's configs/
```

The same rule applies to `scripts/`, `logs/`, `data/`, `tests/` and `research/`. Some domains are in a folder for domains of one kind, for example a trading domain in `agents/trading/`. Such a domain is also a direct child of the system. The links of the system point directly to its folders.

You only read through child links. You do not copy them. Child links are the only folder links in the system. Relink makes them from the folder tree.

Relink removes a child link when the child is removed. Tools that scan folders do not follow child links. Now each `subagents.link/` contains only its placeholder `[domain-name]/`, because no domain has its folders yet. No level links a `.claude/` folder.

## The parts

Each part below tells these facts in this sequence:

1. What the part is.
2. What it contains.
3. What it gets from other parts, and what it gives to other parts.
4. When and where it runs.
5. Its status.

A plain statement is a decision. "The plan is" or "we propose" shows a proposal. Each part names its open subjects. The list at the end of this document gives all open subjects.

No part runs yet. The files in this document exist, but most of them are empty. Nobody wrote the scripts yet.

### Agents and their levels

An agent is one folder with its own AI instructions. It is responsible for one part of the Agent OS. Agents are in levels. Each agent has a parent above it. Only the system agent has no parent.

The system agent looks after the full Agent OS. A domain agent is responsible for one area of work. Each domain puts its agents in the levels that its work needs. An agent can have versions.

The versions can have different settings, instructions, code or AI models. The versions run at the same time and compete. The system keeps the better versions. An agent can be code, AI or both.

All agents are in `agents/`. The system is in `agents/system/`. A domain is directly in `agents/`, or in a folder for domains of one kind, for example `agents/trading/`. The folder of a domain is the folder of its domain agent. The agents of its lower levels are subfolders of it. Each agent has the standard folder.

The system will have hundreds of agents. The name of an agent must show quickly what the agent is. Two agents must not have the same name. Thus each agent has one name. The name is unique in the full system.

The folder, settings, logs, data, docs and screen of the agent use this name. Do not change or use again a name, also after you delete the agent. Some domains put the mode and the AI model of an agent into its name. Then the mode is always the last part: test or live. We propose these rules:

- Each name starts with the code of its domain. The code of the system is `sys`.
- The name of the system agent is `sys-system-agent`.
- The system keeps a list of all agents. The script that makes agents uses this list to check new names.

An improvement does not change an agent that runs. An improvement always becomes a new agent in test mode. We propose that the new agent records its source agent. We also propose that it records all differences in its `docs/changes.md`.

Each level also has helpers. A helper is an AI assistant with its own instructions and tools. Each helper is a Claude Code sub-agent, in one file in the `.claude/agents/` of the level. A helper runs in the session of its own level. It writes its results as files. Agents read these files through links.

One shared script, create-agent, makes new agents. It is in `agents/system/scripts/system/`. It checks the name, makes the standard folder and runs the `init.sh` of the new agent. The owner can ask for a new agent in plain words.

Then the system makes the agent and connects it into the system. The plan is that each level runs in its own folder. Thus a session sees only its own setup, links and children.

Open subjects: Does a small change make a new version? Can an agent change its own settings?

Its docs: `agents/agents.index.md`

### The system agent and the shared files

The system agent is the system manager. It monitors each domain. It monitors the health, the costs and the development of the full system. It makes a plan for each new domain before the system makes the domain. It answers the questions of the owner about the full system.

The system agent is in `agents/system/`. It has the same standard folder as all agents. It has only two differences. It is the root of the family tree. Its folders also contain the files that all agents use.

The instructions of the system agent are in `agents/system/CLAUDE.md`. Claude Code reads this file automatically when it starts in `agents/system/`. The owner starts Claude Code in this folder on the server. The file tells each AI these facts:

- what the project is, and its stage;
- what to read first, and in which sequence;
- where the items are;
- the rules for each AI;
- what to do after each input or update;
- which document each type of change makes old, and which skill writes that document;
- how the File Tree page operates;
- the job of the system manager.

The part about the system manager is our proposal. It stays a proposal until the owner approves it.

One rule controls the shared files. If agents of different domains use a file, the file is in the system domain. If only one domain uses a file, the file is in that domain. If only one agent uses a file, the file is in the folder of that agent. `agents/system/` keeps the shared settings in `configs/`, the shared scripts in `scripts/`, the shared logs in `logs/` and the shared data in `data/`.

It also has its own `docs/`, `tests/` and `research/`. Its `package.json` and `requirements.txt` list the packages that the shared scripts use. We propose this rule: when a second agent needs a file of one agent, move the file into the shared folder. Then both agents link to it.

The system gets questions about the full system from the owner. It reads the files of its children through the `subagents.link/` folders. It gives each agent the shared settings, scripts and data. It always gives them as links to the one real file.

The plan is that the `init.sh` of the system installs the git hooks of the repository. Then it runs relink for the full project. The plan is that the `start.sh` of the system starts the scheduler and the session of the system. Both files are empty now.

Open subject: Must the owner approve a change to the shared settings before the change gets to live agents?

Its docs: `agents/system/system.index.md`

### Domains

A domain is one area of work. The folder of the domain is the folder of its domain agent. The domain agent finds, makes and updates the agents of its area. It makes sure that they get to the goal of the domain. It answers the questions of the owner about the domain.

Each domain tells these facts:

- its goal;
- the levels of its agents;
- where its agents can do actions;
- where its agents only collect information;
- the rules that it adds to the shared rules, for example the money limits of trading.

A domain has the standard folder, as each level has. It has its own instructions, its own self-improvement helper, its jobs file and its links file. It has its own workers and its research. It has its own documents: a vision, a README, an ASD-STE100 version of the README and a rebuild prompt. These documents tell only about the domain.

A domain keeps all items that only it needs, for example its own settings, notes and scripts. To make a new domain, copy the domain that is most similar. It has the same levels, rules and documents. Then change only the differences.

A domain gets its part of the shared settings, scripts and data through links. It reads the level below it through its child links. The system reads each domain through its own child links.

Domains of one kind are in one folder. `agents/trading/` contains the trading domains. Its `docs/` contains the vision, the README, the ASD-STE100 README and the rebuild prompt of trading. These documents tell what all trading domains share and how to make a new trading domain. Its `researches/` contains the trading studies that are complete. It has no agent, settings or scripts of its own.

The first trading domain is the prediction-market domain, `agents/trading/prediction-market/`. It starts with Polymarket. This domain is the second stage of the project. Now only its folders exist. Its `docs/` folder contains earlier notes. They are kept for stage two. The other folders contain no written files.

The next trading domain is copy trading. The system makes it as a copy of the prediction-market domain when the owner asks. Agents of other kinds come later as their own domains, for example social media or management.

Its docs: `agents/trading/docs/README.md`

### Workers and data

Workers are scripts. They collect information on a schedule, for example prices, news, important events and errors. They keep the information in files. The name of a script shows its kind.

`.worker.` shows a worker. `.system.` shows the machinery, for example setup, schedules, links and tests. These two kinds apply to all agents. A domain can add its own kinds.

Agents in different domains can use one worker. Such a worker is shared. It is in `agents/system/scripts/workers/`. It writes to `agents/system/data/workers/[worker]/`. It writes its log to `agents/system/logs/workers/[worker]/`.

Its job is in the jobs file of the system. If only one domain needs a worker, the worker is in that domain. If only one agent needs a worker, the worker is in the `scripts/` of that agent. It writes into the `data/` of that agent, in one folder for each source. No shared worker exists now.

The plan is a workers helper. It will know all workers and their data. An agent that needs new information asks the workers helper. The helper finds data that exists, extends a worker or makes a new worker. Then it tells the agent where the data is and how and when to use it. Thus hundreds of agents do not make the same worker two times.

AI helpers prepare raw information for the agents. A helper of the system writes its result into `agents/system/data/subagents/[subagent]/`. A helper of a lower level writes into the `data/` of its level. Agents link to these results as to all other data.

The system keeps all information in files that a person can open. It uses no database for now. Lists and records are JSON files. Logs that grow have one entry on each line.

Text is Markdown. Shared scripts let agents add, read, change, remove and filter entries in a list safely. We propose that each source keeps a `latest` file next to its dated files. Then links to the `latest` file continue to operate when new files come.

The records of the system are in `agents/system/data/system/`. Examples are the list of all links and the record of the scheduler for each job. The contents of each `data/` folder are output of runs. They are not source files.

Open subjects: How does an agent find the new data since its last run? What is the name and the file of the workers helper?

Its docs: `agents/system/scripts/workers/workers.index.md` and `agents/system/data/data.index.md`

### Jobs and the scheduler

The system will have hundreds of agents. Each agent runs scripts and AI sessions on its own timer. Without a list, nobody can see what runs and when. To stop a task, you must search through the code. Thus each agent has one jobs file that lists all its tasks. One scheduler runs all jobs.

The jobs file is in the `configs/` of the agent. Its name comes from the agent. For the system, it is `agents/system/configs/system.workers.json`. For each other agent, it is `[name].workers.json`.

A job is a script or an AI run. An AI run can be the main run of the agent, a helper, a skill, a workflow or a command. For each job, the file tells these facts:

- what the job does;
- if the job is on or off;
- how frequently it runs: at an interval, at a time of day, one time on a date, after another job, or only by hand;
- where it runs: on the server, in the cloud or in a desktop app;
- which AI platform and model it uses.

The owner and the agent can see, change and stop each job in this file. A parent sees the jobs files of its children through `configs/subagents.link/`. The exact fields of a job are our proposal.

The system has these jobs:

- relink when a links file changes;
- a check of all links;
- a news digest for the domains;
- the self-improvement of the system;
- the nightly run of the knowledge base agent;
- a weekly review of the shared scripts.

All system jobs are off now. They stay in the file. They run only when the owner sets them to on.

One scheduler finds each jobs file and runs each job at its time. The scheduler is a shared script in `agents/system/scripts/system/`. The plan is that the `start.sh` of the system starts the scheduler. The operating system keeps it in operation. The `start.sh` of each other agent does only one run.

A jobs file tells only what must run. The record of the runs is in other locations:

- the record of the scheduler, in `agents/system/data/system/`;
- the log of the scheduler, in `agents/system/logs/system/`;
- the `logs/` of each agent.

Thus a jobs file changes only when somebody changes a job.

The scheduler also controls the time between intervals. When an important file of an agent changes, the scheduler stops the current run. Then it starts a new run with the new information. Changes that are not important wait for the next run.

An agent can wait for a result, for example its research. When the result is ready, the agent runs again with it. A helper of the system checks the capacity of the server. It sets the maximum number of runs at the same time.

We propose two rules. Jobs in the cloud, in a desktop app or on GitHub get no keys and do no live actions. To stop a job, set it to off. Do not delete it.

Open subjects: Which computer runs the scheduler? Does the scheduler make cloud jobs automatically? Which list of important files has priority? How do tests with their own schedules get to the scheduler? What is the exact limit of runs at the same time?

Its docs: `agents/system/configs/system.workers.index.md` and `agents/system/scripts/system/system.index.md`

### Links between agents

Links give each agent the files that it needs from other locations. Links are not copies. If each agent keeps its own copy of a shared file, the copies become different. A repair to one copy does not get to the other copies.

Thus an agent gets shared files as links. A link looks like a file in the folder of the agent, but it points to the one real file. The name of each link contains "link", for example `system.config.link.json` or `subagents.link/`. Thus you can see the difference between a link and a real file.

There are two kinds of links. A file link points to one file that the logic of the agent needs. The file can be anywhere in `agents/`. It can be in the system, in the domain or parent of the agent, in another domain, or in a named agent.

The file link is in a content folder of the agent. The agent only reads through it. A child link is a folder link from a parent to the folder of one child. The section about levels above describes child links.

Each agent lists its file links in one small file in its `configs/`. This file is the links file. For the system, it is `agents/system/configs/system.links.json`. For each other agent, it is `[name].links.json`. For each link, the file tells which file, from where, the location of the link and the reason.

The system sets the list when it makes the agent. Later, the agent, its self-improvement helper or the owner can change it. The list of the system is short. It has two links that let the test folders of the system run the shared test runner.

One shared script, relink, is in `agents/system/scripts/system/`. It reads each links file. It makes the file links and the child links. It removes the links that no file lists.

It checks that no link is broken. Each level below the system has `scripts/relink.system.link.js`. This is a link to relink, and it does relink for that agent only.

Relink runs at these times:

1. When a links file changes.
2. When somebody reviews changes: before the changes go into the repository, and after new changes come from the repository.
3. When an agent edits its own links file.

We propose these items:

- Git hooks start relink. The `init.sh` of the system installs them.
- A hook in the AI settings of each agent starts relink.
- Relink writes a list of all links to `agents/system/data/system/`. Then each person can see which agent reads which file.
- A second shared script, check-links, checks all links after each change.

Do not link a file in the keys folder. Do not link a file in a `.claude/` folder.

Links also let agents listen to each other. An agent can use the output of another agent. To do this, it links to that output. The new data gets to the agent on its next run. If the agent marks the file as important, the new data stops the current run.

Open subjects: Are the links kept in the repository? Can an agent link each file of another agent, or only the files that the other agent lists as its output?

Its docs: `agents/system/configs/system.links.index.md`

### Settings and AI models

The settings are in a small number of JSON files. All of them are in `agents/system/configs/`.

`system.config.json` is the one global settings file. It contains all settings that you can control for the full system. It does not contain jobs or models. The plan is that it has these sections:

- defaults;
- the modes: test as the default, the general stop switch, and the list of agents that can do live actions;
- schedule defaults, with the maximum number of runs at the same time and a maximum AI cost for each day;
- the rules to start a run again when an important file changes;
- notifications.

When a section becomes long, move it into its own file. Settings that only one domain needs, for example money and accounts, are not in this file.

`models.config.json` is the models file. It tells which AI platform and model each agent, helper and AI worker uses. It also tells which platforms you can use. A job can name its own model. If it does not, the models file sets the model.

| Kind of work | Model |
|---|---|
| Thinking, planning, analysis and improvement, and the agents that act | Claude Opus 5.5 at high thinking effort |
| Unimportant tasks | a medium model at medium effort, Claude Sonnet 5.5 |
| Light, high-volume work such as collecting and filtering data | Cursor with its Composer 2.5 model |
| Unimportant work, once connected | free models through OpenRouter, in rotation |
| Later | Codex and Kimi |

Claude Code is the default platform. Each part that uses AI has a route to a platform and a model. Some domains put the model in the name of an agent. For these, we propose that the script that makes agents checks that the name and the route agree.

Each agent below the system has its own settings file, `[name].config.json`. It is next to the jobs file and the links file of the agent. The agent reads the global settings and the models file through links. A domain can keep its own settings file for its area. We propose these rules:

- The settings join in a fixed sequence: global settings, domain settings, agent settings, then the choices of the owner. Examples of these choices are stop and approve.
- A lower level can only make a limit stricter. It cannot make a limit less strict.
- The agent reads the settings at the start of each run. Thus a change applies from the next run of each agent.
- A change to the modes needs the approval of the owner.

All four settings files of the system exist, and they are empty. Their exact fields are our proposal.

Open subjects: What is the exact structure of the files? Which settings are shared, and which settings are for one agent? Two or three example agents will help to decide this. What are the exact default models?

Its docs: `agents/system/configs/configs.index.md`

### Actions: test and live

An action is something that an agent does in the outside world, for example buy, sell or post. Each action has a test mode and a live mode from the start. The settings of the agent select the mode. Each new agent and each change runs in test mode first.

In test mode, nothing real occurs, and errors cost nothing. Some names contain the mode of the agent. Then a test agent and a live agent are always two different agents.

Each domain tells where its agents can do actions. It also tells where its agents only collect information. The system domain has no script that does actions. Each domain writes its own scripts for actions. All these scripts go through the same gate.

A script that does an action reads the mode from the settings of the agent before the action. In test mode, the script does not do a real action. The service that does the action logs each action, in test mode and in live mode. A shared service logs into `agents/system/logs/services/[service]/`. The services of a domain log into the `logs/` of that domain.

An agent does live actions only after it shows good results. It also needs the approval of the owner. The owner approves one agent at a time. No agent can approve live actions, for itself or for another agent. Self-improvement never does live actions. We propose that an action is live only when all these conditions are true:

- The agent is on the list of agents that can do live actions.
- The owner approved the run.
- The settings of the agent ask for live mode.
- The stop switch is off.

We also propose that an agent can never set itself to live mode.

Outside text can contain hidden instructions that try to trick an AI. Examples of outside text are news and social posts. Thus an agent uses outside text only as data. It does not obey instructions in outside text. The system gets protection against such instructions at the same time as live actions.

We propose hard limits for each outside action. Code in the scripts that do actions checks these limits before each action. A domain or an agent can only make the limits stricter. We also propose one general stop switch in the global settings. It stops all outside actions immediately. Only the owner can set it to on or off.

Its docs: `agents/system/configs/system.config.index.md`

### Keys and secrets

Keys to accounts and services are the most dangerous items in the system. A key in a log, a shared file or an AI conversation can become public. An AI that reads a live key can use it incorrectly. Thus all keys are in one folder, `.secrets/`, at the top of the repository. This folder is outside the folders of all agents.

The folder contains these files:

- `.secrets/test/.env`: all test keys in one file. The file has comment sections. Each key name starts with its account or platform. Agents can read and update this file.
- `.secrets/live/.env`: the same key names with real values. Only the owner uses it. The owner makes it when live actions start.
- `.secrets/test/.env.example` and `.secrets/live/.env.example`: the key names, each with a comment of one line. They contain no values.
- `.secrets/secrets.index.json`: which keys exist, what each key is for and who uses it. It never contains a value. The plan is that it stays the same as the key files automatically.

The folder, its subfolders, its notes and `secrets.index.json` are in git. The File Tree page shows them. The `.env` files contain the values. They never go into git.

The page shows them as local files only. The page never reads, shows or edits their text. Key names use capital letters and underscores, for example `ANTHROPIC_API_KEY` or `GROQ_API_KEY`. `AGENT_OS_ENV` tells if a script runs in test mode or live mode.

A script gets only the keys that its settings name. It gets them when it runs. One shared loader, load-secret, gives the keys. It is in `agents/system/scripts/system/`. The settings of an agent or a job list the names of the keys that it needs.

The loader gives only these keys to the process of that one script. Do not link, copy or log a key. Do not show a key to an AI. The plan is that the `.claude/settings.json` of each level stops AI sessions from reading or editing the live keys. The exact operation of the loader is our proposal.

Open subjects: What keeps the list of keys the same as the key files? How does the system keep live keys safe when agents do live actions?

Its docs: `.secrets/.secrets.index.md`

### Logs

Logs are the record of all events: each run, decision, action, job, helper call, error and cost.

Some logs are not for one agent. These logs are shared. They are in `agents/system/logs/`, in one folder for each source:

- `system/`: the scheduler, restarts, relink, link checks, errors and costs;
- `services/[service]/`: each action of each shared service;
- `workers/[worker]/`: the shared workers;
- `subagents/[subagent]/`: the calls of helpers, with each request from the File Tree page on the server of the owner.

A domain keeps the logs of its own jobs and services in its own `logs/`. The system reads the logs of each domain through `agents/system/logs/subagents.link/`.

The logs of each agent are real files in its own `logs/`. They contain its runs, its decisions, the runs of its jobs and its test results. The agent links only the small number of shared logs that it needs. Each level reads the logs of its children through its child links. Thus the screens of the owner can start at the logs of the system and go down level by level.

Logs never contain the value of a key. The contents of each `logs/` folder are output of runs. They are not source files. The folders stay.

Open subjects: What is the exact log format? How long does the system keep logs?

Its docs: `agents/system/logs/logs.index.md`

### Tests

Each level tests its instructions, its helpers and its code in its own `tests/` folder. Thus you can check each change before and after it runs.

`agents/system/tests/agents/` contains the tests of the instructions and helpers of the system. Each test is a `[test-id].test.md` file with a scenario and the expected behaviour. `agents/system/tests/scripts/` contains the tests of the code of the system. Each test is a `[test-id].test.[js|py]` file.

Each of the two folders has these files:

- `tests.config.json`: the list of its tests. In this list, the owner can set each test to on or off. The owner can also see the time of the last run, the result and the next action.
- `run-tests.system.link.js`: a link to the shared run-tests script. The script runs the tests of the folder. It writes the results into the list and into the logs of the level.

Each other level has the same two folders.

An agent can also have its own method to test on old data, where this is useful. For example, it can use one month of old data as if it is live data. We propose that each test has its own schedule: by hand, when the tested file changes, at an interval, or before an agent goes live. We also propose that a test of instructions runs the AI of the agent in test mode on prepared data, with no keys. Nobody wrote a test yet. The two lists are empty.

Open subject: What does a failed test stop?

Its docs: `agents/system/tests/tests.index.md`

### Research

Each level keeps a record of its research: the questions, the results and the decisions that came from them.

`agents/system/research/` contains `index.json`. This file has one entry for each research item. The entry gives its question, status, results, decisions and the files that it used. The folder also has one folder for each item, `[research-id]-[slug]/`. This folder has a README and all the output of the item.

The self-improvement helper of the system is the main writer. The owner, the other helpers and each agent can also start research when they need it. The list of the system is empty now. Three studies are complete: one about prediction-market strategies, one about agents that improve themselves and one about the structure of trading agents. They are in `agents/trading/researches/`.

Each level reads the research of its children through `research/subagents.link/`. A self-improvement helper reads the old items before it starts a new item. Thus it does not do the same work two times. The exact fields of the list are our proposal.

Its docs: `agents/system/research/research.index.md`

### Self-improvement helpers

A self-improvement helper is the helper at each level that makes better versions of the items of that level. The helper of the system is `agents/system/.claude/agents/sys-self-improvement-agent.md`. It improves the system: its shared scripts, its settings, its selection of AI models and its documents. When a new AI model or tool comes, it starts test versions to try it. The helper of a domain compares the agents of the domain and proposes new agents. The helper above a group of agents makes new versions of these agents.

A helper reads the results, logs and decisions of its items through the child links of its level. It also reads research, outside news and the comments of the owner. It writes a short report about each new version. When the owner approves the report, the script that makes agents makes the version.

The version is a new agent in test mode. A version can change all items: settings, instructions, code or the AI model. The helper also records its research in `research/`. It adds tests for each change.

Self-improvement helpers keep a memory between runs in the `.claude/agent-memory/` of their level. All of them use shared templates. Thus they improve agents in a similar way that has good tests. The helper of the system is a job in the jobs file of the system.

This job is off. Self-improvement never does live actions. It never uses the live keys.

Open subject: Can a helper remove a version that loses, or can it only propose this?

Its docs: `agents/system/.claude/agents/sys-self-improvement-agent.index.md`

### Each agent's AI setup

Each level has its own Claude Code folder, `.claude/`. A session that starts in the folder of a level reads only the instructions, settings, skills and helpers of that level.

Each `.claude/` contains the same parts:

- `settings.json`: the permissions, hooks, environment and model. It goes into the repository.
- `settings.local.json`: the changes of one person. Git ignores it.
- `rules/`: instructions, one topic in each file.
- `skills/`: one folder for each skill.
- `commands/`: short prompts that start by name.
- `workflows/`: scripts that become commands.
- `output-styles/`.
- `agents/`: the helpers of the level.
- `agent-memory/`: the memory that the helpers keep and share through the repository.
- `agent-memory-local/`: memory on one computer only. Git ignores it.

The instructions of the system are one level up, in `agents/system/CLAUDE.md`. In the `.claude/` of the system, `agents/` contains the three helpers. `skills/` contains eleven skills: `knowledge-intake`, `file-index`, `vision-doc`, `readme-doc`, `readme-asd-doc`, `rebuild-prompt-doc`, `claude-md-doc`, `change-plan`, `make-questions`, `ide-build` and `ide-sync`. `readme-asd-doc` writes the ASD-STE100 version of each README.

`claude-md-doc` keeps `CLAUDE.md` correct. The other folders contain only general placeholders. The two settings files are empty. Edit the helpers and skills where they are.

No level links the `.claude/` of another level. No agent keeps documents in its `.claude/`. Its documents are in its own `docs/`. We propose that the instructions of each agent use one common base, the common prompt. We also propose a hook in the `settings.json` of each level. The hook runs relink when the session edits its links file.

Open subjects: How does the common base get to the instructions of each level? Where do other levels keep their `CLAUDE.md`? What does a version on Cursor use instead of `.claude/`? Which skills do all agents share?

Its docs: `agents/system/.claude/.claude.index.md`

### The knowledge base and the docs

The owner plans the project through many short messages. In such a project, answers become lost, documents do not agree, and closed questions open again. Thus one helper, the knowledge base agent, keeps all knowledge and writes the documents.

The knowledge base agent is `agents/system/.claude/agents/knowledge-base-agent.md`. It uses these skills:

- `knowledge-intake`: keeps and sorts an input;
- `file-index`: writes the notes of each file;
- `vision-doc`, `readme-doc` and `rebuild-prompt-doc`: one skill for each document;
- `readme-asd-doc` and `claude-md-doc`: planned.

The agent gets these inputs:

- each message from the owner, in the project chat or on the File Tree page;
- each answer to a question of the owner, because an answer is also knowledge;
- each change to the files of the system;
- each new fact from a session.

The agent gives these outputs:

- the input, kept word for word;
- updated notes;
- each related document, written again;
- updated notes for each changed file;
- a short report to the owner.

The report tells what changed and which questions only the owner can answer. The agent runs in the session that got the input. Its nightly job is off now.

Each change request starts with a plan. Each AI uses the `change-plan` skill. The skill writes one plan for each request. The name of the plan has its date, time and subject. An index lists each plan and its status.

The owner sees the plan before somebody builds the change. After the build, each part of the knowledge in the plan goes to the file that owns it. Then the documents are made correct, and the plan goes to the archive. Questions and small repairs need no plan.

The documents have two types of readers. The owner reads them to understand and control the project. An AI reads them before it changes an item. Thus they must be exact enough for action. For each file, an AI can get the full context.

The context has the How it works file and the Details file of the file, and the How it works file of each folder above it. It also has the related files, agents, skills and documents. When a file changes, these relations tell what else must change. All of these changes occur in the same round. Each question of the owner gets its answer in the location where the owner can find it.

The documents have levels:

- the project: `docs/`;
- the system domain: `agents/system/docs/`;
- trading: `agents/trading/docs/`;
- the apps: `apps/docs/`;
- each app: the `docs/` of that app.

Each level has four documents:

1. `vision.md`: read it first.
2. `README.md`: each part, exactly.
3. `README.asd.md`: the same README in ASD-STE100. The owner uses it to compare with the source.
4. `rebuild-prompt.md`: the exact specification that an AI coding agent uses to build the folder of that level again.

In one level, write the documents in this sequence in each round. Across levels, write the lowest changed level first. Then write each level above it. `agents/system/docs/` contains the four documents of the system, `how-to/` and `subagents.link/`.

`how-to/` contains the earlier runbooks for usual tasks: make an agent, add a worker, a link, a key or a test, and process an input. They stay until we write each one again for the current system.

`subagents.link/` has one link for each domain, to the documents of that domain. The page build makes `docs/file-tree.md` in each round. This file is a plain list of all paths in the repository.

Notes and documents are separate. The documents are for persons and for AI. They are plain. A person who is not technical can read them.

They contain no reference numbers, codes or history. The notes are for agents. The notes of each item are its metadata files, next to it. The records are in `apps/project-IDE/data/`:

- `inputs/`: each input of the owner, word for word;
- `decisions.md`: the decisions and their reasons;
- `changelog.md`: the changes;
- `plans/`: the plans.

There is no memory folder. The lasting rules are in `agents/system/CLAUDE.md`.

Open subject: Does a person write the lists of agents and workers, or does a script make them?

Its docs: `agents/system/.claude/agents/knowledge-base-agent.md` and `apps/project-IDE/data/README.md`

### The project IDE

The project IDE is the window of the owner on the project. The owner builds the Agent OS by vibecoding. The owner tells what they want in plain words. Then AI writes the plans, the documents and later the code. Thus it quickly becomes difficult to see what exists and why.

The File Tree page is a map of all folders and files that you can click. It shows the notes that explain each item. On this page the owner understands, monitors, controls and analyses the project. The same map gives each AI the context that it needs for exact changes. To finish it is the first task of the current stage.

The app is in `apps/project-IDE/`, and it has its own documents. The system domain contains the items that look after it. The project IDE agent is `agents/system/.claude/agents/project-ide-agent.md`. It has two skills:

- `ide-build`: makes the data of the page from the repository. It writes the plain file tree. It checks the page at the width of a desktop and of a phone. It publishes the page at the same link. Its scripts are in `agents/system/.claude/skills/ide-build/scripts/`: `materialize.py`, `enrich.py`, `tabs.py`, `build_map.py`, `index_files.py`, `check_tree.py` and `check_page.js`.
- `ide-sync`: brings back the changes from the page. It gets all items that the owner left on the page. It writes each edit into its file, word for word. It gives each message to the knowledge base agent. It runs the requests. Then it builds the page again.

The source of the page is in `apps/project-IDE/current-ui/`. The code of the server is in `apps/project-IDE/server/`. Edit each item where it is.

The page shows the tree exactly as the files on the disk. A switch shows or hides the notes of each file. Each item has tabs: File, How it works and Details. On the File tab, the owner can read, edit and comment. An Example tab, a Questions tab or an ASD-STE100 tab shows only when its file exists.

A request box under the tabs sends a question or a change to AI. On the server of the owner, the box also has a voice button. The owner can delete each item except the top, with a note for the AI. The Apply changes button moves all changes from the page into the files.

The project IDE agent runs at these times:

- when the owner asks for a sync or pushes Apply changes;
- after each round that changed the tree or a document;
- when a request from the page asks for work.

Open subject: How does the server of the owner update the published page on claude.ai?

Its docs: `apps/project-IDE/docs/README.md`

### The server

The plan is that the full system runs on one server of the owner for now. It is easy to move the system to a larger computer when it needs more power. The scheduler and each job on the server run there. The sessions of each agent run in its own folder. The key files are on that computer. They are never in git.

The repository is on GitHub. The owner works on it from two locations: Claude in the cloud project and Claude Code on their server. Both use the same repository. A change from the cloud gets to the main line as a pull request. The pull request merges only when the owner tells it to.

The File Tree page also runs on the server of the owner. Claude Code operates behind its request box. Each request on the page runs as a Claude Code session that starts in `agents/system/`. Thus the session reads the instructions, helpers and skills of the system.

You start the page from the top of the repository with `python3 apps/project-IDE/server/server.py`. The service listens only on its own computer. The owner gets to it through a private tunnel, never through the open internet.

The page cannot open the keys folder. Some actions wait for the owner to push Allow or Refuse on the page:

- push;
- delete an item that the owner did not delete;
- install;
- network tools;
- an action outside the repository.

These settings are our defaults. The owner can change them.

Open subjects: Which computer runs the scheduler? Who merges the changes from the two locations of the owner?

Its docs: `apps/project-IDE/docs/README.md`

## Where each part's docs are

| Part | Its docs | What they add |
|---|---|---|
| Agents and their levels | `agents/agents.index.md` | How the system, the domains and their levels fit together |
| The system agent and the shared files | `agents/system/system.index.md` | Each item of the system folder |
| Domains | `agents/trading/docs/README.md` | What the trading domains share, and how to make a new one |
| Workers and data | `agents/system/scripts/workers/workers.index.md`, `agents/system/data/data.index.md` | The shared workers and the shared data |
| Jobs and the scheduler | `agents/system/configs/system.workers.index.md`, `agents/system/scripts/system/system.index.md` | The jobs file, and the shared scripts that operate the system |
| Links between agents | `agents/system/configs/system.links.index.md` | The links file |
| Settings and AI models | `agents/system/configs/configs.index.md` | The global settings and the models file |
| Actions: test and live | `agents/system/configs/system.config.index.md` | The settings for test and live, the live list and the stop switch |
| Keys and secrets | `.secrets/.secrets.index.md` | The keys folder and its files |
| Logs | `agents/system/logs/logs.index.md` | The shared logs for each source |
| Tests | `agents/system/tests/tests.index.md` | The structure of the tests of each level |
| Research | `agents/system/research/research.index.md` | The research list of the system |
| Self-improvement helpers | `agents/system/.claude/agents/sys-self-improvement-agent.index.md` | The self-improvement helper of the system |
| Each agent's AI setup | `agents/system/.claude/.claude.index.md` | The parts of an AI folder |
| The knowledge base and the docs | `agents/system/.claude/agents/knowledge-base-agent.md`, `apps/project-IDE/data/README.md` | How the system keeps the knowledge and writes the documents |
| The project IDE | `apps/project-IDE/docs/README.md` | The File Tree page, and how the system builds, checks and publishes it |
| The server | `apps/project-IDE/docs/README.md` | The needs of the server, how to start it and get to it, and its settings |

## Still open in the design

These design subjects are not decided. The list shows them by part. The vision contains the questions about the goals and the business. The documents of each domain contain the open subjects of that domain.

**Agents and their levels**
- Does a small change make a new version of an agent? Examples are a new link, a changed job or a new model for one job.
- Can an agent change its own settings and documents? Or can only its self-improvement helper and its domain agent do this?

**The system agent and the shared files**
- Must the owner approve a change to the shared settings before the change gets to live agents?
- Must a file move automatically to the shared folders when a second agent needs it?

**Workers and data**
- How does an agent find the new data since its last run: with file times, or with a bookmark for each agent?
- Where are the workers helper and the helper that sets the limit of runs at the same time? What are their names?

**Jobs and the scheduler**
- Which computer runs the scheduler: the computer of the owner or a server that always operates?
- Does the scheduler make cloud jobs automatically, or does the owner approve each one?
- The global settings and the main run of an agent can both name important files. Which list has priority?
- The scheduler reads only jobs files. How do tests with their own schedules get to the scheduler?

**Links between agents**
- Does the repository keep the links, or does relink make them again after each download?
- Can an agent link each file of another agent, or only the files that the other agent lists as its output?

**Settings and AI models**
- What is the exact structure of the settings files? Which settings are shared?
- What are the exact default models: the thinking effort, the model for helpers, the other models?

**Keys and secrets**
- What keeps the list of keys the same as the key files?

**Logs**
- What is the exact log format? How long does the system keep logs?

**Tests**
- Does a failed test stop the runs of an agent, or only its move to live actions?

**Each agent's AI setup**
- Do the instructions of each level get the common base through a link, or as a copy when the system makes the agent?
- Do other levels keep their `CLAUDE.md` at the top of their folder, as the system does, or in `.claude/`?
- What does a version on Cursor use instead of `.claude/`?
- Which skills do all agents share? Can an agent get a shared skill as a link?

**The knowledge base and the docs**
- Does a person write the lists of agents, workers and other items? Or does a script make them from one list that the screens of the owner also read?

**The project IDE**
- How does the server of the owner update the published page on claude.ai?

**The server**
- Who merges the changes from the two locations of the owner?
