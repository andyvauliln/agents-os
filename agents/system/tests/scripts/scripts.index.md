---
about: agent-os/agents/system/tests/scripts/
basis: 76356043d88f
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# scripts/

## What it is

Tests of the system's scripts, which are the shared scripts in `scripts/` that every agent uses through file links. Each test is a node or pytest file on fixture data, with no network and no secrets; `tests.config.json` lists them with their switches, schedules and results; `run-tests.system.link.js` runs this folder's tests. Results go back into the config and to `logs/tests.jsonl`. The formats are proposed.

## Who looks after it

It is written by the system agent, sys-self-improvement-agent and the owner.

## When and how it changes

It changes when a test is added or removed. It is empty for now.

## Who uses it, and when

It is read by run-tests (planned shared script); and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Tests"), `agents/system/tests/` and its folder's How it works file `agents/system/tests/tests.index.md`.

## Related knowledge

It reads `agents/system/scripts/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Tests").

## Keep in mind


