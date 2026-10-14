---
about: agent-os/agents/system/logs/workers/
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
---
# workers/

## What it is

The logs of the shared workers, one folder per worker. No worker exists yet, so it holds only the name pattern `[worker]/`.

## Who looks after it

It is written by the shared workers (planned).

## When and how it changes

It changes when a shared worker is added or removed. It is empty for now.

## Who uses it, and when

It is read by the system agent; sys-self-improvement-agent; and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Logs"), `agents/system/logs/` and its folder's How it works file `agents/system/logs/logs.index.md`.

## Related knowledge

It is written by `agents/system/scripts/workers/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Logs") and `agents/system/docs/README.md` (section "Workers and data").

## Keep in mind


