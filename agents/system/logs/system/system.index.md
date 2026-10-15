---
about: agent-os/agents/system/logs/system/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# system/

## What it is

The system's own log: one JSONL stream of what the shared machinery does. The scheduler logs runs started and finished, failed jobs and important file changes (cancel and restart, or wait); relink logs each link it creates or removes; check-links logs broken links; `load-secret` logs keys loaded or refused, by name only; `costs` lines record tokens and dollars per agent, giving the AI cost across all agents. The system's SI sub-agent reads errors and costs here. The events are proposed; file naming and retention are open.

## Who looks after it

It is written by the scheduler, relink, check-links and load-secret (planned shared scripts).

## When and how it changes

At run time, whenever the shared machinery does something; the folder itself changes only when its format changes. It is empty for now.

## Who uses it, and when

It is read by the system agent; sys-self-improvement-agent; and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Logs"), `agents/system/logs/` and its folder's How it works file `agents/system/logs/logs.index.md`.

## Related knowledge

It is written by `agents/system/scripts/system/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Logs") and `agents/system/docs/README.md` (section "Keys and secrets").

## Keep in mind

- When you log a key event, write key names, mode and result only; never a value.
