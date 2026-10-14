---
about: agent-os/agents/system/.claude/skills/[skill-name]/SKILL.md
basis: 01336eac60db
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# [skill-name]/SKILL.md

## What it is

The pattern for every further system-level skill: one folder per skill, named after it, with `SKILL.md` as its entry point and any supporting files next to it. The frontmatter carries `name` and `description`, and the body holds the steps (format proposed). A skill is invoked as `/name` or picked up automatically.

## Who looks after it

It is written by the owner and an agent through change-plan.

## When and how it changes

It changes when the format of a skill's front matter or steps changes. It is a name pattern, not a real item: it tells what each item made from it will hold.

## Who uses it, and when

It is read by an agent that makes a new system skill.

## Where it is mentioned

It is described in `agents/system/.claude/skills/` and its folder's How it works file `agents/system/.claude/skills/[skill-name]/[skill-name].index.md`.

## Related knowledge

It has the same format as `agents/system/.claude/skills/change-plan/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Each agent's AI setup") and `agents/system/docs/rebuild-prompt.md` (section "The standard .claude/ folder").

## Keep in mind


