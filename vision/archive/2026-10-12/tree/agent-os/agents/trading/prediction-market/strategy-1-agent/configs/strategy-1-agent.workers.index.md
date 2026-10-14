---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/configs/strategy-1-agent.workers.json
node: n-21.2.1
basis: ccf115ceccb1
written: 2026-10-01T00:55:34Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# strategy-1-agent.workers.json

## Summary

The strategy agent's jobs file: everything the strategy runs, in the shared workers format. The example holds three jobs: the daily strategy session (an `agent` run of [21.1.5]), `compare-variants` after it, which writes the variant report to `data/`, and the nightly self-improvement sub-agent run that creates new test variants. The owner turns jobs on or off and moves their times here; runtime state goes to the scheduler state and job logs, never into this file. Its format is proposed.

## Keep in mind

- When you pause a job, set `enabled: false`; never delete it.
