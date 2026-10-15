---
about: agent-os/apps/project-IDE/server/claude_bridge.py
basis: 8d62241e46c7
written: 2026-10-15T10:35:00Z
by: knowledge-base-agent
confirmed: 2026-10-15T10:40:41Z
---
# claude_bridge.py

## What it is

Runs each request from the server page as a Claude Code session through the Claude Agent SDK, so the system's `CLAUDE.md`, agents and skills load as its own. A run that carries notes (every message from the ask box and every send from the Notes and runs panel) works on its own branch: it gets a worktree from `worktrees.py` and Claude Code starts in `.worktrees/<run>/agents/system/`; a follow-up from the same chat continues on that branch while it exists. Delete and Apply changes runs work in the repository itself. Before every step it checks: nothing may touch the keys folder; a file outside the run's checkout, and any tool or command not on the allow list in `server.config.json`, waits for the owner's Allow or Refuse; a page deletion of exactly the item goes ahead. It sets the run's and its notes' status as the run moves (planning when the run uses the `change-plan` skill, need human while an Allow or Refuse waits, then the `STATUS:` line of the answer, cancelled on Stop, failed on error), merges the branch into `main` when the run ends done and the send option says auto merge, asks for the summary, streams every step to the page and logs each run.

## Who looks after it

It is written by project-ide-agent.

## When and how it changes

It changes when a rule on what Claude Code may do, the start folder, the worktree flow or the statuses of a run change.

## Who uses it, and when

It is read by `apps/project-IDE/server/server.py`.

## Where it is mentioned

It is described in `apps/project-IDE/server/README.md` and its folder's How it works file `apps/project-IDE/server/server.index.md`.

## Related knowledge

It is read by `apps/project-IDE/server/server.py`. It reads `apps/project-IDE/server/server.config.json` and `agents/system/CLAUDE.md`, and uses `apps/project-IDE/server/worktrees.py`, `apps/project-IDE/server/notes.py` and `apps/project-IDE/server/run_summary.py`. It writes `agents/system/logs/subagents/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE"), `apps/project-IDE/docs/README.md` (sections "Notes and runs" and "The server") and `agents/system/docs/README.md` (section "Keys and secrets").

## Keep in mind

- Pushing, deleting anything but the item the owner deleted, anything outside the run's checkout and any live action wait for the owner's click; the keys folder is never opened.
- A run with notes never commits on `main` itself: it works on its branch, and only the merge moves `main`.
