---
about: agent-os/apps/project-IDE/data/README.md
basis: b6057092e4f7
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# README.md

## What it is

The guide to the records folder: a table of what each part holds (`inputs/`, `decisions.md`, `changelog.md`, `plans/`, `archive/`, `sources/`, `overrides.json`, `page-store/`) and how the records change. Every owner input goes through `knowledge-intake`; a change that alters the system is planned first with `change-plan`. The records are history: nothing in them is rewritten, only added.

## Who looks after it

It is written by knowledge-base-agent and knowledge-intake.

## When and how it changes

It changes when a part of the records folder is added, removed or used differently.

## Who uses it, and when

It is read by knowledge-base-agent, project-ide-agent and every AI session on the project.

## Where it is mentioned

It is described in `apps/project-IDE/docs/README.md` and its folder's How it works file `apps/project-IDE/data/data.index.md`.

## Related knowledge

It links to `agents/system/.claude/skills/knowledge-intake/SKILL.md` and `apps/project-IDE/data/inputs/README.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `apps/project-IDE/docs/README.md` (section "Where each part's docs are").

## Keep in mind

- When you add a part to the records folder, add its row to the table here.
