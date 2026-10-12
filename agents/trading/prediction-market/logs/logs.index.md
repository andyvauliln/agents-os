---
about: agent-os/agents/trading/prediction-market/logs/
node: n-19.4
basis: 3dfb39f6061b
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# logs/

## Summary

The domain's own logs, as real files. The domain session and the domain SI record per run the inputs used, reasoning, decisions, actions, cost and the effective config. `jobs/[job-id]/` holds the run logs of the domain's jobs, such as the price collector and the markets catalog, and `services/[service]/` the order logs of its acting services: every order placed or blocked, in test and live, the source of every PnL number. `subagents.link/` gives the domain its strategies' logs, and the system and the UI read this folder through their own child links. The content is git-ignored runtime output, while the folder stays in git. The formats are proposed.

## Keep in mind

- When you need a log from elsewhere, link that one file through the links file, and only if the domain's logic needs it.
