---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/check_tree.py
basis: 8f6ac821c628
written: 2026-10-14T15:04:45Z
by: project-ide-agent
confirmed: 2026-10-14T15:07:13Z
---
# check_tree.py

## Summary

The last check before publishing: the items of the page data must be exactly the files git keeps, the folders that hold them and the top, with each item's path as its id. The local keys files are the only items allowed on top. It prints "tree ok" or what differs.

## Keep in mind

- When it fails, build again; never edit the page data by hand.
