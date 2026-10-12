---
about: agent-os/agents/system/docs/feature-map.md
node: n-2.12
basis: 5798d5f0b44d
written: 2026-10-06T21:56:21Z
by: knowledge-base-agent
confirmed: 2026-10-07T09:34:43Z
---
# feature-map.md

## Summary

The map from each feature area to the files that implement it, so any agent can find where logic lives and what a change will touch. One table per area (data collection, triggers, run loop, execution, self-improvement, agent creation, routing, UI, docs, safety) gives the logic, the files with [n] numbers and the owning agent type; a gaps list ends it. The knowledge agent keeps it; agents read it before changing things. Still a proposal. The owner has decided that features get their own files, each mapped to its files and back, with small features inside bigger ones; once that is built, those files replace this table.

## Keep in mind

- When you add, move, rename or remove a feature or file, update this map and `file-tree.md` together; every [n] named here must exist in the tree.
