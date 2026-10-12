---
about: agent-os/agents/system/
node: n-10
basis: 9334cbf7b822
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T19:52:55Z
---
# system/

## Summary

The system level of the Agent OS: the system agent and the home of everything every agent shares, whatever its domain. Like every level it has the standard agent folder; its agent, the system manager, oversees the domains, the system's health and its development, and answers the owner's questions about the whole system.

Its folders hold what holds for any agent: `configs/` the global settings (test or live, the live list, the general stop switch, schedules, notifications) and model routing; `scripts/` the shared machinery (create-agent, the scheduler, relink, load-secret, run-tests) and collectors shared by several domains; `logs/` and `data/` the shared logs and outputs; `docs/` the vision, README, rebuild prompt and the topic notes every agent reads. Its `.claude/` holds the project's rules and the helpers: self-improvement, the knowledge base agent and the project IDE agent.

Agents use shared files through read-only file links, never copies. The system reaches each domain through `subagents.link/`, one level at a time; everything about trading lives in the prediction-market domain.

## Keep in mind

- When agents of different domains need the same agent-local thing, move it into the matching shared folder here and give each a file link; what one domain needs stays in that domain (proposed).
- When a rule or setting holds only for one domain, put it in that domain, not here.
- When an owner input or a system change comes in, run it through the knowledge agent so the docs and the How it works files stay current.
