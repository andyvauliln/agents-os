---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/logs/
node: n-34
basis: a452cbb82f33
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
---
# logs/

## Summary

The trading agent's own logs, as real files, plus links to the few shared logs it needs. Every main run ends with a line in `runs.jsonl` (inputs read, decisions with price and probability, model, tokens, cost, status) and a section in `run-[date].md` with a memory note for the next run. `run-agent` writes the merged `effective-config.json` here at each run start, `run-job` logs every job under `logs/jobs/[job-id]/`, and `run-tests` appends to `tests.jsonl` [34.2]. A file link [34.1] brings in the log of its domain's price collector. The strategy, SI, metrics and, level by level, the UI read this folder through the strategy's `logs/subagents.link/`. The contents are git-ignored; the formats, log format and retention are still open or proposed.

## Keep in mind

- When you write a log here, never include a secret value.
- When you need a shared log, link its `latest.log` through the links file; never copy it in.
