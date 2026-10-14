---
about: agent-os/apps/project-IDE/server/
basis: 38db3c3d1c39
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# server/

## What it is

The File Tree page on the owner's own server, with Claude Code behind its request box. It is the same page as on claude.ai: here it finds this service next to it, keeps the owner's notes and messages as files in the repository, writes edits to a file or its How it works straight into the file, and sends each request to Claude Code, which starts in `agents/system/`, works in the repository and shows each step on the page. A Delete pressed on the page goes to Claude Code at once. Pushing, other deletions and anything outside the repository wait for the owner's click. `server.py` serves the page and the files, `claude_bridge.py` runs the requests, `voice.py` turns voice recordings into text through Groq, `server.config.json` holds the settings and `README.md` says how to start it and reach it safely.

## Who looks after it

It is written by project-ide-agent.

## When and how it changes

It changes when the owner asks for a change to the server page.

## Who uses it, and when

It is read by the owner and project-ide-agent.

## Where it is mentioned

It is described in `apps/project-IDE/server/README.md`, `apps/project-IDE/docs/README.md` and its folder's How it works file `apps/project-IDE/project-IDE.index.md`.

## Related knowledge

It reads `apps/project-IDE/current-ui/file-tree-explorer.html` and `agents/system/CLAUDE.md`. It writes `apps/project-IDE/data/page-store/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (section "The server").

## Keep in mind

- Reachable only from the machine or through an SSH tunnel, never the open internet.
- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
