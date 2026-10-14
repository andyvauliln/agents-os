# Trading

## In short

Trading is the first kind of work the Agent OS does, and everything about it lives in one place: a folder of trading domains, with trading's own docs and its research. A trading domain is one area of trading, such as prediction markets. Every trading domain runs many small trading agents side by side, tries each idea in test mode with no real money, keeps the versions that work and lets only the owner put real money in. The first trading domain is prediction markets on Polymarket; a new one starts as a copy of it and changes only what is its own. The system level stays general: nothing about money, markets or orders is written in the system's docs, settings or scripts, and all of it lives here, in trading and its domains.

Where it stands: trading's docs and its research studies exist. The prediction-market domain exists as its empty folders, and its `docs/` already holds all the trading notes the project has; its other files are kept aside and it is written again in the project's second stage. Nothing that trades is built yet.

This document is the full, exact description of every part of `agents/trading/` and of what every trading domain holds, with the path to each part's own docs. It describes parts from the outside, never the logic inside an agent. Why trading has its own place, how it should work and its rules are in the vision, `agents/trading/docs/vision.md`.

## Trading at a glance

`agents/trading/` is a folder, not an agent. It has no AI instructions, no settings, no scripts and no jobs of its own, and no `.claude/` folder. Like every part of the Agent OS, each file and folder in it has a How it works file and a Details file next to it.

| Part | What it is for | Where it lives |
|---|---|---|
| Trading's docs | what every trading domain shares, how a new one is made, how to rebuild this folder | `agents/trading/docs/` |
| Research studies | the studies the trading domains start from | `agents/trading/researches/` |
| Prediction-market domain | the first trading domain, stage two; folders and the trading notes today | `agents/trading/prediction-market/` |
| Later trading domains | copies of the prediction-market domain, made when the owner asks | `agents/trading/[domain]/`, none yet |
| Trading dashboard | the prediction-market domain's dashboard, empty | `apps/trading-ui/` |

How the parts connect:

1. The system agent reaches each trading domain directly, through its child links; this folder adds no level of agents between them.
2. A domain agent starts its strategies from the research studies here and from the owner's ideas.
3. Inside a domain, information flows down: workers collect prices and other data into the domain's `data/`, and each strategy and trading agent links the files it needs.
4. Trading agents write their decisions and orders to logs; their results flow up, level by level, to the domain agent and to the owner's dashboard.
5. The owner approves new trading agents and real money, and can stop any trading agent.

## How trading is laid out

```
agents/trading/
├── trading.index.md / trading.meta.json   How it works and Details of this folder
├── docs/                                  trading's own docs
│   ├── vision.md                          why trading, what every trading domain shares
│   ├── README.md                          this file
│   ├── README.asd.md                      this file again in ASD-STE100
│   └── rebuild-prompt.md                  how an AI rebuilds this folder
├── researches/                            the research studies
│   ├── prediction-market-research/        ways to make money on prediction markets
│   ├── self-improving-agents/             agents that improve themselves
│   └── trding-agents-arhiteches/          how trading agents are built
└── prediction-market/                     the first trading domain (stage two)
```

Every trading domain uses the standard agent folder at each of its three levels:

```
[agent folder]/
├── .claude/          the agent's AI setup: rules, skills, commands, sub-agents, workflows, output styles, memory
├── configs/          settings, jobs and links files, plus links to shared settings
├── scripts/          the agent's own scripts, plus links to shared ones
├── logs/             run logs and session logs
├── data/             what the agent's workers collect, plus links to shared data
├── docs/             vision.md, README.md, rebuild-prompt.md and the agent's notes
├── tests/            agents/ (tests of instructions) and scripts/ (tests of scripts)
├── research/         one folder per research item
└── [child agent]/    the agents one level down
```

A level with children has `subagents.link/` inside each content folder (`configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/`), one folder link per child pointing at that child's folder of the same kind. A trading agent has no children and no `subagents.link/`.

## The parts

### Trading's docs

`agents/trading/docs/` holds trading's own docs for people and for AI: `vision.md` (why trading has its own place, what every trading domain shares, how a new one is made), this `README.md`, `README.asd.md` (this README in ASD-STE100 Simplified Technical English, to compare with this one) and `rebuild-prompt.md` (the prompt an AI follows to rebuild this folder). Each doc has its How it works and Details files, an outline file (`[name].example.md`) and an open-questions file (`[name].questions.md`) next to it.

They sit between the system's docs above and each trading domain's docs below. They describe only what every trading domain shares; a single domain's detail stays in its own docs. When a trading domain changes in a way that touches what all domains share, these docs are brought in line, and then the system's docs above them.

The knowledge base agent writes them with the `vision-doc`, `readme-doc`, `readme-asd-doc` (planned) and `rebuild-prompt-doc` skills; the owner can change them on the File Tree page.

Its docs: `agents/trading/docs/docs.index.md`

