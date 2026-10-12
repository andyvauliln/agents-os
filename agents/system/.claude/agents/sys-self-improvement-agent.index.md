---
about: agent-os/agents/system/.claude/agents/sys-self-improvement-agent.md
node: n-10.1.1.1
basis: 6c9eda4d64f4
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
confirmed: 2026-10-09T09:57:03Z
---
# sys-self-improvement-agent.md

## Summary

The system's self-improvement helper: it improves the system itself (shared scripts, shared configs, model routing and shared docs) and reacts to new models and tools. It runs as a nightly job in [11.10], reads errors and costs in [15.1], the domains through `subagents.link/`, owner comments and outside news, and writes research items to [10.9] and proposals marked pending owner. Its file template, memory place and outputs are proposals.

## Keep in mind

- When you try a change, make it a new test version; never edit a running agent, touch live agents, loosen a limit or read `.secrets/live/`.
- When you want to change a shared file, record it as a proposal marked pending owner instead of applying it.
- When you set its model, set it in its job or [11.11], not in this file.
