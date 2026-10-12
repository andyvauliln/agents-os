---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/scripts/
node: n-30
basis: ac0a3c0fb0ea
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
---
# scripts/

## Summary

The trading agent's code: its own scripts in JS/TS or Python, plus read-only links to the shared scripts it uses. Each name says its kind: `.worker.` fetches data (`get-polymarket-data.worker.py` [31]) and `.system.` is machinery (`clean-data.system.js` [32]), as at every level, and the domain's own `.decision.` acts (`make-buy.decision.js` [33], the only way the agent trades). The links bring in the domain's risk check [30.1] and the system's `relink` [30.3] and `run-tests` [30.2], so a fix to a shared script reaches every agent at once. Own scripts log to `logs/` and write data to `data/` (proposed), each running as a job in the jobs file. The strategy sees this folder through its `scripts/subagents.link/`. Still open: other script kinds, and when a local worker moves to shared.

## Keep in mind

- When you name a script, end it with its kind: `.worker.`, `.system.` or the domain's `.decision.`.
- When you need a shared script, link it through the links file; never copy it into this folder.
- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
