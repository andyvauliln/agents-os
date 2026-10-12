---
about: agent-os/agents/trading/prediction-market/scripts/subagents.link/
node: n-19.3.1
basis: 140e42504f8e
written: 2026-10-01T00:56:32Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# subagents.link/

## Summary

The domain's view of its strategies' scripts: one folder link per strategy, named after the strategy's folder and pointing at that strategy's `scripts/`. The domain session and the domain SI read each strategy's scripts here, without copies. Relink builds the entries from the folder tree (the strategy's `init.sh` runs it) and removes them after stop-or-delete; they are read-only for the domain and never listed in a links file. The domain has the same `subagents.link/` in each of its seven content folders.

## Keep in mind

- When you scan files, never follow this folder recursively; go down one `subagents.link/` at a time.
- When you find an entry missing or stale, run relink; never add or remove a child link by hand.
