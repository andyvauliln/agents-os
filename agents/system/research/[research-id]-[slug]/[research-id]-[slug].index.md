---
about: agent-os/agents/system/research/[research-id]-[slug]/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# [research-id]-[slug]/

## What it is

One folder per system research item, named by its id and slug, such as `r-0001-[slug]/`. It holds a `README.md` with the question, method, results, decisions and what it led to (the index entry in more words), plus every artifact: datasets, run outputs, charts, notes. The format is proposed.

## Who looks after it

It is written by sys-self-improvement-agent, the owner and any agent that runs the research.

## When and how it changes

It changes when a research item is started; it grows while the research runs. It is a name pattern, not a real item: it tells what each item made from it will hold.

## Who uses it, and when

It is read by sys-self-improvement-agent; the owner, on the File Tree page; and the system agent.

## Where it is mentioned

It is described in `agents/system/research/index.json`, `agents/system/docs/README.md` (section "Research") and its folder's How it works file `agents/system/research/research.index.md`.

## Related knowledge

The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Research").

## Keep in mind

- When you run research, keep every artifact in the item's folder, and never a secret value.
