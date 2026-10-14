---
about: agent-os/agents/system/scripts/subagents.link/[domain-name]/
basis: 981c7ce4dc3d
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# [domain-name]/

## Summary

One folder link per domain, named after the domain's folder and pointing at that domain's `scripts/`. Through it the system reads the domain's own scripts and, one `subagents.link/` further down, those of the levels below it. It is read-only, built by relink from the folder tree, listed in no links file, and removed when the domain goes.
