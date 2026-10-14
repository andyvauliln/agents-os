---
about: agent-os/agents/system/tests/subagents.link/
node: n-10.8.3
basis: 289ae5740f72
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# subagents.link/

## Summary

The system's view of its domains' tests: one folder link per domain, each pointing at that domain's `tests/`. The system, the UI and self-improvement helpers read the domains' test configs and results through it, going down one `subagents.link/` at a time. Relink builds and removes these links from the folder tree; they are read-only and listed in no links file.

## Keep in mind

- When you need to change a domain's test, change it in the domain's own `tests/`; these links are read-only.
