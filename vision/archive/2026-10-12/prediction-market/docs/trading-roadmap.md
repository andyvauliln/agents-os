# Agent OS, prediction-market domain: Trading roadmap (v0.1)

The trading layer of the system's roadmap: the trading decisions done so far, the domain's next and later steps (MVP strategies, the price collector, a first trading UI, live trading with money), and the open trading design questions. Read it together with the system's `roadmap.md`, which holds the phase, the general decisions and the general questions; a later trading domain copies it. One line per item. Decision texts and dates are in decisions.md; the owner's own trading questions are in `trading-vision-notes.md`.

## Done so far
Trading decisions. The general ones are in the system's `roadmap.md`.

### Sub-agents and self-improvement
<!-- k: id=tr-road-done-subagents applies=[19.6.13] sources=D-008,D-018,D-026,D-032,D-056 status=decided -->
- D-032: the strategy agent creates, tests and compares its own variants and folds winners back.

### Names
<!-- k: id=tr-road-done-names applies=[19.6.13] sources=D-012,D-032,D-056 status=decided -->
- D-032: variant names start with their strategy; the strategy agent's ID carries its platform/model and mode.

## Next
<!-- k: id=tr-road-next applies=[19.6.13] sources=in-20260929-1452,in-20260929-1455,in-20260929-1537,derived,D-056 status=proposed -->
- Pick the MVP strategies for Polymarket (`trading-vision-notes.md` `vis-q-mvp`).
- The domain's part of the repo skeleton: the prediction-market domain, one strategy, one test variant.
- Run the Polymarket price collector [19.3.5] and the first variant in test mode.
- A first trading UI: agent list, logs, performance, approvals (the domain's dashboard [45]).

## Later
<!-- k: id=tr-road-later applies=[19.6.13],[19.2.4],[47.2.1] sources=in-20260929-1455,in-20260929-1537,in-20260930-0812,D-027,D-056 status=decided -->
- More trading domains (crypto, content-driven, combinations), each copied from this one when needed (D-056).
- Live trading: funded accounts, owner approval for every live account (live keys in `live/.env`: the system's roadmap).

## Biggest open questions
The open trading design questions, grouped by area, one per entry. The owner's own trading questions (MVP strategies, real money, venues, the Polymarket suite, self-improvement scope and metrics) are in `trading-vision-notes.md`.

### Names

#### Whose version is v[N]
<!-- k: id=road-q-version-owner applies=[23],[21] sources=D-032,in-20260930-1453-2,D-056 status=open -->
Does `v[N]` belong to the variant name or to the strategy (`strategy-1` becoming `strategy-1-v2`)?

#### Suffixes on the strategy folder
<!-- k: id=road-q-strategy-folder-suffix applies=[21] sources=D-032,in-20260930-1453-2,D-056 status=open -->
Should the strategy folder carry `.[platform-model]-[test|live]` too, or only its ID in config and the index?

#### A real strategy name
<!-- k: id=road-q-strategy-folder-name applies=[21] sources=derived,D-056 status=open -->
Should the strategy folder carry a real strategy name (e.g. `market-making/`) instead of `strategy-1-agent/`?

#### What makes a new variant
<!-- k: id=road-q-new-variant applies=[27.3],[27.4] sources=D-012,D-031,D-056 status=open -->
Is a link change or a small job change a new variant (new `v[N]`), or may it happen in place?

### Agents and runs

#### Who decides a trade
<!-- k: id=road-q-decision-maker applies=[33] sources=in-20260929-1452,D-056 status=open -->
Is a trading decision made by code, by the LLM, or both (the LLM proposes, code enforces the limits)?

#### Retiring variants
<!-- k: id=road-q-si-retire applies=[21.1.1.1] sources=D-032,D-056 status=open -->
May the strategy's SI sub-agent retire variants on its own, or only create them?

#### The strategy definition
<!-- k: id=road-q-strategy-definition applies=[21],[21.6] sources=derived,D-056 status=open -->
Where is the strategy definition kept: as a skill in [21.1.2], or in `docs/` [21.6] (proposed)?

### Data and logs

#### Positions
<!-- k: id=road-q-positions applies=[35] sources=in-20260929-1452,D-056 status=open -->
Where do the portfolio and positions live: in the agent's `data/`, or in a ledger?

### Tests and research

#### Backtests
<!-- k: id=road-q-backtest applies=[49],[50] sources=D-025,D-056 status=open -->
Is a backtest a test, a research item, or both (research runs it, a test guards the result)?

### The dashboard

#### UI access
<!-- k: id=road-q-ui-access applies=[45] sources=in-20260929-1455,D-056 status=open -->
Does the UI read the files directly or through an API layer, and how is it reached (local only, with auth)?

### Venues and apps

#### Prediction-market venues
<!-- k: id=road-q-pm-venues applies=[19] sources=derived,D-056 status=open -->
Polymarket only, or Kalshi and other venues too?

#### The Polymarket suite as a forked app
<!-- k: id=road-q-pm-suite-app applies=[43],[19] sources=D-055,D-056 status=open -->
Does the Polymarket suite v2 (`trading-vision-notes.md` `vis-q-polymarket-suite`) come in as a forked app in `apps/` [43]? Moved here from the open questions of [43].

## Changelog
- v0.1 (2026-10-07): created from the trading parts of the system's `roadmap.md` v0.1 (D-056, D-058); eleven trading questions moved here whole; the Polymarket suite question added from the tree notes of [43] (`road-q-pm-suite-app`).
