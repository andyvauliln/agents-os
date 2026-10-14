---
about: agent-os/agents/trading/prediction-market/docs/index/accounts.md
node: n-19.6.18.1
basis: 12b78d2b7f6c
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:08:15Z
---
# accounts.md

## Summary

The list of every trading account of the domain, one row each: id, venue, mode, whether it is funded and approved by the owner, its capital, the agent that uses it and its key names, never values. It is written by hand from the domain config's `accounts` and the secrets index, and funding is tracked only here and in the config. No account exists yet; the one row is an example, and the id format is open.

## Keep in mind

- When you add or fund an account, update its row here and its entry in the domain config together; only the owner approves a live one.
