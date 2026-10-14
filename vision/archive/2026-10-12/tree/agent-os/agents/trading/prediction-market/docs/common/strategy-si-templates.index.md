---
about: agent-os/agents/trading/prediction-market/docs/common/strategy-si-templates.md
node: n-19.6.16.3
basis: 25a734c23a66
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# strategy-si-templates.md

## Summary

The templates the domain's self-improvement sub-agents are built from, the trading layer of the system's SI templates: the trading lines of the base template, the domain template (compare strategies, propose new ones) and the strategy template with the variant loop, where a strategy proposes one change, creates it as a test variant, tests and compares it, then folds a winner back or retires it. Whether an SI sub-agent may retire variants itself is open.

## Keep in mind

- When you try a change as an SI sub-agent, make it a new test variant through create-agent; never touch live agents or raise a risk cap.
