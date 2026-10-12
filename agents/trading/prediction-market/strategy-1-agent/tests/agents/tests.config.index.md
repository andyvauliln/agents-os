---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/tests/agents/tests.config.json
node: n-21.12.1.1
basis: 330fc731adf4
written: 2026-10-01T00:58:25Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# tests.config.json

## Summary

The list of every test of the strategy's prompt and sub-agents, with the owner's on or off switch per test. Each entry names its target, file, schedule (`manual`, `on_change`, `interval:[x]`, `before_promote`) and owner; `run-tests` writes back the last run, result, duration and fail count, and a failure gets a `next_action`. `create-agent` scaffolds it empty. The field names are proposed.

## Keep in mind

- When you add a test, add its entry here and leave the state fields to `run-tests`.
