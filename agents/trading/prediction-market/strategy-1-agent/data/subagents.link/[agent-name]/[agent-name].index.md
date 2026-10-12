---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/data/subagents.link/[agent-name]/
node: n-21.5.1.1
basis: 06d15134a72a
written: 2026-10-01T00:56:59Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# [agent-name]/

## Summary

One folder link per trading variant, named after the variant and pointing at that variant's `data/`. The strategy reads each variant's outputs here when it compares variants; it never writes there. `relink` makes the link when the variant is created and removes it when the variant is deleted.
