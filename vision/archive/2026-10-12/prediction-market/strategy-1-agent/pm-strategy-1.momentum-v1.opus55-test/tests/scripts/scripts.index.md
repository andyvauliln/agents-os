---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/scripts/
node: n-49.2
basis: 5ba21e0b2da6
written: 2026-10-01T01:02:00Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# scripts/

## Summary

Tests of the agent's code: its own scripts and the shared scripts it links. Each test is a node or pytest file [49.2.2] that runs on fixture data with no network and no secrets, with an entry in `tests.config.json` [49.2.1], where the owner turns it on or off. The runner link [49.2.3] runs them through the shared `run-tests`, which writes the results back into the config and into `logs/tests.jsonl`. The example test checks that `make-buy` keeps to the maximum position size. The fields and file format are proposed.

## Keep in mind

- When you test code, put the test here; tests of the prompt or sub-agents go in `tests/agents/`.
