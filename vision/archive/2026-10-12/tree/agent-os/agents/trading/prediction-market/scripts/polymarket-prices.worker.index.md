---
about: agent-os/agents/trading/prediction-market/scripts/polymarket-prices.worker.py
node: n-19.3.5
basis: d25ca1900849
written: 2026-10-07T14:13:07Z
by: knowledge-base-agent
---
# polymarket-prices.worker.py

## Summary

The domain's Polymarket price collector, moved here from the system: it runs on a schedule as one of the domain's jobs and writes prices and volume for the active markets to `data/polymarket-prices/`, with its run logs in `logs/jobs/polymarket-prices/`. Trading agents link its `latest.json`.
