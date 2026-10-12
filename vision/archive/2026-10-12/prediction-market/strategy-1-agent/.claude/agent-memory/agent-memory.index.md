---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/.claude/agent-memory/
node: n-21.1.12
basis: 646f892106b5
written: 2026-10-05T13:25:49Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:05:50Z
---
# agent-memory/

## Summary

Committed memory for the strategy's sub-agents that use `memory: project`, one folder per sub-agent with a `MEMORY.md`. The main one belongs to the self-improvement sub-agent, `pm-strategy-1-self-improvement-agent/MEMORY.md`: it reads it first on each nightly run so it does not repeat work, and saves one-line lessons and research item ids there. The research itself stays in `research/` [21.13], tests in `tests/`, and the cross-variant history in `data/` [21.5].

## Keep in mind

- When you close a research item, save only its id and a one-line lesson here.
