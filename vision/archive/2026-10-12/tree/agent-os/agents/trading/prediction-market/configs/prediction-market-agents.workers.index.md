---
about: agent-os/agents/trading/prediction-market/configs/prediction-market-agents.workers.json
node: n-19.2.1
basis: 84a4f402cc2f
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:08:15Z
---
# prediction-market-agents.workers.json

## Summary

The domain agent's jobs file: everything the prediction-market domain runs, each job with on or off, schedule, where it runs, platform and model. The example jobs are the domain session every 4 hours, the Polymarket price collector every 5 minutes, the hourly `markets-catalog` script, the nightly self-improvement sub-agent and a one-off election-night resolution check. The owner edits it in the UI, the scheduler reads it, and the system sees it through `configs/subagents.link/`. The job fields are proposed.

## Keep in mind

- When you pause a job, set `enabled: false`; never delete it to pause.
- When you give a job `secret_keys`, list key names only and keep it a `local` job; cloud, desktop and GitHub Actions jobs get no keys.
- When you look for run results, read `logs/jobs/[id]/` and the scheduler state; this file never changes at run time.
