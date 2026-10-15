---
about: agent-os/apps/project-IDE/server/README.md
basis: 2db420e07765
written: 2026-10-15T10:45:00Z
by: knowledge-base-agent
confirmed: 2026-10-15T11:08:51Z
---
# README.md

## What it is

The owner's guide to the server page: what the server needs (the repository, Python, Node, Claude Code and its SDK, a way for Claude Code to sign in), how to set it up once with `./init.sh` and start or restart it with `./start.sh` from the top of the repository (sync, stop the old server, rebuild, start; a service starts it at boot), the manual start with `server.py`, how to open it through an SSH tunnel, and what happens when the owner uses it: edits, the ask box, the Notes and runs panel with its statuses and send options, each run on its own branch in `.worktrees/` and its merge into `main`, the page of a run, voice notes, Delete, Apply changes and the steps that wait for the owner's click. It ends with every setting and every file of the folder.

## Who looks after it

It is written by project-ide-agent.

## When and how it changes

It changes when a setting, a start step (`init.sh`, `start.sh`), a safety rule, a file of the server or the way notes and runs work changes.

## Who uses it, and when

It is read by the owner.

## Where it is mentioned

It is described in its folder's How it works file `apps/project-IDE/server/server.index.md`.

## Related knowledge

It links to `apps/project-IDE/server/server.config.json`, every code file of the server (`server.py`, `claude_bridge.py`, `notes.py`, `runs.py`, `run_summary.py`, `worktrees.py`, `voice.py`) and the start scripts `init.sh` and `start.sh` at the top of the repository. It has the same format as `apps/project-IDE/docs/README.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (section "The server").

## Keep in mind


