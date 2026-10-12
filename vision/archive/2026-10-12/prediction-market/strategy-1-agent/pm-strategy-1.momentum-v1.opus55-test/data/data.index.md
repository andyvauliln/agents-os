---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/
node: n-35
basis: abe5d9929376
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
---
# data/

## Summary

Everything the trading agent reads and makes as data. Its own outputs are real files, one folder per producer, such as `get-polymarket-data/` [35.2] from its worker, and (proposed) a metrics snapshot `metrics/latest.json` that the strategy uses to compare variants. Everything else comes in as read-only file links [35.1]: its domain's Polymarket prices and markets catalog, and the system's news digest. Each run reads what is new here. The strategy, and level by level the UI, see this folder through the strategy's `data/subagents.link/`. The contents are git-ignored. Still open: where positions live (here or in a ledger), and how "new since the last run" is tracked.

## Keep in mind

- When you write data, write only into your own producer folders; the links here are read-only.
- When you produce a file others may link, keep a stable `latest.*` next to the dated files.
