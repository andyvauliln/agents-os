---
about: agent-os/apps/project-IDE/server/
basis: dd835944ef0d
written: 2026-10-15T10:37:00Z
by: knowledge-base-agent
confirmed: 2026-10-15T10:40:56Z
---
# server/

## What it is

The File Tree page on the owner's own server, with Claude Code behind it. It is the same page as on claude.ai: here it finds this service next to it, writes edits to a file or its How it works straight into the file, and sends each request to Claude Code, which shows each step on the page. A Notes and runs panel in the header lists every note the owner types or records and every Claude Code run in the repository, from the page or a terminal; notes sent together become one run, and each run from the page works on its own branch in `.worktrees/` until it is merged into `main` here. Each run has a page with every step. Pushing, other deletions and anything outside the repository wait for the owner's click. The files, one job each: `server.py` serves the page and the routes, `claude_bridge.py` runs the requests, `notes.py` keeps notes and run records, `runs.py` reads Claude Code's transcripts, `run_summary.py` writes each run's summary and tags, `worktrees.py` makes and merges each run's branch, `voice.py` turns recordings into text through Groq, `server.config.json` holds the settings and `README.md` says how to start it and use it.

## Who looks after it

It is written by project-ide-agent.

## When and how it changes

It changes when the owner asks for a change to the server page, its panel or the way runs work and reach `main`.

## Who uses it, and when

It is read by the owner and project-ide-agent.

## Where it is mentioned

It is described in `apps/project-IDE/server/README.md`, `apps/project-IDE/docs/README.md` and its folder's How it works file `apps/project-IDE/project-IDE.index.md`.

## Related knowledge

It reads `apps/project-IDE/current-ui/file-tree-explorer.html`, `agents/system/CLAUDE.md` and Claude Code's own transcripts. It writes `apps/project-IDE/data/page-store/`, `agents/system/logs/subagents/project-ide-agent/` and `.worktrees/`. The rules that apply to it come from `agents/system/CLAUDE.md` (sections "Rules" and "The File Tree page"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (sections "Notes and runs", "The page of a run" and "The server").

## Keep in mind

- Reachable only from the machine or through an SSH tunnel, never the open internet.
- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
