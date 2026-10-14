---
about: agent-os/agents/trading/prediction-market/.claude/agent-memory-local/
node: n-19.1.13
basis: 86b495817bf8
written: 2026-10-01T00:53:39Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# agent-memory-local/

## Summary

The memory of domain sub-agents that use `memory: local`: the same as `agent-memory/`, but machine-local tool state that is git-ignored and never committed. It is part of the standard `.claude/` every level has.

## Keep in mind

- When you need a sub-agent's memory kept in git, use `memory: project` and `agent-memory/` instead.
