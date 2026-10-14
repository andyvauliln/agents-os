---
about: agent-os/agents/trading/prediction-market/docs/how-to/add-trading-account.md
node: n-19.6.17.3
basis: af84006d31a0
written: 2026-10-07T18:56:50Z
by: knowledge-base-agent
---
# add-trading-account.md

## Summary

The runbook for adding a trading account at a venue with its keys or wallet, the trading steps added to the system's `how-to/add-account-or-secret.md`: the owner creates the account, its key names carry an account prefix such as `POLYMARKET_ACCT1_`, the account goes into the domain config's `accounts` and `index/accounts.md`, a test run checks the keys, and rotation revokes the old key at the venue. The steps are proposed.

## Keep in mind

- When you add an account, write only key names in configs and the index, never values; a live entry needs the owner's approval.
