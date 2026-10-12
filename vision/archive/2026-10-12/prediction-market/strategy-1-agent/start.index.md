---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/start.sh
node: n-21.11
basis: 80512d60c4fb
written: 2026-10-01T00:59:34Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# start.sh

## Summary

Starts one strategy session: Claude Code in the strategy folder, with the strategy's own `.claude/` and links, reading the variants through `subagents.link/`. The scheduler calls it for the daily `agent` job in the strategy's workers file, and the owner can also run it by hand. This wiring is proposed.
