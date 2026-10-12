---
about: agent-os/agents/system/logs/subagents.link/[domain-name]/
node: n-15.5.1
basis: 1f3b94b11d13
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# [domain-name]/

## Summary

One folder link per domain, named after the domain's folder and pointing at that domain's `logs/` [19.4]. The UI and the system's sub-agents read the domain's logs through it and, one `subagents.link/` further down, those of the levels below it. It is read-only, built by relink from the folder tree, listed in no links file, and removed when the domain goes.
