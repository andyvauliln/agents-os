---
about: agent-os/agents/trading/prediction-market/configs/
node: n-19.2
basis: ac22135c860d
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# configs/

## Summary

The domain's configs, as real files named after the domain folder. `prediction-market-agents.config.json` holds the domain's own settings, everything about money and markets: risk limits, trading accounts, venues, fees, market filters, the currency, the order stop switch and trade notifications; every trading agent links it, and a lower layer may only tighten a limit. `prediction-market-agents.workers.json` lists everything the domain runs, such as the domain session, the price collector and the markets catalog, and `prediction-market-agents.links.json` the files it links. `subagents.link/` gives the domain every strategy's configs. General settings stay in the system's `system.config.json` and routing in `models.config.json`; the shape of the domain config is still a proposal.

## Keep in mind

- When you change what the domain runs, edit its jobs file; when it needs a file from elsewhere, edit its links file and let relink build the link.
- When you change the domain config's risk limits, accounts or order stop switch, get the owner's approval first.
