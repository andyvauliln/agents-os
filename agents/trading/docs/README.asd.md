# Trading (ASD-STE100)

This file is the ASD-STE100 version of `README.md` in this folder. `README.md` is the source. If the two files do not agree, use `README.md`.

## In short

Trading is the first type of work in the Agent OS. All of the trading work is in one folder. This folder contains the trading domains, the trading docs and the trading research.

A trading domain is one area of trading, for example prediction markets. Each trading domain operates many small trading agents at the same time. Each idea starts in test mode, with no real money. The system keeps the versions that work. Only the owner can give real money to an agent.

The first trading domain is prediction markets on Polymarket. A new trading domain starts as a copy of the prediction-market domain. Then it changes only its own parts.

Status: the trading docs and the research studies exist. The prediction-market domain has only empty folders. Its old files are in an archive. The project writes this domain again in stage two. No part that trades exists at this time.

This document gives a full and exact description of each part of `agents/trading/`. It also tells what each trading domain contains, and where the docs of each part are. It does not tell how an agent makes decisions. The vision, `agents/trading/docs/vision.md`, tells why trading has its own folder, how trading must operate and the rules.

## Trading at a glance

`agents/trading/` is a folder. It is not an agent. It has no AI instructions, no settings, no scripts and no jobs. It has no `.claude/` folder. Each file and each folder in it has a How it works file and a Details file.

| Part | Purpose | Location |
|---|---|---|
| Trading's docs | Tell what all trading domains share, how to make a new domain and how to build this folder again | `agents/trading/docs/` |
| Research studies | Give the start information for the trading domains | `agents/trading/researches/` |
| Prediction-market domain | The first trading domain. Stage two. Folders only at this time | `agents/trading/prediction-market/` |
| Later trading domains | Copies of the prediction-market domain. The owner asks for them | `agents/trading/[domain]/`. None at this time |
| Trading dashboard | The dashboard of the prediction-market domain. Empty | `apps/trading-ui/` |

How the parts connect:

1. The system agent connects to each trading domain directly, through its child links. This folder does not add a level of agents.
2. A domain agent uses the research studies and the ideas of the owner to start its strategies.
3. In a domain, information goes down. Workers collect prices and other data into the `data/` folder of the domain. Each strategy and each trading agent links the files that it needs.
4. Trading agents write their decisions and orders to logs. Their results go up, level by level, to the domain agent and to the dashboard of the owner.
5. The owner approves new trading agents and real money. The owner can stop each trading agent.

## How trading is laid out

```
agents/trading/
├── trading.index.md / trading.meta.json   How it works and Details of this folder
├── docs/                                  trading's own docs
│   ├── vision.md                          why trading, what all trading domains share
│   ├── README.md                          the source of this file
│   ├── README.asd.md                      this file
│   └── rebuild-prompt.md                  how an AI builds this folder again
├── researches/                            the research studies
│   ├── prediction-market-research/        ways to make money on prediction markets
│   ├── self-improving-agents/             agents that make themselves better
│   └── trding-agents-arhiteches/          how trading agents are built
└── prediction-market/                     the first trading domain (stage two)
```

Each trading domain uses the standard agent folder at each of its three levels:

```
[agent folder]/
├── .claude/          the AI setup of the agent: rules, skills, commands, sub-agents, workflows, output styles, memory
├── configs/          settings, jobs and links files, and links to shared settings
├── scripts/          the scripts of the agent, and links to shared scripts
├── logs/             run logs and session logs
├── data/             the data that the workers of the agent collect, and links to shared data
├── docs/             vision.md, README.md, rebuild-prompt.md and the notes of the agent
├── tests/            agents/ (tests of instructions) and scripts/ (tests of scripts)
├── research/         one folder for each research item
└── [child agent]/    the agents one level below
```

A level with children has a `subagents.link/` folder in each content folder. The content folders are `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/` and `research/`. `subagents.link/` contains one folder link for each child. Each link goes to the folder of the same type in that child. A trading agent has no children. Thus it has no `subagents.link/` folder.

## The parts

### Trading's docs

`agents/trading/docs/` contains the trading docs. People and AI read them. The docs are:

- `vision.md`: why trading has its own folder, what all trading domains share and how to make a new domain.
- `README.md`: the full description of the parts.
- `README.asd.md`: this file. It is `README.md` in ASD-STE100 Simplified Technical English. Use it to compare the two texts.
- `rebuild-prompt.md`: the prompt that an AI uses to build this folder again.

Each doc has a How it works file and a Details file. Each doc also has an outline file (`[name].example.md`) and a file of open questions (`[name].questions.md`).

These docs are between the system docs above and the docs of each trading domain below. They tell only what all trading domains share. The details of one domain stay in the docs of that domain. If a change in a domain affects all domains, update these docs. Then update the system docs above them.

The knowledge base agent writes these docs. It uses the skills `vision-doc`, `readme-doc`, `readme-asd-doc` (planned) and `rebuild-prompt-doc`. The owner can also change the docs on the File Tree page.

Its docs: `agents/trading/docs/docs.index.md`

### Research studies

