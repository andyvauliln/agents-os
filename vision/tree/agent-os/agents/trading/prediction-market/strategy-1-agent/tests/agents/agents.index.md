---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/tests/agents/
node: n-21.12.1
basis: 825bb7120551
written: 2026-10-01T00:58:25Z
by: summary-worker
confirmed: 2026-10-12T15:40:56Z
---
# agents/

## Summary

Tests of the strategy's LLM behaviour: its prompt `CLAUDE.md` and its sub-agents. It holds one scenario file per test, the `tests.config.json` that lists them with the owner's on or off switch and their last results, and a runner link to the shared `run-tests`. Each test runs Claude Code headless in a temporary copy of the strategy folder, in test mode with no secrets. No test is written yet.
