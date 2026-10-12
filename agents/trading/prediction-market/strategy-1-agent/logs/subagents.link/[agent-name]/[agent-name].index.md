---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/logs/subagents.link/[agent-name]/
node: n-21.4.1.1
basis: d6e61e73fb49
written: 2026-10-01T00:56:59Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# [agent-name]/

## Summary

One folder link per trading variant, named after the variant and pointing at that variant's `logs/`: its per-run inputs, reasoning, decisions, actions and cost. The strategy reads them here when it compares variants; it never writes there. `relink` makes the link when the variant is created and removes it when the variant is deleted.
