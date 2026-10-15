---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/configs/pm-strategy-1.momentum-v1.opus55-test.config.json
node: n-27.2
basis: 7526d8436073
written: 2026-10-07T19:03:05Z
by: knowledge-base-agent
confirmed: 2026-10-09T09:57:03Z
---
# pm-strategy-1.momentum-v1.opus55-test.config.json

## Summary

The variant's own config, a real file in its folder: who it is (`agent.name`, type, domain, strategy, `parent`), the requested `mode` (`test`), `capital_and_risk` caps that may only tighten the domain's caps in `prediction-market-agents.config.json`, `secret_keys` (key names only) and the strategy's knobs (momentum window, entry and exit thresholds). Routes, jobs and links live in their own files. Each run merges it with the system and domain configs into `logs/effective-config.json`. Shape proposed; whether the agent may edit it is open.

## Keep in mind

- When you change a strategy parameter or any other setting here, make a new test variant with a new name and `parent` set to this one.
- When you set a risk cap, make it tighter than the domain config's `risk`; a looser value is ignored.
- When you need a key, list its name in `secret_keys`; never write a value.
- When you set `mode: live`, know it is only a request: live also needs the owner's approval, the allowlist and an owner-approved account.
