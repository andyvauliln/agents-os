---
about: agent-os/start.sh
basis: 64b55b817974
written: 2026-10-15T07:10:39Z
by: knowledge-base-agent
---
# start.sh

## What it is

The script that starts or restarts the project IDE on the owner's server. `./start.sh` brings in new commits from GitHub when that is safe, stops the old server, rebuilds the page data, starts the server and waits until it answers its health check. It also has `--no-pull`, `stop`, `status`, `logs` and `serve`, the last being what the boot service runs.

## Who looks after it

The project IDE agent, with the owner. Its spec is in the project IDE rebuild prompt.

## When and how it changes

It changes when the way the IDE starts changes: the sync rule, which processes it stops, the rebuild, the service or the server's address. After a change, the server README, the IDE README with its twin and the IDE rebuild prompt are brought in line. Some of its choices are a proposal waiting for the owner's yes: the service name, pulling only when the branch can move forward cleanly, and reporting the page items that wait instead of syncing them.

## Who uses it, and when

The owner, to start, restart, stop or check the IDE. The systemd user service `project-ide` runs `./start.sh serve` at boot. `./init.sh` runs it at the end of the set-up.

## Where it is mentioned

`apps/project-IDE/server/README.md`, `apps/project-IDE/docs/README.md` and its twin, `apps/project-IDE/docs/rebuild-prompt.md`, `docs/README.md` and its twin, `docs/rebuild-prompt.md`, `agents/system/docs/README.md`, `agents/system/CLAUDE.md` and `HANDOFF.md`.

## Related knowledge

It runs `agents/system/.claude/skills/ide-build/scripts/rebuild.py` and `apps/project-IDE/server/server.py`, reads the port from `apps/project-IDE/server/server.config.json` and counts the waiting items in `apps/project-IDE/data/page-store/nodes/`. `init.sh` installs the service that runs it. It is not `agents/system/start.sh`, the system's own start script for the agents.

## Keep in mind

- When the branch and GitHub have both moved, or other files have local changes, it skips the pull; merge by hand, never let the script merge.
- When you change which processes it stops, keep the check that a process runs `project-IDE/server/server.py`, so it never kills another program.
- When items wait on the page, it only reports them; run the sync through Claude Code (Apply changes, or "sync the file tree").
