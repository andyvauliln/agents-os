---
about: agent-os/agents/system/.claude/agent-memory/
node: n-10.1.12
basis: c0cefc10fb2d
written: 2026-10-05T13:25:49Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:02:04Z
---
# agent-memory/

## Summary

The committed memory of system sub-agents that use `memory: project`: one folder per sub-agent with a `MEMORY.md`. The system's self-improvement sub-agent keeps its memory here. Memory holds lessons and pointers only, such as a research id with a one-line lesson; the research itself lives in `research/` [10.9], test state in `tests/`, history in `data/`. Before new work, the sub-agent reads its memory and the research index so it does not repeat itself.

## Keep in mind

- When you finish research, save only the item id and a one-line lesson here; the research stays in `research/`.
