---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/configs/subagents.link/[agent-name]/
node: n-21.2.2.1
basis: 1c41181f59e9
written: 2026-10-01T00:55:34Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# [agent-name]/

## Summary

One folder link per trading variant of the strategy, named after the variant (e.g. `pm-strategy-1.momentum-v1.opus55-test/`) and pointing at that variant's `configs/`. Through it the strategy reads each variant's config, jobs and links files; it never writes there. `relink` makes the link when the variant is created and removes it when the variant is deleted.

## Keep in mind

- When you want to change a variant's config, make a new test variant instead of editing through this link.
