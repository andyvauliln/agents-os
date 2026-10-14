---
about: agent-os/agents/system/logs/workers/[worker]/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# workers/[worker]/

## What it is

One log folder per shared worker, named after it. The draft format is plain text: a dated `YYYY-MM-DD.log` plus a stable `latest.log`, one line per event (`ts LEVEL worker message`). At the end of each run the worker also prints a JSON summary line that `run-job` keeps in the job log. An agent links `latest.log` only when it needs it. Whether these logs become JSONL like the others is open.

## Who looks after it

It is written by a shared worker, when one is built.

## When and how it changes

It changes when a shared worker is created; then every run adds lines. It is a name pattern, not a real item: it tells what each item made from it will hold.

## Who uses it, and when

It is read by the system agent; sys-self-improvement-agent; the owner, on the File Tree page; and agents that link the latest log.

## Where it is mentioned

It is described in `agents/system/logs/workers/` and its folder's How it works file `agents/system/logs/workers/workers.index.md`.

## Related knowledge

It is written by `agents/system/scripts/workers/`. It has the same format as `agents/system/data/workers/[worker]/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Logs") and `agents/system/docs/README.md` (section "Workers and data").

## Keep in mind

- When you rotate dated logs, keep replacing `latest.log` in one step; agents' links point at it.
