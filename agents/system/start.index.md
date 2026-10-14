---
about: agent-os/agents/system/start.sh
basis: 674b4c90b427
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# start.sh

## What it is

The system's start script. Like every level's `start.sh` it does one run of its level, here a system session at `agents/system/`; the scheduler calls it for the main-run job, and the owner can run it by hand. At the system level it also starts the one central scheduler, which runs every job in every workers file while the OS keeps it alive. This is proposed; which machine runs the scheduler is open.

## Who looks after it

It is written by knowledge-base-agent (the plan); and the system agent, once the shared scripts are written.

## When and how it changes

It changes when the way the system starts its session or the scheduler changes. It is empty for now.

## Who uses it, and when

It is read by the owner, by hand; the scheduler (planned shared script), for the system's main-run job; and the operating system service that keeps the scheduler running.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Jobs and the scheduler") and its folder's How it works file `agents/system/system.index.md`.

## Related knowledge

It has the same format as `agents/system/init.sh`. It reads `agents/system/configs/system.workers.json` and `agents/system/scripts/system/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Jobs and the scheduler").

## Keep in mind

- When you need the scheduler running, start it only through this script; there is one scheduler for all agents.
