---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/system.config.link.json
node: p-agent-os-agents-trading-prediction-market-strategy-1-agent-pm-strategy-1.momentum-v1.opus55-test-configs-system.config.link.json
basis: 1454a981eddf
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# system.config.link.json

## Summary

A read-only file link to the global `system.config.json` [11.1]: defaults, modes with the general stop switch and the live allowlist, schedule defaults, triggers and notifications (sections proposed). Risk caps and trading accounts are in the domain's config, linked next to it. For each run the system, domain and own configs are merged into `logs/effective-config.json`, which is what counts. Relink builds the link from its required entry in the links file [27.3].

## Keep in mind

- When you want a different value for this agent, set it in its own config [27.2]; this link is read-only, and risk caps may only be tightened.
