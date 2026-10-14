---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/scripts/tests.config.json
node: n-49.2.1
basis: d73250a151cc
written: 2026-10-01T01:02:00Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# tests.config.json

## Summary

The list of every script test in `tests/scripts/`, with the same fields as the agent tests' config [49.1.1]: id, name, target script, test file, `enabled`, `schedule`, `owner`, the state `run-tests` writes back (`last_run`, `last_result`, `last_duration_ms`, `fail_count`), and `notes` and `next_action`. The owner turns tests on or off here or in the UI. The example test `t-scripts-001` checks that `make-buy` respects the maximum position size; it failed, so it carries a next action. The field names are proposed.

## Keep in mind

- When you add a test, give it a new `t-scripts-NNN` id that is never reused, and leave the state fields to `run-tests`.
- When you find a failing test, write its `next_action` and `notes`.
