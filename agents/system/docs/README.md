# The system domain

## In short

The Agent OS is the owner's personal system for running AI agents of any kind: agents that trade, that work on social media or that help with management. It runs many small agents side by side, each with one clear job, tries every idea safely first and keeps what works. The system domain is the top of it: the system agent, which oversees every domain, the health of the whole system and its development, and everything every agent shares, from the standard agent folder and the scheduler to the links, the settings, the safety rules, the keys and the helpers that keep the knowledge and the owner's window on the project. The project is in its first stage: the design is complete and laid out as real files, and nothing of the system runs yet.

This document is the full, exact description of every main part of the system domain and how the parts fit together, with the path to each part's own docs. It describes the parts from the outside and never the logic inside an agent. It describes only what holds for every agent; what one area of work adds, such as money and orders for trading, is in that area's own docs. Why the system exists, how it should behave and its business logic are in the vision, `agents/system/docs/vision.md`.

## The system at a glance

The whole Agent OS is one repository of plain folders and files. Every agent is one folder laid out the same way, holding its own files and links to files elsewhere. The system domain lives in `agents/system/`: its own agent, the shared files every agent uses, and the helpers that look after the project. A few shared parts outside that folder, such as the keys folder and the File Tree page, serve every agent alike.

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

| Part | What it is for | Where it lives |
|---|---|---|
| Agents and their levels | every agent, from the system down to the levels a domain defines, in one standard folder | `agents/` |
| The system agent and the shared files | looks after the whole system and holds what every agent shares | `agents/system/` |
| Domains | one area of work each, owned by a domain agent | `agents/trading/` and the domains inside it |
| Workers and data | collect information and keep it as plain files | `agents/system/scripts/workers/`, `agents/system/data/` |
| Jobs and the scheduler | everything an agent runs, in one list per agent, started by one scheduler | each agent's `configs/`, `agents/system/scripts/system/` |
| Links between agents | give each agent the files it needs from elsewhere, without copies | each agent's `configs/` and content folders |
| Settings and AI models | what can be controlled, and which AI model each part uses | `agents/system/configs/` |
| Actions: test and live | every outside action in a test or live mode, behind one gate | the scripts that act, `agents/system/configs/system.config.json` |
| Keys and secrets | the keys to accounts and services, kept apart from everything else | `.secrets/` |
| Logs | the record of what happened | `agents/system/logs/`, each agent's `logs/` |
| Tests | checks of every level's instructions, helpers and code | `agents/system/tests/`, each level's `tests/` |
| Research | what each level studied and what it led to | `agents/system/research/`, each level's `research/` |
| Self-improvement helpers | prepare better versions at every level | each level's `.claude/agents/` |
| Each agent's AI setup | each level's own instructions, settings, skills and helpers | each level's `.claude/` |
| The knowledge base and the docs | keep everything we know and turn it into docs | `agents/system/docs/`, the planning area `vision/` |
| The project IDE | the owner's window on the project: the File Tree page | `apps/project-IDE/`, looked after from `agents/system/.claude/` |
| The server | the machine everything runs on, and the page's service there | one of the owner's servers |

What passes between the parts, from information coming in to actions, results and improvements:

1. **Jobs start everything.** The scheduler reads every agent's jobs file and starts each job at its time: a worker, an agent's own run or one of its helpers.
2. **Workers bring information in.** A worker fetches from its source and writes a file: a shared worker into `agents/system/data/workers/[worker]/`, a domain's or an agent's own worker into that level's `data/`. AI helpers that prepare information read those files and write their result as a file too.
3. **Links hand each agent its files.** Each agent lists the files it needs from elsewhere in its links file, and one shared script, relink, turns the list into links in the agent's own folders. The agent reads through them and never gets a copy. A change to a file the agent marks as important starts a fresh run; other changes wait for its next run.
4. **Agents act through scripts.** An action in the outside world goes through a script, in the mode the agent's settings set, test or live, after the gate checks the mode, the limits and the stop switch. A script that needs a key gets it at run time through one shared loader, and only the keys its settings name.
5. **Results stay with the agent.** Every agent writes its own logs and data in its own folder, and each level reads its children's folders through child links: the system sees every domain, a domain the first level below it, and so on down.
6. **Self-improvement closes the loop.** The self-improvement helper of a level reads what that level owns, with research, outside news and the owner's comments, and writes a short report on a new version. Once the owner approves it, the version is created as a new agent in test mode.
7. **The owner's words become files.** Everything the owner leaves in the project chat or on the File Tree page reaches the knowledge base agent, which keeps it word for word and brings the notes and the docs in line; edits made on the page are written into their files.

## How the project is laid out

