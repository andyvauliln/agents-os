---
about: agent-os/agents/trading/prediction-market/tests/scripts/tests.config.json
node: n-19.12.2.1
basis: 08885feda81f
written: 2026-10-01T00:57:42Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# tests.config.json

## Summary

The list of every script test of the domain level, the tests that check the domain's own scripts. It has the same fields as the agent tests config: an id like `t-scripts-001`, target and test file, `enabled` (the owner switches it in the UI), schedule and owner, plus the last run, result, duration and fail count that `run-tests` writes back, and a `next_action` after a failure. The field names are proposed.

## Keep in mind

- When you add a test, give it a new `t-scripts-NNN` id, unique in the domain and never reused, and leave the state fields to `run-tests`.
