---
about: agent-os/agents/system/.claude/agents/knowledge-base-agent.md
basis: edc634c5ae0f
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# knowledge-base-agent.md

## What it is

The knowledge base agent: the project's librarian and writer. It saves every owner message, every answer we give, every change to the system and what a session learned, so nothing gets lost or contradicts itself. From those notes it writes the docs in plain, book-like language, each with that doc's own skill, and keeps the three main docs in line after every update: the vision first, then the README, then the rebuild prompt for AI. The docs are also the context every AI works from, so they must be exact enough to act on: for any file, what it is for, how it works, what depends on it and what holds for it from the levels above. It also keeps the How it works file of every file and folder. The File Tree page itself is looked after by the project IDE agent.

## Who looks after it

It is written by the owner and knowledge-base-agent with knowledge-intake.

## When and how it changes

It changes when the owner changes how knowledge is kept or how a doc is written, or a skill of the agent is added or renamed.

## Who uses it, and when

It is read by Claude Code started in agents/system/ (as a helper) and the owner.

## Where it is mentioned

It is described in `agents/system/docs/README.md` and its folder's How it works file `agents/system/.claude/agents/agents.index.md`.

## Related knowledge

It reads `agents/system/.claude/skills/knowledge-intake/SKILL.md`, `agents/system/.claude/skills/file-index/SKILL.md`, `agents/system/.claude/skills/vision-doc/SKILL.md`, `agents/system/.claude/skills/readme-doc/SKILL.md`, `agents/system/.claude/skills/readme-asd-doc/SKILL.md`, `agents/system/.claude/skills/rebuild-prompt-doc/SKILL.md` and `agents/system/.claude/skills/claude-md-doc/SKILL.md`. It links to `agents/system/.claude/agents/project-ide-agent.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "When and how to update each doc"), `docs/metadata.md` and `agents/system/docs/README.md` (section "The knowledge base and the docs").

## Keep in mind

- When you write any doc, write for a reader who is not technical: no reference numbers, codes or ids.
- When you mark something decided, make sure the owner said it; otherwise it is an idea or an open question.
- When the owner asks a question, write the answer where they should have found it.
