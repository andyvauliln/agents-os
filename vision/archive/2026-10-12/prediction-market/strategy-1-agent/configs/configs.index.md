---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/configs/
node: n-21.2
basis: bf8410188cb5
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
---
# configs/

## Summary

The strategy agent's configuration, as real files: its jobs file `strategy-1-agent.workers.json` (the daily strategy session, `compare-variants` and the nightly self-improvement run) and its links file `strategy-1-agent.links.json` (the domain's markets catalog, the domain's comparison rules `trading-metrics.md`, the relink and test runners). Its `subagents.link/` shows every variant's configs, so the strategy can compare them. A fold-back of a winning change updates the strategy's config here. Still open: whether the strategy gets its own `[name].config.json`, as its variants and its domain have, and whether its files take its ID `pm-strategy-1-agent.opus55-test` or keep the folder name. The domain reads this folder through its own child links.

## Keep in mind

- When you want to change how the strategy trades, test it as a new variant first; only a winner is folded back here.
