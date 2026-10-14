---
about: agent-os/agents/trading/prediction-market/docs/common/trading-prompt.md
node: n-19.6.16.2
basis: 32398d4685a5
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# trading-prompt.md

## Summary

The trading layer of the common prompt: draft prompt text that the strategy manager and the trading agent add to the base prompt, section by section. It adds `trading-safety.link.md`, `trading-agent-architecture.link.md` and `strategy.md` to the read order, orders only through decision scripts, changes as new test variants, never raising a risk cap, and the order stop switch checked first. The text is proposed and changes only with the owner's approval.

## Keep in mind

- When you want to change this layer, get the owner's approval first; no agent changes it on its own.
