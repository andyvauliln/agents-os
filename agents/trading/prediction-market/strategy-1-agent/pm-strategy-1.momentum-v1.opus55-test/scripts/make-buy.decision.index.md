---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/make-buy.decision.js
node: n-33
basis: 3d31e8803082
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
---
# make-buy.decision.js

## Summary

The agent's only way to trade, called with one decision (market, action, size, price, probability, reason). It reads the mode from `effective-config.json`, test unless live-allowed, and calls the domain's risk check [30.1]: both stop switches first (the general one and the domain's order switch), then the risk caps; a failed check blocks the order. In test it records a simulated fill, in live a real order (proposed; no executor yet). Open: whether code, the model or both decide.

## Keep in mind

- When you change this script, keep both stop switches and the risk check in code before every order, in test and in live.
- When you give this script venue keys, take them from `load-secret` through `secret_keys`, never from code or the prompt.
