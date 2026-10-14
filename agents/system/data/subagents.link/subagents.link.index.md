---
about: agent-os/agents/system/data/subagents.link/
basis: fe4ebcdfeff2
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:09:25Z
---
# subagents.link/

## Summary

The system's view of its domains' data: one folder link per domain, each pointing at that domain's `data/`. The UI reads every agent's results through it one level at a time, without copies. Relink builds and removes these links from the folder tree; they are read-only and listed in no links file.

## Keep in mind

- When you scan data, never follow these links recursively; go down one `subagents.link/` at a time.
