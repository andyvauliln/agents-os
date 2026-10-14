---
about: agent-os/agents/system/.claude/agents/sys-self-improvement-agent.md
basis: 674b4c90b427
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# sys-self-improvement-agent.md

## What it is

The system's self-improvement helper: it improves the system itself (shared scripts, shared configs, model routing and shared docs) and reacts to new models and tools. It runs as a nightly job in `configs/system.workers.json`, reads errors and costs in the system's logs, the domains through `subagents.link/`, owner comments and outside news, and writes research items to `research/` and proposals marked pending owner. Its file template, memory place and outputs are proposals.

## Who looks after it

It is written by knowledge-base-agent, when the owner asks for it to be written.

## When and how it changes

It changes when its instructions are first written, or its scope, limits or job change. It is empty for now.

## Who uses it, and when

It is read by Claude Code started in agents/system/ (as a helper) and the system's jobs file (its switched-off job).

## Where it is mentioned

It is described in `agents/system/docs/README.md` and its folder's How it works file `agents/system/.claude/agents/agents.index.md`.

## Related knowledge

It writes `agents/system/.claude/agent-memory/` and `agents/system/research/`. It reads `agents/system/configs/models.config.json`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Each agent's AI setup"), `agents/system/docs/rebuild-prompt.md` (section "The standard .claude/ folder") and `agents/system/docs/README.md` (section "Self-improvement helpers").

## Keep in mind

- When you try a change, make it a new test version; never edit a running agent, touch live agents, loosen a limit or read `.secrets/live/`.
- When you want to change a shared file, record it as a proposal marked pending owner instead of applying it.
- When you set its model, set it in its job or in `configs/models.config.json`, not in this file.
