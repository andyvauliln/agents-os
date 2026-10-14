---
about: agent-os/apps/project-IDE/data/page-store/
node: n-53.2.7
basis: f0ca5b844679
written: 2026-10-05T15:37:34Z
by: knowledge-base-agent
confirmed: 2026-10-06T10:52:16Z
---
# page-store/

## Summary

On the owner's server, the page's own store as files: `nodes/`, `changes/` and `inputs/`, one JSON document per file, the same documents the page keeps on claude.ai. The server page writes them the moment the owner saves a note, an edit or a message; a request typed on the page is in `inputs/` with its answer, cost and session. The project IDE agent folds them into the files with ide-sync, as it does with the claude.ai store.

## Keep in mind

- When you fold a document into the files, mark it processed or delete its file; never drop the owner's words.
