---
about: agent-os/agents/system/docs/index/agents.md
node: n-2.18.1
basis: bffc232586b6
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:03:12Z
---
# agents.md

## Summary

The registry of agent names: one row per agent ever created, retired ones included, so no name is reused. Each row gives the name (the agent's ID everywhere), type, domain, parent, route, mode, status, created date and path. `create-agent` checks and reserves names here, relink looks up `@[name]` link sources here, and the UI lists agents from it. Today it holds only planned, example and replaced names; whether a JSON registry becomes its source is open.

## Keep in mind

- When you name a new agent, check it here first, retired and replaced names included, and reserve it before scaffolding.
- When an agent is retired, keep its row and change its status; never delete a row or reuse a name.
- When an agent goes live, add a new row for the `-live` agent with the test agent as parent; the test row stays.
