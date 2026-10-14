---
about: agent-os/agents/system/tests/agents/[test-id].test.md
node: n-10.8.1.2
basis: 74d11de1a6d6
written: 2026-10-06T21:55:22Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:02:04Z
---
# [test-id].test.md

## Summary

One Markdown file per agent test of the system prompt, a system sub-agent or a system skill, named by its id (`t-agents-NNN`). It has a title saying what it checks, then the target, fixtures, how it runs, what is expected and how it is graded. `run-tests` runs it headless in a temporary copy of the system folder, in test mode with no secrets. The format is proposed; naming each test after what it tests and what it checks is proposed too and waits for the owner.

## Keep in mind

- When you write the expectation, make it checkable by a script where you can; a judge sub-agent is only for fuzzy ones.
- When you add a test file, add its entry to this folder's `tests.config.json` too.
