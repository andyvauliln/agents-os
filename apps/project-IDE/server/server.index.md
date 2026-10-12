---
about: agent-os/apps/project-IDE/server/
node: n-53.3
basis: 11d68992fb45
written: 2026-10-06T21:09:36Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:30:32Z
---
# server/

## Summary

The File Tree page on the owner's own server, with Claude Code behind its request box. It is the same page as on claude.ai: here it finds this service next to it, keeps the owner's notes and messages as files in the repository, writes edits to a file or its How it works straight into the file, and sends each request to Claude Code, which starts in the system folder, works in the repository and shows each step on the page. A Delete pressed on the page goes to Claude Code at once: it deletes the item and cleans the project of it, keeping the owner's note in mind. Pushing, other deletions and anything outside the repository wait for the owner's click. `server.py` serves the page and the files, `claude_bridge.py` runs the requests, `voice.py` turns the owner's voice recordings into text through Groq, `server.config.json` holds the settings and `README.md` says how to start it and reach it safely. Written and tested on a copy of the repository; it goes live on the server after the GitHub sync.

## Keep in mind

- Reachable only from the machine or through an SSH tunnel, never the open internet.
- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
