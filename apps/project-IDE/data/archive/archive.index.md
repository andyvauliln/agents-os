---
about: agent-os/apps/project-IDE/data/archive/
basis: 4436e9b6a325
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# archive/

## What it is

A place for retired files kept for history, one folder per date. Today it holds only the name pattern `[date]/`. Nothing here is read while working.

## Who looks after it

It is written by knowledge-base-agent and file-index.

## When and how it changes

It changes when an item is retired, or `build_map.py --orphans` finds a metadata file whose item is gone and it is moved here. It is empty for now.

## Who uses it, and when

It is read by the owner and every AI session that looks back.

## Where it is mentioned

It is described in `apps/project-IDE/docs/README.md` and its folder's How it works file `apps/project-IDE/data/data.index.md`.

## Related knowledge

It is written by `agents/system/.claude/skills/ide-build/scripts/build_map.py`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules") and `docs/metadata.md` (section "How the build finds stale How it works files").

## Keep in mind