With hundreds of agents, a person or a tool must be able to find anything without asking. So the project is one tree, every level of it is laid out the same way, and the repository on disk is exactly the tree the File Tree page shows. The top of the repository:

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
└── vision/                 the planning area: inputs, decisions, notes, plans, build tools, page source
```

The system domain's own folder, `agents/system/`:

```text
agents/system/
├── CLAUDE.md          read first by Claude Code started here: the project, its stage, the rules, the round
├── .claude/           the system's AI setup: settings, helpers, skills
├── configs/           system.config.json, models.config.json, system.workers.json, system.links.json
├── scripts/           system/ (the machinery), workers/ (shared collectors)
├── logs/              system/, services/, workers/, subagents/
├── data/              system/, workers/, subagents/
├── docs/              vision.md, README.md, README.asd.md, rebuild-prompt.md
├── tests/             agents/, scripts/
├── research/          index.json and one folder per item
├── package.json       the JavaScript packages the shared scripts use
├── requirements.txt   the Python packages the shared scripts use
├── init.sh            sets up the project: git hooks, then relink everywhere
└── start.sh           starts the scheduler and the system's own session
```

Every agent's folder, at every level, has the same parts:

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

Each content folder (`configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/`) holds the agent's own real files, links to the files it uses from elsewhere and, at a level with children, one link per child. Because every agent looks the same, the shared tools find things in the same places at every level.

Code follows one rule everywhere: every code file holds one runnable thing, such as one function, one endpoint, one script or one worker, with one purpose. It may take parameters, but it never mixes several jobs. Related things are grouped in a folder, one per file.

Next to every file and folder sit its notes. Its How it works file explains it in plain words: `vision.index.md` next to `vision.md`, the file's name without its extension, and `configs/configs.index.md` inside a folder. Its Details file, `vision.meta.json`, holds its facts and relations: what kind of thing it is, whether it is in git, who writes and reads it, what changes with it and where its knowledge comes from. Some files also have an Example file, `x.example.md`, with the structure of the file, and a Questions file, `x.questions.md`, with what is still open about it; these exist only where they are written. Every planned file and folder already exists on disk: a file with a draft carries its text, the rest are empty, and a placeholder such as `[domain-name]/` is a real folder holding only its notes.

### How a level reaches its children

If any agent could reach into any other, a change in one place could break agents nobody thought of, and no agent could be understood on its own. So parents see their children, never the other way round: the system looks into each domain, each domain into the first level below it, and so on down; lower levels never reach up.

A parent does this through child links. Each content folder of a level with children holds a folder `subagents.link/` with one folder link per direct child, named after the child and pointing at the child's folder of the same kind:

```text
agents/system/docs/subagents.link/[domain-name]/      → that domain's docs/
agents/system/configs/subagents.link/[domain-name]/   → that domain's configs/
```

The same holds for `scripts/`, `logs/`, `data/`, `tests/` and `research/`. A domain that sits inside a folder of domains, such as a trading domain inside `agents/trading/`, is still a direct child of the system: the system's links point straight at its folders. Child links are only read through, never copied, and they are the only folder links in the system. Relink makes them from the folder tree and removes them when a child is gone, and tools that scan folders never follow them. Today each `subagents.link/` holds only its placeholder `[domain-name]/`, because no domain has its folders built yet. No `.claude/` folder is linked at any level.

## The parts

Each part below says what it is, what it holds, what it takes from the other parts and gives them, when and where it runs, and its status. What is stated plainly is decided; our proposals say "the plan is" or "we propose"; the details still open are named in each part and listed at the end. Nothing runs yet: the files named here exist, most of them still empty, and the scripts are not written.

### Agents and their levels

An agent is one folder with its own AI instructions, responsible for one piece of the Agent OS. Agents sit in levels, and every agent has a parent above it; only the system agent has none. The system agent looks after the whole Agent OS. A domain agent owns one area of work. Below it, each domain arranges its agents in the levels its work needs. Any agent can have versions that differ in settings, instructions, code or AI model; they run side by side and compete, and the better ones are kept. An agent can be plain code, AI or a mix.

All agents live under `agents/`: the system in `agents/system/`, and the domains, either directly under `agents/` or inside a folder that groups domains of one kind, such as `agents/trading/`. A domain's folder is its domain agent's folder, and the agents of the levels it defines are sub-folders of it. Every agent has the standard folder.

With hundreds of agents, a name must say at a glance what an agent is, and two agents must never be mixed up. So every agent has one name, unique across the whole system and used for its folder, settings, logs, data, docs and place on the owner's screens. A name is never changed or reused, even after the agent is deleted. Where a domain puts the agent's mode and AI model in its names, the mode, test or live, is always the last part. We propose that every name starts with its domain's code, `sys` for the system, that the system agent's name is `sys-system-agent`, and that a list of every agent ever created is kept for the script that creates agents to check against.

An improvement never changes a running agent: it always becomes a new agent in test mode. We propose that the new agent records the agent it came from and says exactly what differs in its `docs/changes.md`.

Every level also has helpers: AI assistants with their own instructions and tools, built as Claude Code sub-agents, one file each in the level's `.claude/agents/`. A helper runs in its own level's session and writes its results as files, which agents read through links.

New agents are made by one shared script, create-agent, in `agents/system/scripts/system/`, which checks the name, sets up the standard folder and runs the new agent's `init.sh`. The owner can ask for one in plain words, and the system builds it and fits it in. The plan is that each level runs in its own folder, so a session sees only its own setup, links and children.

Still open: whether a small change makes a new version, and whether an agent may edit its own settings.

Its docs: `agents/agents.index.md`

### The system agent and the shared files

The system agent is the system manager. It oversees every domain, the health and costs of the whole system and its development, plans each new domain before it is built, and answers the owner's questions about the whole system. It lives in `agents/system/`, with the same standard folder as every agent, and differs in two ways only: it is the root of the family tree, and its folders also hold the files every agent shares.

Its instructions are `agents/system/CLAUDE.md`. Claude Code loads this file by itself when it starts in `agents/system/`, which is how the owner starts it on their server. It tells every AI working on the project what the project is and which stage it is in, what to read first and in which order, where things are, the rules every AI follows, what to do after every input or update, which doc each kind of change makes stale and which skill writes it, how the File Tree page works, and the system manager's job. The system manager's part of it is our proposal until the owner confirms it.

The shared files follow one rule: a file used by agents of different domains lives in the system domain, a file only one domain needs lives in that domain, and a file only one agent needs lives in that agent's own folder. `agents/system/` holds the shared settings in `configs/`, the shared scripts in `scripts/`, the shared logs in `logs/` and the shared data in `data/`, next to its own `docs/`, `tests/` and `research/`; its `package.json` and `requirements.txt` list what the shared scripts use. We propose that when a second agent needs a file that so far belonged to one agent, the file moves into the matching shared folder and both agents link it.

The system takes the owner's questions about the whole and everything its children write, read through `subagents.link/` in each content folder. It gives every agent the shared settings, scripts and data, always as links to the one real file. The plan is that the system's `init.sh` installs the repository's git hooks and runs relink for the whole project, and that its `start.sh` starts the scheduler and the system's own session. Both are empty for now.

Still open: whether a change to the shared settings needs the owner's approval before it reaches live agents.

Its docs: `agents/system/system.index.md`

### Domains

A domain is one area of work, and its folder is its domain agent's folder. The domain agent finds, creates and updates the agents of its area, makes sure they reach the domain's goal, and answers the owner's questions about it. Each domain says what its goal is, which levels its agents sit in, where its agents may act and where they only collect information, and what it adds to the shared rules, such as trading's limits on money.

Like every level, a domain has the standard folder, with its own instructions, its own self-improvement helper, its jobs and links files, its own workers, its research, and its own docs: a vision, a README with its twin in Simplified Technical English, and a rebuild prompt, each telling only the domain's story. A domain keeps everything only it needs, such as its own settings, notes and scripts. A new domain starts as a copy of the one most like it, with the same levels, rules and docs, and changes only what is different.

A domain takes its share of the shared settings, scripts and data through links, and reads the next level down through its child links. The system reaches every domain through its own child links.

Domains of one kind are grouped in one folder. `agents/trading/` holds the trading domains: its `docs/` holds trading's own vision, README, README twin and rebuild prompt, what every trading domain shares and how a new one is made, and its `researches/` holds the trading studies already done. It has no agent, settings or scripts of its own. Its first domain is the prediction-market domain, `agents/trading/prediction-market/`, with Polymarket first. That domain is the project's second stage: today only its folders exist, and nothing in it is written. The next trading domain, copy trading, is copied from it when the owner asks. Agents of other kinds, such as social media or management, come later as domains of their own.

Its docs: `agents/trading/docs/README.md`

### Workers and data

Workers are plain scripts that collect information on a schedule, such as prices, news, important events and errors, and save what they find as files. A script's name says its kind: `.worker.` for a worker and `.system.` for the machinery, such as setup, scheduling, links and tests. These two kinds hold for every agent, and a domain may add kinds of its own.

A worker that agents in several domains use is shared: it lives in `agents/system/scripts/workers/`, writes to `agents/system/data/workers/[worker]/` and logs to `agents/system/logs/workers/[worker]/`, and its job is in the system's jobs file. A worker only one domain needs lives in that domain, and one only one agent needs lives in that agent's `scripts/` and writes into its `data/`, one folder per producer. No shared worker exists yet.

One helper, the workers helper, is planned to know every worker and what it collects. An agent that needs new information asks it, and it points the agent to data that already exists, extends a running worker or creates a new one, then tells the agent where the data is and how and when to use it. So hundreds of agents never build the same worker twice.

AI helpers prepare raw information for the agents. A system helper writes its result into `agents/system/data/subagents/[subagent]/`; a lower level's helper writes into its own level's `data/`; agents link these results like any other data.

All information is kept in plain files a person can open, with no database for now: lists and records in JSON, logs that grow with one entry per line, text in Markdown. Shared scripts let agents add, read, change, remove and filter list entries safely. We propose that every producer keeps a stable `latest` file next to its dated files, so links to it keep working while new files arrive. The system's own records, such as the list of every link and the scheduler's record of every job, sit in `agents/system/data/system/`. The contents of every `data/` folder are runtime output, not source.

Still open: how an agent tells what is new since its last run, and the workers helper's name and file.

Its docs: `agents/system/scripts/workers/workers.index.md` and `agents/system/data/data.index.md`

### Jobs and the scheduler

With hundreds of agents each running scripts and AI sessions on its own timer, nobody could see what runs when, and switching something off would mean hunting through code. So every agent has one jobs file listing everything it runs, and one scheduler runs every job.

The jobs file sits in the agent's `configs/`, named after the agent: `agents/system/configs/system.workers.json` for the system, `[name].workers.json` for every other agent. A job is a plain script or an AI run: the agent's main run, one of its helpers, a skill, a workflow or a command. For each job the file says what it does, whether it is switched on, how often it runs (every few minutes, at a time of day, once on a date, after another job, or only by hand), where it runs (on the server, in the cloud or in a desktop app) and which AI platform and model it uses. The owner and the agent can see, change and switch off any job there, and a parent sees its children's jobs files through `configs/subagents.link/`. The exact fields of a job are our proposal.

The system's own jobs are relinking when a links file changes, checking every link, a news digest for the domains, the system's self-improvement, the knowledge base agent's nightly catch-up and a weekly review of the shared scripts. Every system job is switched off for now: they stay in the file and run only once the owner turns them on.

One scheduler, a shared script in `agents/system/scripts/system/`, finds every jobs file and runs each job at its time. The plan is that the system's `start.sh` starts it and the operating system keeps it running, while each agent's own `start.sh` only does one run. A jobs file says only what should run; what happened is kept apart, in the scheduler's record in `agents/system/data/system/`, its log in `agents/system/logs/system/` and each agent's own `logs/`, so a jobs file changes only when someone changes a job.

The scheduler also handles the moments between intervals. When an important file of an agent changes, the run in progress stops and a new one starts with the fresh information; unimportant changes wait for the next run. When something an agent waits for is ready, such as research it started, the agent runs again with it. A system helper checks what the server can take and sets how many agents run in parallel. We propose that jobs in the cloud, in a desktop app or on GitHub get no keys and never act live, and that a job is paused by switching it off, never by deleting it.

Still open: which machine runs the scheduler, whether it registers cloud jobs on its own, which list of important files wins, how tests with their own schedules reach it, and the parallel limit in detail.

Its docs: `agents/system/configs/system.workers.index.md` and `agents/system/scripts/system/system.index.md`

### Links between agents

Links give each agent the files it needs from elsewhere without copying them. If every agent kept its own copy of a shared file, hundreds of copies would drift apart, and a fix to one would never reach the others. So an agent gets shared files as links that look like files in its folder but point to the one real file. Every link has "link" in its name, such as `system.config.link.json` or `subagents.link/`, so it can be told from a real file at a glance.

There are two kinds. A file link points to one file the agent's logic needs, from anywhere under `agents/`: the system, its own domain or parent, another domain or any agent by its name. It sits in the agent's content folder, and the agent only reads through it. A child link is a folder link from a parent to one child's folder, described above.

Each agent lists its file links in one small file in its `configs/`, its links file: `agents/system/configs/system.links.json` for the system, `[name].links.json` for every other agent. For each link it says which file, from where, where the link appears and why. The list is set when the agent is created and changed later by the agent, its self-improvement helper or the owner. The system's own list is short: the two links that let its test folders run the shared test runner.

One shared script, relink, in `agents/system/scripts/system/`, reads every links file, creates the file links and the child links, removes links nobody lists and checks that none is broken. Every level below the system has `scripts/relink.system.link.js`, a link to it that relinks that agent only. Relink runs when a links file changes, when changes are reviewed (before they are saved to the repository and after new changes are downloaded) and when an agent edits its own links file. We propose that git hooks installed by the system's `init.sh` and a hook in each agent's AI settings start it, that relink writes a list of every link to `agents/system/data/system/`, so anyone can see who reads which file, and that a second shared script, check-links, checks every link after each change. Nothing is ever linked into the keys folder or into any `.claude/` folder.

Links are also how agents listen to each other. An agent that finds another's output useful subscribes by linking it; new data reaches it on its next run or, if the agent marks the file as important, interrupts the run in progress.

Still open: whether the links themselves are saved in the repository, and whether an agent may link any file of another agent or only the files it lists as its outputs.

Its docs: `agents/system/configs/system.links.index.md`

### Settings and AI models

Settings come in a few plain JSON files, all in `agents/system/configs/`.

`system.config.json` is the one global settings file, with everything that can be controlled for the whole system except jobs and models. The plan is for it to have sections for defaults, the modes (test by default, the general stop switch and the list of agents allowed to act live), schedule defaults (including how many runs may go at once and a daily cap on AI cost), the rules for restarting runs when an important file changes, and notifications. A section that grows long moves into a file of its own. Settings only one domain needs, such as money and accounts, are never here.

`models.config.json` is the models file: which AI platform and model each agent, helper and AI worker uses, and which platforms can be used. A job may name its own model; otherwise the models file decides.

| Kind of work | Model |
|---|---|
| Thinking, planning, analysis and improvement, and the agents that act | Claude Opus 5.5 at high thinking effort |
| Unimportant tasks | a medium model at medium effort, Claude Sonnet 5.5 |
| Light, high-volume work such as collecting and filtering data | Cursor with its Composer 2.5 model |
| Unimportant work, once connected | free models through OpenRouter, in rotation |
| Later | Codex and Kimi |

Claude Code is the default platform. Every part that uses AI has a configured route to a platform and a model. Where a domain puts the model in an agent's name, we propose that the script that creates agents checks the two agree.

Every agent below the system has its own settings file, `[name].config.json`, next to its jobs and links files, and reads the global settings and the models file through links. A domain may keep its own settings file for what only its area needs. We propose that settings combine in a fixed order, from the global settings through the domain's and the agent's own to the owner's choices such as stopping or approving, except that a lower level may only tighten a limit, never loosen it; that settings are read at the start of each run, so a change applies from every agent's next run; and that changes to the modes need the owner's approval.

All four configuration files of the system exist and are empty; their exact fields are our proposal.

Still open: the files' exact shape, which settings are shared and which belong to each agent (to be settled with two or three example agents), and the model defaults in detail.

Its docs: `agents/system/configs/configs.index.md`

### Actions: test and live

An action is anything an agent does in the outside world, such as buying, selling or posting, and every action works in a test mode and a live mode from the start, chosen in the agent's settings. Every new agent and every change runs in test mode first, where nothing real happens and mistakes cost nothing. Where an agent's name carries its mode, a test agent and a live agent are always two different agents.

Each domain says where its agents may act and where they only collect information. The system domain itself has no script that acts: each domain writes its own, and every one of them passes the same gate.

A script that acts reads the mode from the agent's settings before it acts, and in test mode never acts for real. The service that acts logs every action, test or live: a shared service in `agents/system/logs/services/[service]/`, a domain's own services in that domain's `logs/`.

An agent acts live only after it has shown good results, and only when the owner approves it, one agent at a time. No agent can approve going live, for itself or another, and self-improvement never acts live. We propose that an action is live only when the agent is on the list of agents allowed to act live, the run is approved by the owner, the agent asks for live mode in its own settings and the stop switch is off; and that an agent can never switch itself to live.

Outside text, such as news and social posts, can carry hidden instructions meant to trick an AI, so an agent treats outside text as data, never as instructions, and protection against it is built together with acting live. We propose hard limits on every outside action, written in code in the scripts that act and checked before every action, which a domain or an agent may only make stricter, and one general stop switch in the global settings that halts every outside action at once, which only the owner turns on or off.

Its docs: `vision/docs/safety.md`

### Keys and secrets

Keys to accounts and services are the most dangerous thing in the system: a key in a log, a shared file or an AI conversation can leak, and an AI that reads a live key could misuse it. So every key lives in one folder, `.secrets/`, at the top of the repository, outside every agent's folder.

It holds:

- `.secrets/test/.env`: all test keys in one file, in comment sections, with names that start with their account or platform. Agents may read and update it.
- `.secrets/live/.env`: the same key names with real values, for the owner only, set up when acting live begins.
- `.secrets/test/.env.example` and `.secrets/live/.env.example`: the key names with a one-line comment each and no values.
- `.secrets/secrets.index.json`: which keys exist, what each is for and who uses it, never a value. It is meant to stay in step with the key files automatically.

The folder, its subfolders, its notes and `secrets.index.json` are in git and show on the File Tree page. The `.env` files, which hold the values, never go in git; the page lists them as local-only and never reads, shows or edits them. Key names are upper case with underscores, such as `ANTHROPIC_API_KEY` or `GROQ_API_KEY`, and `AGENT_OS_ENV` says whether a script runs in test or live.

A script gets only the keys its settings name, at the moment it runs, through one shared loader, load-secret, in `agents/system/scripts/system/`: an agent's settings or a job list the key names needed, and the loader gives just those keys to that one script's process. Keys are never linked, copied, logged or shown to an AI, and every level's `.claude/settings.json` is meant to block AI sessions from reading or editing the live keys. How the loader works in detail is our proposal.

Still open: what keeps the list of keys in step with the key files, and how live keys are kept safe once agents act for real.

Its docs: `.secrets/.secrets.index.md`

### Logs

Logs are the record of what happened: every run, decision, action, job, helper call, error and cost.

Logs that belong to no single agent are shared and sit in `agents/system/logs/`, by source: `system/` for the scheduler, restarts, relink, link checks, errors and costs; `services/[service]/` for every action of each shared service that acts; `workers/[worker]/` for the shared workers; and `subagents/[subagent]/` for the calls of helpers, including every request sent from the File Tree page on the owner's server. A domain keeps the logs of its own jobs and services in its own `logs/`. The system reaches each domain's logs through `agents/system/logs/subagents.link/`.

Each agent's own logs are real files in its own `logs/`: its runs, its decisions, the runs of its jobs and its test results. It links only the few shared logs it needs. Each level reads its children's logs through its child links, so the owner's screens can start at the system's logs and go down level by level.

Logs never hold a key's value, and the contents of every `logs/` folder are runtime output, not source; the folders themselves stay.

Still open: the exact format and how long logs are kept.

Its docs: `agents/system/logs/logs.index.md`

### Tests

Every level tests its instructions and helpers, and its code, in its own `tests/` folder, so every change can be checked before and after it runs.

`agents/system/tests/agents/` holds the tests of the system's instructions and helpers, each a `[test-id].test.md` with a scenario and the expected behaviour. `agents/system/tests/scripts/` holds the tests of its code, each a `[test-id].test.[js|py]`. Each folder has a `tests.config.json`, the list of its tests, where the owner can switch each test on or off and see when it last ran, its result and what to do next, and a `run-tests.system.link.js`, a link to the shared run-tests script, which runs that folder's tests and writes the results back into the list and into the level's logs. Every other level has the same two folders.

Where it makes sense, an agent also has its own way of being tested on past data, such as replaying a month of old data as if it were live. We propose that each test has its own schedule (by hand, when the file it checks changes, at an interval, or before an agent goes live), and that tests of instructions run the agent's AI in test mode on prepared data, with no keys. No test is written yet; both lists are empty.

Still open: what a failing test stops.

Its docs: `agents/system/tests/tests.index.md`

### Research

Every level keeps a record of its research: what was asked, what was found and what it led to.

`agents/system/research/` holds `index.json`, one entry per item with its question, status, results, the decisions it led to and the files it used, and one folder per item, `[research-id]-[slug]/`, with a README and everything the item produced. The system's self-improvement helper is the main writer; the owner, the other helpers and any agent can start a piece of research when they need one. The system's own list is empty for now. The studies already done, on prediction-market strategies, on agents that improve themselves and on how trading agents are built, sit in `agents/trading/researches/`.

Each level reads its children's research through `research/subagents.link/`. A self-improvement helper reads past items before it starts a new one, so work is not repeated. The exact fields of the list are our proposal.

Its docs: `agents/system/research/research.index.md`

### Self-improvement helpers

A self-improvement helper is the helper at each level that keeps preparing better versions of what that level owns. The system's, `agents/system/.claude/agents/sys-self-improvement-agent.md`, improves the system itself (its shared scripts, settings, choice of AI models and docs) and reacts to new AI models and tools by starting test versions to try them. A domain's compares its agents across the area and proposes new ones; the one above a group of agents prepares new versions of them.

A helper takes the results, logs and decisions of what it owns, read through its level's child links, together with research, outside news and the owner's comments. It gives a short report on each new version it prepares. Once the owner approves the report, the version is created through the script that creates agents, as a new agent in test mode. A version may change anything: settings, instructions, code or the AI model. The helper also records what it studied in `research/` and adds tests for what it changes.

Self-improvement helpers keep a memory between runs in their level's `.claude/agent-memory/`, and they are all built from shared templates, so they improve agents in a similar, well-tested way. The system's runs as a switched-off job in the system's jobs file. Self-improvement never acts live and never touches the live keys.

Still open: whether a helper may retire a losing version on its own.

Its docs: `agents/system/.claude/agents/sys-self-improvement-agent.index.md`

### Each agent's AI setup

Each level has its own Claude Code folder, `.claude/`, so a session started in a level's folder loads that level's instructions, settings, skills and helpers, and nothing else.

Every `.claude/` holds the same parts:

- `settings.json`, its permissions, hooks, environment and model, saved to the repository, and `settings.local.json`, each person's own changes, meant to stay out of it;
- `rules/`, instructions on one topic each; `skills/`, one folder per skill; `commands/`, short prompts started by name; `workflows/`, scripts that become commands; `output-styles/`;
- `agents/`, the level's helpers;
- `agent-memory/`, the memory its helpers keep and share through the repository, and `agent-memory-local/`, memory kept on one machine only.

The system's instructions sit one level up, at `agents/system/CLAUDE.md`. In the system's `.claude/` today, `agents/` holds the three helpers and `skills/` holds eight skills: `knowledge-intake`, `file-index`, `vision-doc`, `readme-doc`, `rebuild-prompt-doc`, `change-plan`, `ide-build` and `ide-sync`. Two more are planned for this stage: `readme-asd-doc`, which writes each README's twin in Simplified Technical English, and `claude-md-doc`, which keeps `CLAUDE.md`. The other folders hold only general placeholders, and both settings files are empty. While we plan, the source of the helpers and skills is the planning area, and the build copies them into place.

No level links another level's `.claude/`, and no agent keeps docs inside it: its docs are in its own `docs/`. We propose that every agent's instructions build on one common base, the common prompt, and that a hook in each level's `settings.json` reruns relink when the session edits its links file.

Still open: how the common base reaches each level's instructions, where other levels keep their `CLAUDE.md`, what a version that runs on Cursor uses instead of `.claude/`, and which skills every agent shares.

Its docs: `agents/system/.claude/.claude.index.md`

### The knowledge base and the docs

A project planned through many short messages easily loses track: answers are forgotten, documents disagree, settled questions reopen. So one helper, the knowledge base agent, keeps everything we know and turns it into the docs.

It is `agents/system/.claude/agents/knowledge-base-agent.md`, with its skills `knowledge-intake` for keeping and sorting an input, `file-index` for every file's notes, and one skill per doc: `vision-doc`, `readme-doc`, `rebuild-prompt-doc`, and the planned `readme-asd-doc` and `claude-md-doc`. It takes every message from the owner, in the project chat or on the File Tree page, every answer given to the owner's questions, because an answer is knowledge too, every change to the system's files and whatever a session learned. It gives the input kept word for word, its notes brought up to date, every doc the input touches rewritten, the notes of every changed file refreshed, and a few plain lines to the owner on what changed and what only they can answer. It runs in the session that received the input; its nightly catch-up job is switched off for now.

Every change request starts with a plan. The `change-plan` skill, which every AI follows, writes one plan per request, named by its date, time and subject, with an index of every plan and its status. The owner sees the plan before anything is built; once it is built, each piece of its knowledge moves to the file that owns it, the docs are brought in line, and the plan goes to the archive. Questions and small fixes need no plan.

The docs serve two readers at once. The owner reads them to understand and steer the project; an AI reads them before it changes anything, so they must be exact enough to act on. For any file an AI can get its whole context: the file's own notes, the knowledge that applies to it directly and from every folder above it, and the files, agents, skills and docs related to it. When a file changes, those relations say what else must follow, and each is brought in line before the round ends. Every question the owner asks gets its answer written where the owner should have found it.

The docs come in levels: the project's in `docs/`, the system domain's in `agents/system/docs/`, trading's in `agents/trading/docs/`, the apps' in `apps/docs/` and each app's in its own `docs/`. At every level there are four: `vision.md`, read first; `README.md`, every part exactly; `README.asd.md`, the same README in Simplified Technical English, kept for the owner to compare with the original; and `rebuild-prompt.md`, the exact spec an AI coding agent rebuilds that level's folder from. Inside a level they are written in that order every round; across levels the lowest level that changed comes first, then each level above it. `agents/system/docs/` holds the system's four and `subagents.link/`, one link per domain to that domain's docs. The plain list of every path in the repository, `docs/file-tree.md`, is built by the page build every round.

Notes and docs are kept apart. The docs are for people and for AI: plain, readable by someone who is not technical, with no reference numbers, codes or history. The notes are for agents. While we plan, they live in the planning area `vision/`: in `vision/docs/`, every owner input word for word in `inputs/`, the decisions with their reasons in `decisions.md`, `changelog.md`, the tree notes `file-tree.md` with one section per file and folder, the knowledge map, and the topic notes agents read while they work (overview, architecture, conventions, safety, data schemas, flows, metrics, glossary, roadmap, feature map, the runbooks in `how-to/`, the shared knowledge in `common/` and the lists in `index/`); in `vision/plans/`, the plans; in `vision/.claude/memory/`, the working notes every Claude reads. The planned home of the records is `apps/project-IDE/data/`, where the build keeps a copy.

Still open: where the topic notes live once the planning area is retired, whether the lists of agents and workers are written by hand or generated, and an automatic check of the tree notes against the real folders.

Its docs: `agents/system/.claude/agents/knowledge-base-agent.md` and `vision/docs/README.md`

### The project IDE

The project IDE is the owner's own window on the project. The owner builds the Agent OS by vibecoding: they say what they want in plain words, and AI writes the plans, the docs and later the code, so it quickly becomes hard to see what exists and why. The File Tree page is a clickable map of every folder and file with the notes that explain it, where the owner understands, watches, steers and analyses the project. The same map gives every AI working on the project the context it needs to change things precisely. Finishing it is the first task of the current stage.

The app itself lives in `apps/project-IDE/`, with its own docs. The system domain holds what looks after it: the project IDE agent, `agents/system/.claude/agents/project-ide-agent.md`, with two skills. `ide-build` builds the page's data from the repository, writes the plain file tree, checks the page at a desktop and a phone width and publishes it at the same link; its scripts are in `agents/system/.claude/skills/ide-build/scripts/`: `parse.py`, `enrich.py`, `tabs.py`, `build_map.py`, `index_files.py` and `check_page.js`. `ide-sync` is the way back: it takes everything the owner left on the page, writes each edit into its file word for word, hands every message to the knowledge base agent, runs the requests, then rebuilds the page. While we plan, the build's scripts, the page's source and the server's code live in the planning area, `vision/tools/`, `vision/explorer/` and `vision/server/`.

The page shows the tree exactly as the files on disk, with a switch that shows or hides every file's notes. Each item has tabs: File, which the owner can read, edit and comment on, How it works, Details, and an Example, Questions or Simplified Technical English tab only where that file exists. A request box under the tabs sends a question or a change to AI, with a voice button on the owner's server. Any item but the top can be deleted with a note for the AI, and an Apply changes button carries every change waiting on the page into the files.

The project IDE agent runs when the owner asks for a sync or presses Apply changes, after every round that changed the tree or a doc, and when a request from the page asks for work.

Still open: how the published page is updated from the owner's server.

Its docs: `apps/project-IDE/docs/README.md`

### The server

For now the whole system is meant to run on one of the owner's servers, built so it can move easily to a bigger machine when it needs more power. The scheduler and every job that runs on the server run there, each agent's sessions in its own folder, and the key files sit on that machine, never in git.

The repository is on GitHub, and the owner works on it from two places: Claude in the cloud project and Claude Code on their server, both through the same repository. A change from the cloud reaches the main line as a pull request that is merged only on the owner's word.

The File Tree page also runs on the owner's server, with Claude Code behind its request box: every request typed on the page runs as a Claude Code session started in `agents/system/`, so the system's instructions, helpers and skills load as its own. While we plan, it is started from the top of the repository with `python3 vision/server/server.py`. It listens only on the machine itself, and the owner reaches it through a private tunnel, never the open internet. Nothing from the page can open the keys folder, and pushing, deleting anything other than the item the owner deleted, installing, network tools and anything outside the repository wait for the owner's Allow or Refuse on the page. These settings are our defaults, which the owner can change.

Still open: which machine runs the scheduler, and who merges the changes made from the two places the owner works.

Its docs: `apps/project-IDE/docs/README.md`

## Where each part's docs are

| Part | Its docs | What they add |
|---|---|---|
| Agents and their levels | `agents/agents.index.md` | how the system, the domains and their levels fit |
| The system agent and the shared files | `agents/system/system.index.md` | the system folder item by item |
| Domains | `agents/trading/docs/README.md` | what the trading domains share and how a new one is made |
| Workers and data | `agents/system/scripts/workers/workers.index.md`, `agents/system/data/data.index.md` | the shared workers and the shared data |
| Jobs and the scheduler | `agents/system/configs/system.workers.index.md`, `agents/system/scripts/system/system.index.md` | the jobs file, and the shared scripts that run the system |
| Links between agents | `agents/system/configs/system.links.index.md` | the links file |
| Settings and AI models | `agents/system/configs/configs.index.md` | the global settings and the models file |
| Actions: test and live | `vision/docs/safety.md` | the rules for test and live, going live, hard limits and the stop switch |
| Keys and secrets | `.secrets/.secrets.index.md` | the keys folder and its files |
| Logs | `agents/system/logs/logs.index.md` | the shared logs by source |
| Tests | `agents/system/tests/tests.index.md` | how each level's tests are laid out |
| Research | `agents/system/research/research.index.md` | the system's research list |
| Self-improvement helpers | `agents/system/.claude/agents/sys-self-improvement-agent.index.md` | the system's self-improvement helper |
| Each agent's AI setup | `agents/system/.claude/.claude.index.md` | the parts of an AI folder |
| The knowledge base and the docs | `agents/system/.claude/agents/knowledge-base-agent.md`, `vision/docs/README.md` | how the knowledge is kept and the docs are written |
| The project IDE | `apps/project-IDE/docs/README.md` | the File Tree page, how it is built, checked and published |
| The server | `apps/project-IDE/docs/README.md` | what the server needs, how to start and reach it, its settings |

## Still open in the design

The design details not settled yet, by part. Questions about the goals and the business are in the vision; the open points of one domain are in that domain's docs.

**Agents and their levels**
- Does a small change, such as a new link, a changed job or a new model on one job, make a new version of an agent, or can it happen in place?
- May an agent change its own settings and docs, or only its self-improvement helper and its domain agent?

**The system agent and the shared files**
- Must the owner approve a change to the shared settings before it reaches live agents?
- Should a file move to the shared folders automatically when a second agent needs it?

**Workers and data**
- How does an agent tell what is new since its last run: by file times, or by a bookmark kept per agent?
- Where do the workers helper and the helper that sets the parallel limit sit, and what are they called?

**Jobs and the scheduler**
- Which machine runs the scheduler: the owner's computer or an always-on server?
- Does the scheduler register cloud jobs on its own, or does the owner confirm each one?
- When an agent's important files are named both in the global settings and with its main run, which list wins?
- How do tests with their own schedules reach the scheduler, which reads only jobs files?

**Links between agents**
- Are the links saved in the repository, or rebuilt by relink after every download?
- May an agent link any file of another agent, or only the files that agent lists as its outputs?

**Settings and AI models**
- What exactly do the settings files look like, and which settings are shared?
- What are the model defaults in detail: the thinking effort, the model for helpers, the further models?

**Keys and secrets**
- What keeps the list of keys in step with the key files?

**Logs**
- What is the exact log format, and how long are logs kept?

**Tests**
- Does a failing test stop an agent's runs, or only its move to acting live?

**Each agent's AI setup**
- Does each level's instructions take in the common base through a link, or as a copy made when the agent is created?
- Do the other levels keep their `CLAUDE.md` at the top of their folder, like the system, or inside `.claude/`?
- What does a version that runs on Cursor use instead of `.claude/`?
- Which skills does every agent share, and may an agent get a shared skill as a link?

**The knowledge base and the docs**
- Where do the topic notes and the records live once the planning area `vision/` is retired?
- Are the lists of agents, workers and the rest written by hand, or generated from one list the owner's screens also read?
- Should a check compare the tree notes with the real folders automatically?

**The project IDE**
- How is the published page on claude.ai updated from the owner's server?

**The server**
- Who merges the changes made from the two places the owner works?
