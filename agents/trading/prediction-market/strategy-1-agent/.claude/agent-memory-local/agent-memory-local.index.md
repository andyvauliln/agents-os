---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/.claude/agent-memory-local/
node: n-21.1.13
basis: 86b495817bf8
written: 2026-10-01T00:54:10Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# agent-memory-local/

## Summary

Machine-local memory for strategy sub-agents that use `memory: local`. It is git-ignored local tool state, so its content stays on the machine that wrote it. No strategy sub-agent uses it yet.

## Keep in mind

- When you need memory that survives a fresh clone or is shared, use `agent-memory/` instead.
