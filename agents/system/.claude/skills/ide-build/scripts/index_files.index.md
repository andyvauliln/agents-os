---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/index_files.py
basis: 70115fa99970
written: 2026-10-14T15:04:45Z
by: project-ide-agent
confirmed: 2026-10-14T15:07:13Z
---
# index_files.py

## Summary

Lists the items of the tree from the repository: every file git keeps, the folders that hold them and the local keys files, with the top as `agent-os`. It knows where each item's How it works and Details files are, named after the item without its extension, so `vision.md` has `vision.index.md` and `vision.meta.json`; a file that shares its name with a sibling or its folder keeps its extension. It reads and writes the How it works files with their header, and finds missing and orphan metadata files.

## Keep in mind

- When the file set is built, split this file into one file per job; today it does several.
