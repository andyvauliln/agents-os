# README.md: the trading and prediction-market parts (from `.claude/docs/README.md` before the general rewrite of 2026-10-09)

Kept word for word for the prediction-market domain's own docs later. Each block is a passage of the system README that was removed or rewritten in general terms because it was about trading or the prediction-market domain; some passages also hold general sentences that were kept, reworded, in the new README. The full earlier file is `README.before-general.md` in this folder.

## From: In short

The Agent OS is a personal system for trading with AI. It runs many small trading agents at the same time, each following one strategy, and keeps the ones that make money; small programs collect information such as prices and news, each agent is given only the information its strategy needs, every new idea is tried in test mode first, and a self-improvement helper keeps preparing better versions of each strategy, like a wheel that keeps turning. The owner steers everything from one screen: they give ideas in plain words, approve every new version of a strategy before it starts, and are the only one who can approve real money.

The project is being planned, and nothing of the trading system is built yet: everything below is the design as it stands.

This document is the full, exact description of every main part of the system and how the parts fit together, with the path to each part's own docs. It describes the parts from the outside and never the logic inside an agent, such as how a strategy decides. Why the system exists, how it should behave and how it makes money are in the vision, `agents/system/docs/vision.md`.

## From: The system at a glance: picture

```text
  outside world: prices, news, events, errors
          │
          ▼
  workers ─────────────────► data files, kept by source
     ▲                             │ file links, read-only
     │                             ▼
  scheduler ── starts runs ──► agents at four levels
     ▲                           system agent
     │                           └─► domain agents
     └── every agent's               └─► strategy agents ◄──► self-improvement helpers
         jobs file                       └─► trading agents ──► actions, test or live
                                                 │
                                                 ▼
                                 own logs, data and results, read by the level above

  keys folder ──► one shared loader ──► only the script that needs a key, at run time
  the owner ──► File Tree page ──► project IDE agent, knowledge base agent ──► files, docs
  the owner ──► trading dashboard (later) ──► watch, approve real money, stop an agent
```

## From: The system at a glance: table rows

| Part | What it is for | Where it lives |
|---|---|---|

| Agents and their four levels | every agent, from the whole system down to one trading agent, in one standard folder | `agents/` |

| Domains | one area of trading each, owned by a domain agent | `agents/trading/prediction-market/`, `agents/copy-trading-agents/` |
| Strategies | one way to make money, owned by a strategy agent with its variations | `agents/trading/prediction-market/strategy-1-agent/` |
| Trading agents | one variation of a strategy each; the agents that trade | inside their strategy's folder |

| Actions: test and live | every action in test or live mode, through scripts | `agents/system/scripts/decisions/`, each agent's `scripts/` |

| The trading dashboard | where the owner watches and steers the trading | `apps/trading-ui/` |

## From: The system at a glance: steps

4. **Trading agents act through scripts.** An action, such as a buy or a sell, goes through the agent's decision scripts in the mode its settings set, test or live. The service that acts logs every action in `agents/system/logs/services/[service]/`. A script that needs a key gets it at run time through one shared loader, and only the keys its settings name.
5. **Results stay with the agent.** Every agent writes its own logs and data in its own folder, and each level reads its children's folders through child links: the system sees every domain, a domain every strategy, a strategy every trading agent.
6. **Self-improvement closes the loop.** A strategy's self-improvement helper reads its trading agents' results, logs and decisions, with research, outside news and the owner's comments, and writes a short report on a new variation. Once the owner approves it, the variation is created as a new trading agent in test mode, next to the others. What was studied goes into `research/`, new checks into `tests/`.
7. **The owner's words become files.** Everything the owner leaves in the project chat or on the File Tree page reaches the knowledge base agent, which saves it and brings the notes and the docs in line; edits made on the page are written into their files. The plan is for the trading dashboard to read every level's files from the system down and to write the owner's actions back as files, such as a job switched off or an account approved.

## From: How the project is laid out: top of the tree

