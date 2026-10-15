---
about: agent-os/apps/project-IDE/server/run_summary.py
basis: 8aebb94ff8ba
written: 2026-10-15T10:32:00Z
by: knowledge-base-agent
confirmed: 2026-10-15T10:40:41Z
---
# run_summary.py

## What it is

Writes a short summary of a finished run, 4 to 10 sentences in ASD-STE100, and one to four tags (question, change, fix, docs, ui, server, setup, sync, plan, research, delete, failed, waiting; a new one only when none fits). It hands Claude Haiku the request, the answer, one line per step and the files changed, from a folder outside the repository with its own short instructions, so it loads no project settings and is never listed as a run. It runs after each page run, in the background for finished terminal runs in the list, and again on the run page's Write it again. One summary costs about half a cent to one cent.

## Who looks after it

It is written by project-ide-agent.

## When and how it changes

It changes when the owner wants another model, another tag list or another length of summary.

## Who uses it, and when

It is read by `apps/project-IDE/server/server.py` and `apps/project-IDE/server/claude_bridge.py`; the summary and tags go into the run's record.

## Where it is mentioned

It is described in `apps/project-IDE/server/README.md`, `apps/project-IDE/docs/README.md`, `apps/project-IDE/docs/rebuild-prompt.md` and its folder's How it works file `apps/project-IDE/server/server.index.md`.

## Related knowledge

It reads `runs.summary_model` in `apps/project-IDE/server/server.config.json` and a run from `apps/project-IDE/server/runs.py`. Its writing rules are those of ASD-STE100, as in `docs/metadata.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (sections "Notes and runs", "The page of a run" and "The server").

## Keep in mind

- When you change the tag list, change it in the docs too, so the owner's filters keep their meaning.
