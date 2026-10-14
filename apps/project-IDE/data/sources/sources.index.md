---
about: agent-os/apps/project-IDE/data/sources/
basis: 37b510d0fb10
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# sources/

## What it is

The earlier knowledge notes the docs were written from, kept but not referenced: no doc, skill, agent or metadata file reads them now, and whether to use them is decided later. It holds the old topic notes (overview, architecture, conventions, safety, flows, data schemas, glossary, metrics, roadmap, feature map, the vision notes and the inputs vision), `common/` and `index/` with the shared notes and the hand-written lists, `knowledge-sources/` with what each system doc rested on, and `prediction-market/` with the domain's earlier metadata files kept as data for stage two. `[doc].md` is the name pattern for one knowledge-sources note.

## Who looks after it

It is written by knowledge-base-agent.

## When and how it changes

Nothing changes it until the owner decides whether to use the notes.

## Who uses it, and when

Nobody reads it now.

## Where it is mentioned

It is described in its folder's How it works file `apps/project-IDE/data/data.index.md`.

## Related knowledge

The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules") and `docs/metadata.md`. The build treats `prediction-market/metadata/` as plain data (`KEPT` in `agents/system/.claude/skills/ide-build/scripts/index_files.py`).

## Keep in mind

- When you need knowledge from a note here, write it into the level doc that owns it; do not point to the note.
