# Input 2026-10-15: run the project IDE on this server; root start.sh and init.sh

- From: the owner, in Claude Code chat on the owner's server
- Date: 2026-10-15

## Raw input
~~~text
let's make project ide run on this server and check if it's working, it should be running on start pc, make also root files ./start.sh init.sh start it's also should have some process how to start it that we sync before if we have something, kill previous process and start new with rebuilding etc
~~~

## Answer
~~~text
Done and tested on this server. ./init.sh (run once) checks git, curl, python3 >= 3.10, node and the claude CLI, makes .venv/ (git ignores it) with claude-agent-sdk for the request box, installs and enables the systemd user service project-ide (it runs ./start.sh serve; lingering is on, so it starts at boot before login), then runs ./start.sh. ./start.sh syncs (git fetch; when behind, puts back the three built files and fast-forwards only when nothing else is changed and there are no local commits, else skips with a warning; never merges, stashes or pushes; reports how many page items wait to be synced, without syncing them), stops the service and any stray server.py on the port, rebuilds with the new rebuild.py (a new data version only when the data changed), starts the service or a background process, and waits until /api/health answers. Also: --no-pull, stop, status, logs, serve. Health: ok, agent on, write-through on, voice off (no GROQ key on this machine). Restarts stop the old and a stray server; a second start keeps the data version; the page store round trip works. check_page.js cannot run here yet: Chromium needs system libraries (sudo npx playwright install-deps).
~~~

## Processed into
- start.sh, init.sh, agents/system/.claude/skills/ide-build/scripts/rebuild.py, with their How it works and Details
- D-073
- apps/project-IDE/server/README.md and its Questions file (the open question on the page check)
- agents/system/.claude/skills/ide-build/SKILL.md and scripts/README.md
- apps/project-IDE/docs/README.md and its twin, apps/project-IDE/docs/rebuild-prompt.md
- docs/README.md and its twin, docs/rebuild-prompt.md
- agents/system/docs/README.md and its twin, agents/system/docs/rebuild-prompt.md
- agents/system/CLAUDE.md, HANDOFF.md
