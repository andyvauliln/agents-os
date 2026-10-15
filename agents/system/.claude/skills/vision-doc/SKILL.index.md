---
about: agent-os/agents/system/.claude/skills/vision-doc/SKILL.md
basis: d68df4e4687e
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# vision-doc/SKILL.md

## What it is

The skill the knowledge base agent uses to write the vision, the top-level doc: what we are building and why, the concept, how the system should work, the business logic, worked examples, where we are and what is open, ending with where to go deeper. Its outline lists the twelve sections and what goes in each, and the File Tree page shows that outline as the vision's Example. It keeps the vision high, with no folders or files, sets lengths for each level, says how to update the doc after a new input, and what the vision's How it works panel answers.

## Who looks after it

It is written by the owner and knowledge-base-agent.

## When and how it changes

It changes when the owner changes what a vision must hold, its sections, lengths or update steps.

## Who uses it, and when

It is read by knowledge-base-agent.

## Where it is mentioned

It is described in its folder's How it works file `agents/system/.claude/skills/vision-doc/vision-doc.index.md`.

## Related knowledge

It writes `agents/system/docs/vision.md` and `docs/vision.md`. It links to `agents/system/.claude/skills/readme-doc/SKILL.md`. It is read by `agents/system/.claude/agents/knowledge-base-agent.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "When and how to update each doc"), `docs/metadata.md` and `agents/system/docs/README.md` (section "The knowledge base and the docs").

## Keep in mind

- When you update the vision, rewrite the sections an input touches; never add 'Update:' notes.
- When the vision changes, bring the README and then the rebuild prompt in line.
- When you change this doc at one level, check the same doc at the level above and climb to the system.
