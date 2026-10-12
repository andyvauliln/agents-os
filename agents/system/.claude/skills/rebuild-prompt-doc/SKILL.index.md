---
about: agent-os/agents/system/.claude/skills/rebuild-prompt-doc/SKILL.md
node: n-10.1.2.7
basis: 7131f2517688
written: 2026-10-07T08:58:18Z
by: knowledge-base-agent
---
# rebuild-prompt-doc/SKILL.md

## Summary

The skill the knowledge base agent uses to write the rebuild prompt, the instructions an AI coding agent follows to rebuild the whole system from an empty repository and end with the same working system. Its outline lists the sections (the task, ground rules, the full tree, conventions, every part, the build order, the acceptance checks, what not to build), and the File Tree page shows it as the prompt's Example. It says how to write for AI: exact names and formats, clear status, checks that can be run, never a secret value. The prompt is updated last, after every change to the design. Every level has its own: a domain's, strategy's or trading agent's prompt builds only its own folder, assumes the levels above and lists its children's prompts in build order.

## Keep in mind

- When you write the prompt, take every path and format from the tree notes.
- When something is still open, put it under 'Do not build' with what to leave in its place.
- When you change this doc at one level, check the same doc at the level above and climb to the system.
