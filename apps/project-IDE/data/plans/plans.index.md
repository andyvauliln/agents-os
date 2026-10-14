---
about: agent-os/apps/project-IDE/data/plans/
basis: 3c10ab114c24
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# plans/

## What it is

One plan for every change request, written with the `change-plan` skill before anything is built. A plan is the working document of one change: the owner sees it, the build follows its steps, and once it is built its knowledge moves to the files that own it. It holds the plans written so far, among them the plan to live without the planning folder `vision/` (`2026-10-13-leave-vision.md`, being built) and its file list, `index.json` with every plan and its status, and the name pattern `[plan].md`.

## Who looks after it

It is written by knowledge-base-agent and change-plan.

## When and how it changes

It changes when a change request gets a plan, or a plan's status changes.

## Who uses it, and when

It is read by the owner and every AI session that builds a change.

## Where it is mentioned

It is described in `apps/project-IDE/docs/README.md` and its folder's How it works file `apps/project-IDE/data/data.index.md`.

## Related knowledge

It is written by `agents/system/.claude/skills/change-plan/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules") and `docs/metadata.md`.

## Keep in mind

- When you add a plan, add its row to `index.json` too, and keep its status true as it moves on.
