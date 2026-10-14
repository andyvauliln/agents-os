---
about: agent-os/apps/trading-ui/
node: n-45
basis: fc4916df0f4d
written: 2026-10-07T14:21:32Z
by: knowledge-base-agent
confirmed: 2026-10-09T09:57:03Z
---
# trading-ui/

## Summary

The prediction-market domain's dashboard: a Next.js API and web app where the owner will watch and control its trading agents. It will show each agent in full (parts, logs, performance, data used and produced, every decision, every improvement being tested) and let the owner create an agent from a plain input, read a report on each new strategy variant and approve it before it starts, approve or reject a live account, stop or delete agents, and comment or ask an agent questions. It reaches every level's files from the system down through `subagents.link/`. It is empty for now, and it may never be needed if the project IDE next to it, `apps/project-IDE/`, does the job. Open: whether it reads files directly or through an API layer, and how it is accessed.

## Keep in mind

- When an action touches live money, it needs the owner's approval in the UI; nothing else can grant it.
