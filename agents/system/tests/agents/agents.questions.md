# Questions: agents/

## Open questions for the owner

- **Should each test be named after what it tests and checks, such as `pm-self-improvement-agent.never-touches-live.test.md`, instead of `[test-id].test.md`?** A name that says what is checked shows at a glance what a failing test means. Recommended: yes, `{target}.{check}.test.md`, in the same folder. From: the owner's question of 2026-10-06 on where tests live.

## The owner's questions

### 2026-10-06: Where tests for agents live and how they are named

> and where do we store tests for agents and subagent and how we name them?

In the `tests/agents/` folder of the level that holds the agent, one file per test, listed in that folder's `tests.config.json`. The name pattern today is `[test-id].test.md`, a scenario with the expected behaviour. Naming each test after what it tests and checks, such as `pm-self-improvement-agent.never-touches-live.test.md`, was proposed and waits for the owner; no test is written yet.

Docs improved: agents/system/tests/agents/agents.index.md.
