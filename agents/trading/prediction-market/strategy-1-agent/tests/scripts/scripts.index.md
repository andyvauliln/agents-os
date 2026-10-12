---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/tests/scripts/
node: n-21.12.2
basis: 4d787c32d3a0
written: 2026-10-01T00:58:25Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# scripts/

## Summary

Tests of the strategy's code: its own scripts and the shared scripts it links. It holds one node or pytest file per test, running on fixtures with no network and no secrets, the `tests.config.json` that lists them with the owner's on or off switch and last results, and a runner link to the shared `run-tests`. No test is written yet.
