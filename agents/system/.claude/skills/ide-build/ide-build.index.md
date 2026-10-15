---
about: agent-os/agents/system/.claude/skills/ide-build/
basis: 482e931898ab
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# ide-build/

## What it is

The skill that builds the File Tree page from the repository, checks it and publishes it, with its scripts inside it so the two move together. `SKILL.md` gives the steps; `scripts/` holds the build scripts and the page check. The project IDE agent runs it after every round that changes the tree, a doc or a How it works file.

## Who looks after it

It is written by the owner, project-ide-agent and knowledge-base-agent.

## When and how it changes

It changes when a file is added to or removed from the skill or its scripts folder.

## Who uses it, and when

It is read by project-ide-agent and ide-sync (its last step).

## Where it is mentioned

It is described in `agents/system/.claude/skills/` and its folder's How it works file `agents/system/.claude/skills/skills.index.md`.

## Related knowledge

It links to `agents/system/.claude/skills/ide-build/SKILL.md` and `agents/system/.claude/skills/ide-build/scripts/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "The File Tree page"), `docs/metadata.md`, `agents/system/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (section "How the page is built and checked").

## Keep in mind


