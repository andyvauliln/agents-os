---
about: agent-os/agents/system/data/system/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# system/

## What it is

The system's own state files, the runtime memory of the shared machinery. `scheduler-state.json` holds every job's last run, result, next run and failure count; only the scheduler writes it, so workers files never change at run time. `links.index.json` lists every link in the project (owner agent, where it appears, real target, required, status); only relink writes it, and the UI, `check-links` and the runbooks read it to see who reads which file. Both formats are proposed. Still open: whether a `run-state.json` with per-agent read cursors is needed, which depends on how "new since the last run" is tracked.

## Who looks after it

It is written by the scheduler (planned), for its record of jobs; and relink (planned), for the list of links.

## When and how it changes

At run time, when a job runs or a link changes; the folder changes only when a record is added or its format changes. It is empty for now.

## Who uses it, and when

It is read by check-links (planned); the system agent; and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Jobs and the scheduler"), `agents/system/data/` and its folder's How it works file `agents/system/data/data.index.md`.

## Related knowledge

It is written by `agents/system/scripts/system/`. It is built from `agents/system/configs/system.workers.json` and `agents/system/configs/system.links.json`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Workers and data") and `agents/system/docs/README.md` (section "Jobs and the scheduler").

## Keep in mind

- When you need these files changed, let their one writer do it: the scheduler for `scheduler-state.json`, relink for `links.index.json`.
- When you move or delete a file others read, check `links.index.json` for its readers first.
