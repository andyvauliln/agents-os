---
about: agent-os/agents/system/.claude/skills/ide-sync/
basis: c1ba1a1d84fd
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# ide-sync/

## What it is

The folder of the ide-sync skill, which brings everything the owner left on the File Tree page back into the files. It holds `SKILL.md`, the steps an agent follows; `SKILL.questions.md`, its open questions for the owner; and their metadata files.

## Who looks after it

It is written by the owner, project-ide-agent and knowledge-base-agent.

## When and how it changes

It changes when a file is added to or removed from the skill folder, or the skill is renamed.

## Who uses it, and when

It is read by project-ide-agent and the server's Claude Code session.

## Where it is mentioned

It is described in `agents/system/.claude/skills/` and its folder's How it works file `agents/system/.claude/skills/skills.index.md`.

## Related knowledge

It links to `agents/system/.claude/skills/ide-sync/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "The File Tree page"), `docs/metadata.md`, `agents/system/docs/README.md` (section "The project IDE"), `apps/project-IDE/docs/README.md` (section "How the page is built and checked") and `apps/project-IDE/docs/README.md` (section "How the owner's work comes back").

## Keep in mind

- When you change the skill, change `SKILL.md` here; the folder holds no other copy.
