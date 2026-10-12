---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/risk-check.decision.link.js
node: n-30.1
basis: e647a3bae6fc
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# risk-check.decision.link.js

## Summary

A read-only file link to the domain's shared risk check `scripts/decisions/risk-check.decision.js` [14.3], so every trading agent of the domain uses one copy and gets every fix at once. The decision script [33] calls it before every order: both stop switches first, then the domain's global, per-agent and per-venue caps as tightened by the agent's config, and for live the allowlist and an owner-approved account. A failed check blocks the order and alerts the owner (proposed).

## Keep in mind

- When you want stricter limits for this agent, tighten `capital_and_risk` in its config; never copy or edit the shared check through this link.
