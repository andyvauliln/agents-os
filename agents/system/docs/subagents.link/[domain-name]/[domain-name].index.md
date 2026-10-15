---
about: agent-os/agents/system/docs/subagents.link/[domain-name]/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# [domain-name]/

## What it is

One folder link per domain, named after the domain's folder and pointing at that domain's own `docs/`, so the system can read the domain's docs, and from there those of the levels below it, without copies. It is read-only: the system writes only its own docs. `relink` builds it from the folder tree and removes it when the domain is gone; it is never listed in a links file.

## Who looks after it

It is written by relink (planned shared script in agents/system/scripts/system/), when a domain is added; never by hand.

## When and how it changes

Only when a domain is added or removed; relink makes or deletes the link. It is a name pattern, not a real item: it tells what each item made from it will hold.

## Who uses it, and when

It is read by the system agent; the owner, on the File Tree page; sys-self-improvement-agent; and knowledge-base-agent.

## Where it is mentioned

It is described in `agents/system/docs/subagents.link/`, `agents/system/docs/README.md` (section "How a level reaches its children") and its folder's How it works file `agents/system/docs/subagents.link/subagents.link.index.md`.

## Related knowledge

It links to `agents/trading/prediction-market/docs/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "How a level reaches its children").

## Keep in mind

- When you need a domain's docs, read them through this link; never write into it.
- When a domain is added or removed, let `relink` make or remove this link; never create it by hand.
