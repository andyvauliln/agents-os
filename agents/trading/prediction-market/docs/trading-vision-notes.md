# Agent OS, prediction-market domain: Trading vision notes (v0.1)

The trading layer of the system's technical vision notes `vision.md`: what the owner wants from trading, in their terms. It holds the trading parts of the agent folder, the agent types and the requirements, the trading domains and strategy examples, the trading UI and what trading acts on, the trading ideas still being weighed, and the trading questions. Read it together with `vision.md`; a later trading domain copies it.

## What it is
<!-- k: id=tr-vis-what-it-is applies=[19] sources=in-20260929-1452,in-20260929-1455,D-056 status=decided -->
General rule: see `vision.md` (What it is).

The owner's first picture was a personal system that runs hundreds of trading agents of different types across several domains, which differ by domain, strategy and configuration. Trading now lives in the prediction-market domain, and a later trading domain is copied from it (D-056).

## Building blocks (the owner's model)

### The agent folder (the owner's first list)
<!-- k: id=tr-vis-block-agent-folder applies=[23],[19.2.4] sources=in-20260929-1452,D-056 status=decided -->
The owner's full first list: one folder per agent with: config, common config, docs, logs, common prompt, agent prompt, memory, self-improvement strategy, list of workers and subscriptions, trading accounts, data, previous run and next runs info, current portfolio, analytics. Its trading items: trading accounts are now the domain's `accounts` [19.2.4]; the portfolio and analytics still have no home (`trading-roadmap.md`).

### Agent types
<!-- k: id=tr-vis-agent-types applies=[19.1.5],[21.1.1.1],[23] sources=in-20260929-1455,D-018,D-022,D-026,D-056 status=decided -->
The owner's types in trading terms:
- **Main agents** run a strategy and decide, in test or live mode. Now the trading variants under a strategy [23].
- **The main domain agent** finds, analyses, creates and updates strategies and their self-improvement agents, and makes sure the domain makes money.
- **The per-strategy self-improvement agent** is dynamic per strategy but built from shared templates. For a strategy it is [21.1.1.1] (D-018).

## Requirements for every trading agent
<!-- k: id=tr-vis-requirements applies=[19],[21],[23] sources=in-20260929-1452,D-056 status=decided -->
- Has backtesting where the strategy allows it.
- Its configurations also set the initial capital and the risk-management strategy.
- Purpose: run and compare many variants, combine strategies and approaches, keep what works.
- Strategy-specific parts sit on top of the shared base and the domain's parts.

## Domains and strategy examples
<!-- k: id=vis-domains applies=[4],[19] sources=in-20260929-1452,in-20260929-1455,D-056 status=decided -->
- **Prediction markets:** up to about 80 ways to make money, e.g. market making, analysing outcome probabilities, agents that model and simulate possible futures. The first domain (Polymarket, [19]).
- **Crypto and bitcoin trading:** technical trading and other approaches.
- **Content-driven:** take one YouTuber, extract everything they say, and trade on it.
- **Combinations:** blend strategies, e.g. combine the ones with the best win rates.
- More domains later; the vision may still change.

## The self-improvement wheel
<!-- k: id=tr-vis-wheel applies=[19.1.1.2],[21.1.1.1],[19.6.16.3],[19.6.6] sources=in-20260929-1455,in-20260930-1453-2,D-056 status=decided -->
For trading, the owner approves live funding, and the goal is strategies that are fast, cheap, efficient, simple, understandable and profitable, with bugs fixed and changes tested. The strategy agent runs this loop on itself through its variants (D-032): `trading-architecture.md` `arch-strategy-variants`.

## What the owner wants to see and do
<!-- k: id=tr-vis-ui applies=[45] sources=in-20260929-1455,D-056 status=decided -->
The owner first placed the UI in the trading UI [45] (Next.js API and UI, for monitoring and analysis of all agents and the system). [45] stays where the owner put it, as the prediction-market domain's dashboard (D-058). For trading, the owner approves or rejects giving an agent an account with money.

### What the system acts on
<!-- k: id=tr-vis-action-scope applies=[14.3],[47],[19.2.4] sources=in-20261001-1037,D-056 status=decided -->
Every action (buy, sell and others) supports test and live from the start; on blockchains test can use testnets and live the main networks. For now actions only on blockchains, any network and app; centralised exchanges and other apps are data sources only.

## Ideas under evaluation
These came from an earlier discussion (the first brief, section 5). They are not decisions: each is weighed on its own.

### Strategy vs instance
<!-- k: id=vis-idea-strategy-instance applies=[21],[23] sources=in-20260929-1452,D-056 status=proposed -->
Strategies are templates; instances are configured runs (strategy version, capital, risk policy, model, mode); experiments generate instances. The strategy agent with its variants (D-022, D-032) is close to this.

### Agents decide, a separate layer executes
<!-- k: id=vis-idea-executor applies=[33],[14.3] sources=in-20260929-1452,in-20261001-1037,D-056 status=proposed -->
Proposed, re-explained to the owner as problem and solution (in-20261001-1037): agents only write orders; one shared executor checks hard limits in code and places them in test or live. Every action already supports test and live from the start (D-035).

