---
about: agent-os/agents/trading/prediction-market/.claude/agent-memory/
node: n-19.1.12
basis: f308737c4262
written: 2026-10-05T13:25:49Z
by: knowledge-base-agent
confirmed: 2026-10-07T18:57:42Z
---
# agent-memory/

## Summary

The persistent memory of the domain's sub-agents that use `memory: project`: one `MEMORY.md` per sub-agent, committed to git. The first planned one is the domain self-improvement sub-agent's, `pm-self-improvement-agent/MEMORY.md`. Memory holds only dated lessons and pointers such as a research item id. Research lives in `research/` and test state in `tests/`, and the SI reads its memory and `research/index.json` before new work so it does not repeat itself.

## Keep in mind

- When you save a lesson, write one line with the research item id; the research itself goes in `research/`.
