---
about: agent-os/agents/system/data/subagents.link/
basis: fe4ebcdfeff2
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:09:25Z
---
# subagents.link/

## What it is

The system's view of its domains' data: one folder link per domain, each pointing at that domain's `data/`. The UI reads every agent's results through it one level at a time, without copies. Relink builds and removes these links from the folder tree; they are read-only and listed in no links file.

## Who looks after it

It is written by relink (planned shared script in agents/system/scripts/system/), from the folder tree.

## When and how it changes

It changes when a domain is added or removed; relink then adds or removes its link. It is empty for now.

## Who uses it, and when

It is read by the system agent; the owner, on the File Tree page; and sys-self-improvement-agent.

## Where it is mentioned

It is described in `agents/system/data/`, `agents/system/docs/README.md` (section "How a level reaches its children") and its folder's How it works file `agents/system/data/data.index.md`.

## Related knowledge

It links to `agents/trading/prediction-market/data/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "How a level reaches its children").

## Keep in mind

- When you scan data, never follow these links recursively; go down one `subagents.link/` at a time.
