---
about: agent-os/agents/system/scripts/
node: n-14
basis: fb74545fd416
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# scripts/

## Summary

The shared scripts every agent uses, in JS/TS or Python, sorted by kind twice: by sub-folder and by the suffix `[name].[kind].[ext]`. The two general kinds are `system/`, the machinery (create-agent, run-agent, the scheduler and run-job, relink and check-links, load-secret, run-tests, notifier), and `workers/`, the data collectors shared by several domains. A domain keeps its own scripts and kinds, such as the prediction-market domain's `decisions/`, and the system reads them through `subagents.link/`. Agents use a shared script through a file link, so an improvement reaches every agent at once. System-support agents write here; domain and self-improvement agents propose.

## Keep in mind

- When you name a script, use `[name].[kind].[ext]` and put it in the sub-folder of its kind.
- When a second agent needs an agent-local script, move it to the shared `scripts/` of the nearest level both agents share (here when they are in different domains) and give each a file link; never copy it.
- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
