---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/scripts/run-tests.system.link.js
node: n-49.2.3
basis: c0dd1560e28f
written: 2026-10-01T01:02:00Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# run-tests.system.link.js

## Summary

A read-only file link to the shared `run-tests` script [14.1]. Because it sits in `tests/scripts/`, it runs only script tests and reads this folder's `tests.config.json`: `node tests/scripts/run-tests.system.link.js`, with `--id` for one test or `--schedule` to narrow the set. create-agent adds it and relink builds it, so a fix to the shared script reaches every agent at once.
