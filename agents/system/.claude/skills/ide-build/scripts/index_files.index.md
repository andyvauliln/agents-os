---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/index_files.py
basis: 70115fa99970
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# index_files.py

## What it is

Lists the items of the tree from the repository: every file git keeps, the folders that hold them and the local keys files, with the top as `agent-os`. It knows where each item's How it works and Details files are, named after the item without its extension, so `vision.md` has `vision.index.md` and `vision.meta.json`; a file that shares its name with a sibling or its folder keeps its extension. It reads and writes the How it works files with their header, and finds missing and orphan metadata files.

## Who looks after it

It is written by the owner, project-ide-agent and knowledge-base-agent.

## When and how it changes

It changes when a metadata naming rule, the Details fields or the planning sources of drafts change.

## Who uses it, and when

It is read by `agents/system/.claude/skills/ide-build/scripts/enrich.py` and `agents/system/.claude/skills/ide-build/scripts/build_map.py`.

## Where it is mentioned

It is described in `docs/metadata.md` and its folder's How it works file `agents/system/.claude/skills/ide-build/scripts/scripts.index.md`.

## Related knowledge

It is read by `agents/system/.claude/skills/ide-build/scripts/enrich.py` and `agents/system/.claude/skills/ide-build/scripts/build_map.py`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "The File Tree page"), `docs/metadata.md`, `agents/system/docs/README.md` (section "The project IDE"), `apps/project-IDE/docs/README.md` (section "How the page is built and checked") and `agents/system/.claude/skills/ide-build/scripts/README.md`.

## Keep in mind

- When the file set is built, split this file into one file per job; today it does several.
