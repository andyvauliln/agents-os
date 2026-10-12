---
about: agent-os/agents/system/init.sh
node: n-10.6
basis: 3a3575ef750d
written: 2026-10-01T01:01:42Z
by: summary-worker
confirmed: 2026-10-07T19:02:04Z
---
# init.sh

## Summary

The system's setup script, safe to run again. Like every level's `init.sh` it installs dependencies and ends by running relink. At the system level it also installs the repo's git hooks (`pre-commit`, `post-merge`, `post-checkout`) that run relink at review time, and relinks the whole project, so running it once after a clone sets everything up. After that, relink runs by itself whenever a links file changes. How it ties into the machinery is proposed.

## Keep in mind

- When you clone the repo, run this once so the git hooks that keep links in step are installed.
