---
about: agent-os/agents/trading/prediction-market/logs/jobs/[job-id]/
node: n-19.4.2
basis: cd33758ae317
written: 2026-10-07T14:13:07Z
by: knowledge-base-agent
---
# jobs/[job-id]/

## Summary

The run logs of the domain's own jobs, one folder per job (for example `polymarket-prices` and `markets-catalog`): `history.jsonl` with one line per run and `latest.log` with the output of the last run, written by `run-job`. A trading agent links a worker's `latest.log` when it needs to see if its data is fresh.
