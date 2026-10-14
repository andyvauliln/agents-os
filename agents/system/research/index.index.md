---
about: agent-os/agents/system/research/index.json
basis: 0b926e7a68a1
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# index.json

## Summary

The history of every research item at the system level, one entry each: id `r-NNNN` and slug, topic and question, status (`planned`, `running`, `done`, `abandoned`), who asked and who ran it, start and finish, a short results summary, decisions, links, and what it led to (new agents, changes, tests, other research). Researchers read it before new work so nothing is repeated. The field names are proposed.

## Keep in mind

- When you start research, read this index first, then add the item as `planned` before you run it.
- When you number an item, use a new `r-NNNN`; ids are never reused.
- When you close an item, set `done` or `abandoned` and fill `results_summary`, `decisions` and `related`.
