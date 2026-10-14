---
about: agent-os/agents/system/scripts/subagents.link/
basis: 260b791cfa2d
written: 2026-10-01T00:57:24Z
by: summary-worker
confirmed: 2026-10-14T15:09:25Z
---
# subagents.link/

## Summary

The system's view of its domains' scripts: one folder link per domain, each pointing at that domain's `scripts/`. The system, its sub-agents and the index builders read domain scripts through it, reaching deeper levels one `subagents.link/` at a time. Relink builds and removes these links from the folder tree; they are read-only and listed in no links file.

## Keep in mind

- When you need to change a domain's script, change it in the domain's own folder; these links are read-only.
