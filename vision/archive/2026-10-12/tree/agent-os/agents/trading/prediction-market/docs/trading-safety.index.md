---
about: agent-os/agents/trading/prediction-market/docs/trading-safety.md
node: n-19.6.8
basis: 55d624946af3
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# trading-safety.md

## Summary

The domain's money rules, the trading layer of the system's `safety.md` and shared mechanics: only the owner approves an account with real money; a live order needs a funded, owner-approved account; risk caps sit in the domain config, are enforced in code and may only be tightened below; the order stop switch refuses orders and winds trading down; plus account keys and what self-improvement may change. It changes only on an explicit owner decision.

## Keep in mind

- When you add a risk limit, enforce it in the decision and risk-check scripts, never only in a prompt.
- When you set a cap in an agent's config, only tighten the domain's cap; a looser value is ignored.
- When you write a script that places orders, check the general stop switch and the order stop switch before every order, in test and in live.
- When you want to change this note or the domain config's risk, accounts or order stop switch, get the owner's approval first.
