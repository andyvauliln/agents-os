---
about: agent-os/agents/system/tests/scripts/[test-id].test.[js-py]
basis: 674b4c90b427
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# [test-id].test.[js|py]

## What it is

One script test per file, named by its id (`t-scripts-NNN`): a normal node or pytest file that checks a system script on fixture data. Each has an entry in this folder's `tests.config.json`, and `run-tests` runs it from there. The format is proposed.

## Who looks after it

It is written by the system agent or sys-self-improvement-agent, when it adds a test; and the owner.

## When and how it changes

It changes when a test of a shared script is added or the script it checks changes. It is a name pattern, not a real item: it tells what each item made from it will hold.

## Who uses it, and when

It is read by run-tests (planned shared script); and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/tests/scripts/tests.config.json`, `agents/system/docs/README.md` (section "Tests") and its folder's How it works file `agents/system/tests/scripts/scripts.index.md`.

## Related knowledge

It reads `agents/system/scripts/system/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Tests").

## Keep in mind

- When you write a script test, use fixture data only, with no network and no secrets.
