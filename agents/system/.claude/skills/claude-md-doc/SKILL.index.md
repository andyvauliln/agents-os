---
about: agent-os/agents/system/.claude/skills/claude-md-doc/SKILL.md
basis: e91e706cc6cd
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# claude-md-doc/SKILL.md

## What it is

The skill that writes and keeps `agents/system/CLAUDE.md`, the file Claude Code reads first when it starts in the system folder. It says what the project is and its stage, the docs to read in order, the lasting rules, the steps after every input or update, and which doc each kind of change makes stale. It is used when the stage, the reading list, a rule or the steps of a round change.

## Who looks after it

It is written by the owner and knowledge-base-agent.

## When and how it changes

It changes when the owner changes what CLAUDE.md must hold or how it is kept.

## Who uses it, and when

It is read by knowledge-base-agent.

## Where it is mentioned

It is described in `agents/system/docs/README.md` and its folder's How it works file `agents/system/.claude/skills/claude-md-doc/claude-md-doc.index.md`.

## Related knowledge

It writes `agents/system/CLAUDE.md`. It is read by `agents/system/.claude/agents/knowledge-base-agent.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "When and how to update each doc"), `docs/metadata.md` and `agents/system/docs/README.md` (section "The knowledge base and the docs").

## Keep in mind


