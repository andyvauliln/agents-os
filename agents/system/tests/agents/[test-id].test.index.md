---
about: agent-os/agents/system/tests/agents/[test-id].test.md
basis: 674b4c90b427
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# [test-id].test.md

## What it is

One Markdown file per agent test of the system prompt, a system sub-agent or a system skill, named by its id (`t-agents-NNN`). It has a title saying what it checks, then the target, fixtures, how it runs, what is expected and how it is graded. `run-tests` runs it headless in a temporary copy of the system folder, in test mode with no secrets. The format is proposed; naming each test after what it tests and what it checks is proposed too and waits for the owner.

## Who looks after it

It is written by the system agent or sys-self-improvement-agent, when it adds a test; and the owner.

## When and how it changes

It changes when a test of the system's instructions or helpers is added or its expectation changes. It is a name pattern, not a real item: it tells what each item made from it will hold.

## Who uses it, and when

It is read by run-tests (planned shared script); and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/tests/agents/tests.config.json`, `agents/system/docs/README.md` (section "Tests") and its folder's How it works file `agents/system/tests/agents/agents.index.md`.

## Related knowledge

It reads `agents/system/CLAUDE.md` and `agents/system/.claude/agents/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Tests").

## Keep in mind

- When you write the expectation, make it checkable by a script where you can; a judge sub-agent is only for fuzzy ones.
- When you add a test file, add its entry to this folder's `tests.config.json` too.
