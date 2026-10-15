---
about: agent-os/apps/project-IDE/current-ui/real-files.json
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# real-files.json

## What it is

The text of every file on the page, one entry per item, keyed by its path. `enrich.py` writes it next to the page data in every build; the page loads it the first time a file is opened, so the page itself stays small, and on the owner's server the same texts are read fresh from disk. A keys file, a file over 200 KB, a file that is not text and the two built data files are not in it.

## Who looks after it

It is made by `agents/system/.claude/skills/ide-build/scripts/enrich.py`; nobody edits it by hand.

## When and how it changes

It changes when the build runs after a round that changed a file, a folder or a metadata file. It is empty for now.

## Who uses it, and when

It is read by `apps/project-IDE/current-ui/file-tree-explorer.html` and `apps/project-IDE/server/server.py`.

## Where it is mentioned

It is described in `apps/project-IDE/docs/README.md` and its folder's How it works file `apps/project-IDE/current-ui/current-ui.index.md`.

## Related knowledge

It is written by `agents/system/.claude/skills/ide-build/scripts/enrich.py`. It is read by `apps/project-IDE/current-ui/file-tree-explorer.html` and `apps/project-IDE/server/server.py`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `apps/project-IDE/docs/README.md` (section "What the page reads").

## Keep in mind

- When it is out of date, rebuild it; never edit it by hand.
