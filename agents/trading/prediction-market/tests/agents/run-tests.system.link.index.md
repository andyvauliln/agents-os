---
about: agent-os/agents/trading/prediction-market/tests/agents/run-tests.system.link.js
node: n-19.12.1.3
basis: a4f4a0c917bf
written: 2026-10-01T00:57:42Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# run-tests.system.link.js

## Summary

A file link to the shared `run-tests` script. Run from here as `node tests/agents/run-tests.system.link.js`, it presets kind `agents` and this folder's `tests.config.json`, runs every enabled test or the one named with `--id`, and writes the results back to the config and to the domain's `logs/tests.jsonl`. `create-agent` adds this link at every level, and relink builds it.
