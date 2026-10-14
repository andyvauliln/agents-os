---
about: agent-os/agents/trading/prediction-market/
node: n-19
basis: 894f0d7ea6ba
written: 2026-10-09T09:55:29Z
by: knowledge-base-agent
confirmed: 2026-10-09T12:41:47Z
---
# prediction-market/

## Summary

The prediction-market domain (Polymarket first), the first domain in the `trading/` folder, and its domain-level agent, which is responsible for the whole domain: its strategies, their health, money made, and the owner's questions and comments about it. It holds everything about trading in the Agent OS, and a later trading domain is copied from it. Its prompt `.claude/CLAUDE.md` holds the domain owner role, and its self-improvement sub-agent improves the domain.

Its own config holds the risk limits, the trading accounts, the venues with their fees and market filters, the currency, the order stop switch and the trade notifications, read after the system's settings and before each agent's own. `scripts/decisions/` holds the shared buy, sell and risk-check scripts every trading agent calls; the Polymarket price collector runs every 5 minutes and the markets catalog every hour, with their job logs and data, and every order goes to the order logs.

Its `docs/` holds the trading layer of every system note (`trading-safety.md`, `trading-metrics.md` and the rest), the trading runbooks and the list of trading accounts. Its strategies sit below it, starting with `strategy-1-agent/`, and it reads each through `subagents.link/`. For now actions happen only on blockchains; centralised exchanges are data sources only.

## Keep in mind

- When something is shared by two or more strategies of this domain, keep it at the domain level and let them link it; when it is shared by more domains, it goes to the system.
- When you change the domain config's risk limits or accounts, get the owner's approval first; a lower level may only tighten a limit.
