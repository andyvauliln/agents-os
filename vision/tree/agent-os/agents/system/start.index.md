---
about: agent-os/agents/system/start.sh
node: n-10.7
basis: 98cc77824e9f
written: 2026-10-01T01:01:42Z
by: summary-worker
confirmed: 2026-10-12T15:40:56Z
---
# start.sh

## Summary

The system's start script. Like every level's `start.sh` it does one run of its level, here a system session at `agents/system/`; the scheduler calls it for the main-run job, and the owner can run it by hand. At the system level it also starts the one central scheduler, which runs every job in every workers file while the OS keeps it alive. This is proposed; which machine runs the scheduler is open.

## Keep in mind

- When you need the scheduler running, start it only through this script; there is one scheduler for all agents.
