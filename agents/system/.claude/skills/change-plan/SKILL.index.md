---
about: agent-os/agents/system/.claude/skills/change-plan/SKILL.md
basis: 1da0d41172a4
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# change-plan/SKILL.md

## What it is

The main development skill: every change request gets a plan before anything is built. A request from the owner, from the File Tree page or from an agent that wants to improve the system becomes one plan file, named by the request's date, time and subject. The plan says what was asked, what it is for, what exists today, the change part by part with examples, the choices for the owner with a recommended default, the steps with a check for each, everything it touches, and where each piece of its knowledge will live once built. The owner sees it before the build. After the build, its knowledge moves into the files that own it, the docs are brought in line from the vision down, and the plan is archived. Questions and small fixes, such as a typo or a rebuild of the page, need no plan. Proposed, written on the owner's request.

## Who looks after it

It is written by the owner and knowledge-base-agent.

## When and how it changes

It changes when the owner changes how changes are planned, approved, built or archived, or what a plan must contain.

## Who uses it, and when

It is read by every AI that changes the system, knowledge-base-agent and Claude Code started in agents/system/.

## Where it is mentioned

It is described in `agents/system/docs/README.md` and its folder's How it works file `agents/system/.claude/skills/change-plan/change-plan.index.md`.

## Related knowledge

It writes `apps/project-IDE/data/plans/`. It links to `agents/system/.claude/skills/make-questions/SKILL.md`. It is read by `agents/system/CLAUDE.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "When and how to update each doc"), `docs/metadata.md` and `agents/system/docs/README.md` (section "The knowledge base and the docs").

## Keep in mind

- When a change request arrives, save the owner's words first, then write the plan before you build anything.
- When the build is done, move every piece of the plan's knowledge to its home and archive the plan; never leave knowledge only in a plan.
- When a later change touches the same thing, start from the files that hold the knowledge now, not from the archived plan.
