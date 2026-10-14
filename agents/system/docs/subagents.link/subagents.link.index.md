---
about: agent-os/agents/system/docs/subagents.link/
node: n-2.20
basis: a9bb7dc8a733
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# subagents.link/

## Summary

The system's view of its domains' docs: one folder link per domain, each pointing at that domain's own `docs/`. Each domain's docs link on to the levels below it, so every agent's docs can be read from here one level at a time, without copies. `relink` adds a link from the folder tree when a domain is set up and removes it after a stop or delete. The UI, the system session, self-improvement helpers and the knowledge agent read through it; nothing writes into it.

## Keep in mind

- When you scan the docs, never follow these links recursively; go down one `subagents.link/` at a time and read real files only.
- When a domain is added or removed, let `relink` make or remove its link; never create one by hand or list it in a links file.
