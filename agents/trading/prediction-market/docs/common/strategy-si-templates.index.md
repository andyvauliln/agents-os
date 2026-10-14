---
about: agent-os/agents/trading/prediction-market/docs/common/strategy-si-templates.md
basis: f2c93af3887d
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# strategy-si-templates.md

## Summary

The templates the domain's self-improvement sub-agents are built from, the trading layer of the system's SI templates: the trading lines of the base template, the domain template (compare strategies, propose new ones) and the strategy template with the variant loop, where a strategy proposes one change, creates it as a test variant, tests and compares it, then folds a winner back or retires it. Whether an SI sub-agent may retire variants itself is open.

## Keep in mind

- When you try a change as an SI sub-agent, make it a new test variant through create-agent; never touch live agents or raise a risk cap.
