---
about: agent-os/agents/trading/prediction-market/scripts/markets-catalog.worker.py
node: n-19.3.3
basis: 876f779994b2
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:08:15Z
---
# markets-catalog.worker.py

## Summary

The prediction-market domain's own worker: every hour, as the `markets-catalog` job in the domain's jobs file, it writes the catalogue of Polymarket markets the domain cares about to `data/markets-catalog/latest.json`. Proposed fields per market: id, question, category, liquidity, resolution time and whether it is tradable. The domain session reads it, and the strategy and every variant link it through `@domain`. Still open: whether market resolutions, needed for calibration, are added here or by a separate worker.
