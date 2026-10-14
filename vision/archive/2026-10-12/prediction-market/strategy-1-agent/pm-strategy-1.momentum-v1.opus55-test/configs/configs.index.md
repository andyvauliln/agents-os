---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/
node: n-27
basis: 3efa73b52c99
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:07:29Z
---
# configs/

## Summary

The trading agent's own configs, as real files, plus read-only links to the shared ones. Three files carry its name: the config [27.2] (identity, `mode: test`, tighten-only risk caps, key names, strategy knobs), the jobs file [27.4] (main run every 15 minutes, its worker, one-off jobs) and the links file [27.3] (every file it reads from elsewhere). Three file links [27.1] bring in the global `system.config.json`, its domain's `prediction-market-agents.config.json` (risk caps, accounts, the order stop switch) and the routing file `models.config.json`. The strategy's SI or the owner change the files; a changed config is a new variant, recorded in `changes.md`. The strategy sees this folder through its `configs/subagents.link/`. Still open: which settings are individual or common, and whether the agent may edit its own config.

## Keep in mind

- When you change a config or a job's logic, make it a new test variant with a new name; do not edit a running variant in place.
- When you write any file here, use key names only, never a secret value.
