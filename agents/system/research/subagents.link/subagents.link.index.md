---
about: agent-os/agents/system/research/subagents.link/
basis: a8a9689c0440
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:09:25Z
---
# subagents.link/

## What it is

The system's view of its domains' research: one folder link per domain, each pointing at that domain's `research/`. The system's self-improvement helper and the UI read the domains' research through it, going down one `subagents.link/` at a time. Relink builds and removes these links from the folder tree; they are read-only and listed in no links file.

## Who looks after it

It is written by relink (planned shared script in agents/system/scripts/system/), from the folder tree.

## When and how it changes

It changes when a domain is added or removed; relink then adds or removes its link. It is empty for now.

## Who uses it, and when

It is read by the system agent; the owner, on the File Tree page; and sys-self-improvement-agent.

## Where it is mentioned

It is described in `agents/system/research/`, `agents/system/docs/README.md` (section "How a level reaches its children") and its folder's How it works file `agents/system/research/research.index.md`.

## Related knowledge

It links to `agents/trading/prediction-market/research/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "How a level reaches its children").

## Keep in mind

- When you need to add to a domain's research, write it in the domain's own `research/`; these links are read-only.
