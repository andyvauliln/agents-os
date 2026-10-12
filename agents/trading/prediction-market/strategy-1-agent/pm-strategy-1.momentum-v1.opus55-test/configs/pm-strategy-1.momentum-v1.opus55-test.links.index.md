---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/pm-strategy-1.momentum-v1.opus55-test.links.json
node: n-27.3
basis: bfe35ea0f227
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:07:29Z
---
# pm-strategy-1.momentum-v1.opus55-test.links.json

## Summary

The variant's links file: every file it reads from elsewhere, each entry with `to` (where the link appears), `from` (the real file, as `@system`, `@domain`, `@strategy` or any agent's `@[name]`), `why` and `required`. Examples: the system and domain configs, the domain's prices and risk check, and both safety notes. `create-agent` writes it; the agent, its strategy's SI or the owner edit it, and relink builds the symlinks. Still open: whether a link change makes a new variant.

## Keep in mind

- When you add or change a link, edit its entry here and rerun relink (`node scripts/relink.system.link.js`); never make or delete a symlink by hand.
- When you add a link, never point it into `.secrets/` or any `.claude/`, and never put `to` inside `subagents.link/`.
- When you add or remove a link, record it in `docs/changes.md` under `Links`.
