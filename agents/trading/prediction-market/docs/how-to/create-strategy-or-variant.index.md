---
about: agent-os/agents/trading/prediction-market/docs/how-to/create-strategy-or-variant.md
node: n-19.6.17.1
basis: 8740f00afb25
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# create-strategy-or-variant.md

## Summary

The runbook for creating a strategy or a variant, the trading steps added to the system's `how-to/create-agent.md`. Most new variants come from a strategy's self-improvement sub-agent; the name starts with the strategy's ID, the config may only tighten the domain's risk caps, funding is tracked in `index/accounts.md`, and a variant from the loop gets a research item and a line in the strategy's history. The steps are proposed.

## Keep in mind

- When you create a variant, check its name starts with its strategy's ID and its platform/model part matches its route.
