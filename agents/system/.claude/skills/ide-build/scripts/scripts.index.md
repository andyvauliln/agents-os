---
about: agent-os/agents/system/.claude/skills/ide-build/scripts/
node: n-10.1.2.5.2
basis: b8813347654f
written: 2026-10-07T09:33:30Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:02:04Z
---
# scripts/

## Summary

The build scripts, in Python with nothing beyond the standard library, plus one page check in JavaScript. `parse.py` reads the tree notes, `enrich.py` builds the page data with help from `tabs.py`, `build_map.py` builds the knowledge map and finds out-of-date How it works files, `index_files.py` knows where each How it works and Details file lives, and `check_page.js` tests the page before it is published. `README.md` explains how to run them.

## Keep in mind

- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
