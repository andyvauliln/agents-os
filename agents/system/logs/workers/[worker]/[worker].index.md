---
about: agent-os/agents/system/logs/workers/[worker]/
basis: 981c7ce4dc3d
written: 2026-10-01T00:58:18Z
by: summary-worker
confirmed: 2026-10-14T15:07:13Z
---
# workers/[worker]/

## Summary

One log folder per shared worker, named after it. The draft format is plain text: a dated `YYYY-MM-DD.log` plus a stable `latest.log`, one line per event (`ts LEVEL worker message`). At the end of each run the worker also prints a JSON summary line that `run-job` keeps in the job log. An agent links `latest.log` only when it needs it. Whether these logs become JSONL like the others is open.

## Keep in mind

- When you rotate dated logs, keep replacing `latest.log` in one step; agents' links point at it.
