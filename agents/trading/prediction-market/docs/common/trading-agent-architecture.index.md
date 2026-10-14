---
about: agent-os/agents/trading/prediction-market/docs/common/trading-agent-architecture.md
basis: 5c34ea29ac92
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# trading-agent-architecture.md

## Summary

The trading layer of the system's `common/agent-architecture.md`: a trading agent's run may also buy, sell or sell all; it acts only through its decision scripts, which read the mode and call the shared risk check; and the history across a strategy's variants lives in the strategy's `data/`. Every trading agent links it as `trading-agent-architecture.link.md`. Still open: whether code or the model makes a trading decision, and where positions are kept.

## Keep in mind

- When you place an order for a trading agent, go through its decision scripts; never place one directly.
