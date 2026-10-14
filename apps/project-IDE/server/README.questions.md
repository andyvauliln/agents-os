# Questions: README.md

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-05: Does the page work from a different server?

> so now this 2 files represent current ui and can open it another server and everything ll works? i ll have same ui

Any web server can serve the two files, and they show the same page. But you can only look at it. Saved notes, edits and requests to Claude come from claude.ai.

The full page runs on the owner's server with `server.py`. The server does these tasks:

1. It keeps the notes of the page as files.
2. It writes edits directly into the files.
3. It runs each request as a Claude Code session.

While we plan, you start it with `python3 vision/server/server.py`. You get access to it through an SSH tunnel.

Docs improved: apps/project-IDE/server/README.md.

### 2026-10-09: Does the IDE on the server work as the claude.ai page does?

> if i start project-ide right now will it works same like current artifcat does

Yes, but with differences by design:

1. The request box needs `claude-agent-sdk`, and Claude Code must be signed in on the server.
2. Voice needs `GROQ_API_KEY`.
3. The server keeps the notes of the page as files.

While we plan, the server runs from `vision/`. The page comes from `vision/explorer/`. Edits go into the file that the page showed. Claude Code starts in `vision/`.

This changed later: at the time of the question, the server looked for folders that did not exist yet. It found no page. The agent changed it to run from `vision/`.

Docs improved: apps/project-IDE/server/README.md.

### 2026-10-13: After the move, does the IDE work on a different server?

> and what about ide ll it works on another server same like it works here right now?

Yes. It works as it does here:

1. It is the same page.
2. Edits go directly into the files.
3. The request box runs Claude Code in the repository, with Allow and Refuse.
4. The microphone works with `GROQ_API_KEY`.
5. A push always asks you first.

After the move out of `vision/`, only `server.config.json` changes. It gets the page and store folders and the logs. It has no planning folder. Claude Code starts in `agents/system/`.

This is not proved yet. We tested it one time on a copy of the repository on 2026-10-05. A full server test after the move is a step of the plan.

Docs improved: apps/project-IDE/server/README.md.
