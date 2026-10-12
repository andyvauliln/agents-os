---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/agents/tests.config.json
node: n-49.1.1
basis: 068df00e6960
written: 2026-10-01T01:02:00Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# tests.config.json

## Summary

The list of every agent test in `tests/agents/`, and the switch the owner uses to turn each one on or off (here or in the UI). Each entry gives the test's id, name, target (`CLAUDE.md` or a sub-agent), file, `enabled`, `schedule` (`manual`, `on_change`, `interval:[x]` or `before_promote`) and `owner`. `run-tests` writes back `last_run`, `last_result`, `last_duration_ms` and `fail_count`; a failure gets `notes` and a `next_action`. create-agent creates it empty. The field names are proposed.

## Keep in mind

- When you add a test, give it a new `t-agents-NNN` id that is never reused, and leave the state fields to `run-tests`.
- When you find a failing test, write its `next_action` and `notes`.
