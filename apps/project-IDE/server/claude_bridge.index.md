---
about: agent-os/apps/project-IDE/server/claude_bridge.py
node: n-53.3.3
basis: cec23e79d846
written: 2026-10-07T14:21:32Z
by: knowledge-base-agent
---
# claude_bridge.py

## Summary

Runs each request typed on the server page as a Claude Code session through the Claude Agent SDK, started in `agents/system/`, so the system's `CLAUDE.md`, agents and skills load as its own. A follow-up in the same box continues the same session. Before every step it checks: nothing may touch the keys folder; a file outside the repository, and any tool or command not on the allow list in `server.config.json` (push, delete, installs, network tools), waits for the owner's Allow or Refuse on the page. When the owner pressed Delete on the page, the request carries that item, and one command that deletes exactly it and its How it works and Details files goes ahead without a second click; Claude Code then cleans the project of it as the sync skill says, keeping the owner's note in mind. It streams the text, the steps, the questions and the result with its cost and time, tells the page every file the request changed, even when Claude Code committed them, so the page marks them changed, and logs each request, with every step that waited for the owner in full, in the project IDE agent's log folder.

## Keep in mind

- Pushing, deleting anything but the item the owner deleted, anything outside the repository and any live action wait for the owner's click; the keys folder is never opened.
