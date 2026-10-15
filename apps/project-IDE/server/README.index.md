---
about: agent-os/apps/project-IDE/server/README.md
basis: e570e83d6553
written: 2026-10-15T07:11:30Z
by: knowledge-base-agent
confirmed: 2026-10-15T07:11:37Z
---
# README.md

## What it is

The owner's guide to the server page: what the server needs (the repository, Python, Node, Claude Code and its SDK, a way for Claude Code to sign in), how to set it up once with `./init.sh` and start or restart it with `./start.sh` from the top of the repository (sync, stop the old server, rebuild, start; a service starts it at boot), the manual start with `server.py`, how to open it through an SSH tunnel, what happens to notes, edits and requests, which steps wait for the owner's click, and what every setting does. It also explains voice input: the microphone button, the Groq key it needs and how a model that hits its limit is skipped.

## Who looks after it

It is written by project-ide-agent.

## When and how it changes

It changes when a setting, a start step (`init.sh`, `start.sh`) or a safety rule of the server changes.

## Who uses it, and when

It is read by the owner.

## Where it is mentioned

It is described in its folder's How it works file `apps/project-IDE/server/server.index.md`.

## Related knowledge

It links to `apps/project-IDE/server/server.config.json`, `apps/project-IDE/server/server.py`, `apps/project-IDE/server/voice.py` and the start scripts `init.sh` and `start.sh` at the top of the repository. It has the same format as `apps/project-IDE/docs/README.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (section "The server").

## Keep in mind


