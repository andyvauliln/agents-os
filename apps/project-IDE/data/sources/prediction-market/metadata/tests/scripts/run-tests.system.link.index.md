---
about: agent-os/agents/trading/prediction-market/tests/scripts/run-tests.system.link.js
node: n-19.12.2.3
basis: c0dd1560e28f
written: 2026-10-01T00:57:42Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# run-tests.system.link.js

## Summary

A file link to the shared `run-tests` script. Run from here as `node tests/scripts/run-tests.system.link.js`, it presets kind `scripts` and this folder's `tests.config.json`, runs every enabled test or the one named with `--id`, and writes the results back to the config and to the domain's `logs/tests.jsonl`. `create-agent` adds this link at every level, and relink builds it.
