---
about: agent-os/agents/system/tests/agents/tests.config.json
basis: 0b926e7a68a1
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# tests.config.json

## What it is

The list of every agent test at the system level: tests of the system prompt and its sub-agents. Each entry has an id like `t-agents-001`, a target, the test file, `enabled`, a schedule (`manual`, `on_change`, `interval:[x]`, `before_promote`) and an owner. `run-tests` writes back last run, result, duration and failure count, and a failure gets a `next_action`. The owner switches tests on or off in the UI. Field names are proposed.

## Who looks after it

It is written by the system agent or sys-self-improvement-agent, when it adds a test; the owner, who switches tests on or off; and run-tests (planned), for the results.

## When and how it changes

It changes when a test is added, switched on or off, or run. It is empty for now.

## Who uses it, and when

It is read by run-tests (planned shared script); and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Tests"), `agents/system/docs/rebuild-prompt.md` (section "Tests") and its folder's How it works file `agents/system/tests/agents/agents.index.md`.

## Related knowledge

It is read by `agents/system/tests/agents/run-tests.system.link.js`. It has the same format as `agents/system/tests/scripts/tests.config.json`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Tests").

## Keep in mind

- When you add a test, fill only its own fields; leave `last_run`, `last_result` and `fail_count` to `run-tests`.
- When you see a test fail, write a `next_action` saying what should be done next.
