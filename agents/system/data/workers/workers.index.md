---
about: agent-os/agents/system/data/workers/
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
---
# workers/

## What it is

The outputs of the shared workers, one folder per worker, each run a dated file plus a stable `latest.*` that agents link. No worker exists yet, so it holds only the name pattern `[worker]/`.

## Who looks after it

It is written by the shared workers (planned).

## When and how it changes

It changes when a shared worker is added or removed. It is empty for now.

## Who uses it, and when

It is read by agents, through file links to latest files; and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "Workers and data"), `agents/system/data/` and its folder's How it works file `agents/system/data/data.index.md`.

## Related knowledge

It is written by `agents/system/scripts/workers/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Workers and data").

## Keep in mind

- When an agent needs a worker's output, link its `latest.*` file; never copy it.
