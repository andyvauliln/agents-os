---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/tests/
node: n-21.12
basis: 5cd3edb52c38
written: 2026-10-01T00:58:25Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# tests/

## Summary

The strategy agent's tests, so every change to the strategy can be checked before and after it runs. `agents/` tests the strategy manager prompt and its sub-agents by running Claude Code headless on fixtures, in test mode with no secrets; `scripts/` tests its code on fixtures with no network. Each has a `tests.config.json` where the owner switches tests on or off and where `run-tests`, called through the runner link in that folder, writes back results, also appended to `logs/tests.jsonl`. `subagents.link/` shows every variant's tests. Placing `tests/` at the folder root is proposed. Open: whether a failing test blocks runs or only promotion, and whether a backtest belongs here or in research.

## Keep in mind

- When you change the strategy prompt, a sub-agent or a script, add or update its test and run it.
