---
about: agent-os/agents/system/tests/scripts/run-tests.system.link.js
basis: 674b4c90b427
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# run-tests.system.link.js

## What it is

A file link to the shared `run-tests` script in `scripts/system/`. Called from here, it presets kind `scripts` and this folder's `tests.config.json`, so `node tests/scripts/run-tests.system.link.js` runs the system's script tests, or one with `--id`. It is listed in `system.links.json` and built by relink; it is a link, never a copy.

## Who looks after it

It is written by relink (planned shared script in agents/system/scripts/system/), from the system's links file.

## When and how it changes

It changes when the system's links file changes this link; relink makes it again. It is empty for now.

## Who uses it, and when

It is read by the owner, by hand; the scheduler (planned); and the system agent.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Tests") and its folder's How it works file `agents/system/tests/scripts/scripts.index.md`.

## Related knowledge

It is built from `agents/system/configs/system.links.json`. It reads `agents/system/tests/scripts/tests.config.json`. It links to `agents/system/scripts/system/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Tests") and `agents/system/docs/README.md` (section "Links between agents").

## Keep in mind

- When you find this link missing or wrong, fix its entry in `system.links.json` and rerun relink; never copy `run-tests` here.
