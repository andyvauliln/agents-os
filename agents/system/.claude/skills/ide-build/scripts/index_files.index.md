---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/index_files.py
node: n-10.1.2.5.2.6
basis: 35d5a77cd098
written: 2026-10-07T09:33:39Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:02:04Z
---
# index_files.py

## Summary

Knows where every How it works and Details file lives: next to the draft for items that have one, otherwise in a copy of the planned tree while we plan, and next to the real file in the repository. Each is named after its file without the extension, so `vision.md` has `vision.index.md` and `vision.meta.json`. It reads and writes them with their header and makes the empty Details files.

## Keep in mind

- When the file set is built, split this file into one file per job; today it does several.
