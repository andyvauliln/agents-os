---
about: agent-os/agents/system/.claude/agent-memory/[subagent-name]/MEMORY.md
basis: 674b4c90b427
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# [subagent-name]/MEMORY.md

## What it is

The memory of one system sub-agent that uses `memory: project`, in a folder named after the sub-agent. It has no frontmatter and holds dated lessons and pointers, such as `see r-0001`, never the research itself. It is committed with the rest of `.claude/`. The format is a proposal.

## Who looks after it

It is written by the helper agent its folder is named after.

## When and how it changes

It changes when the helper learns a lesson worth keeping, or the memory format changes. It is a name pattern, not a real item: it tells what each item made from it will hold. It is a proposal of an agent, not yet approved by the owner.

## Who uses it, and when

It is read by the same helper agent, before new work.

## Where it is mentioned

It is described in its folder's How it works file `agents/system/.claude/agent-memory/[subagent-name]/[subagent-name].index.md`.

## Related knowledge

It links to `agents/system/research/`. It is written by `agents/system/.claude/agents/sys-self-improvement-agent.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Each agent's AI setup"), `agents/system/docs/rebuild-prompt.md` (section "The standard .claude/ folder") and `agents/system/docs/README.md` (section "Self-improvement helpers").

## Keep in mind

- When you record research, write only the item id and a one-line lesson here; the research stays in `research/`.
