---
about: agent-os/agents/trading/prediction-market/docs/trading-overview.md
node: n-19.6.5
basis: e0b1ff31142d
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# trading-overview.md

## Summary

The trading layer of the system's `overview.md`, read together with it: the trading rules to keep in mind, the idea in one paragraph, the domain's strategy and trading-agent levels, its config and dashboard, a diagram of the domain, how a trading run places orders, how the strategy loop improves strategies, going live with money, and a table of where each trading note lives. A later trading domain copies it.

## Keep in mind

- When you change a trading agent's config, prompt, code or model, make it a new test variant with a new name; never change a running variant in place.
- When you want an agent to trade with real money, leave the approval to the owner: only they approve an account with money.