### A ledger owns the portfolio
<!-- k: id=vis-idea-ledger applies=[35] sources=in-20260929-1452,in-20261001-1037,D-056 status=proposed -->
Proposed, re-explained to the owner as problem and solution (in-20261001-1037): one ledger, written only by the order-placing part, holds every agent's positions, cash and history; agents read it. Where positions live is open: `trading-roadmap.md` `road-q-positions`.

### Not every strategy fits a periodic LLM loop
<!-- k: id=vis-idea-strategy-kinds applies=[21] sources=in-20260929-1452,in-20261001-1037,D-056 status=decided -->
Decided: a strategy can be plain code, AI or a mix. Market making and arbitrage need fast, event-driven code; other strategies gain from an AI's judgement.

### Champion and challenger
<!-- k: id=vis-idea-champion-challenger applies=[19.6.11],[21.1.1.1] sources=in-20260929-1452,D-056 status=proposed -->
Self-improvement produces challengers that are tested against the current champion before promotion, instead of an agent editing itself live. The strategy loop (D-032) is now scored this way: `trading-metrics.md` `metric-champion`.

### LLM backtests can leak
<!-- k: id=vis-idea-backtest-leak applies=[49],[50] sources=in-20260929-1452,in-20261001-1037,D-056 status=decided -->
Decided: every strategy may have its own back-testing approach with its own settings, where applicable (e.g. a month of old data replayed as if live). Caution kept: a model may already know past outcomes, so AI back-tests can look better than reality.

### Agents use other agents' data
<!-- k: id=tr-vis-idea-meta-agents applies=[19] sources=in-20260929-1452,in-20261001-1037,D-056 status=decided -->
Trading examples: a risk-management agent that tells every agent to sell everything on news of a collapse or a war. Ensembles and capital allocators fit here too.

## Principles the owner stated

### Test first, the owner approves money
<!-- k: id=tr-vis-principle-test-first applies=[19.2.4],[19.6.8],[45] sources=in-20260929-1455,D-056 status=decided -->
Only the owner approves giving an agent an account with money. Money rules: `trading-safety.md`.

## Open questions
The owner's trading questions from the first brief and their second input. Answered ones say where.

### First domain and MVP strategies
<!-- k: id=vis-q-mvp applies=[19] sources=in-20260929-1452,in-20260929-1455,in-20261001-1037,D-056 status=decided -->
Answered: the owner gives the first Polymarket strategy; the wheel starts with it (test mode, self-improvement), and more strategies follow once the flow works.

### Paper first, and when real money starts
<!-- k: id=vis-q-real-money applies=[19.2.4],[19.6.17.2] sources=in-20260929-1452,in-20261001-1037,D-056 status=open -->
Partly answered: real money starts after an agent and its strategy show good results, with the owner's approval per account. Open: capital limits for the first live accounts.

### Venues and accounts
<!-- k: id=vis-q-venues applies=[19.2.4],[47] sources=in-20260929-1452,in-20261001-1037,D-056 status=decided -->
Answered: each strategy gets its own venues and accounts, chosen while that strategy is built. For now actions only on blockchains (`tr-vis-action-scope`).

### The existing Polymarket suite v2
<!-- k: id=vis-q-polymarket-suite applies=[43] sources=in-20260929-1452,in-20261001-1037,D-056 status=decided -->
Answered: workers and data of the existing suite (liquidity provision, cross-platform arbitrage, resolution sniping, copy trading) are reused by strategies where they fit.

### Human approval and notifications
<!-- k: id=tr-vis-q-approvals applies=[19.6.8],[19.2.4] sources=in-20260929-1452,in-20260929-1455,in-20261001-1037,D-056 status=open -->
For trading, the owner approves live funding and every new strategy configuration (variant) after reading a report on it (D-035).

### What self-improvement may change, and how success is measured
<!-- k: id=vis-q-si-scope applies=[19.6.11],[21.1.1.1] sources=in-20260929-1452,in-20260929-1455,in-20261001-1037,D-056 status=open -->
Partly answered: self-improvement may change anything (config, prompts, code, model, platform); every new configuration needs the owner's approval before it runs. Open: the success metrics (PnL, win rate, drawdown, calibration).

### Keys and wallets
<!-- k: id=tr-vis-q-keys applies=[47] sources=in-20260929-1452,D-023,D-027,in-20261001-1037,D-056 status=open -->
On blockchains, test can use testnets. Wallet keys sit in the same store `.secrets/` as every other key (`vis-q-keys`).

### Full folder per variant or a thin folder over shared code
<!-- k: id=vis-q-variant-folder applies=[23] sources=in-20260929-1455,in-20260929-1703,D-020,D-022,D-056 status=decided -->
Answered: every variant is a full standard folder with its own real files and file links to the shared files it needs (D-022, D-020).

## Changelog
- v0.1 (2026-10-07): created from the trading parts of the system's `vision.md` v0.2 (D-056, D-058). Moved with their ids: `vis-domains`, `vis-idea-strategy-instance`, `vis-idea-executor`, `vis-idea-ledger`, `vis-idea-strategy-kinds`, `vis-idea-champion-challenger`, `vis-idea-backtest-leak`, `vis-q-mvp`, `vis-q-real-money`, `vis-q-venues`, `vis-q-polymarket-suite`, `vis-q-si-scope`, `vis-q-variant-folder`. The copy-trading plan was removed from `vis-domains` and `vis-q-mvp` (D-056).
