---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/parse.py
node: n-10.1.2.5.2.2
basis: 5e51d719e339
written: 2026-10-05T13:25:49Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:02:04Z
---
# parse.py

## Summary

Reads the tree notes: each line of the numbered tree becomes an item with its parent, path, number and comment, and each item gets its section. It also reads the retired items, the decisions and the feature map, and writes all of it as one file for `enrich.py`.
