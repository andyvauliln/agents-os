---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/prediction-market-agents.config.link.json
node: p-agent-os-agents-trading-prediction-market-strategy-1-agent-pm-strategy-1.momentum-v1.opus55-test-configs-prediction-market-agents.config.link.json
basis: d15e8c278749
written: 2026-10-07T19:05:03Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# prediction-market-agents.config.link.json

## Summary

A read-only file link to its domain's settings, `prediction-market-agents.config.json` [19.2.4]: the risk caps, its trading account, the venues and fees, and the order stop switch it works within. Each run merges it between the system config and the agent's own config into `logs/effective-config.json`; the agent's config may only tighten its limits. Relink builds the link from its required entry in the links file [27.3].

## Keep in mind

- When you want a stricter limit for this agent, set it in its own config [27.2]; this link is read-only, and a limit may only be tightened.
