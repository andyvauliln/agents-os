---
about: agent-os/agents/system/requirements.txt
basis: 674b4c90b427
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# requirements.txt

## What it is

The system level's Python dependencies: the libraries the shared Python scripts need, installed by `init.sh`. Still open: whether each agent gets its own virtual environment or all agents share one.

## Who looks after it

It is written by the system agent, when a shared Python script needs a package; and the owner.

## When and how it changes

It changes when a shared Python script needs a package or no longer needs one. It is empty for now.

## Who uses it, and when

It is read by agents/system/init.sh (planned: installs the packages) and pip.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "The system agent and the shared files") and its folder's How it works file `agents/system/system.index.md`.

## Related knowledge

It has the same format as `agents/system/package.json`. It is read by `agents/system/init.sh` and `agents/system/scripts/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "The system agent and the shared files").

## Keep in mind


