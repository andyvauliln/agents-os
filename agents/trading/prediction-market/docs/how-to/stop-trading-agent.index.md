---
about: agent-os/agents/trading/prediction-market/docs/how-to/stop-trading-agent.md
node: n-19.6.17.4
basis: 6e8a81caca0f
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# stop-trading-agent.md

## Summary

The runbook for stopping a trading agent, the trading steps added to the system's `how-to/stop-or-delete-agent.md`: for a live agent, close or flatten its open positions and have the owner set its account back to unfunded; for a variant retired by the strategy loop, record why in the strategy's research item and history. Whether a self-improvement sub-agent may retire variants on its own is still open. The steps are proposed.

## Keep in mind

- When you stop a live trading agent, check it has no open positions left.
