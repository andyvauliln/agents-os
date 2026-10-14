---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/research/index.json
node: n-21.13.1
basis: ddc9a0a0f7c0
written: 2026-10-01T00:59:34Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# index.json

## Summary

The strategy's research history: one entry per item, `r-NNNN`, with its question, status (`planned`, `running`, `done`, `abandoned`), who asked and who ran it, a short result, the decisions taken and what it led to (`related` variants, changes and tests). The self-improvement sub-agent writes most items, one per proposed change, and reads the index first so no work is repeated; the UI shows it. The fields are proposed.

## Keep in mind

- When you start research, read this index first and add the item before you run anything.
- When you close an item, fill `results_summary`, `decisions` and `related`, and set the status to `done` or `abandoned`.
