---
about: agent-os/agents/system/.claude/agents/sys-self-improvement-agent.md
basis: 674b4c90b427
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# sys-self-improvement-agent.md

## Summary

The system's self-improvement helper: it improves the system itself (shared scripts, shared configs, model routing and shared docs) and reacts to new models and tools. It runs as a nightly job in `configs/system.workers.json`, reads errors and costs in the system's logs, the domains through `subagents.link/`, owner comments and outside news, and writes research items to `research/` and proposals marked pending owner. Its file template, memory place and outputs are proposals.

## Keep in mind

- When you try a change, make it a new test version; never edit a running agent, touch live agents, loosen a limit or read `.secrets/live/`.
- When you want to change a shared file, record it as a proposal marked pending owner instead of applying it.
- When you set its model, set it in its job or in `configs/models.config.json`, not in this file.
