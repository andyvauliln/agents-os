---
about: agent-os/agents/system/tests/subagents.link/[domain-name]/
node: n-10.8.3.1
basis: 181c93538151
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# [domain-name]/

## Summary

One folder link per domain, named after the domain's folder and pointing at that domain's `tests/` [19.12]. Through it the system sees the domain's test configs and results and, one `subagents.link/` further down, those of the levels below it. It is read-only, built by relink from the folder tree, listed in no links file, and removed when the domain goes.
