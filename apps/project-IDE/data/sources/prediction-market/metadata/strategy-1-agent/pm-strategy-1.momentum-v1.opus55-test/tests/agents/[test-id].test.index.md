---
about: agent-os/agents/trading/prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/tests/agents/[test-id].test.md
node: n-49.1.2
basis: 74d11de1a6d6
written: 2026-10-01T01:02:00Z
by: summary-worker
confirmed: 2026-10-07T19:05:50Z
---
# [test-id].test.md

## Summary

One Markdown scenario per agent test, named after its id, such as `t-agents-001.test.md`. It starts `# t-agents-NNN: what it checks`, then lists Target, Fixtures, Run, Expect and Graded by. `run-tests` runs it by starting Claude Code headless in a temporary copy of the agent folder, in test mode, with no secrets. Script checks grade it first; a judge sub-agent only for fuzzy expectations. Example: the agent refuses to trade when the kill switch is on. The format is proposed.

## Keep in mind

- When you write an agent test, add its entry to this folder's `tests.config.json` too.
