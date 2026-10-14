---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/clean-data.system.js
node: n-32
basis: a498395aaf6a
written: 2026-10-01T00:56:59Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# clean-data.system.js

## Summary

The agent's own system script that cleans and normalises the raw data its worker fetched, before the agent reads it. It runs right after the worker [31] and writes a cleaned file, such as `clean.json`, next to the raw one in `data/get-polymarket-data/` (proposed). The `.system.` suffix marks it as machinery, not a worker or a decision script. Still open: whether it stays agent-local or moves to the shared system scripts [14.1].
