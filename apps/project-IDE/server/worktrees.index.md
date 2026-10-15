---
about: agent-os/apps/project-IDE/server/worktrees.py
basis: a6db7467465d
written: 2026-10-15T10:32:00Z
by: knowledge-base-agent
confirmed: 2026-10-15T10:40:41Z
---
# worktrees.py

## What it is

Gives each run from the page its own branch and checkout, so several runs can work at once without touching the files the server shows. For a run it makes the branch `ide/<date>-<subject>` from `main` and a git worktree in `.worktrees/<run>/` at the top of the repository (git ignores that folder). It merges a finished run: it brings the branch up to date with `main`, rebuilds the built files when only they conflict (the page data, `real-files.json`, `docs/file-tree.md`) and stops with "need human" on any other conflict, then moves `main` forward in the repository the server shows and rebuilds the page. It also removes or discards a run's worktree and branch.

## Who looks after it

It is written by project-ide-agent.

## When and how it changes

It changes when the way a run gets its branch, or the way a branch reaches `main`, changes. Pull requests on GitHub are a later step of the plan and will change it.

## Who uses it, and when

It is read by `apps/project-IDE/server/claude_bridge.py`, which makes a worktree when a run with notes starts, and by `apps/project-IDE/server/server.py` for Merge into main and Discard the branch on a run page.

## Where it is mentioned

It is described in `apps/project-IDE/server/README.md`, `apps/project-IDE/docs/README.md`, `apps/project-IDE/docs/rebuild-prompt.md` and its folder's How it works file `apps/project-IDE/server/server.index.md`.

## Related knowledge

It reads `worktrees` in `apps/project-IDE/server/server.config.json` and runs `agents/system/.claude/skills/ide-build/scripts/rebuild.py` after a merge. `.gitignore` keeps `.worktrees/` out of git. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (sections "Notes and runs", "The page of a run" and "The server").

## Keep in mind

- When you change the merge, keep it a fast-forward of `main` on this server: it never pushes.
- When a conflict is in any file but the three built files, stop and ask the owner; never pick a side.
