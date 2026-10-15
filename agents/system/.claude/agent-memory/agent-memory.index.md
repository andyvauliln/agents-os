---
about: agent-os/agents/system/.claude/agent-memory/
basis: dcff7604cc26
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# agent-memory/

## What it is

The committed memory of system sub-agents that use `memory: project`: one folder per sub-agent with a `MEMORY.md`. The system's self-improvement sub-agent keeps its memory here. Memory holds lessons and pointers only, such as a research id with a one-line lesson; the research itself lives in `research/`, test state in `tests/`, history in `data/`. Before new work, the sub-agent reads its memory and the research index so it does not repeat itself.

## Who looks after it

It is written by the helper agents with `memory: project` (knowledge-base-agent, project-ide-agent, sys-self-improvement-agent).

## When and how it changes

It changes when a helper with `memory: project` first saves a lesson, or a helper is added or removed. It is empty for now.

## Who uses it, and when

It is read by the same helper agents, before new work.

## Where it is mentioned

It is described in `agents/system/docs/README.md` and its folder's How it works file `agents/system/.claude/.claude.index.md`.

## Related knowledge

It is written by `agents/system/.claude/agents/knowledge-base-agent.md`, `agents/system/.claude/agents/project-ide-agent.md` and `agents/system/.claude/agents/sys-self-improvement-agent.md`. It links to `agents/system/research/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Each agent's AI setup") and `agents/system/docs/rebuild-prompt.md` (section "The standard .claude/ folder").

## Keep in mind

- When you finish research, save only the item id and a one-line lesson here; the research stays in `research/`.
