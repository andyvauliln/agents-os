---
about: agent-os/agents/system/docs/subagents.link/
basis: 6b29f71594bd
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# subagents.link/

## What it is

The system's view of its domains' docs: one folder link per domain, each pointing at that domain's own `docs/`. Each domain's docs link on to the levels below it, so every agent's docs can be read from here one level at a time, without copies. `relink` adds a link from the folder tree when a domain is set up and removes it after a stop or delete. The UI, the system session, self-improvement helpers and the knowledge agent read through it; nothing writes into it.

## Who looks after it

It is written by relink (planned shared script in agents/system/scripts/system/), from the folder tree.

## When and how it changes

It changes when a domain is added or removed; relink then adds or removes its link. It is empty for now.

## Who uses it, and when

It is read by the system agent; the owner, on the File Tree page; sys-self-improvement-agent; and knowledge-base-agent.

## Where it is mentioned

It is described in `agents/system/docs/`, `agents/system/docs/README.md` (section "How a level reaches its children") and its folder's How it works file `agents/system/docs/docs.index.md`.

## Related knowledge

It links to `agents/trading/prediction-market/docs/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "How a level reaches its children").

## Keep in mind

- When you scan the docs, never follow these links recursively; go down one `subagents.link/` at a time and read real files only.
- When a domain is added or removed, let `relink` make or remove its link; never create one by hand or list it in a links file.
