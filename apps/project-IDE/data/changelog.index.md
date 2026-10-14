---
about: agent-os/apps/project-IDE/data/changelog.md
basis: 6b0d58819d82
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# changelog.md

## What it is

The project's history: what changed, when and why, newest first. Each entry gives the date, the change, the area and the decision or input behind it; per-agent changes stay in the agents' own folders and logs. The knowledge base agent adds an entry for every round. It sits with the project's other records (inputs, decisions, plans) in `apps/project-IDE/data/`.

## Who looks after it

It is written by knowledge-base-agent and knowledge-intake.

## When and how it changes

Every round adds an entry.

## Who uses it, and when

It is read by the owner, every AI session on the project and `agents/system/.claude/skills/ide-build/scripts/enrich.py`.

## Where it is mentioned

It is described in its folder's How it works file `apps/project-IDE/data/data.index.md`.

## Related knowledge

It links to `apps/project-IDE/data/decisions.md` and `apps/project-IDE/data/inputs/index.json`. It is written by `agents/system/.claude/skills/knowledge-intake/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/CLAUDE.md` (section "After every input or update").

## Keep in mind

- When you finish a round that changed the system, add its entry here in the same change.
