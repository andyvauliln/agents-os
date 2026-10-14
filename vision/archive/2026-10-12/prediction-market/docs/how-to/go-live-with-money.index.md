---
about: agent-os/agents/trading/prediction-market/docs/how-to/go-live-with-money.md
node: n-19.6.17.2
basis: c12aea3bd89d
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# go-live-with-money.md

## Summary

The runbook for giving a test trading agent real money, the trading steps added to the system's `how-to/promote-to-live.md`. The variant must meet the promotion rules in `trading-metrics.md`, and the strategy or its SI proposes it; only the owner approves, funds an account, adds its live keys and marks it funded and approved in the domain config. Then its orders are watched through the order log and notifications. The steps are proposed.

## Keep in mind

- When you prepare a promotion, only propose it; only the owner approves an account with real money.
- When you take an agent live, check its risk caps are no looser than the domain config's and the order stop switch is off.
