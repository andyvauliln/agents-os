---
about: agent-os/agents/trading/prediction-market/tests/agents/[test-id].test.md
node: n-19.12.1.2
basis: 74d11de1a6d6
written: 2026-10-01T00:57:42Z
by: summary-worker
confirmed: 2026-10-07T18:57:42Z
---
# [test-id].test.md

## Summary

The pattern for one agent test of the domain level: a Markdown file titled `# t-agents-NNN: what it checks`, with Target (such as the domain's `CLAUDE.md` or a sub-agent), Fixtures, Run, Expect and Graded by. `run-tests` runs it headless in a temporary copy of the domain folder, in test mode with no secrets and no real orders, and grades it by script checks first. The format is proposed.

## Keep in mind

- When you write the expectation, make a script able to check it where you can; a judge sub-agent is only for fuzzy expectations.
