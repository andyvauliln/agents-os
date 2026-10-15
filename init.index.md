---
about: agent-os/init.sh
basis: b9212fded114
written: 2026-10-15T07:10:39Z
by: knowledge-base-agent
---
# init.sh

## What it is

The one-time set-up of the owner's server for the project IDE. It checks the tools, makes `.venv/` with the Python package of the request box, installs the systemd user service `project-ide` that starts the IDE at boot, and then runs `./start.sh`. `--no-service` leaves the service out. It is safe to run again.

## Who looks after it

The project IDE agent, with the owner. Its spec is in the project IDE rebuild prompt.

## When and how it changes

It changes when what the server needs changes (a tool, a Python package) or the service changes. After a change, the server README and the IDE docs are brought in line, and the owner runs it again so the service file is rewritten. The service name and `.venv/` are a proposal waiting for the owner's yes.

## Who uses it, and when

The owner, once on a new server, and again after a change to it or to the service.

## Where it is mentioned

`apps/project-IDE/server/README.md`, `apps/project-IDE/docs/README.md` and its twin, `apps/project-IDE/docs/rebuild-prompt.md`, `docs/README.md` and its twin, `docs/rebuild-prompt.md`, `agents/system/docs/README.md`, `agents/system/CLAUDE.md` and `HANDOFF.md`.

## Related knowledge

It writes `~/.config/systemd/user/project-ide.service`, which runs `start.sh serve`, and `.venv/` at the top of the repository, which `.gitignore` leaves out. The service gets the caller's PATH and Claude Code settings folder, so it finds node and `claude` and uses the same sign-in. It is not `agents/system/init.sh`, the system's own set-up script for the agents.

## Keep in mind

- When you change it, never let it read or write a keys file; the server reads the keys it names itself.
- When lingering is off and cannot be turned on, the IDE starts only at login; the owner runs the `sudo loginctl enable-linger` line it prints.
