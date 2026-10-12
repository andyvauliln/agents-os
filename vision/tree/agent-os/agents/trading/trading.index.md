---
about: agent-os/agents/trading/
node: n-56
basis: 2887bce64511
written: 2026-10-09T09:55:29Z
by: knowledge-base-agent
confirmed: 2026-10-09T15:06:20Z
---
# trading/

## Summary

The folder of trading domains. Trading is the first kind of work the Agent OS does, and everything about it lives below this folder, so the system level stays general. Today it holds `docs/`, `researches/` with the research studies (the first real files in the tree) and the prediction-market domain `prediction-market/`; the copy-trading domain `copytrading/` comes next and will start as a copy of the prediction-market domain.

It is not an agent: it has no prompt, config, scripts or jobs of its own yet. The trading notes, the trading config and the decision scripts stay in the prediction-market domain until a second trading domain needs them; then the shared part can move up here.

## Keep in mind

- When you add a trading domain, create it with `create-agent` as a copy of the prediction-market domain; never copy a folder by hand.
- When something about money, accounts, markets or orders is written, keep it inside `trading/`; nothing about trading goes above it.
- When this folder changes, check its three docs and the system's README and rebuild prompt.
