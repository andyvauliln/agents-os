---
about: agent-os/agents/system/data/
node: n-16
basis: 66c4adae2f3e
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# data/

## Summary

The system's shared data, sorted by source, as JSON and Markdown files with no database. `system/` holds the machinery's state: every job's last and next run, and the links index of who reads which file. `workers/` holds the shared workers' outputs, each a dated file plus a stable `latest.*` that agents link; `subagents/` holds sub-agent digests, built once for many readers. Through `subagents.link/` the system and the UI reach each domain's data and the levels below. Each agent keeps its own data in its own `data/`. The content is git-ignored runtime output. Still open: how "new since the last run" is tracked.

## Keep in mind

- When you give an agent shared data, link the `latest.*` file through its links file; never copy it.
- When you add data, put it here only if agents in more than one domain use it; data one agent or one domain uses stays in its own folder.
