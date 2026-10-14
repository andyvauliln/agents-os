---
about: agent-os/agents/system/tests/scripts/
basis: 856710bf4d78
written: 2026-10-01T01:00:33Z
by: summary-worker
confirmed: 2026-10-14T15:07:13Z
---
# scripts/

## Summary

Tests of the system's scripts, which are the shared scripts in `scripts/` that every agent uses through file links. Each test is a node or pytest file on fixture data, with no network and no secrets; `tests.config.json` lists them with their switches, schedules and results; `run-tests.system.link.js` runs this folder's tests. Results go back into the config and to `logs/tests.jsonl`. The formats are proposed.
