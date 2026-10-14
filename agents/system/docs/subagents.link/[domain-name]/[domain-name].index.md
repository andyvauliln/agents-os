---
about: agent-os/agents/system/docs/subagents.link/[domain-name]/
node: n-2.20.1
basis: 31e9e5907dc6
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# [domain-name]/

## Summary

One folder link per domain, named after the domain's folder and pointing at that domain's own `docs/`, so the system can read the domain's docs, and from there those of the levels below it, without copies. It is read-only: the system writes only its own docs. `relink` builds it from the folder tree and removes it when the domain is gone; it is never listed in a links file.

## Keep in mind

- When you need a domain's docs, read them through this link; never write into it.
- When a domain is added or removed, let `relink` make or remove this link; never create it by hand.
