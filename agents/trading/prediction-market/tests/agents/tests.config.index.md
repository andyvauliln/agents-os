---
about: agent-os/agents/trading/prediction-market/tests/agents/tests.config.json
node: n-19.12.1.1
basis: 330fc731adf4
written: 2026-10-01T00:57:42Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# tests.config.json

## Summary

The list of every agent test of the domain level, the tests that check the domain owner's prompt and the domain sub-agents. Each entry has an id like `t-agents-001`, its target and test file, `enabled` (the owner switches it in the UI), a schedule (`manual`, `on_change`, `interval:[x]` or `before_promote`) and an owner. The shared `run-tests` writes back the last run, result, duration and fail count, and a failure gets a `next_action`. The field names are proposed.

## Keep in mind

- When you add a test, give it a new `t-agents-NNN` id, unique in the domain and never reused, and leave the state fields to `run-tests`.
