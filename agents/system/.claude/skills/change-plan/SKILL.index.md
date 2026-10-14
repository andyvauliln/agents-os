---
about: agent-os/agents/system/.claude/skills/change-plan/SKILL.md
node: n-10.1.2.8
basis: b49787288b72
written: 2026-10-06T21:55:22Z
by: knowledge-base-agent
confirmed: 2026-10-06T22:01:28Z
---
# change-plan/SKILL.md

## Summary

The main development skill: every change request gets a plan before anything is built. A request from the owner, from the File Tree page or from an agent that wants to improve the system becomes one plan file, named by the request's date, time and subject. The plan says what was asked, what it is for, what exists today, the change part by part with examples, the choices for the owner with a recommended default, the steps with a check for each, everything it touches, and where each piece of its knowledge will live once built. The owner sees it before the build. After the build, its knowledge moves into the files that own it, the docs are brought in line from the vision down, and the plan is archived. Questions and small fixes, such as a typo or a rebuild of the page, need no plan. Proposed, written on the owner's request.

## Keep in mind

- When a change request arrives, save the owner's words first, then write the plan before you build anything.
- When the build is done, move every piece of the plan's knowledge to its home and archive the plan; never leave knowledge only in a plan.
- When a later change touches the same thing, start from the files that hold the knowledge now, not from the archived plan.
