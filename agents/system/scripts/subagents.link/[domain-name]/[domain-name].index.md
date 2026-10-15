---
about: agent-os/agents/system/scripts/subagents.link/[domain-name]/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# [domain-name]/

## What it is

One folder link per domain, named after the domain's folder and pointing at that domain's `scripts/`. Through it the system reads the domain's own scripts and, one `subagents.link/` further down, those of the levels below it. It is read-only, built by relink from the folder tree, listed in no links file, and removed when the domain goes.

## Who looks after it

It is written by relink (planned shared script in agents/system/scripts/system/), when a domain is added; never by hand.

## When and how it changes

Only when a domain is added or removed; relink makes or deletes the link. It is a name pattern, not a real item: it tells what each item made from it will hold.

## Who uses it, and when

It is read by the system agent; the owner, on the File Tree page; and sys-self-improvement-agent.

## Where it is mentioned

It is described in `agents/system/scripts/subagents.link/`, `agents/system/docs/README.md` (section "How a level reaches its children") and its folder's How it works file `agents/system/scripts/subagents.link/subagents.link.index.md`.

## Related knowledge

It links to `agents/trading/prediction-market/scripts/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "How a level reaches its children").

## Keep in mind


