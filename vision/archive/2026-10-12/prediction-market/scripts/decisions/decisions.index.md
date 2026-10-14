---
about: agent-os/agents/trading/prediction-market/scripts/decisions/
node: n-14.3
basis: 7cc277b24427
written: 2026-10-07T14:13:07Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:08:15Z
---
# decisions/

## Summary

The prediction-market domain's shared trading building blocks, moved here from the system: `*.decision.js|py` scripts for buying, selling and the risk check, which every trading agent's own decision scripts call through file links. The risk check is code, never the model: before each order it checks the stop switch, then the risk caps in the domain's config as the agent tightened them, then for live the allowlist and an owner-approved, funded account. In test an order becomes a simulated fill. Every action, placed or blocked, goes to the domain's order logs, the source of all PnL. All of this is proposed: there is no separate executor yet, and whether code, the model or both decide is open.

## Keep in mind

- When you change the risk check, keep the stop switch first and every cap in code; a prompt is never the only limit.
- When you write a script that acts, read the mode from config first; in test it never touches real money.
- When you place or block an order, log one line to the domain's order logs.
- When you add code here, give each runnable thing its own file with one purpose; group related ones in a folder.