```text
agent-os/
├── README.md                  the front page: what this is and where to start
├── .gitignore                 keeps keys, local tool state and run output out of git
├── .secrets/                  every key, outside the agents' folders and out of git
├── agents/                    every domain, the system included
│   ├── system/                the system agent and the files every agent shares
│   ├── prediction-market-agents/             the prediction-market domain
│   │   └── strategy-1-agent/                 one strategy
│   │       └── pm-strategy-1.momentum-v1.opus55-test/   one trading agent
│   └── copy-trading-agents/                  the copy-trading domain
└── apps/                      our own apps, the outside apps we use, and research clones
    ├── project-IDE/           the owner's window: the File Tree page and what it is built from
    ├── temp/                  repositories cloned only to study them, never kept in git
    └── trading-ui/            the trading dashboard, empty for now
```

## From: How a level reaches its children

If any agent could reach into any other, a change in one place could break agents nobody thought of, and no agent could be understood on its own. So parents see their children, never the other way round: the system looks into each domain, a domain into its strategies, a strategy into its trading agents, and lower levels never reach up.

A parent does this through child links. Each content folder of a level with children holds a folder `subagents.link/` with one folder link per direct child, named after the child and pointing at the child's folder of the same kind. For docs:

```text
agents/system/docs/subagents.link/[domain-name]/                     → that domain's docs/
agents/trading/prediction-market/docs/subagents.link/[agent-name]/    → that strategy's docs/
agents/trading/prediction-market/strategy-1-agent/docs/subagents.link/[agent-name]/
                                                                     → that trading agent's docs/
```

The same holds for the other content folders, so the system reaches any agent in at most three steps. Child links are only read through, never copies, and they are the only folder links in the system. Relink makes them from the folder tree and removes them when a child is gone, and tools that scan folders never follow them. A trading agent has no children, so it has no `subagents.link/`, and no `.claude/` folder is linked at any level.

## From: Agents and their four levels

An agent is one folder with its own AI instructions, responsible for one piece of the Agent OS. Agents sit at four levels. The system agent looks after the whole Agent OS. A domain agent owns one area of trading, such as prediction markets. A strategy agent owns one strategy and keeps improving it. A trading agent is one variation of a strategy, with its own settings, AI model and mode, test or live; it is the one that trades.

All agents live under `agents/`. Every direct child of `agents/` is a domain, and the system is one of them: `agents/system/`, `agents/trading/prediction-market/` and `agents/copy-trading-agents/`. A domain's folder is its domain agent's folder, its strategies are sub-folders of it, and each strategy's trading agents are sub-folders of the strategy. Every agent has the standard folder, and its instructions are always `.claude/CLAUDE.md` in its own folder.

With hundreds of agents, a name must say at a glance what an agent is, and two agents must never be mixed up. So every agent has one name, unique across the whole system and used for its folder, settings, logs, data, docs and place on the dashboard. A trading agent's name starts with its strategy, then its variation name and version, its AI model and its mode: `pm-strategy-1.momentum-v1.opus55-test` is version 1 of the "momentum" variation of the first prediction-market strategy, on Opus 5.5, in test mode. A strategy agent's name carries its model and mode the same way, `pm-strategy-1-agent.opus55-test`, while its folder keeps the plain name `strategy-1-agent/`. Because the model is in the name, agents that differ only by model can run side by side. A name is never changed or reused: the list of agents, `agents/system/docs/index/agents.md`, keeps every agent ever created, retired ones too, and the script that creates agents checks each new name against it. The naming rule is decided; the exact format is our proposal. The plan is that moving an agent to real money creates a new agent whose name ends in `-live`.

Every level also has helpers: AI assistants with their own instructions and tools, built as Claude Code sub-agents, one file each in the level's `.claude/agents/`. The plan is that a helper never runs inside a trading agent's run: it runs in its own level's session and writes its results as files, which agents read through links.

