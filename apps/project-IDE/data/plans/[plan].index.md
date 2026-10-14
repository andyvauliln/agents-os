---
about: agent-os/apps/project-IDE/data/plans/[plan].md
basis: 674b4c90b427
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# [plan].md

## What it is

The name pattern for one plan for one change request, written for the owner in plain words with the `change-plan` skill: what was asked, what it is for, what exists today, the change part by part, the choices with a recommended default, the steps with a check for each, what it touches, where its knowledge goes once built, and a log of what happened. It is named by the request's date and subject. It stays a proposal until the owner says go.

## Who looks after it

It is written by knowledge-base-agent and change-plan.

## When and how it changes

It changes when a real plan is made for each change request; it is changed while it is built and archived when its knowledge is in its homes. It is a name pattern, not a real item: it tells what each item made from it will hold.

## Who uses it, and when

It is read by the owner and every AI session that builds the change.

## Where it is mentioned

It is described in its folder's How it works file `apps/project-IDE/data/plans/plans.index.md`.

## Related knowledge

It is written by `agents/system/.claude/skills/change-plan/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules") and `docs/metadata.md`.

## Keep in mind

- When a step changes while you build, change the plan and say why in its log.
