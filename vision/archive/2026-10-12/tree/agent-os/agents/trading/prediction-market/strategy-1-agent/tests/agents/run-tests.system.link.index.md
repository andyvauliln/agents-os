---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/tests/agents/run-tests.system.link.js
node: n-21.12.1.3
basis: a4f4a0c917bf
written: 2026-10-01T00:58:25Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# run-tests.system.link.js

## Summary

A link to the shared `run-tests` script. Called from `tests/agents/`, it presets the agent kind and runs the tests listed in this folder's `tests.config.json`, e.g. `node tests/agents/run-tests.system.link.js --id t-agents-001`. Results go back into the config and to the strategy's `logs/tests.jsonl`. `create-agent` adds it when it scaffolds the agent.
