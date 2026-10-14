---
about: agent-os/agents/system/.claude/agents/project-ide-agent.md
basis: de23647519c1
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# project-ide-agent.md

## What it is

The project IDE agent: it looks after the owner's File Tree page, which is also how every AI sees the context of a file. It builds the page from the repository and publishes it, brings back what the owner leaves on it (messages, notes, edits to a file or its How it works, new or deleted items) into the files, runs the requests the owner sends from the page, and deletes cleanly: when the owner deletes a file or folder on the page, it removes it and everything in the project that points to it, keeping the owner's note in mind. It saves every message and edit word for word and hands the knowledge to the knowledge base agent. On the owner's server it can be the Claude Code session behind the page's request box, and it never pushes without the owner's click.

## Who looks after it

It is written by the owner and knowledge-base-agent.

## When and how it changes

It changes when the way the page is built, synced or deleted from changes, or its skills change.

## Who uses it, and when

It is read by Claude Code started in agents/system/ (as a helper), the server's Claude Code session behind the page's request box and the owner.

## Where it is mentioned

It is described in `apps/project-IDE/docs/README.md` and its folder's How it works file `agents/system/.claude/agents/agents.index.md`.

## Related knowledge

It reads `agents/system/.claude/skills/ide-build/SKILL.md`, `agents/system/.claude/skills/ide-sync/SKILL.md` and `agents/system/.claude/skills/file-index/SKILL.md`. It writes `apps/project-IDE/current-ui/file-tree-explorer.html` and `apps/project-IDE/current-ui/file-tree.data.json`. It links to `agents/system/.claude/agents/knowledge-base-agent.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "The File Tree page"), `docs/metadata.md`, `agents/system/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (section "How the page is built and checked").

## Keep in mind

- When the owner leaves anything on the page, put it in a file before you clear it from the page.
