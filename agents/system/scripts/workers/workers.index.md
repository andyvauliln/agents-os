---
about: agent-os/agents/system/scripts/workers/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# workers/

## What it is

The shared data collectors: `*.worker.py|js` scripts that fetch data from outside sources, such as news, for agents in more than one domain. Each runs as a job in `system.workers.json` and writes a dated file plus a stable `latest.*` into `data/workers/[worker]/`, with its log in `logs/workers/[worker]/`; readers link `latest.*` and never copy it. A collector only one domain needs lives in that domain. Agents ask the workers helper, which reuses, extends or creates a worker.

## Who looks after it

It is written by the system's helpers and the workers helper (planned).

## When and how it changes

It changes when a worker that agents of several domains use is added, changed or removed. It is empty for now.

## Who uses it, and when

It is read by the scheduler and run-job (planned), through the system's jobs file; and the owner.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Workers and data"), `agents/system/docs/rebuild-prompt.md` (section "Workers and data"), `agents/system/scripts/` and its folder's How it works file `agents/system/scripts/scripts.index.md`.

## Related knowledge

It writes `agents/system/data/workers/` and `agents/system/logs/workers/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Workers and data").

## Keep in mind

- When you write output, write the dated file first, then replace `latest.*` in one step (temp file, then rename).
- When you add a worker, check the existing workers and the links index first; if the data already exists, link it instead.
- When you give a worker a key, list it in its job's `secret_keys` and load it through `load-secret`, never from the code.
- When you add code here, give each runnable thing its own file with one purpose; group related ones in a folder.
