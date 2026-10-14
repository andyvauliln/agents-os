---
about: agent-os/agents/system/.claude/skills/knowledge-intake/
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
---
# knowledge-intake/

## What it is

The folder of the knowledge-intake skill, which saves each owner input word for word and files its knowledge in the right docs and metadata files. It holds `SKILL.md`, the steps an agent follows; `SKILL.questions.md`, its open questions for the owner; and their metadata files.

## Who looks after it

It is written by the owner and knowledge-base-agent.

## When and how it changes

It changes when a file is added to or removed from the skill folder, or the skill is renamed.

## Who uses it, and when

It is read by knowledge-base-agent and ide-sync.

## Where it is mentioned

It is described in `agents/system/.claude/skills/` and its folder's How it works file `agents/system/.claude/skills/skills.index.md`.

## Related knowledge

It links to `agents/system/.claude/skills/knowledge-intake/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "When and how to update each doc"), `docs/metadata.md` and `agents/system/docs/README.md` (section "The knowledge base and the docs").

## Keep in mind

- When you change the skill, change `SKILL.md` here; the folder holds no other copy.
