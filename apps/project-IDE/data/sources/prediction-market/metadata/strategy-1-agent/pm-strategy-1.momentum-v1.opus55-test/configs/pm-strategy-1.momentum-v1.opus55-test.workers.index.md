---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/pm-strategy-1.momentum-v1.opus55-test.workers.json
node: n-27.4
basis: 1d863c23192d
written: 2026-10-01T01:06:09Z
by: knowledge-agent
confirmed: 2026-10-07T19:05:50Z
---
# pm-strategy-1.momentum-v1.opus55-test.workers.json

## Summary

The variant's jobs file: everything it runs, each job with on or off, schedule, where it runs, platform and model. In the example: `main-run`, its own Claude Code session every 15 minutes, restarted when `data/polymarket-prices.link.json` changes; its worker `get-polymarket-data` every 15 minutes, `clean-data` after it, and a one-off `close-before-resolution` before markets resolve. The owner edits it in the UI; the scheduler reads it and keeps run state elsewhere. Field format proposed.

## Keep in mind

- When you want to pause a job, set `enabled: false`; never delete it.
- When you change a job's logic (prompt, model, tools, inputs), make a new variant; turning a job on or off or moving its time may happen in place. (Proposed: whether the owner may change a model in place is still open.)
- When you give a job `secret_keys`, keep it `local`: `cloud`, `desktop` and `github-actions` jobs get no keys and never trade.
