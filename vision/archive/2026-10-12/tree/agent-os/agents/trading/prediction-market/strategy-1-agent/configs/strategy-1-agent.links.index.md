---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/configs/strategy-1-agent.links.json
node: n-21.2.3
basis: b03ee8affade
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
---
# strategy-1-agent.links.json

## Summary

The strategy agent's links file: every file the strategy links from elsewhere and where each link appears in its own folders. The examples link the domain's markets catalog, to compare variants market by market, the domain's `trading-metrics.md`, which says how variants are compared and promoted, and the system's `relink` and `run-tests` scripts. `create-agent` writes it first; then the strategy, its SI sub-agent or the owner edit it, and `relink` builds the symlinks. The format is proposed.

## Keep in mind

- When you edit it, run `node scripts/relink.system.link.js` and read its report; never make a symlink by hand.
- When you add an entry, never point `from` into `.secrets/` or any `.claude/`, and never put `to` inside `subagents.link/`.
