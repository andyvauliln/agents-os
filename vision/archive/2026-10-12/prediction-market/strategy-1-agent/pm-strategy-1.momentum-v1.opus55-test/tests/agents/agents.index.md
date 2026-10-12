---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/agents/
node: n-49.1
basis: 7504e1a575e6
written: 2026-10-01T01:02:00Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# agents/

## Summary

Tests of the agent's prompt (`CLAUDE.md`) and its sub-agents, that is, of LLM behaviour. Each test is a scenario file [49.1.2] with an entry in `tests.config.json` [49.1.1], where the owner turns it on or off. The runner link [49.1.3] hands them to the shared `run-tests`, which copies the fixtures into a temporary copy of the agent folder and runs Claude Code headless there, in test mode, with no secrets and no real orders. Script checks grade the transcript, the files written and the decision calls; a judge sub-agent only handles fuzzy expectations. Results go back into the config and into `logs/tests.jsonl`. The fields and the scenario format are proposed.

## Keep in mind

- When you test the prompt or a sub-agent, put the test here; tests of code go in `tests/scripts/`.
