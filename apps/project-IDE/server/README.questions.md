# Questions: README.md

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-05: Does the page work from another server?

> so now this 2 files represent current ui and can open it another server and everything ll works? i ll have same ui

Served by any web server, the two files show the same page, but view only: saving notes and edits and asking Claude come from claude.ai. The full page runs on the owner's server with `server.py`, which keeps the page's notes as files, writes edits straight into the files and runs each request as a Claude Code session. While we plan it starts with `python3 vision/server/server.py` and is reached through an SSH tunnel.

### 2026-10-09: Does the IDE on the server work like the claude.ai page?

> if i start project-ide right now will it works same like current artifcat does

Yes, with differences by design: the request box needs `claude-agent-sdk` and Claude Code signed in on the server, voice needs `GROQ_API_KEY`, and the page's notes are kept as files. While we plan the server runs from `vision/`: the page from `vision/explorer/`, edits into the file the page showed, and Claude Code started in `vision/`. This changed later: when asked, the server looked for folders that did not exist yet and found no page; it was fixed to run from `vision/`.

### 2026-10-13: Will the IDE work on another server after the move?

> and what about ide ll it works on another server same like it works here right now?

Yes: the same page, edits go straight into the files, the request box runs Claude Code in the repository with Allow and Refuse, the microphone works with `GROQ_API_KEY`, and a push always asks. After the move out of `vision/`, only `server.config.json` changes: the page and store folders, the logs, no planning folder, and Claude Code started in `agents/system/`. It is not proven yet: it was tested once on a copy of the repository on 2026-10-05, and a full server test after the move is a step of the plan.
