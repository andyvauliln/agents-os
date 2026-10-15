---
about: agent-os/apps/project-IDE/server/notes.py
basis: 576c943c33d5
written: 2026-10-15T10:32:00Z
by: knowledge-base-agent
confirmed: 2026-10-15T10:40:41Z
---
# notes.py

## What it is

Keeps the rows of the Notes and runs panel. A note is anything the owner types or records for Claude Code on the server page; each is one file in `apps/project-IDE/data/page-store/notes/`, with its text, status, checkbox, where it was made (ask box, notes panel or selection, with the item, tab, selected text and line) and the versions it was sent from and merged at. A run record is one file per run in `agents/system/logs/subagents/project-ide-agent/runs/`, with what the transcript lacks: status, notes, send options, branch, summary and tags. It sorts the list (need human first, then at work, then newest), combines notes into one request, and reads the `STATUS:` line at the end of a run's answer. Git ignores both folders.

## Who looks after it

It is written by project-ide-agent.

## When and how it changes

It changes when the owner wants a new status, a new field on a note or a run, or a new send option.

## Who uses it, and when

It is read by `apps/project-IDE/server/server.py` for every notes and runs route, and by `apps/project-IDE/server/claude_bridge.py`, which sets each run's and note's status as the run moves.

## Where it is mentioned

It is described in `apps/project-IDE/server/README.md`, `apps/project-IDE/docs/README.md`, `apps/project-IDE/docs/rebuild-prompt.md` and its folder's How it works file `apps/project-IDE/server/server.index.md`.

## Related knowledge

It reads `send_options` in `apps/project-IDE/server/server.config.json`. The run that takes a note files its words as an owner input in `apps/project-IDE/data/inputs/`, and `ide-sync` only checks notes left ready. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (sections "Notes and runs", "The page of a run" and "The server").

## Keep in mind

- When you add a status, add it to the page's rows and the docs in the same round.
- After a restart, notes and runs that were at work become failed: never leave one at work with no run behind it.
