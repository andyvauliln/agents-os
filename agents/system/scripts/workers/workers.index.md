---
about: agent-os/agents/system/scripts/workers/
node: n-14.2
basis: ca5be8c0e077
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:08:15Z
---
# workers/

## Summary

The shared data collectors: `*.worker.py|js` scripts that fetch data from outside sources, such as news, for agents in more than one domain. Each runs as a job in `system.workers.json` and writes a dated file plus a stable `latest.*` into `data/workers/[worker]/` [16.2], with its log in [15.3]; readers link `latest.*` and never copy it. A collector only one domain needs lives in that domain. Agents ask the workers helper, which reuses, extends or creates a worker.

## Keep in mind

- When you write output, write the dated file first, then replace `latest.*` in one step (temp file, then rename).
- When you add a worker, check `index/workers.md` and the links index first; if the data already exists, link it instead.
- When you give a worker a key, list it in its job's `secret_keys` and load it through `load-secret`, never from the code.
- When you add code here, give each runnable thing (function, endpoint, script, worker) its own file with one purpose; group related ones in a folder.
