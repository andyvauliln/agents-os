---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/build_map.py
node: n-10.1.2.5.2.5
basis: 11b1c827efd6
written: 2026-10-06T21:09:36Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:02:04Z
---
# build_map.py

## Summary

Builds the knowledge map from the knowledge tags in the notes, and keeps the How it works files honest: it lists the out-of-date ones from the deepest up, the ones whose file is gone, and what each is written from, and it writes or confirms them.

## Keep in mind

- When the notes or the tree change, run it until nothing is out of date and nothing is left over.
- When the file set is built, split this file into one file per job; today it does several.
