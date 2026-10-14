---
about: agent-os/agents/system/tests/scripts/tests.config.json
basis: 0b926e7a68a1
written: 2026-10-01T01:00:33Z
by: summary-worker
confirmed: 2026-10-14T15:07:13Z
---
# tests.config.json

## Summary

The list of every script test at the system level, with the same fields as the agent tests' config: an id like `t-scripts-001`, the target script, the test file, `enabled`, a schedule (`manual`, `on_change`, `interval:[x]`, `before_promote`) and an owner. `run-tests` writes back last run, result, duration and failure count, and a failure gets a `next_action`. The owner switches tests on or off in the UI. Field names are proposed.

## Keep in mind

- When you add a test, fill only its own fields; leave `last_run`, `last_result` and `fail_count` to `run-tests`.
