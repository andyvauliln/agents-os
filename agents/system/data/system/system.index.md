---
about: agent-os/agents/system/data/system/
node: n-16.1
basis: 2fafba2e0ddf
written: 2026-10-01T00:59:23Z
by: summary-worker
confirmed: 2026-10-07T19:08:15Z
---
# system/

## Summary

The system's own state files, the runtime memory of the shared machinery. `scheduler-state.json` holds every job's last run, result, next run and failure count; only the scheduler writes it, so workers files never change at run time. `links.index.json` lists every link in the project (owner agent, where it appears, real target, required, status); only relink writes it, and the UI, `check-links` and the runbooks read it to see who reads which file. Both formats are proposed. Still open: whether a `run-state.json` with per-agent read cursors is needed, which depends on how "new since the last run" is tracked.

## Keep in mind

- When you need these files changed, let their one writer do it: the scheduler for `scheduler-state.json`, relink for `links.index.json`.
- When you move or delete a file others read, check `links.index.json` for its readers first.