An agent reads its own files, the files it links and its children's folders, and writes only its own real files. New agents are made by one shared script, create-agent, in `agents/system/scripts/system/`, which checks the name, sets up the standard folder and runs the new agent's `init.sh`; the owner can ask for one in plain words, and the system builds it and fits it in.

The plan is that each level runs in its own folder, so a session sees only its own setup, links and children, as a job in its agent's jobs file. At the start the system runs the system agent, the prediction-market domain agent, one strategy agent and two or three variations of it.

## From: The system agent and the shared files

The system agent looks after the whole Agent OS: every area of trading, the system's health, its own development, the files every agent shares, and the owner's questions about the whole. It lives in `agents/system/`, a domain like the others with the same standard folder, and differs in two ways only: its agent runs the whole system, and its folders also hold the files every agent shares.

## From: Domains

### Domains

A domain is one area of trading, and its folder, directly under `agents/`, is its domain agent's folder. The domain agent finds, creates and updates the strategies of its area, makes sure the area makes money and runs smoothly, and answers the owner's questions about it.

The first domain is prediction markets, in `agents/trading/prediction-market/`, with Polymarket first. Copy trading comes next, in `agents/copy-trading-agents/`, with the same layout; crypto, trading on content such as a YouTuber's videos, and combinations of strategies come later, each as a domain of its own.

Besides the standard folder, the prediction-market domain holds:

- `.claude/CLAUDE.md`, the domain agent's instructions, and `.claude/agents/pm-self-improvement-agent.md`, its self-improvement helper;
- `configs/prediction-market-agents.workers.json`, its jobs, and `configs/prediction-market-agents.links.json`, its links;
- `scripts/markets-catalog.worker.py`, its own worker, which keeps a catalogue of the Polymarket markets the domain cares about in `data/markets-catalog/`, and `scripts/relink.system.link.js`, a link to the shared relink script that relinks this agent only;
- `research/prediction-market-research/`, the studies of ways to make money on prediction markets, with the evidence on which work, from which the first strategy is chosen;
- `docs/README.md`, `docs/vision.md` and `docs/rebuild-prompt.md`, the domain's own docs;
- one sub-folder per strategy, such as `strategy-1-agent/`.

A domain takes its share of the shared settings through links and reads its strategies' folders through its child links. It gives its strategies what it collects for the whole area, such as the markets catalogue, which they link. The settings for a whole domain, such as its trading venues, fees and market filters, are planned as a section of the system settings. The plan is that the domain's session runs in its own folder as a job in its jobs file, and its self-improvement helper once a night.

Still open: the venues besides Polymarket and the first copy-trading targets.

Its docs: `agents/trading/prediction-market/docs/README.md`; for copy trading, `agents/copy-trading-agents/docs/README.md`

## From: Strategies

### Strategies

A strategy is one way to make money in a domain, such as market making, and a strategy agent owns it: it prepares variations, tests and compares them, and keeps the winners. A strategy can be plain code, AI or a mix: market making and arbitrage need fast code that reacts instantly, while others gain from an AI's judgement.

The example strategy is `agents/trading/prediction-market/strategy-1-agent/`, the first Polymarket strategy, which the owner chooses. Besides the standard folder it holds:

- `.claude/CLAUDE.md`, the strategy agent's instructions, and `.claude/agents/pm-strategy-1-self-improvement-agent.md`, its self-improvement helper;
- `configs/strategy-1-agent.workers.json`, its jobs, and `configs/strategy-1-agent.links.json`, its links;
- `scripts/relink.system.link.js`, the link to the shared relink script;
- `data/`, the history of its variations side by side;
- `docs/README.md`, `docs/vision.md` and `docs/rebuild-prompt.md`, and the strategy itself as a written definition, which we propose to keep in `docs/`;
- `tests/`, `research/`, and one sub-folder per trading agent, such as `pm-strategy-1.momentum-v1.opus55-test/`.

