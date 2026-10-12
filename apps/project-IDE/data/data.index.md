---
about: agent-os/apps/project-IDE/data/
node: n-53.2
basis: 90ee1e4cf54d
written: 2026-10-05T15:37:34Z
by: knowledge-base-agent
confirmed: 2026-10-07T14:22:08Z
---
# data/

## Summary

This project's knowledge and the data the page is built from, in one place any AI session can read to catch up. It holds every owner input word for word in `inputs/`, the decision log, the changelog, the tree notes `file-tree.md` (one section per file and folder), the knowledge map, `sources/` (what each people doc rests on), `page-store/` (on the owner's server, the page's notes, edits and messages as files), `overrides.json` (the owner's page edits kept in the page data), `memory/` (working notes), `plans/` and `archive/`. The knowledge base agent writes it; the project IDE agent reads it to build the page. The topic notes agents read while they work stay in `agents/system/docs/`, and so do the docs for people.

## Keep in mind

- When the owner says anything about the system, store it here word for word before filing its knowledge.
- When a file here is generated (the knowledge map), rebuild it; never edit it by hand.
