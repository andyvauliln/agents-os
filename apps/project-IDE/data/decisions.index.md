---
about: agent-os/apps/project-IDE/data/decisions.md
basis: 9318efadc87d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-15T07:11:37Z
---
# decisions.md

## What it is

The decision log: a history of what the owner decided, when, why and from which input, so settled questions are not reopened. Each entry has its number, date, decision, reasons, sources and a status: decided, proposed (an agent's idea waiting for the owner's yes) or replaced (kept for history, with what replaced it). The rule a decision made lives in the doc or metadata file that owns it. The page reads the log to show a decision when one is named. It sits with the project's other records in `apps/project-IDE/data/`.

## Who looks after it

It is written by knowledge-base-agent and knowledge-intake.

## When and how it changes

It changes when the owner decides something that changes the system, its rules or its structure. The page reads it in every build, through `enrich.py`, to show a decision when one is named.

## Who uses it, and when

It is read by every AI session on the project and the owner.

## Where it is mentioned

It is described in `docs/metadata.md` and its folder's How it works file `apps/project-IDE/data/data.index.md`.

## Related knowledge

It links to `apps/project-IDE/data/inputs/index.json` and `apps/project-IDE/data/changelog.md`. It is written by `agents/system/.claude/skills/knowledge-intake/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules") and `docs/metadata.md` (section "Decisions").

## Keep in mind

- When you record a decision, write the rule in the file that owns it; this log only says what, when and why.
- When an agent proposes a change, add it here as proposed and wait for the owner.
- When a decision is replaced, mark the old entry replaced instead of editing or deleting it.
