---
about: agent-os/agents/system/.claude/agents/knowledge-base-agent.md
node: n-10.1.1.2
basis: 6698c20578fd
written: 2026-10-06T20:55:10Z
by: knowledge-base-agent
confirmed: 2026-10-09T09:57:03Z
---
# knowledge-base-agent.md

## Summary

The knowledge base agent: the project's librarian and writer. It saves every owner message, every answer we give, every change to the system and what a session learned, so nothing gets lost or contradicts itself. From those notes it writes the docs in plain, book-like language, each with that doc's own skill, and keeps the three main docs in line after every update: the vision first, then the README, then the rebuild prompt for AI. The docs are also the context every AI works from, so they must be exact enough to act on: for any file, what it is for, how it works, what depends on it and what holds for it from the levels above. It also keeps the How it works file of every file and folder. The File Tree page itself is looked after by the project IDE agent.

## Keep in mind

- When you write any doc, write for a reader who is not technical: no reference numbers, codes or ids.
- When you mark something decided, make sure the owner said it; otherwise it is an idea or an open question.
- When the owner asks a question, write the answer where they should have found it.
