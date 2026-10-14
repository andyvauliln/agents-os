---
about: agent-os/agents/system/logs/subagents/[subagent]/
basis: 981c7ce4dc3d
written: 2026-10-01T00:58:18Z
by: summary-worker
confirmed: 2026-10-14T15:07:13Z
---
# subagents/[subagent]/

## Summary

One log folder per system sub-agent, named after it, such as `news-digest`. Each call is one JSONL line: time, sub-agent, model, number of input files, output path, duration, cost and status. The cost of a shared sub-agent counts to the level that runs it, not to its readers (still open). The format is proposed.

## Keep in mind

- When you log a call's cost, name the field `cost_usd`; the drafts' `usd` does not match the other logs.
