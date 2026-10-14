---
about: agent-os/agents/system/data/subagents.link/[domain-name]/
node: n-16.4.1
basis: feb87ea8a8d0
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# [domain-name]/

## Summary

One folder link per domain, named after the domain's folder and pointing at that domain's `data/` [19.5]. Through it the system and the UI reach the domain's data and, one `subagents.link/` further down, the data of the levels below it. It is read-only, built by relink from the folder tree, listed in no links file, and removed when the domain goes.
