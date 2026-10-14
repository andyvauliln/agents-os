---
about: agent-os/agents/system/docs/flows.md
node: n-2.15
basis: 794b10166c5f
written: 2026-10-01T00:53:59Z
by: summary-worker
confirmed: 2026-10-07T09:34:43Z
---
# flows.md

## Summary

Every flow in the system, step by step, each with a diagram, the files it touches and the owning agent type. Data flows follow data from workers through links to agents, triggers, the run loop and its test or live actions, logs to the UI, self-improvement and outside signals. User flows cover what the owner does: create, review, approve live money, stop, comment or ask, review a proposed change. The knowledge agent updates it when a flow changes.

## Keep in mind

- When you change a flow, keep the files it names the same as `feature-map.md` names for that feature.