### Research studies

`agents/trading/researches/` holds the research studies, real files that were here before any trading agent. The folder keeps the owner's name `researches/`; every agent's own research history lives in its `research/` folder instead.

- `prediction-market-research/`: forty-two studies of ways to make money on prediction markets, numbered `01` to `34` and `50` to `57`, one Markdown file each, such as `01-maker-reward-pool-farming.md` and `21-llm-forecasting-agents.md`. Some describe practices to avoid, such as wash trading and insider trading. `_evidence/` holds the background evidence (`E1` to `E9`: venue mechanics, incentive programs, resolution, profitability, other venues, tooling, AI forecasting, multi-agent simulation, legal) with the strategy lists and one row per study; `_pipeline/` holds the pipeline that wrote the studies.
- `self-improving-agents/`: one study of approaches and architectures for agents that improve themselves.
- `trding-agents-arhiteches/`: a study of how trading agents are built: `README.md`, twenty-nine architecture specs in `specs/`, their diagrams in `diagrams/` and a gallery page `index.html`.

The domain agents read these studies when they look for strategies; the owner reads them on the File Tree page. A study is not changed after the fact; when it leads to a decision, the decision is recorded in the notes.

Its docs: `agents/trading/researches/researches.index.md`

### The trading domains

Each trading domain is a full domain of the Agent OS, in its own folder under `agents/trading/`, and a direct child of the system agent. Each arranges its agents in three levels, each with the standard agent folder:

- **The domain agent**, in the domain's folder: finds, creates and updates strategies, makes sure the domain makes money, answers the owner's questions.
- **Strategy agents**, one folder each inside the domain, such as `strategy-1-agent/`: each owns one way to make money, its definition and its versions.
- **Trading agents** (variants), one folder each inside their strategy: the versions that actually trade.

**The prediction-market domain** (`agents/trading/prediction-market/`) is the first. It trades on Polymarket first. Today it holds only its folders, each with a `.gitkeep`: the standard folder of the domain (with `scripts/decisions/`, `logs/jobs/`, `logs/services/`, `data/markets-catalog/`, `data/polymarket-prices/`, `docs/common/`, `docs/how-to/` and `docs/index/` inside), one strategy `strategy-1-agent/`, and one example trading agent below it, `pm-strategy-1.momentum-v1.opus55-test/`, where "momentum" is only a placeholder. Its docs folder already holds all the trading knowledge the project has: the trading notes (overview, architecture, conventions, safety, data formats, flows, metrics, glossary, roadmap, feature map), the trading agent's design, the trading prompt, the strategy self-improvement templates, the how-to guides, the list of trading accounts, the outlines of its docs, the notes for its vision, and the trading parts that were taken out of the system's README and rebuild prompt. Its other earlier files are kept in `vision/archive/2026-10-12/prediction-market/`. In the second stage the domain is written again from them, with its own vision, README and rebuild prompt.

**Later trading domains**, such as copy trading, are copies of the prediction-market domain, made when the owner asks. None is in the tree.

Its docs: `agents/trading/prediction-market/docs/`, the trading notes today; its `README.md` comes with the second stage

### What every trading domain holds

Every trading domain has the same kinds of trading parts, in its own standard folder. The prediction-market domain defines them first and a copied domain keeps their shape:

- **The domain's trading settings**, one file in its `configs/`: risk limits for the whole domain, per agent and per venue; the trading accounts; the venues, fees and market filters; the currency; the order stop switch; and which trade alerts reach the owner. In the prediction-market domain it is `prediction-market-agents.config.json`. Trading agents reach it through a file link and may only make its limits tighter (our proposal).
- **The shared trading scripts**, in `scripts/decisions/`: the scripts that buy, sell and check risk, named `[name].decision.[ext]`. `decision` is a script kind the trading domains add to the system's `worker` and `system` kinds. Every order goes through a decision script, which reads the mode and the limits before it acts. Trading agents link the ones they need.
- **The order logs**, in `logs/services/[service]/`: every order, test or live, logged by the service that placed it.
- **The trading notes**, in `docs/`: the trading layer of the system's notes, each named with a `trading-` prefix (overview, architecture, conventions, safety, data formats, flows, metrics, glossary, roadmap, feature map), plus `common/` (the trading agent's design, the trading prompt, the strategy self-improvement templates), `how-to/` (go live with money, add a trading account, stop a trading agent, create a strategy or variant) and `index/` (the list of trading accounts). A domain also keeps `doc-outlines.md`, which says what the docs of each of its levels hold.

Its docs: each trading domain's own `docs/README.md`

### Names of strategies and trading agents

