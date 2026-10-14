---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/
basis: a8d75d5f1e5f
written: 2026-10-14T15:04:45Z
by: project-ide-agent
confirmed: 2026-10-14T15:07:13Z
---
# scripts/

## Summary

The build scripts, in Python with nothing beyond the standard library, plus one page check in JavaScript. `enrich.py` builds the page data from the files on disk with help from `index_files.py` and `tabs.py`, `materialize.py` gives new items their empty metadata files and writes the plain tree, `build_map.py` finds out-of-date How it works files, and `check_page.js` and `check_tree.py` test the page and its tree before it is published. `README.md` explains how to run them.

## Keep in mind

- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
