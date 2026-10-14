---
about: agent-os/agents/system/scripts/system/
node: n-14.1
basis: 76947222e689
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:03:52Z
---
# system/

## Summary

The machinery every agent runs on, as shared `*.system.js|py` scripts. `create-agent` checks that a new name is valid and never used, reserves it, scaffolds the standard folder and runs `init.sh`; `run-agent` merges the configs into `effective-config.json` and starts Claude Code in the agent's own folder. One central `scheduler` runs every job in every workers file, and `run-job` runs one. `relink` builds every link from the links files and the folder tree, and `check-links` checks them. `load-secret` gives a script only its declared keys at run time. Also `check-secrets-index`, `run-tests`, `notifier` and planned scripts for the JSON lists. Agents call them through file links.

## Keep in mind

- When you write a script that lists files, make it read real files only; never follow `.link` folders recursively.
- When you change `load-secret`, keep values out of logs and the LLM, and refuse undeclared keys and unapproved live keys.
- When you change `create-agent`, keep the name check: reject any name in the registry, retired ones too.
- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
