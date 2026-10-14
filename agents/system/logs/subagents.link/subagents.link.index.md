---
about: agent-os/agents/system/logs/subagents.link/
basis: 98636f1ee045
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:09:25Z
---
# subagents.link/

## What it is

The system's view of its domains' logs: one folder link per domain, each pointing at that domain's `logs/`. The UI starts at the system's `logs/` and goes down through these links one level at a time, reading every agent's logs without copies. Relink builds and removes them from the folder tree; they are read-only and listed in no links file.

## Who looks after it

It is written by relink (planned shared script in agents/system/scripts/system/), from the folder tree.

## When and how it changes

It changes when a domain is added or removed; relink then adds or removes its link. It is empty for now.

## Who uses it, and when

It is read by the system agent; the owner, on the File Tree page; and sys-self-improvement-agent.

## Where it is mentioned

It is described in `agents/system/logs/`, `agents/system/docs/README.md` (section "How a level reaches its children") and its folder's How it works file `agents/system/logs/logs.index.md`.

## Related knowledge

It links to `agents/trading/prediction-market/logs/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "How a level reaches its children").

## Keep in mind

- When you scan logs, never follow these links recursively; go down one `subagents.link/` at a time.
