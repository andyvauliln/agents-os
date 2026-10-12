---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/scripts/[test-id].test.[js|py]
node: n-49.2.2
basis: 33c78a830ca8
written: 2026-10-01T01:02:00Z
by: summary-worker
confirmed: 2026-10-12T11:29:26Z
---
# [test-id].test.[js|py]

## Summary

One script test per file, named after its id, such as `t-scripts-001.test.js` or `.py`. It is a normal node or pytest file that checks one of the agent's own or linked scripts on fixture data. Each test has an entry in this folder's `tests.config.json`, and `run-tests` runs it from there. The format is proposed.

## Keep in mind

- When you write a script test, use fixture data only: no network and no secrets.
