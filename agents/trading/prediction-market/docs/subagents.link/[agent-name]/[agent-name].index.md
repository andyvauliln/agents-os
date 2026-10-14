---
about: agent-os/agents/trading/prediction-market/docs/subagents.link/[agent-name]/
node: n-19.6.1.1
basis: eb1ec6ec4f41
written: 2026-10-01T00:55:20Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# [agent-name]/

## Summary

One folder link per strategy, named after the strategy's folder (for example `strategy-1-agent/`), pointing at that strategy's `docs/`. Through it the domain reads the strategy's docs without copies, and reaches its variants' `docs/` one `subagents.link/` further down. Relink builds and removes it from the folder tree; it is read-only and never listed in a links file.

## Keep in mind

- When you need a strategy's files changed, leave it to the strategy; the domain writes only its own files.
