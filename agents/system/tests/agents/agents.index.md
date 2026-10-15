---
about: agent-os/agents/system/tests/agents/
basis: 46decf4081ed
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# agents/

## What it is

Tests of the system's LLM behaviour: its prompt `CLAUDE.md` and its sub-agents. Each test is one Markdown file named `[test-id].test.md`: a scenario with fixtures, an expectation and how it is graded; no test is written yet, and naming each test after what it tests and checks is a proposal; `tests.config.json` lists every test with its on/off switch, schedule and last result; `run-tests.system.link.js` runs this folder's tests. Each test runs headless in a temporary copy of the system folder, forced to test mode with no secrets, and results go back to the config and to `logs/tests.jsonl`. The owner turns tests on or off in the UI. The formats are proposed.

## Who looks after it

It is written by the system agent, sys-self-improvement-agent and the owner.

## When and how it changes

It changes when a test is added or removed. It is empty for now.

## Who uses it, and when

It is read by run-tests (planned shared script); and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Tests"), `agents/system/tests/` and its folder's How it works file `agents/system/tests/tests.index.md`.

## Related knowledge

It reads `agents/system/CLAUDE.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Tests").

## Keep in mind

- When you test code rather than prompt or sub-agent behaviour, put the test in `tests/scripts/`.
