---
about: agent-os/agents/system/research/subagents.link/
node: n-10.9.3
basis: 07477b4bf368
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# subagents.link/

## Summary

The system's view of its domains' research: one folder link per domain, each pointing at that domain's `research/`. The system's self-improvement helper and the UI read the domains' research through it, going down one `subagents.link/` at a time. Relink builds and removes these links from the folder tree; they are read-only and listed in no links file.

## Keep in mind

- When you need to add to a domain's research, write it in the domain's own `research/`; these links are read-only.
