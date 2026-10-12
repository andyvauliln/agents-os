---
about: agent-os/agents/trading/prediction-market/scripts/
node: n-19.3
basis: a1dd1bc815c6
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# scripts/

## Summary

The domain's scripts: its own scripts as real files in JS/TS or Python, with the kind in the name (`.worker.`, `.system.`, or `.decision.`, the kind this domain adds for trading), plus file links to shared scripts. `decisions/` holds the domain's shared buy, sell and risk-check scripts (proposed), which every trading agent links; the risk check is code and runs before every order. Two workers collect the domain's data: `polymarket-prices.worker.py` (prices for the active markets) and `markets-catalog.worker.py` (the hourly catalogue of markets). `relink.system.link.js` relinks only the domain, and `subagents.link/` shows each strategy's scripts. Still open: other script kinds, and whether code, the model or both decide a trade.

## Keep in mind

- When you need a shared script, link it through the links file; never copy it, so a fix reaches every agent at once.
- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
