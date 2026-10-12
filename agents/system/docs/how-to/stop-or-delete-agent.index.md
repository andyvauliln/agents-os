---
about: agent-os/agents/system/docs/how-to/stop-or-delete-agent.md
node: n-2.11.5
basis: e4814a9ad7c2
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# stop-or-delete-agent.md

## Summary

The runbook for stopping, retiring or deleting an agent. It turns off the agent's jobs (in an emergency the general stop switch stops every outside action at once), does the stop steps its domain adds, marks it paused or retired in the registry, and to delete archives the folder, runs relink to drop its child links and warn its readers, and fixes those readers. The steps are proposed; where archives live is still open.

## Keep in mind

- When you retire or delete an agent, keep its name reserved in the registry; names are never reused.
- When relink warns that readers still link to the agent's files, fix each reader's links file: point it elsewhere, disable or remove the entry.
