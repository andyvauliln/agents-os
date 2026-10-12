---
about: agent-os/agents/system/tests/
node: n-10.8
basis: d407ccea13bd
written: 2026-10-01T01:00:33Z
by: summary-worker
confirmed: 2026-10-07T19:02:04Z
---
# tests/

## Summary

The system's tests, so every change to the system's prompt, sub-agents or scripts can be checked before and after it runs. `agents/` tests LLM behaviour: the system prompt and its sub-agents, run headless in a temporary copy of the folder, in test mode with no secrets. `scripts/` tests the system's scripts, the shared ones, with node or pytest on fixtures. Each has a `tests.config.json`, where the owner switches tests on or off and `run-tests` writes results, plus a runner link to `run-tests`; results also go to `logs/tests.jsonl`. Through `subagents.link/` the system sees each domain's tests. Every level has this layout; placing it at the folder root rather than in `.claude/` is proposed. Open: whether a failing test blocks runs or only promotion.

## Keep in mind

- When you add a test, put prompt and sub-agent tests in `agents/` and code tests in `scripts/`, each with an entry in that folder's `tests.config.json`.
