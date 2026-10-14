---
about: agent-os/agents/
basis: 367efb8936d2
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# agents/

## What it is

All agents of the Agent OS, one folder per domain. The system is a domain too: `system/` holds the system agent and everything every agent shares, whatever its domain. `trading/` is a folder of trading domains with trading's own docs; its first domain, `trading/prediction-market/`, holds everything about trading today, and the next, `trading/copytrading/`, will be copied from it. Inside the prediction-market domain sit its strategy agents, and inside each strategy its trading agents, one per version being tested.

Every level uses one identical agent folder: `.claude/` with the level's prompt, then `configs/`, `scripts/`, `logs/`, `data/`, `docs/`, `tests/`, `research/` and the level files. Each content folder holds the level's own files, file links to what it reads elsewhere, and `subagents.link/` to its children. Agents are created by `create-agent`, and self-improvement creates new test versions. Secrets, the apps and cloned code live outside this folder.

## Who looks after it

It is written by the owner, knowledge-base-agent and project-ide-agent (ide-sync).

## When and how it changes

It changes when a domain or an agent level is added, moved or removed.

## Who uses it, and when

It is read by the owner, every agent and Claude Code started in agents/system/.

## Where it is mentioned

It is described in `docs/README.md`, `agents/system/docs/README.md`, `agents/trading/docs/README.md`, `docs/file-tree.md` and its folder's How it works file `agent-os.index.md`.

## Related knowledge

The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `docs/README.md` (section "Agents") and `agents/system/docs/README.md` (section "Agents and their levels").

## Keep in mind

- When you add an agent, give it a unique name and the standard folder through `create-agent`; never copy a folder by hand.
- When an agent needs another agent's file, add a link to its links file; it never writes into another agent's folder.
