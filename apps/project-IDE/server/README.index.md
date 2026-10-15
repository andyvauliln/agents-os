---
about: agent-os/apps/project-IDE/server/README.md
basis: 52ce4f35e529
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# README.md

## What it is

The owner's guide to the server page: what the server needs (the repository, Python, Node, Claude Code and its SDK, a way for Claude Code to sign in), how to start the service from the top of the repository and open it through an SSH tunnel, what happens to notes, edits and requests, which steps wait for the owner's click, and what every setting does. It also explains voice input: the microphone button, the Groq key it needs and how a model that hits its limit is skipped.

## Who looks after it

It is written by project-ide-agent.

## When and how it changes

It changes when a setting, a start step or a safety rule of the server changes.

## Who uses it, and when

It is read by the owner.

## Where it is mentioned

It is described in its folder's How it works file `apps/project-IDE/server/server.index.md`.

## Related knowledge

It links to `apps/project-IDE/server/server.config.json`, `apps/project-IDE/server/server.py` and `apps/project-IDE/server/voice.py`. It has the same format as `apps/project-IDE/docs/README.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (section "The server").

## Keep in mind


