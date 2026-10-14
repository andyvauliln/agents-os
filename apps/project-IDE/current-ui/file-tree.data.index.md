---
about: agent-os/apps/project-IDE/current-ui/file-tree.data.json
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# file-tree.data.json

## What it is

Everything the page shows, in one generated file: every item, with its path as its id, its status, its How it works and Details, its Example, Questions and ASD-STE100 text where those files exist, and its extra tabs, plus the decisions the page shows when one is named. `enrich.py` builds it from the files on disk and the metadata files next to each item, with a new data version each time. The text of each file is in `real-files.json` next to it. It cannot hold a copy of itself, so its File tab shows it exactly as the page loaded it, read-only.

## Who looks after it

It is made by `agents/system/.claude/skills/ide-build/scripts/enrich.py`; nobody edits it by hand.

## When and how it changes

It changes when the build runs after a round that changed a file, a folder or a metadata file. It is empty for now.

## Who uses it, and when

It is read by `apps/project-IDE/current-ui/file-tree-explorer.html` and `apps/project-IDE/server/server.py`.

## Where it is mentioned

It is described in `apps/project-IDE/docs/README.md` and its folder's How it works file `apps/project-IDE/current-ui/current-ui.index.md`.

## Related knowledge

It is written by `agents/system/.claude/skills/ide-build/scripts/enrich.py`. It is read by `apps/project-IDE/current-ui/file-tree-explorer.html`. It is built from `apps/project-IDE/data/decisions.md` and `apps/project-IDE/data/overrides.json`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `apps/project-IDE/docs/README.md` (section "What the page reads").

## Keep in mind

- When it is out of date or two copies disagree, rebuild it; never edit or merge it by hand.
