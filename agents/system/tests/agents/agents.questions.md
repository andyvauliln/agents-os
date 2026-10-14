# Questions: agents/

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-06: Where tests for agents live and how they are named

> and where do we store tests for agents and subagent and how we name them?

In the `tests/agents/` folder of the level that holds the agent, one file per test, listed in that folder's `tests.config.json`. The name pattern today is `[test-id].test.md`, a scenario with the expected behaviour. Naming each test after what it tests and checks, such as `pm-self-improvement-agent.never-touches-live.test.md`, was proposed and waits for the owner; no test is written yet.
