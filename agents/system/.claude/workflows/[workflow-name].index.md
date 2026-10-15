---
about: agent-os/agents/system/.claude/workflows/[workflow-name].js
basis: 674b4c90b427
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# [workflow-name].js

## What it is

The pattern for a system-level workflow: one dynamic workflow script (`.js`) per workflow, named after it, which becomes a `/<name>` command in system sessions. No concrete workflow is named yet.

## Who looks after it

It is written by the owner or an agent through change-plan, when a real workflow is made.

## When and how it changes

It changes when the workflow format changes, or a real workflow replaces the pattern. It is a name pattern, not a real item: it tells what each item made from it will hold. It is a proposal of an agent, not yet approved by the owner.

## Who uses it, and when

It is read by Claude Code started in agents/system/.

## Where it is mentioned

It is described in `agents/system/.claude/workflows/`, `agents/system/docs/rebuild-prompt.md` and its folder's How it works file `agents/system/.claude/workflows/workflows.index.md`.

## Related knowledge

The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Each agent's AI setup") and `agents/system/docs/rebuild-prompt.md` (section "The standard .claude/ folder").

## Keep in mind


