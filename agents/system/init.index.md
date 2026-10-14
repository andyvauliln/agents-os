---
about: agent-os/agents/system/init.sh
basis: 674b4c90b427
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# init.sh

## What it is

The system's setup script, safe to run again. Like every level's `init.sh` it installs dependencies and ends by running relink. At the system level it also installs the repo's git hooks (`pre-commit`, `post-merge`, `post-checkout`) that run relink at review time, and relinks the whole project, so running it once after a clone sets everything up. After that, relink runs by itself whenever a links file changes. How it ties into the machinery is proposed.

## Who looks after it

It is written by knowledge-base-agent (the plan); and the system agent, once the shared scripts are written.

## When and how it changes

It changes when the way the project is set up changes, such as the git hooks or the relink call. It is empty for now.

## Who uses it, and when

It is read by the owner, once after a clone; and create-agent (planned shared script).

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "The system agent and the shared files") and its folder's How it works file `agents/system/system.index.md`.

## Related knowledge

It has the same format as `agents/system/start.sh`. It reads `agents/system/package.json`, `agents/system/requirements.txt` and `agents/system/scripts/system/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md` and `agents/system/docs/README.md` (section "Links between agents").

## Keep in mind

- When you clone the repo, run this once so the git hooks that keep links in step are installed.
