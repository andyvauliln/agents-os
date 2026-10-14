---
about: agent-os/agents/system/docs/common/agent-architecture.md
node: n-2.17.1
basis: 19dcef57461a
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# agent-architecture.md

## Summary

How one agent works inside, the same at every level: the parts of the standard folder, the run loop (read what is new, analyse, decide, act), how a run starts, sub-agents and their results as linked data files, memory, and how an agent gets data through read-only file links. A domain adds its own layer, as the prediction-market domain does for trading agents. Still open: how `CLAUDE.md` uses the common prompt, and how "new since the last run" is tracked.

## Keep in mind

- When you store an agent's memory, keep lessons and pointers only; research goes to `research/` and change records to `docs/changes.md` (proposed rule).
