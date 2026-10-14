---
about: agent-os/agents/system/tests/agents/
basis: 4ad153594f20
written: 2026-10-14T12:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# agents/

## Summary

Tests of the system's LLM behaviour: its prompt `CLAUDE.md` and its sub-agents. Each test is one Markdown file named `[test-id].test.md`: a scenario with fixtures, an expectation and how it is graded; no test is written yet, and naming each test after what it tests and checks is a proposal; `tests.config.json` lists every test with its on/off switch, schedule and last result; `run-tests.system.link.js` runs this folder's tests. Each test runs headless in a temporary copy of the system folder, forced to test mode with no secrets, and results go back to the config and to `logs/tests.jsonl`. The owner turns tests on or off in the UI. The formats are proposed.

## Keep in mind

- When you test code rather than prompt or sub-agent behaviour, put the test in `tests/scripts/`.
