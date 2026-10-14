---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/build_map.py
basis: 9b9821ef3717
written: 2026-10-14T15:04:45Z
by: project-ide-agent
confirmed: 2026-10-14T15:07:13Z
---
# build_map.py

## Summary

Keeps the How it works files honest. For each item it makes a basis from the item's own content and, for a folder, the names and How it works texts of what is inside, and compares it with the basis in the file: fresh, stale, missing or empty. It lists the stale ones from the deepest up, shows what one is written from, writes or confirms them, and lists metadata files whose item is gone.

## Keep in mind

- When the tree or a file changes, run it until nothing is missing or stale and nothing is left over.
