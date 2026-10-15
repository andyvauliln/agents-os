---
about: agent-os/apps/project-IDE/server/runs.py
basis: 0203ad88cc86
written: 2026-10-15T10:32:00Z
by: knowledge-base-agent
confirmed: 2026-10-15T11:08:51Z
---
# runs.py

## What it is

Turns Claude Code's own transcripts into runs for the Notes and runs panel and the page of a run. It reads every session whose folder is inside the repository, from a terminal or from the page, and the subagents' transcripts inside each session. For the list it gives a short row per session (title, page or terminal, folder, branch, model, steps, largest context, and live while the transcript changed in the last 90 seconds); for the run page it gives every step with its input, output, time, duration, error and context size, the subagents' own steps nested inside, the totals, the checks the run ran, the plans it wrote and the commits it made. It copies nothing and writes nothing.

## Who looks after it

It is written by project-ide-agent.

## When and how it changes

It changes when Claude Code changes the format of its transcripts, or the owner wants more on the run page. A change here is checked by opening a few real runs on the page.

## Who uses it, and when

It is read by `apps/project-IDE/server/server.py` for the run list and each run page, and by `apps/project-IDE/server/run_summary.py`, which summarises a run from what this file returns.

## Where it is mentioned

It is described in `apps/project-IDE/server/README.md`, `apps/project-IDE/docs/README.md`, `apps/project-IDE/docs/rebuild-prompt.md` and its folder's How it works file `apps/project-IDE/server/server.index.md`.

## Related knowledge

It reads Claude Code's transcripts in its settings folder (`runs.claude_config_dir` in `apps/project-IDE/server/server.config.json`, else `CLAUDE_CONFIG_DIR`, else `~/.claude`) and git for the commits. The run records that add status, notes and summary are kept by `apps/project-IDE/server/notes.py`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (sections "Notes and runs", "The page of a run" and "The server").

## Keep in mind

- When Claude Code is updated and the run page shows wrong or empty steps, check the transcript format here first.
- Never write into the transcripts: they belong to Claude Code.
- The list shows only sessions that started at or after `runs.since` in `server.config.json` (now the start of the session that built the panel); empty it to list every session again.
