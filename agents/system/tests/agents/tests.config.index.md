---
about: agent-os/agents/system/tests/agents/tests.config.json
node: n-10.8.1.1
basis: 330fc731adf4
written: 2026-10-01T01:00:33Z
by: summary-worker
confirmed: 2026-10-07T19:02:04Z
---
# tests.config.json

## Summary

The list of every agent test at the system level: tests of the system prompt and its sub-agents. Each entry has an id like `t-agents-001`, a target, the test file, `enabled`, a schedule (`manual`, `on_change`, `interval:[x]`, `before_promote`) and an owner. `run-tests` writes back last run, result, duration and failure count, and a failure gets a `next_action`. The owner switches tests on or off in the UI. Field names are proposed.

## Keep in mind

- When you add a test, fill only its own fields; leave `last_run`, `last_result` and `fail_count` to `run-tests`.
- When you see a test fail, write a `next_action` saying what should be done next.
