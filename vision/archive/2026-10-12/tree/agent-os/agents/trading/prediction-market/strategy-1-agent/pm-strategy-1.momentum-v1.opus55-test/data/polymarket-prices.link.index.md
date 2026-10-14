---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/data/polymarket-prices.link.json
node: p-agent-os-agents-trading-prediction-market-strategy-1-agent-pm-strategy-1.momentum-v1.opus55-test-data-polymarket-prices.link.json
basis: 39e586258ff9
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# polymarket-prices.link.json

## Summary

A read-only file link to the `latest.json` of its domain's price collector `polymarket-prices`, in the domain's `data/polymarket-prices/`, with rows of `market`, `question`, `price_yes`, `volume_usd` and `ts`. The agent reads current prices from it, and the metrics use it to mark open positions for unrealised PnL (proposed). The link stays valid while the collector replaces `latest.json`. Relink builds it from the links file.
