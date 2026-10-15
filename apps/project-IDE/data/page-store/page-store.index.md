---
about: agent-os/apps/project-IDE/data/page-store/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# page-store/

## What it is

On the owner's server, the page's own store as files: `nodes/`, `changes/` and `inputs/`, one JSON document per file, the same documents the page keeps on claude.ai. The server page writes them the moment the owner saves a note, an edit or a message; a request typed on the page is in `inputs/` with its answer, cost and session. The project IDE agent folds them into the files with ide-sync, as it does with the claude.ai store.

## Who looks after it

It is written by `apps/project-IDE/server/server.py`.

## When and how it changes

It changes when the owner saves a note, an edit or a message on the server page; a sync folds the documents into the files. It is empty for now.

## Who uses it, and when

It is read by project-ide-agent and ide-sync.

## Where it is mentioned

It is described in `apps/project-IDE/docs/README.md` and its folder's How it works file `apps/project-IDE/data/data.index.md`.

## Related knowledge

It is written by `apps/project-IDE/server/server.py`. It is read by `agents/system/.claude/skills/ide-sync/SKILL.md`. It links to `apps/project-IDE/server/server.config.json`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `apps/project-IDE/docs/README.md` (section "How the owner's work comes back").

## Keep in mind

- When you fold a document into the files, mark it processed or delete its file; never drop the owner's words.
