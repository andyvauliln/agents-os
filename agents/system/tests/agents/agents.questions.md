# Questions: agents/

## Open questions for the owner

- **Do we name each test after its target and its check, not `[test-id].test.md`?** An example is `pm-self-improvement-agent.never-touches-live.test.md`. Such a name tells at once what a failed test means. Recommended: yes, `{target}.{check}.test.md`, in the same folder. From: the owner's question of 2026-10-06 about the location of tests.

## The owner's questions

### 2026-10-06: Where are the agent tests, and what are their names?

> and where do we store tests for agents and subagent and how we name them?

The tests are in the `tests/agents/` folder of the level that holds the agent. Each test is one file. The `tests.config.json` of that folder lists the tests.

The name pattern today is `[test-id].test.md`. Each test is a scenario with the expected behaviour.

An agent proposed a name that tells the target and the check, for example `pm-self-improvement-agent.never-touches-live.test.md`. This proposal waits for the owner. There is no test yet.

Docs improved: agents/system/tests/agents/agents.index.md.
