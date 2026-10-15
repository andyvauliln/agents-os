---
about: agent-os/agents/system/.claude/agent-memory-local/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# agent-memory-local/

## What it is

Memory for system sub-agents that use `memory: local`: the same kind of lessons as `agent-memory/`, but meant to stay on one machine. It is meant to be git-ignored, but `.gitignore` has no line for it today, so it is tracked in git as an empty placeholder that holds only its own metadata files.

## Who looks after it

It is written by helper agents with `memory: local` (none yet).

## When and how it changes

It changes when a helper with `memory: local` saves a memory on one machine. It is empty for now.

## Who uses it, and when

It is read by the same helper agents.

## Where it is mentioned

It is described in `agents/system/docs/README.md` and its folder's How it works file `agents/system/.claude/.claude.index.md`.

## Related knowledge

It has the same format as `agents/system/.claude/agent-memory/`. It is checked by `.gitignore`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Each agent's AI setup") and `agents/system/docs/rebuild-prompt.md` (section "The standard .claude/ folder").

## Keep in mind

- When you put a real memory file here, first add an ignore line for it, so it does not reach git.
