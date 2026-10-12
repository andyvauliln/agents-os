---
about: agent-os/agents/system/tests/agents/
node: n-10.8.1
basis: 15a284327e31
written: 2026-10-01T01:00:33Z
by: summary-worker
confirmed: 2026-10-07T19:02:04Z
---
# agents/

## Summary

Tests of the system's LLM behaviour: its prompt `CLAUDE.md` and its sub-agents. Each test is a Markdown scenario with fixtures, an expectation and how it is graded; `tests.config.json` lists every test with its on/off switch, schedule and last result; `run-tests.system.link.js` runs this folder's tests. Each test runs headless in a temporary copy of the system folder, forced to test mode with no secrets, and results go back to the config and to `logs/tests.jsonl`. The owner turns tests on or off in the UI. The formats are proposed.

## Keep in mind

- When you test code rather than prompt or sub-agent behaviour, put the test in `tests/scripts/`.
