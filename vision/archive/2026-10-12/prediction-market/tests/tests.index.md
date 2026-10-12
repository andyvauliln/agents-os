---
about: agent-os/agents/trading/prediction-market/tests/
node: n-19.12
basis: 6935eada21d5
written: 2026-10-01T00:58:39Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# tests/

## Summary

The domain's tests, so every change to the domain's prompt, sub-agents or scripts can be checked before and after it runs. `agents/` tests the domain owner's prompt and sub-agents headless in a temporary copy of the domain folder; `scripts/` tests its code with node or pytest on fixtures. Each has a `tests.config.json`, where the owner switches tests on or off, and a runner link to the shared `run-tests`, which writes results back and to `logs/tests.jsonl`. `subagents.link/` gives the domain every strategy's tests. The SI and support agents add tests. Placement at the folder root and the fields are proposed. Still open: whether a failing test blocks runs or only promotion, and where backtests belong.

## Keep in mind

- When you write or run a test, use test mode, fixtures and no secrets; a test never places a real order.
