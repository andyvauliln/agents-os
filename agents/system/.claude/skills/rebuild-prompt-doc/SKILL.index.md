---
about: agent-os/agents/system/.claude/skills/rebuild-prompt-doc/SKILL.md
basis: 3117c7ff2381
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# rebuild-prompt-doc/SKILL.md

## What it is

The skill the knowledge base agent uses to write the rebuild prompt, the instructions an AI coding agent follows to rebuild the whole system from an empty repository and end with the same working system. Its outline lists the sections (the task, ground rules, the full tree, conventions, every part, the build order, the acceptance checks, what not to build), and the File Tree page shows it as the prompt's Example. It says how to write for AI: exact names and formats, clear status, checks that can be run, never a secret value. The prompt is updated last, after every change to the design. Every level has its own: a domain's, strategy's or trading agent's prompt builds only its own folder, assumes the levels above and lists its children's prompts in build order.

## Who looks after it

It is written by the owner and knowledge-base-agent.

## When and how it changes

It changes when the owner changes what a rebuild prompt must hold, its outline or how lower levels get their own.

## Who uses it, and when

It is read by knowledge-base-agent.

## Where it is mentioned

It is described in its folder's How it works file `agents/system/.claude/skills/rebuild-prompt-doc/rebuild-prompt-doc.index.md`.

## Related knowledge

It writes `agents/system/docs/rebuild-prompt.md` and `docs/rebuild-prompt.md`. It is read by `agents/system/.claude/agents/knowledge-base-agent.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "When and how to update each doc"), `docs/metadata.md` and `agents/system/docs/README.md` (section "The knowledge base and the docs").

## Keep in mind

- When you write the prompt, take every path and format from the files on disk and `docs/file-tree.md`.
- When something is still open, put it under 'Do not build' with what to leave in its place.
- When you change this doc at one level, check the same doc at the level above and climb to the system.
