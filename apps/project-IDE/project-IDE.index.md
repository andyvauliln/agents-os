---
about: agent-os/apps/project-IDE/
basis: 2690542b190c
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# project-IDE/

## What it is

The owner's IDE for the project, one of the apps: the File Tree page they use to manage, analyse and view the Agent OS while it is built with AI, and everything the page is built from. It serves every AI as much as the owner: for any file it shows what it is for, how it works, what depends on it and what holds for it from the levels above. Like every app it has its own `docs/`: a vision, a README (the full manual of the IDE), its ASD-STE100 twin and a rebuild prompt. `current-ui/` holds the page and its data, as published on claude.ai; `server/` runs the same page on the owner's server, with Claude Code behind its request box; `data/` holds the project's records: every owner input, the decisions, the changelog, the plans, the owner's page edits and the page's store on the server. The build scripts live in `agents/system/.claude/skills/ide-build/scripts/`. It is not the trading dashboard, which is `trading-ui/`.

## Who looks after it

It is written by project-ide-agent, knowledge-base-agent and the owner.

## When and how it changes

It changes when a part of the IDE (the page, the server, the data or its docs) is added, moved or removed.

## Who uses it, and when

It is read by the owner, every AI session on the project, project-ide-agent and knowledge-base-agent.

## Where it is mentioned

It is described in `apps/project-IDE/docs/README.md`, `apps/project-IDE/docs/vision.md`, `apps/project-IDE/docs/rebuild-prompt.md`, `apps/docs/README.md`, `docs/README.md` and its folder's How it works file `apps/apps.index.md`.

## Related knowledge

It is written by `agents/system/.claude/agents/project-ide-agent.md`, `agents/system/.claude/skills/ide-build/SKILL.md` and `agents/system/.claude/skills/ide-sync/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `docs/README.md` (section "The project IDE").

## Keep in mind

- When something changes on the page or in the files it is built from, rebuild the page; never edit its data by hand.
- When the IDE's parts change, bring its own vision, README and rebuild prompt in line, in that order.