A trading agent's name starts with its strategy and ends with its AI model and its mode: `[strategy-id].[own-name]-v[N].[platform-model]-[test|live]`, for example `pm-strategy-1.momentum-v1.opus55-test`. The folder of a trading agent is named after it. A strategy agent's ID carries its main model and mode too, such as `pm-strategy-1-agent.opus55-test`, while its folder keeps a plain name such as `strategy-1-agent/`. Names are lowercase letters, digits, `-` and `.`, at most 64 characters. The rule that the name starts with the strategy is decided; the exact format is our proposal.

A changed setting, instruction or script makes a new trading agent and raises `v[N]`; a different model changes the model part. Names are never changed or reused, because test and live versions are different agents.

Its docs: `agents/trading/prediction-market/docs/trading-conventions.md`

### Accounts, keys and real money

A trading account is an account or wallet at a venue that a trading agent may use. Accounts are listed in the domain's trading settings, each with its id, venue, mode, whether it is funded, whether the owner approved it, the agent it is assigned to, its maximum capital and the names of its keys; the domain's `docs/index/` keeps a readable list of them.

Keys are kept like every key in the Agent OS: values only in the git-ignored `.env` files in `.secrets/test/` and `.secrets/live/`, known everywhere else by name only, with a prefix per account such as `POLYMARKET_ACCT1_API_KEY`. The system's `load-secret` script hands an account's keys to one process at a time and refuses live keys unless the owner approved the account.

Only the owner approves an account with real money, adds its live keys and changes the risk limits or the accounts. No agent approves an account, for itself or for another.

Its docs: `agents/trading/prediction-market/docs/trading-safety.md`

### Test and live

Every trading agent starts in test mode, including every version made by self-improvement. In test, orders are simulated at the price seen at decision time, or placed on a test network on blockchains. A trading agent goes live only when the owner has approved it and given it a funded, approved account. Every new strategy configuration starts only after the owner has read a report on it and approved it.

For now orders are placed only on blockchains, on any network and app; centralised exchanges and other apps are sources of information only. Every decision script checks the system's general stop switch and the domain's order stop switch before every order, in test and in live; both stop switches are our proposal, and what the order stop switch does with open positions is still open.

Its docs: `agents/trading/prediction-market/docs/how-to/go-live-with-money.md`

### Metrics and comparing versions

Trading agents are measured on money, on top of the system's cost, speed and error measures. We propose: realised and unrealised profit and loss and the return on capital, all from the order logs; win rate with its number of trades; the largest and the current fall from a peak; calibration, comparing the agent's forecasts with what happened and with the market price; and AI cost per trade. Versions of one strategy are compared over the same period and capital, in test against test. Which numbers decide success is still open.

Its docs: `agents/trading/prediction-market/docs/trading-metrics.md`

### Making a new trading domain

A new trading domain is a copy of the prediction-market domain, made when the owner asks. The system's `create-agent` script creates its domain agent and folders, never a copy by hand. The copy keeps the levels, the standard folders, the trading notes, the shape of the trading settings and the decision scripts, and changes what is its own: venues, fees, market filters, information sources, strategies and risk limits. It starts with no funded account. When two domains need the same trading part, that part can move up into `agents/trading/`; until then it stays in the domain.

Its docs: `agents/trading/docs/rebuild-prompt.md`

### The trading dashboard

`apps/trading-ui/` is planned as the prediction-market domain's dashboard: a page where the owner sees every trading agent and its results, approves real money, and stops or deletes agents. It stays in `apps/` and is empty for now; whether it is needed at all is still open.

Its docs: `apps/trading-ui/trading-ui.index.md`

## Where each part's docs are

| Part | Its docs | What they add |
|---|---|---|
| Trading's folder | `agents/trading/trading.index.md` | how the folder works, in short |
| Trading's docs | `agents/trading/docs/docs.index.md` | what each doc is for |
| Research studies | `agents/trading/researches/researches.index.md` | the studies and how they are used |
| Prediction-market domain | `agents/trading/prediction-market/docs/` | empty today; its vision, README and rebuild prompt in stage two |
| Trading notes (kept) | `agents/trading/prediction-market/docs/` | the trading rules, formats, flows and metrics in full |
| Trading dashboard | `apps/trading-ui/trading-ui.index.md` | the planned dashboard |
| The system above | `agents/system/docs/README.md` | everything every agent shares |

## Still open in the design

- **Trading folder:** which parts move up into `agents/trading/` once there are two trading domains.
- **Domains:** which trading domain comes next and when; copy trading is the likely one.
- **Names:** whether `v[N]` belongs to the trading agent or to the strategy; whether strategy folders carry the model and mode too; the shorter form `strategy-1/strategy-1.v1.Claude-Opus5.5/` that has come up for folder names.
- **Safety:** what the order stop switch does with open positions; the capital limits of the first live accounts; how account entries map to key prefixes.
- **Metrics:** which numbers decide success; where positions are kept; where market outcomes are recorded.
- **Self-improvement:** whether a strategy may fold a winning change into itself, or retire losing versions, without the owner.
- **Owner:** the channel for trade alerts.
