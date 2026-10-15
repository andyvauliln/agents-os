---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/tests/subagents.link/
node: n-21.12.3
basis: 6dc54b7bc230
written: 2026-10-01T00:58:25Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# subagents.link/

## Summary

The strategy's child links for tests: one folder link per trading variant, pointing at that variant's `tests/`. Through them the strategy session and its self-improvement sub-agent see each variant's tests and last results, such as whether a challenger's tests for its change pass. `relink` builds the entries from the folder tree and removes them when a variant is deleted; they are read-only and never followed recursively.
