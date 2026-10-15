---
about: agent-os/apps/project-IDE/data/overrides.json
basis: b4a06fe6a5a8
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# overrides.json

## What it is

The owner's edits from the page that are kept in the page data rather than in a file of their own, listed by the item's path. `enrich.py` applies only the edits of the extra tables (such as the key names of a keys file); an item's text, How it works and Details come from its own files, so the other edits here are kept as a record only.

## Who looks after it

It is written by project-ide-agent and ide-sync.

## When and how it changes

It changes when a sync folds in a page edit of an extra table that has no file of its own.

## Who uses it, and when

It is read by `agents/system/.claude/skills/ide-build/scripts/enrich.py`.

## Where it is mentioned

It is described in `apps/project-IDE/current-ui/file-tree.data.json` and its folder's How it works file `apps/project-IDE/data/data.index.md`.

## Related knowledge

It is read by `agents/system/.claude/skills/ide-build/scripts/enrich.py`. It is written by `agents/system/.claude/skills/ide-sync/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `apps/project-IDE/docs/README.md` (section "How the owner's work comes back").

## Keep in mind

- When you rebuild the page, keep this file: without it the owner's edits of the extra tables are lost.
