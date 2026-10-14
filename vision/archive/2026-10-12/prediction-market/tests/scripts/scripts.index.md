---
about: agent-os/agents/trading/prediction-market/tests/scripts/
node: n-19.12.2
basis: 04f74b3b6e9e
written: 2026-10-01T00:58:18Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# scripts/

## Summary

The domain's script tests: checks of the domain's own scripts. It holds `tests.config.json` (the same fields as the agent tests), one `[test-id].test.js` or `.py` file per test, run by node or pytest on fixture data with no network and no secrets, and `run-tests.system.link.js`, the runner link that presets kind `scripts`. Results go back into the config and to the domain's `logs/tests.jsonl`. The fields are proposed.

## Keep in mind

- When you add a test of the prompt or a sub-agent, put it in `tests/agents/`, not here.
