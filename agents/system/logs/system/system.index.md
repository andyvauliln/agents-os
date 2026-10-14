---
about: agent-os/agents/system/logs/system/
node: n-15.1
basis: 9fdc5f1bcdf5
written: 2026-10-01T00:58:18Z
by: summary-worker
confirmed: 2026-10-07T19:02:04Z
---
# system/

## Summary

The system's own log: one JSONL stream of what the shared machinery does. The scheduler logs runs started and finished, failed jobs and important file changes (cancel and restart, or wait); relink logs each link it creates or removes; check-links logs broken links; `load-secret` logs keys loaded or refused, by name only; `costs` lines record tokens and dollars per agent, giving the AI cost across all agents. The system's SI sub-agent reads errors and costs here. The events are proposed; file naming and retention are open.

## Keep in mind

- When you log a key event, write key names, mode and result only; never a value.