A strategy takes what its domain shares through its links file, and reads each trading agent's settings, jobs, logs, data, docs, tests and research through its child links. It gives new variations, made through its self-improvement helper as new trading agents, and folds a winning change back into the strategy: its definition, settings and instructions. Where it makes sense, each strategy has its own way of testing on past data, such as replaying a month of old data as if it were live. The plan is that the strategy's session runs in its own folder once a day, and its self-improvement helper once a night.

Still open: the folder's real name, and where testing on past data belongs.

Its docs: `agents/trading/prediction-market/strategy-1-agent/docs/README.md`

## From: Trading agents

### Trading agents

A trading agent is one variation of a strategy, with its own settings, AI model and mode, and it is the one that trades. It does one run at a time, in its own folder. One trading agent is worked out in full as the example of how every trading agent looks: `agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/`, where "momentum" stands for a variation's name.

It holds:

- in `configs/`: `pm-strategy-1.momentum-v1.opus55-test.config.json`, its own settings, such as its mode, risk limits and strategy parameters; `pm-strategy-1.momentum-v1.opus55-test.workers.json`, its jobs, such as its main run, its own worker and one-off jobs on special dates; `pm-strategy-1.momentum-v1.opus55-test.links.json`, its links; and `system.config.link.json` and `models.config.link.json`, links to the shared settings;
- in `scripts/`: `get-polymarket-data.worker.py`, its own worker; `clean-data.system.js`, which tidies raw data before the agent reads it; `make-buy.decision.js`, its decision script for buying and selling; and the shared scripts it links: `risk-check.decision.link.js`, `relink.system.link.js` and `run-tests.system.link.js`;
- in `logs/`: `runs.jsonl` and `run-[date].md`, its runs; `tests.jsonl`, its test results; and `polymarket-prices.worker.link.log`, a link to the log of a shared worker it depends on;
- in `data/`: `get-polymarket-data/`, its own worker's output, and links to data from elsewhere: `polymarket-prices.link.json` from a shared worker, `news-digest.link.md` from a system helper, `markets-catalog.link.json` from its domain and `whale-signals.link.json` from an agent in another domain;
- in `docs/`: `README.md`, what it is, its parent, model and mode; `strategy.md`; `changes.md`, exactly what differs from its parent and what is being tested; `decisions.md`, a summary of its notable decisions; `notes.md`, the owner's comments and the answers; its own `vision.md` and `rebuild-prompt.md`, like every level; and links to shared docs such as `safety.link.md` and `agent-architecture.link.md`;
- its `tests/`, `research/` and level files.

It takes its data, shared settings and shared scripts through links, and the keys its settings name through the shared loader at run time. It gives its decisions, logs and data, all in its own folder, which its strategy reads through its child links, and its actions, made through its decision scripts in its mode. What it trades and how it decides are described in its own docs, not here.

The plan is that the scheduler starts its main run on a regular interval, such as every fifteen minutes, and again whenever one of its important files changes, such as its price data; its own worker runs as a separate job.

An improvement never changes a running trading agent: it always becomes a new trading agent in test mode. Still open: the version rule, self-editing, and where positions are kept.

Its docs: `agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/README.md`

## From: Workers and data

Workers are plain scripts that collect information on a schedule, such as prices, news, important events and errors, and save what they find as files. A script's name says its kind: `.worker.` for a worker, `.decision.` for a script that acts, `.system.` for the machinery.

A worker that many agents use is shared: it lives in `agents/system/scripts/workers/`, writes to `agents/system/data/workers/[worker]/` and logs to `agents/system/logs/workers/[worker]/`. A worker only one agent needs lives in that agent's `scripts/` and writes into that agent's `data/`, one folder per producer, such as `get-polymarket-data/`. The workers and data of the earlier Polymarket tools are reused wherever they fit a strategy.

AI helpers prepare raw information for the agents, for example by boiling the day's news down to what matters for one market. A system helper writes its result into `agents/system/data/subagents/[subagent]/`, a domain's or a strategy's into its own level's `data/`, and agents link these results like any other data.

## From: Jobs and the scheduler

