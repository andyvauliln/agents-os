---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/tests/agents/[test-id].test.md
node: n-21.12.1.2
basis: 74d11de1a6d6
written: 2026-10-01T00:58:25Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# [test-id].test.md

## Summary

One test of the strategy's LLM behaviour, named by its id `t-agents-NNN`: a Markdown scenario with its target (the strategy prompt or a sub-agent), fixtures, how it runs, what is expected and how it is graded. It runs headless in a temporary copy of the strategy folder, in test mode with no secrets, and script checks grade it before any judge sub-agent. None is written yet.

## Keep in mind

- When you pick its id, take the next unused `t-agents-NNN` of the strategy; ids are never reused.
