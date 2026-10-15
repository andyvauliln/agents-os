---
about: agent-os/agents/system/scripts/system/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# system/

## What it is

The machinery every agent runs on, as shared `*.system.js|py` scripts. `create-agent` checks that a new name is valid and never used, reserves it, scaffolds the standard folder and runs `init.sh`; `run-agent` merges the configs into `effective-config.json` and starts Claude Code in the agent's own folder. One central `scheduler` runs every job in every workers file, and `run-job` runs one. `relink` builds every link from the links files and the folder tree, and `check-links` checks them. `load-secret` gives a script only its declared keys at run time. Also `check-secrets-index`, `run-tests`, `notifier` and planned scripts for the JSON lists. Agents call them through file links.

## Who looks after it

It is written by the system's helpers and sys-self-improvement-agent (proposes changes).

## When and how it changes

It changes when a shared machinery script is added, changed or removed. It is empty for now.

## Who uses it, and when

It is read by every agent, through file links; agents/system/init.sh and agents/system/start.sh (planned); the git hooks (planned); and the owner.

## Where it is mentioned

It is described in `agents/system/docs/rebuild-prompt.md` (section "Jobs and the scheduler"), `agents/system/docs/README.md` (section "Jobs and the scheduler"), `agents/system/scripts/` and its folder's How it works file `agents/system/scripts/scripts.index.md`.

## Related knowledge

It reads `agents/system/configs/system.workers.json`, `agents/system/configs/system.links.json`, `agents/system/configs/system.config.json` and `.secrets/`. It writes `agents/system/data/system/` and `agents/system/logs/system/`. It is tested by `agents/system/tests/scripts/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Jobs and the scheduler"), `agents/system/docs/README.md` (section "Links between agents") and `agents/system/docs/README.md` (section "Keys and secrets").

## Keep in mind

- When you write a script that lists files, make it read real files only; never follow `.link` folders recursively.
- When you change `load-secret`, keep values out of logs and the LLM, and refuse undeclared keys and unapproved live keys.
- When you change `create-agent`, keep the name check: reject any name in the registry, retired ones too.
- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