The jobs file sits in the agent's `configs/`, named after the agent: `agents/system/configs/system.workers.json` for the system, `prediction-market-agents.workers.json`, `strategy-1-agent.workers.json` and `pm-strategy-1.momentum-v1.opus55-test.workers.json` below it. A job is a plain script or an AI run: the agent's main run, one of its helpers, a skill, a workflow or a command. For each job the file says what it does, whether it is switched on, how often it runs (every few minutes, at a time of day, once on a date, after another job, or only by hand), where it runs (on the server, in the cloud or in a desktop app) and which AI platform and model it uses. The owner and the agent can see, change and switch off any job there, and a parent sees its children's jobs files through `configs/subagents.link/`. The exact fields of a job are our proposal.

The real intervals are set per agent. We propose that jobs in the cloud, in a desktop app or on GitHub get no keys and never trade, and that a job is paused by switching it off, never by deleting it.

## From: Links between agents

Links give each agent the files it needs from elsewhere without copying them. If every agent kept its own copy of a shared file, hundreds of copies would drift apart, and a fix to one would never reach the others. So an agent gets shared files as links that look like files in its folder but point to the one real file. Every link has "link" in its name, such as `risk-check.decision.link.js` or `subagents.link/`, so it can be told from a real file at a glance.

There are two kinds. A file link points to one file the agent's logic needs, from anywhere under `agents/`: the system, its own domain or strategy, another domain or any agent by its name. It sits in the agent's content folder, such as `data/polymarket-prices.link.json`, and the agent only reads through it. A child link is a folder link from a parent to one child's folder, described above.

Each agent lists its file links in one small file in its `configs/`, its links file: `agents/system/configs/system.links.json`, `prediction-market-agents.links.json`, `strategy-1-agent.links.json` and `pm-strategy-1.momentum-v1.opus55-test.links.json`. For each link it says which file, from where, where the link appears and why. The list is set when the agent is created and changed later by the agent, its self-improvement helper or the owner.

One shared script, relink, in `agents/system/scripts/system/`, reads every links file, creates the links and the child links, removes links nobody lists and checks that none is broken. Every level below the system has `scripts/relink.system.link.js`, a link to it that relinks that agent only. Relink runs when a links file changes, when changes are reviewed (before they are saved to the repository, after new changes are downloaded and when the owner approves a change) and when an agent edits its own links file. How each moment starts it is our proposal: a job that watches the links files, git hooks installed by the system's `init.sh`, and a hook in each agent's AI settings. We also propose that relink writes a list of every link to `agents/system/data/system/`, so anyone can see who reads which file, and that a second shared script, check-links, checks every link after each change. Nothing is ever linked into the keys folder or into any `.claude/` folder.

Links are also how agents listen to each other. An agent that finds another's output useful subscribes by linking it; new data reaches it on its next run or, if the agent marks the file as important, interrupts the run in progress. For example, a risk-management agent that sees markets collapsing, say because of a big war, can tell every agent to sell everything.

## From: Settings and AI models

`agents/system/configs/system.config.json` is the one system settings file, with everything that can be controlled for the whole system. The plan is for it to have sections for defaults, test and live mode, risk limits, schedule defaults, the rules for restarting runs, trading accounts, notifications and the areas of trading; a section that grows long moves into a file of its own.

`agents/system/configs/models.config.json` is the models file: which AI platform and model each AI part uses, meaning each agent, helper and AI worker, and which platforms can be used. A job may name its own model; otherwise the models file decides.

Every agent has its own settings file, such as `pm-strategy-1.momentum-v1.opus55-test.config.json`, next to its jobs and links files, and reads the system settings and the models file through `system.config.link.json` and `models.config.link.json`. The system reaches each domain's settings through `agents/system/configs/subagents.link/`, and each level the next one down the same way.

Which settings are shared and which belong to each agent is settled with two or three example agents before anything is built. We propose that settings combine in a fixed order, from the system settings through the agent's own to the owner's choices such as stopping or approving, except that an agent's settings may only tighten a risk limit, never loosen it; that settings are read at the start of each run, so a change applies from every agent's next run; and that changes to modes, risk limits and accounts need the owner's approval. The exact fields of every settings file are our proposal.

