---
about: agent-os/apps/project-IDE/data/knowledge-map.json
node: n-2.18.8
basis: 816f034b9714
written: 2026-10-05T13:25:49Z
by: knowledge-base-agent
confirmed: 2026-10-07T14:22:08Z
---
# knowledge-map.json

## Summary

The knowledge map: which knowledge applies to which file or folder, many to many. `build_map.py`, one of the page build scripts, writes it from the knowledge tags in the notes and the tree: every entry with the items it applies to, every item with its file doc, its direct and inherited knowledge and the hash its How it works must match, the archived inputs, and problems such as tags that match nothing. It sits with the project's records in `project-IDE/data/`. The knowledge base agent uses it to find everything a change touches.

## Keep in mind

- When the notes or the tree change, rebuild the map; never edit this file by hand.
