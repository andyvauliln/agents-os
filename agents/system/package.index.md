---
about: agent-os/agents/system/package.json
basis: 0b926e7a68a1
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# package.json

## What it is

The system level's JS/TS dependencies and npm scripts. Here the dependencies are the libraries the shared scripts need. Proposed fields: `name` (the agent's name), `private: true`, `type: "module"`, `scripts.start` running `./start.sh`, and `scripts.test` running both test kinds through `run-tests`. `init.sh` installs it. Still open: dependencies per agent, or shared through a workspace at the repo root.

## Who looks after it

It is written by the system agent, when a shared JavaScript script needs a package; and the owner.

## When and how it changes

It changes when a shared JavaScript script needs a package or no longer needs one, or an npm script changes. It is empty for now.

## Who uses it, and when

It is read by agents/system/init.sh (planned: installs the packages) and npm.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "The system agent and the shared files") and its folder's How it works file `agents/system/system.index.md`.

## Related knowledge

It has the same format as `agents/system/requirements.txt`. It is read by `agents/system/init.sh` and `agents/system/scripts/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "The system agent and the shared files").

## Keep in mind


