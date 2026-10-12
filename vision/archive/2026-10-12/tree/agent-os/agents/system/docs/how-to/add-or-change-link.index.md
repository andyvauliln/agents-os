---
about: agent-os/agents/system/docs/how-to/add-or-change-link.md
node: n-2.11.9
basis: 5068df044a4b
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# add-or-change-link.md

## Summary

The runbook for linking a file an agent needs from anywhere under `agents/`, or changing or removing such a link. The agent finds the file (preferring a stable `latest.*` output), edits one entry in its own links file, lets relink build the symlink and reads its report, adds the path to `on_change` if a change must restart its main run, and records the change in `changes.md`. The steps are proposed; whether a link change makes a new version is open.

## Keep in mind

- When you add, change or remove a link, edit your own links file and let relink act; never create or delete a symlink by hand.
- When you choose a link target, never link anything in `.secrets/` or any `.claude/`, and never put `to` inside `subagents.link/`.
