---
about: agent-os/agents/trading/prediction-market/configs/prediction-market-agents.links.json
node: n-19.2.3
basis: e386df782e9b
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# prediction-market-agents.links.json

## Summary

The domain agent's links file: every file link the domain needs, each with where it appears (`to`), the real file it points at (`from`), why, and whether it is required. Examples: the system's `safety.md`, the shared `relink` and `run-tests` scripts, and optionally the system's news digest; the domain reads its own price and catalogue data in place. `create-agent` writes it first, the domain agent, its SI or the owner edit it, and relink builds the symlinks. The fields are proposed.

## Keep in mind

- When you change an entry, let relink build or remove the symlink (or run `node scripts/relink.system.link.js`); never make a symlink by hand.
- When you add a link, never point it into `.secrets/` or any `.claude/`, and never put `to` inside `subagents.link/`.
