---
about: agent-os/apps/project-IDE/data/
basis: ee3451b422be
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# data/

## What it is

This project's records and the data the page uses, in one place any AI session can read to catch up. It holds every owner input word for word in `inputs/`, the decision log `decisions.md`, the changelog, the change plans in `plans/`, `overrides.json` (the owner's page edits of the extra tables) and `page-store/` (on the owner's server, the page's notes, edits and messages as files). `archive/` is for retired files. `README.md` is the guide to these records. `sources/` keeps the earlier knowledge notes and the earlier prediction-market metadata files, kept but not referenced.

## Who looks after it

It is written by knowledge-base-agent and project-ide-agent.

## When and how it changes

It changes when a record is added: an input, a decision, a changelog line or a plan.

## Who uses it, and when

It is read by every AI session on the project, project-ide-agent, knowledge-base-agent, `agents/system/.claude/skills/ide-build/scripts/enrich.py` and `agents/system/.claude/skills/ide-build/scripts/build_map.py`.

## Where it is mentioned

It is described in `apps/project-IDE/data/README.md`, `apps/project-IDE/docs/README.md` and its folder's How it works file `apps/project-IDE/project-IDE.index.md`.

## Related knowledge

It is written by `agents/system/.claude/skills/knowledge-intake/SKILL.md` and `agents/system/.claude/skills/ide-sync/SKILL.md`. It is read by `agents/system/.claude/skills/ide-build/scripts/enrich.py`. It links to `apps/project-IDE/data/plans/2026-10-13-leave-vision.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (section "How it is laid out").

## Keep in mind

- When the owner says anything about the system, store it in `inputs/` word for word before filing its knowledge.
- When you look for how an item works or why, read its own metadata files and the docs, not the earlier notes here.
