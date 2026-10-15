---
about: agent-os/apps/project-IDE/server/server.py
basis: ea5a2cac0b6e
written: 2026-10-15T10:35:00Z
by: knowledge-base-agent
confirmed: 2026-10-15T11:08:51Z
---
# server.py

## What it is

The small web service behind the page on the owner's server, standard library only. It serves the page and its data from `apps/project-IDE/current-ui/`, keeps the page's comments, edits and messages as one JSON file each in `apps/project-IDE/data/page-store/`, writes an edit to a file's text straight into that file and an edit to How it works into the `x.index.md` next to the item, and hands each request and each deletion to `claude_bridge.py`, streaming its progress back. It also serves the Notes and runs panel: the list of notes and runs, each note's edits, recording, sending and cancelling (through `notes.py`), each run's page and its long steps (through `runs.py`), and a run's summary, merge, discard and stop. It takes a voice recording for a box at `api/voice`, or for a note, which it turns into text in the background. It answers only to the machine's own address.

## Who looks after it

It is written by project-ide-agent.

## When and how it changes

It changes when the page's way of talking to the server, the store, the write-through or a route of the Notes and runs panel changes. Each route change is tested on the page served here.

## Who uses it, and when

It is read by the owner, who starts it; and project-ide-agent.

## Where it is mentioned

It is described in `apps/project-IDE/server/README.md` and its folder's How it works file `apps/project-IDE/server/server.index.md`.

## Related knowledge

It reads `apps/project-IDE/server/server.config.json`, `apps/project-IDE/current-ui/file-tree-explorer.html`, `apps/project-IDE/current-ui/file-tree.data.json`, and hands work to `apps/project-IDE/server/claude_bridge.py`, `apps/project-IDE/server/notes.py`, `apps/project-IDE/server/runs.py`, `apps/project-IDE/server/run_summary.py`, `apps/project-IDE/server/worktrees.py` and `apps/project-IDE/server/voice.py`. It writes `apps/project-IDE/data/page-store/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (sections "Notes and runs" and "The server").

## Keep in mind

- Never open it to the internet: whoever reaches the page can make Claude Code change files and run commands.
- When you change how the page talks to it, test both: the page on claude.ai and the page served here.
- When you add a job, put it in its own file next to this one, as notes, runs, summaries and worktrees are.
