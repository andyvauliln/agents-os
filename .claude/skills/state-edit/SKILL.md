---
name: state-edit
description: Edit the Agent OS state.json safely and keep index.html in step. Use whenever a task changes state.json.
---

# Editing state.json

1. Read `state.json` and find the entry by its path (for example `extension.view.header-view.connections.mcp.state`).
2. Make the change with Edit. Keep key order and two-space indents; the page shows keys in file order.
3. Run `python3 -m json.tool state.json > /dev/null` to check it is valid.
4. Run `python3 build.py`.
5. Commit `state.json` and `index.html` together.

Empty objects (`{}`) are placeholders: under a `files` key, a name with an extension is a file and a name without one is a folder.