Every part that uses AI has a fixed model for its kind of work:

| Kind of work | Model |
|---|---|
| Thinking, planning, analysis and improvement, and running the trading agents | Claude Opus 5.5 at extra-high thinking effort |
| Unimportant tasks | Claude Sonnet 5.5 |
| Light, high-volume work such as collecting and filtering data | Cursor with its Composer 2.5 model |
| Unimportant work, once connected | free models through OpenRouter |
| Later | Codex and Kimi 3 |

The model is part of an agent's name, and we propose that the script that creates agents checks the two agree.

Still open: the files' exact shape, settings files for domains and strategies, and the model defaults in detail.

## From: Actions: test and live

### Actions: test and live

An action is anything an agent does in a market, such as buying or selling, and every action works in a test mode and a live mode from the start, chosen in the agent's settings. On a blockchain, test mode can use a test network. The mode is the last part of every agent's name, so a test agent and a live agent are always two different agents. Every new agent and every change runs in test mode first, where mistakes cost nothing.

For now the system acts only on blockchains, on any network and app there; from centralised exchanges and other apps it only collects information. The trading venues and accounts a strategy needs are chosen while that strategy is built.

Actions go through scripts. Each trading agent has its own decision scripts, such as `make-buy.decision.js`, and links the shared building blocks it needs, such as the risk check, from `agents/system/scripts/decisions/`. A decision script reads the mode from the agent's settings before it acts, and in test mode never touches real money. The service that acts logs every action, test or live, in `agents/system/logs/services/[service]/`.

Real money comes only after an agent and its strategy have shown good results, and only when the owner approves an account for that agent, one account at a time. No agent can approve real money, for itself or another. We propose that an action is live only when the agent is on a list of agents allowed to trade live in the system settings, has an account the owner approved and asks for live mode in its own settings; that an agent can never switch itself to live; and that trading accounts are listed in the system settings with the names of their keys, never the values.

Outside text, such as news and social posts, can carry hidden instructions meant to trick an AI, so protection against it is built together with live trading. We propose hard limits written in code, on order size, losses and allowed markets, checked before every action, and a stop switch in the system settings that halts every agent at once; the idea of one shared part that places every order and checks those limits is still being weighed.

Its docs: `agents/system/scripts/decisions/decisions.index.md`

## From: Keys and secrets

Keys to trading accounts and services are the most dangerous thing in the system: a key in a log, a shared file or an AI conversation can leak, and an AI that reads a live key could misuse it. So every key lives in one protected folder, `.secrets/`, at the top of the repository, outside the agents' folders and never saved to git.

- `.secrets/live/.env`: the same key names with real values, for the owner only, set up when live trading begins.

A script gets only the keys its settings name, at the moment it runs, through one shared loader in `agents/system/scripts/system/`: an agent's settings or a job list the key names needed, and the loader gives just those keys to that one script's process. Keys are never linked, copied, logged or shown to an AI, and every level's `.claude/settings.json` blocks AI sessions from reading or editing the live keys. Keys are created and edited in the local trading dashboard on the owner's own machine, so values never leave it; the File Tree page never holds a value. How the loader works in detail is our proposal.

## From: Logs

Logs that belong to no single agent are shared and sit in `agents/system/logs/`, by source: `system/` for the scheduler, restarts, relink, link checks, errors and costs; `services/[service]/` for every action of each service that acts; `workers/[worker]/` for the shared workers; and `subagents/[subagent]/` for the calls of helpers, including every request sent from the File Tree page on the owner's server. The system reaches each domain's logs through `agents/system/logs/subagents.link/`.

Each agent's own logs are real files in its own `logs/`: its runs, such as `runs.jsonl` and `run-[date].md`, its decisions, the runs of its jobs and its test results in `tests.jsonl`. It links only the few shared logs it needs, such as `polymarket-prices.worker.link.log`. Each level reads its children's logs through its child links, and the plan is for the dashboard to start at the system's logs and go down level by level.