`agents/trading/researches/` contains the research studies. These are real files. They existed before the trading agents. The folder keeps the name `researches/` that the owner gave it. The research history of each agent is in the `research/` folder of that agent.

- `prediction-market-research/`: 42 studies of ways to make money on prediction markets. The numbers are `01` to `34` and `50` to `57`. Each study is one Markdown file, for example `01-maker-reward-pool-farming.md`. Some studies describe practices that you must not do, for example wash trading and insider trading. `_evidence/` contains the background evidence `E1` to `E9`, the strategy lists and one row for each study. `_pipeline/` contains the pipeline that wrote the studies.
- `self-improving-agents/`: one study of methods and architectures for agents that make themselves better.
- `trding-agents-arhiteches/`: one study of how trading agents are built. It contains `README.md`, 29 architecture specifications in `specs/`, their diagrams in `diagrams/` and a gallery page `index.html`.

The domain agents read these studies when they look for strategies. The owner reads them on the File Tree page. Do not change a study after it is complete. If a study causes a decision, record the decision in the notes.

Its docs: `agents/trading/researches/researches.index.md`

### The trading domains

Each trading domain is a full domain of the Agent OS. Each domain has its own folder in `agents/trading/`. Each domain is a direct child of the system agent. Each domain has three levels of agents. Each level uses the standard agent folder:

- **The domain agent** is in the folder of the domain. It finds, makes and updates strategies. It makes sure that the domain makes money. It answers the questions of the owner.
- **Strategy agents** each have one folder in the domain, for example `strategy-1-agent/`. Each strategy agent owns one way to make money, its definition and its versions.
- **Trading agents** (variants) each have one folder in their strategy. They are the versions that trade.

**The prediction-market domain** (`agents/trading/prediction-market/`) is the first domain. It trades on Polymarket first. At this time it contains only folders. Each folder contains a `.gitkeep` file. The folders are:

- the standard folder of the domain, with `scripts/decisions/`, `logs/jobs/`, `logs/services/`, `data/markets-catalog/`, `data/polymarket-prices/`, `docs/common/`, `docs/how-to/` and `docs/index/`;
- one strategy, `strategy-1-agent/`;
- one example trading agent below the strategy, `pm-strategy-1.momentum-v1.opus55-test/`. The word "momentum" is only a placeholder.

The old files of the domain are in `vision/archive/2026-10-12/prediction-market/`. Its trading notes are in `vision/docs/prediction-market-agents/`. In stage two, the project writes the domain again from these files. The domain then gets its own vision, README and rebuild prompt.

**Later trading domains** are copies of the prediction-market domain, for example copy trading. The owner asks for them. At this time, none is in the tree.

Its docs: `agents/trading/prediction-market/docs/`. This folder is empty until stage two adds its `README.md`.

### What every trading domain holds

Each trading domain has the same types of trading parts in its standard folder. The prediction-market domain defines them first. A copied domain keeps their shape.

- **The trading settings of the domain** are one file in its `configs/` folder. This file contains:
  - risk limits for the full domain, for each agent and for each venue;
  - the trading accounts;
  - the venues, fees and market filters;
  - the currency;
  - the order stop switch;
  - the trade alerts that go to the owner.

  In the prediction-market domain, the file is `prediction-market-agents.config.json`. Trading agents connect to it through a file link. A trading agent can only make the limits tighter (proposal).
- **The shared trading scripts** are in `scripts/decisions/`. These scripts buy, sell and check risk. Their names are `[name].decision.[ext]`. The trading domains add the script type `decision` to the system types `worker` and `system`. Each order goes through a decision script. The decision script reads the mode and the limits before it does an action. Trading agents link the scripts that they need.
- **The order logs** are in `logs/services/[service]/`. The service that places an order logs it. This is true for test orders and live orders.
- **The trading notes** are in `docs/`. They are the trading layer of the system notes. Each name starts with `trading-`. The notes are overview, architecture, conventions, safety, data formats, flows, metrics, glossary, roadmap and feature map. Other folders are:
  - `common/`: the design of the trading agent, the trading prompt and the strategy self-improvement templates;
  - `how-to/`: go live with money, add a trading account, stop a trading agent, make a strategy or a variant;
  - `index/`: the list of trading accounts.

  A domain also keeps `doc-outlines.md`. This file tells what the docs of each level contain.

Its docs: the `docs/README.md` file of each trading domain

### Names of strategies and trading agents

The name of a trading agent starts with its strategy. The name ends with its AI model and its mode. The format is `[strategy-id].[own-name]-v[N].[platform-model]-[test|live]`. An example is `pm-strategy-1.momentum-v1.opus55-test`. The folder of a trading agent has the same name as the agent.

The ID of a strategy agent also contains its main model and its mode, for example `pm-strategy-1-agent.opus55-test`. The folder of the strategy keeps a simple name, for example `strategy-1-agent/`.

Names use only lowercase letters, digits, `-` and `.`. The maximum length is 64 characters. The owner decided that the name starts with the strategy. The exact format is a proposal.

A changed setting, instruction or script makes a new trading agent. Then `v[N]` increases by one. A different model changes the model part of the name. Do not change or use again a name. A test version and a live version are different agents.

