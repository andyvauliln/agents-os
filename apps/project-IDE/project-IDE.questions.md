# Questions: project-IDE/

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-05: The project IDE folder in the layout

> sorry i mean like this > i think we should have something like this what do you think?

Agreed, and it is the layout today with one change: the project IDE is `apps/project-IDE/`, with `current-ui/` for the page and its data, `data/` for the project's records, `server/` for the page on the owner's server, and `docs/`. The IDE's logic, the project IDE agent and the skills `ide-build` and `ide-sync`, lives in `agents/system/.claude/`. This changed later: the owner moved it into `apps/` the same day, and while we plan the records are still kept in `vision/`.

Docs improved: apps/project-IDE/project-IDE.index.md.