## From: Tests

`tests/agents/` holds the tests of the level's instructions and helpers, each a `[test-id].test.md` with a scenario and the expected behaviour. `tests/scripts/` holds the tests of its code, each a `[test-id].test.[js|py]`. Each has a `tests.config.json`, the list of its tests, where the owner can switch each test on or off and see when it last ran, its result and what to do next, and a `run-tests.system.link.js`, a link to the shared run-tests script, which runs that folder's tests and writes the results back into the list and into the level's `logs/tests.jsonl`. A trading agent's `scripts/run-tests.system.link.js` runs both kinds.

Tests take the files they check and give results. The system's tests are in `agents/system/tests/`, every other level's in its own folder, and each level reads its children's through `tests/subagents.link/`. We propose that each test has its own schedule (by hand, when the file it checks changes, at an interval, or before an agent moves to real money); that tests of instructions run the agent's AI in test mode on prepared data, with no keys; and that the tests folders sit at the top of each agent's folder.

## From: Research

Three studies already exist and have their places in the tree: `agents/trading/prediction-market/research/prediction-market-research/`, the studies of ways to make money on prediction markets and the pipeline that wrote them; `agents/system/research/self-improving-agents/`, a study of agents that improve themselves; and `agents/system/research/trding-agents-arhiteches/`, a study of how trading agents are built, with specs, diagrams and a page that shows them, under its folder name as it is.

Research takes questions from the helpers, the agents and the owner, and gives results that lead to new variations, changes and tests. Each level reads its children's research through `research/subagents.link/`, so the system's `agents/system/research/` reaches every level. A self-improvement helper reads past items before it starts a new one, so work is not repeated.

The exact fields of the list are our proposal. Still open: the spelling of one folder's name.

Its docs: `agents/system/research/research.index.md`

## From: Self-improvement helpers

A self-improvement helper is the helper at each level that keeps preparing better versions of what that level owns. The system's, `agents/system/.claude/agents/sys-self-improvement-agent.md`, improves the system itself (its shared scripts, settings, choice of AI models and docs) and reacts to new AI models and tools by starting test agents to try them. The prediction-market domain's, `agents/trading/prediction-market/.claude/agents/pm-self-improvement-agent.md`, compares strategies and their variations across the area and proposes new ones. The strategy's, `agents/trading/prediction-market/strategy-1-agent/.claude/agents/pm-strategy-1-self-improvement-agent.md`, prepares new variations of its strategy.

A strategy's helper takes the results, logs and decisions of the strategy's trading agents, read through the strategy's child links, together with research, outside news and the owner's comments. It gives a short report on each new variation it prepares. Once the owner approves the report, the variation is created through the script that creates agents, as a new trading agent in test mode next to the current ones. The variations compete, and the winners become the new standard. A variation may change anything: settings, instructions, code or the AI model. The helper also records what it studied in `research/`, adds tests for what it changes, and keeps the history of the variations in the strategy's `data/`.

Self-improvement helpers keep a memory between runs, which the plan places in their level's `.claude/agent-memory/`, and they are all built from shared templates, so they improve agents in a similar, well-tested way. The plan is that each runs once a night as a job in its level's jobs file, in its own level's session. Self-improvement never touches real money or the live keys.

Still open: whether it may retire a variation on its own.

Its docs: `agents/system/docs/common/self-improvement-templates.md`

## From: The knowledge base and the docs

The docs serve two readers at once. The owner reads them to understand and steer the project; an AI reads them before it changes anything, so they must be exact enough to act on. For any file an AI can get its whole context: the file's own How it works, the knowledge that applies to it directly and from every folder above it (a skill of a strategy's helper inherits what holds for the strategy, its domain and the system), and the files, agents, skills, docs and lists related to it. When a file changes, those relations say what else must follow and how, and each of them is brought in line before the round ends. What a session learns about the system is filed the same way as the owner's messages, even when no file changed. Every question the owner asks gets a home in the docs: the answer is written where the owner should have found it, as an explanation of how exactly that thing works. Today a build script prints this context for any file from the knowledge map; we propose a Details file next to every file that lists its relations, what must change with it and what it inherits from above, shown on the File Tree page.

