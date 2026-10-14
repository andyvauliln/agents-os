---
about: agent-os/agents/system/.claude/agents/project-ide-agent.md
node: n-10.1.1.3
basis: 7f962b6050fb
written: 2026-10-06T20:55:10Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:02:04Z
---
# project-ide-agent.md

## Summary

The project IDE agent: it looks after the owner's File Tree page, which is also how every AI sees the context of a file. It builds the page from the repository and publishes it, brings back what the owner leaves on it (messages, notes, edits to a file or its How it works, new or deleted items) into the files, runs the requests the owner sends from the page, and deletes cleanly: when the owner deletes a file or folder on the page, it removes it and everything in the project that points to it, keeping the owner's note in mind. It saves every message and edit word for word and hands the knowledge to the knowledge base agent. On the owner's server it can be the Claude Code session behind the page's request box, and it never pushes without the owner's click.

## Keep in mind

- When the owner leaves anything on the page, put it in a file before you clear it from the page.
