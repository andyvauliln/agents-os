---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/research/subagents.link/
node: n-21.13.3
basis: 72c17dbe22d0
written: 2026-10-01T00:59:34Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# subagents.link/

## Summary

The strategy's child links for research: one folder link per trading variant, pointing at that variant's `research/`. Through them the strategy session and its self-improvement sub-agent read each variant's own research next to the strategy's. `relink` builds the entries from the folder tree and removes them when a variant is deleted; they are read-only and never followed recursively.
