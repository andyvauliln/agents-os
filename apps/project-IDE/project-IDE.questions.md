# Questions: project-IDE/

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-05: Where is the project IDE folder in the layout?

> sorry i mean like this > i think we should have something like this what do you think?

Agreed. It is the layout today, with one change: the project IDE is `apps/project-IDE/`. It has these folders:

1. `current-ui/` for the page and its data.
2. `data/` for the records of the project.
3. `server/` for the page on the owner's server.
4. `docs/`.

The logic of the IDE is in `agents/system/.claude/`. This is the project IDE agent and the skills `ide-build` and `ide-sync`.

This changed later: the owner moved the project IDE into `apps/` on the same day. While we plan, the records are still in `vision/`.

Docs improved: apps/project-IDE/project-IDE.index.md.
