---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/scripts/
node: n-21.3
basis: 5b368b628c4b
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
---
# scripts/

## Summary

The strategy agent's scripts folder. Today it holds only links: `relink.system.link.js`, which relinks the strategy agent after its links file changes, and `subagents.link/`, through which the strategy reads every variant's scripts. Own scripts would go here as real files in JS/TS or Python, their kind in the name (`.worker.` and `.system.` as at every level, `.decision.` from the domain), each run as a job in the strategy's workers file and writing to its own `logs/` and `data/` (proposed). Shared scripts of the system or the domain are used through file links, never copied. Open: whether there are other script kinds.

## Keep in mind

- When you need a shared script, link it through the links file; never copy it here.
- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
