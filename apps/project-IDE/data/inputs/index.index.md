---
about: agent-os/apps/project-IDE/data/inputs/index.json
basis: 5245735d9611
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# index.json

## What it is

The list of every owner input, one row each, with its categories, a one-line summary and what it was processed into. The knowledge base agent adds a row when it stores an input, page messages included, and fills in what the input changed once its knowledge is placed.

## Who looks after it

It is written by knowledge-base-agent and knowledge-intake.

## When and how it changes

It changes when an input is stored, or its knowledge is placed.

## Who uses it, and when

It is read by knowledge-base-agent and `agents/system/.claude/skills/ide-build/scripts/enrich.py`.

## Where it is mentioned

It is described in `apps/project-IDE/data/inputs/README.md` and its folder's How it works file `apps/project-IDE/data/inputs/inputs.index.md`.

## Related knowledge

It is read by `agents/system/.claude/skills/ide-build/scripts/enrich.py`. It is written by `agents/system/.claude/skills/knowledge-intake/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules") and `docs/metadata.md` (section "Owner inputs").

## Keep in mind

- When you add a row, fill `processed_into` once the knowledge is placed; an input is not finished until then.
