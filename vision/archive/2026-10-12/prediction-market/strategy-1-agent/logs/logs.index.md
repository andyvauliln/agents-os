---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/logs/
node: n-21.4
basis: 931d32bcaee4
written: 2026-10-01T00:56:59Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# logs/

## Summary

The strategy agent's own logs, as real files: the runs of its daily strategy session and of its nightly self-improvement sub-agent, and each job's run history in `logs/jobs/[job-id]/` (`history.jsonl` with trigger, status, duration, cost and tokens, plus `latest.log`). The content is runtime output and git-ignored, while the folder stays. `subagents.link/` gives the strategy every variant's logs, which it reads to compare variants on cost and errors. The log shapes are proposed; still open is whether a run writes one JSONL decision log plus a Markdown summary.
