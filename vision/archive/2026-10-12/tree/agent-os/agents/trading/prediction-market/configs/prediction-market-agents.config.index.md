---
about: agent-os/agents/trading/prediction-market/configs/prediction-market-agents.config.json
node: n-19.2.4
basis: a3faef8d2f08
written: 2026-10-07T14:13:07Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:08:15Z
---
# prediction-market-agents.config.json

## Summary

The prediction-market domain's own settings: everything about money and markets that used to sit in the system's settings. It holds the risk limits for the whole domain and for each agent, the trading accounts with whether each is funded and approved by the owner, the venues with their fees and market filters, the currency, what the stop switch does to orders, positions and accounts, and the trade notifications. It is read after the system's settings and before each agent's own config, and a lower layer may only tighten a limit. Changes to risk or accounts need the owner's approval. The shape is still a proposal.

## Keep in mind

- When you change `risk` or `accounts`, get the owner's approval first and record it.
- When an agent's config sets a limit, it may only be tighter than the one here.
