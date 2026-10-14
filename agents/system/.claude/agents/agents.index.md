---
about: agent-os/agents/system/.claude/agents/
basis: b18fb48fdc8c
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:09:25Z
---
# agents/

## What it is

The system level's helper agents, each with its own instructions and tools. Three are named so far: the self-improvement agent, which keeps improving the system itself and reacts to new models and tools; the knowledge base agent, which keeps everything we know and writes the docs for people; and the project IDE agent, which builds the File Tree page from the repository and brings the owner's notes and edits back into the files. Planned: a workers helper that knows every worker and reuses, extends or creates one when an agent needs data, and a helper that checks the server and sets how many agents may run at once. Each runs on a schedule set in the system's jobs file and hands its results to other agents as data files.

## Who looks after it

It is written by the owner, knowledge-base-agent and change-plan.

## When and how it changes

It changes when a helper agent is added, renamed, removed or its role changes.

## Who uses it, and when

It is read by Claude Code started in agents/system/ and the owner.

## Where it is mentioned

It is described in `agents/system/docs/README.md` and its folder's How it works file `agents/system/.claude/.claude.index.md`.

## Related knowledge

It links to `agents/system/.claude/agents/knowledge-base-agent.md`, `agents/system/.claude/agents/project-ide-agent.md` and `agents/system/.claude/agents/sys-self-improvement-agent.md`. It reads `agents/system/.claude/skills/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Each agent's AI setup") and `agents/system/docs/rebuild-prompt.md` (section "The standard .claude/ folder").

## Keep in mind

- When you need a new system-support role, add it as a helper agent file here, not as a new agent folder.