The same docs exist at every level. Every domain, strategy and trading agent has its own `docs/` with its own vision, README and rebuild prompt, each telling only its own story, and a lower level's rebuild prompt builds only its own folder: shared things are explained once, at the highest level where they apply, and a lower level sums them up in a sentence or two and describes only what differs. Each agent reaches the shared docs it needs through links such as `safety.link.md`, and a parent its children's docs through `docs/subagents.link/`.

## From: The trading dashboard

### The trading dashboard

The trading dashboard is the web app where the owner watches and steers the trading: in a first version, the list of agents, their logs and performance, and the approvals waiting for the owner. It is planned in `apps/trading-ui/` as a Next.js app with its own small service. The folder is empty for now, and the dashboard may never be needed as a separate app if the project IDE does its job.

The plan is that it reads every level's files from the system down through the child links, and writes the owner's actions back as files: a job switched on or off, an approval in the system settings, a comment in an agent's `docs/notes.md`. Through it the owner can open any agent and see everything about it, approve or refuse an account with real money, and stop or delete any agent. Keys are created and edited there, on the owner's own machine.

Still open: whether it becomes an app of its own or part of the owner's window on the project, and how it reads the files and is protected.

Its docs: `apps/trading-ui/trading-ui.index.md`

## From: Where each part's docs are: rows

| Part | Its docs | What they add |
|---|---|---|

| Agents and their four levels | `agents/agents.index.md` | how the domains and their levels fit |
| The system agent and the shared files | `agents/system/system.index.md` | the system folder item by item |
| Domains | `agents/trading/prediction-market/docs/README.md`, `agents/copy-trading-agents/docs/README.md` | each domain's strategies, information, venues and jobs |
| Strategies | `agents/trading/prediction-market/strategy-1-agent/docs/README.md` | the strategy's variations, information and testing on past data |
| Trading agents | `agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/docs/README.md` | what the trading agent reads, produces and runs |

| Actions: test and live | `agents/system/scripts/decisions/decisions.index.md` | the shared building blocks for acting |

| The trading dashboard | `apps/trading-ui/trading-ui.index.md` | what the dashboard is for |

## From: Still open in the design

**Agents and their four levels**
- Does the version number in a name belong to the variation or to the strategy?
- Does a small change, such as a new link, a changed job or a new model on one job, make a new version of an agent, or can it happen in place?
- May an agent change its own settings and docs, or only its self-improvement helper and its domain agent?


**Domains**
- Does the prediction-market domain use Polymarket only, or Kalshi and other venues too?
- Which traders does copy trading follow first, and which worker or agent produces the copy-trading data other agents plan to link?

**Strategies**
- Should a strategy's folder carry a real strategy name, model and mode instead of `strategy-1-agent/`?
- Is the strategy's definition kept in its `docs/` or as a skill?
- Is testing on past data a test, a research item, or both?

**Trading agents**
- Are an agent's positions and cash kept in its own `data/` or in one shared record?

**Workers and data**
- How does an agent tell what is new since its last run: by file times, or by a bookmark kept per agent?
- Where do the workers helper and the helper that sets the parallel limit sit, and what are they called?
- Do the earlier Polymarket tools come in as a forked app in `apps/`?

**Actions: test and live**
- Are the hard limits checked in each agent's scripts, or in one shared part that places every order?

**Research**
- Is the misspelt folder `trding-agents-arhiteches/` renamed when the plan moves into the repository?

**Self-improvement helpers**
- May a strategy's self-improvement helper retire a losing variation on its own, or only propose it?


**The trading dashboard**
- Is it an app of its own or part of the owner's window on the project, and is it needed at all?
- Does it read the files directly or through a small service, and how is it protected?
