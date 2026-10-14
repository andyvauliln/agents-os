---
about: agent-os/agents/system/tests/scripts/[test-id].test.[js-py]
basis: 674b4c90b427
written: 2026-10-01T01:00:33Z
by: summary-worker
confirmed: 2026-10-14T15:07:13Z
---
# [test-id].test.[js|py]

## Summary

One script test per file, named by its id (`t-scripts-NNN`): a normal node or pytest file that checks a system script on fixture data. Each has an entry in this folder's `tests.config.json`, and `run-tests` runs it from there. The format is proposed.

## Keep in mind

- When you write a script test, use fixture data only, with no network and no secrets.
