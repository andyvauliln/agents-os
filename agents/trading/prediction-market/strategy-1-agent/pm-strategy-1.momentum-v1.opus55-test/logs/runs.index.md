---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/logs/runs.jsonl
node: p-agent-os-agents-prediction-market-agents-strategy-1-agent-pm-strategy-1.momentum-v1.opus55-test-logs-runs.jsonl
basis: 5b936fa2b412
written: 2026-10-07T09:32:16Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:05:50Z
---
# runs.jsonl

## Summary

The agent's own run log, one JSON line per main run, written at the end of the run or when a restart cancels it: run id, trigger, the exact inputs read, decisions with price and the agent's probability, model, tokens, cost and status. The strategy, the self-improvement sub-agents, the metrics and the page read it. The format is still a proposal.

## Keep in mind

- When you log a trade decision, include `price` and `prob`: calibration cannot be measured without them.
- When a restart cancels a run, still write its line with `status: cancelled`; cancelled runs cost money and count.
