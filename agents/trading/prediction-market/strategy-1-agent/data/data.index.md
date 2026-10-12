---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/data/
node: n-21.5
basis: 73d6ab09538f
written: 2026-10-01T00:56:59Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# data/

## Summary

The strategy agent's own data, where the strategy loop keeps its results. It holds the daily variant report `variant-report/latest.json` and `latest.md` from `compare-variants`, one row per variant with its change, metrics, role (champion, challenger, retiring) and verdict, and the cross-variant history `changes.md`, one entry each time a variant is created, retired or folded back. The self-improvement sub-agent reads both before new work; the domain's SI sub-agent and the UI read the report. `subagents.link/` shows every variant's data. Both files are proposals. Content here is git-ignored; open: whether `changes.md`, being history, needs an exception or a backup.

## Keep in mind

- When you create, retire or fold back a variant, add an entry to `changes.md` here.
- When you compare variants, use the same window, capital and mode, and write "not enough data" instead of a win below the minimum sample.
