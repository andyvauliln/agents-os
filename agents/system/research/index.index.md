---
about: agent-os/agents/system/research/index.json
basis: 0b926e7a68a1
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# index.json

## What it is

The history of every research item at the system level, one entry each: id `r-NNNN` and slug, topic and question, status (`planned`, `running`, `done`, `abandoned`), who asked and who ran it, start and finish, a short results summary, decisions, links, and what it led to (new agents, changes, tests, other research). Researchers read it before new work so nothing is repeated. The field names are proposed.

## Who looks after it

It is written by sys-self-improvement-agent, the owner and any agent that starts or closes a research item.

## When and how it changes

It changes when a research item is started, changes status or is closed. It is empty for now.

## Who uses it, and when

It is read by sys-self-improvement-agent, before it starts new research; and the owner, on the File Tree page.

## Where it is mentioned

It is described in `agents/system/research/[research-id]-[slug]/`, `agents/system/docs/README.md` (section "Research"), `agents/system/docs/rebuild-prompt.md` (section "Research") and its folder's How it works file `agents/system/research/research.index.md`.

## Related knowledge

The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Research").

## Keep in mind

- When you start research, read this index first, then add the item as `planned` before you run it.
- When you number an item, use a new `r-NNNN`; ids are never reused.
- When you close an item, set `done` or `abandoned` and fill `results_summary`, `decisions` and `related`.
