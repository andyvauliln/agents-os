---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/
node: n-49
basis: 03c34e10b03a
written: 2026-10-01T01:02:00Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# tests/

## Summary

The agent's tests, so every change by the owner, create-agent or the SI sub-agent can be checked before and after it runs. Every level has the same layout. `agents/` [49.1] tests the prompt and sub-agents by running Claude Code headless on fixtures; `scripts/` [49.2] tests code with node or pytest. Each has a `tests.config.json`, where the owner turns tests on or off, and a runner link to the shared `run-tests`; `scripts/run-tests.system.link.js` [30.2] runs both kinds for the scheduler, `before_promote` and `npm test`. Results go back into the configs and into `logs/tests.jsonl` [34.2]. Proposed: every enabled test must pass before promotion to live. Still open: whether a failing test also blocks runs, and whether a backtest is a test, a research item or both.

## Keep in mind

- When you change the prompt, a sub-agent or a script, add or update a test for that change.
- When you run tests, keep them in test mode with no secrets and no real orders.