Its docs: `vision/docs/prediction-market-agents/trading-conventions.md`, until the project writes the domain notes again

### Accounts, keys and real money

A trading account is an account or a wallet at a venue. A trading agent can use it. The trading settings of the domain list the accounts. Each account entry has these data:

- its ID and its venue;
- its mode;
- funded or not funded;
- approved by the owner or not approved;
- the agent that uses it;
- its maximum capital;
- the names of its keys.

The `docs/index/` folder of the domain keeps a list of the accounts that people can read.

Keys follow the key rules of the Agent OS. The key values are only in the `.env` files in `.secrets/test/` and `.secrets/live/`. Git does not keep these files. All other files use only the key names. Each key name has a prefix for its account, for example `POLYMARKET_ACCT1_API_KEY`. The system script `load-secret` gives the keys of an account to one process at a time. It refuses live keys if the owner did not approve the account.

Only the owner can:

- approve an account with real money;
- add its live keys;
- change the risk limits or the accounts.

An agent cannot approve an account. This is true for itself and for other agents.

Its docs: `vision/docs/prediction-market-agents/trading-safety.md`, until the project writes the domain notes again

### Test and live

Each trading agent starts in test mode. This is also true for each version that self-improvement makes. In test mode, the system simulates each order at the price at the time of the decision. On blockchains, test mode can also use a test network.

A trading agent goes live only when the owner approves it. The owner must also give it a funded and approved account. A new strategy configuration starts only after the owner reads a report on it and approves it.

At this time, agents place orders only on blockchains. They can use all networks and apps. Centralised exchanges and other apps are only sources of information.

Each decision script checks two stop switches before each order: the general stop switch of the system and the order stop switch of the domain. It does this in test mode and in live mode. The two stop switches are proposals. The effect of the order stop switch on open positions is an open question.

Its docs: `vision/docs/prediction-market-agents/how-to/go-live-with-money.md`, until the project writes the domain notes again

### Metrics and comparing versions

The system measures trading agents on money. It also uses the cost, speed and error measures of the system. We propose these measures:

- realised profit and loss, unrealised profit and loss, and the return on capital, from the order logs;
- win rate, with the number of trades;
- the largest fall from a peak and the current fall from a peak;
- calibration: the forecasts of the agent compared with the results and with the market price;
- AI cost for each trade.

The system compares the versions of one strategy over the same period and the same capital. It compares test results with test results. The measures that decide success are an open question.

Its docs: `vision/docs/prediction-market-agents/trading-metrics.md`, until the project writes the domain notes again

### Making a new trading domain

A new trading domain is a copy of the prediction-market domain. The owner asks for it. Do these steps:

1. Use the system script `create-agent` to make the domain agent and its folders. Do not copy the folders by hand.
2. Keep the levels, the standard folders, the trading notes, the shape of the trading settings and the decision scripts.
3. Change the parts of the new domain: venues, fees, market filters, information sources, strategies and risk limits.
4. Start the domain with no funded account.

If two domains need the same trading part, move that part up into `agents/trading/`. Until then, keep it in the domain.

Its docs: `agents/trading/docs/rebuild-prompt.md`

### The trading dashboard

`apps/trading-ui/` is the planned dashboard of the prediction-market domain. On this page, the owner sees each trading agent and its results. The owner approves real money there, and stops or deletes agents. The folder stays in `apps/`. It is empty at this time. It is an open question if the project needs it.

Its docs: `apps/trading-ui/trading-ui.index.md`

## Where each part's docs are

| Part | Its docs | Contents |
|---|---|---|
| Trading's folder | `agents/trading/trading.index.md` | a short description of the folder |
| Trading's docs | `agents/trading/docs/docs.index.md` | the purpose of each doc |
| Research studies | `agents/trading/researches/researches.index.md` | the studies and how agents use them |
| Prediction-market domain | `agents/trading/prediction-market/docs/` | empty at this time. Its vision, README and rebuild prompt come in stage two |
| Trading notes (kept) | `vision/docs/prediction-market-agents/` | all the trading rules, formats, flows and metrics |
| Trading dashboard | `apps/trading-ui/trading-ui.index.md` | the planned dashboard |
| The system above | `agents/system/docs/README.md` | all the parts that all agents share |

## Still open in the design

- **Trading folder:** Which parts go up into `agents/trading/` when there are two trading domains?
- **Domains:** Which trading domain is next, and when? Copy trading is the probable next domain.
- **Names:** Is `v[N]` part of the trading agent or part of the strategy? Do strategy folders also contain the model and the mode? Do folders use the shorter form `strategy-1/strategy-1.v1.Claude-Opus5.5/`?
- **Safety:** What does the order stop switch do with open positions? What are the capital limits of the first live accounts? How do account entries connect to key prefixes?
- **Metrics:** Which measures decide success? Where does the system keep positions? Where does the system record market results?
- **Self-improvement:** Can a strategy put a winning change into itself without the owner? Can it stop losing versions without the owner?
- **Owner:** Which channel sends trade alerts to the owner?
