---
about: agent-os/agents/trading/prediction-market/data/subagents.link/[agent-name]/
node: n-19.5.1.1
basis: 5c0b1650f24c
written: 2026-10-01T00:55:20Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# [agent-name]/

## Summary

One folder link per strategy, named after the strategy's folder (for example `strategy-1-agent/`), pointing at that strategy's `data/`. Through it the domain reads the strategy's data without copies, and reaches its variants' `data/` one `subagents.link/` further down. Relink builds and removes it from the folder tree; it is read-only and never listed in a links file.

## Keep in mind

- When you need a strategy's files changed, leave it to the strategy; the domain writes only its own files.
