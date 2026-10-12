---
about: agent-os/agents/system/docs/how-to/add-worker.md
node: n-2.11.2
basis: c4727e4d10f4
written: 2026-10-07T19:07:39Z
by: knowledge-base-agent
---
# add-worker.md

## Summary

The runbook for adding a worker, sub-agent or other job and wiring its output to its readers; the workers helper follows it whenever an agent asks for data. It first checks the workers index and the links index so no source is collected twice and reuses or extends a running worker where it can, then places the script (agent-local, or shared once two agents need it), adds a job to the owning agent's jobs file, links the output into each reader's links file, and adds it to `on_change` where a reader must react at once. The steps are still proposed.

## Keep in mind

- When you need new data, check `index/workers.md` and the links index first; if a job already makes it, add a link instead of a new worker.
- When a second agent needs an agent-local worker, move it to the nearest level both share: their domain's `scripts/` for agents of one domain, the system's `scripts/workers/` across domains.
- When a job needs keys, list key names only, and only on `local` jobs; cloud, desktop and GitHub Actions jobs get none.
