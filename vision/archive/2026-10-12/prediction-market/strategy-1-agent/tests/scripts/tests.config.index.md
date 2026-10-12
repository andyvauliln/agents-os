---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/tests/scripts/tests.config.json
node: n-21.12.2.1
basis: 08885feda81f
written: 2026-10-01T00:58:25Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# tests.config.json

## Summary

The list of every test of the strategy's own and linked scripts, with the same fields as the agent tests list: target, file, schedule, owner, the owner's on or off switch, and the last run, result and `next_action` that `run-tests` and the test's owner write back. `create-agent` scaffolds it empty; the SI sub-agent and the UI read it. The field names are proposed.

## Keep in mind

- When you add a test, add its entry here and leave the state fields to `run-tests`.
