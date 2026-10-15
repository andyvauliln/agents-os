---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/run-tests.system.link.js
node: n-30.2
basis: 11659bc065c5
written: 2026-10-01T00:56:59Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# run-tests.system.link.js

## Summary

A read-only file link to the shared `run-tests` script [14.1]. Run from here (`node scripts/run-tests.system.link.js`, or `npm test`) it runs both kinds of this agent's tests, agent tests and script tests, from their `tests.config.json` files; the scheduler and the `before_promote` check use it too (proposed). It writes each result back into the config and one line per test to `logs/tests.jsonl` [34.2]. Tests always run in test mode, with no secrets.

## Keep in mind

- When you propose the agent for live, run it with `--schedule before_promote`: every enabled test must pass.
