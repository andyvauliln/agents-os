---
about: agent-os/agents/system/tests/scripts/
node: n-10.8.2
basis: a643e5872ffc
written: 2026-10-01T01:00:33Z
by: summary-worker
confirmed: 2026-10-07T19:02:04Z
---
# scripts/

## Summary

Tests of the system's scripts, which are the shared scripts in [14] that every agent uses through file links. Each test is a node or pytest file on fixture data, with no network and no secrets; `tests.config.json` lists them with their switches, schedules and results; `run-tests.system.link.js` runs this folder's tests. Results go back into the config and to `logs/tests.jsonl`. The formats are proposed.
