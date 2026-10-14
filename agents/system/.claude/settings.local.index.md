---
about: agent-os/agents/system/.claude/settings.local.json
basis: 0b926e7a68a1
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# settings.local.json

## What it is

Personal overrides for Claude Code sessions at the system level on one machine, such as another `model` or `env.LOG_LEVEL`. It is meant to be local-only and git-ignored, but `.gitignore` has no line for it today, so it is tracked in git as an empty placeholder (`{}`). Nothing may depend on it; everything shared, the live-keys deny rules included, belongs in `settings.json`.

## Who looks after it

It is written by the owner, on their own machine.

## When and how it changes

It changes when a person sets a personal model, environment value or other override. It is empty for now.

## Who uses it, and when

It is read by Claude Code started in agents/system/ on that machine.

## Where it is mentioned

It is described in its folder's How it works file `agents/system/.claude/.claude.index.md`.

## Related knowledge

It has the same format as `agents/system/.claude/settings.json`. It is checked by `.gitignore`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Each agent's AI setup") and `agents/system/docs/rebuild-prompt.md` (section "The standard .claude/ folder").

## Keep in mind

- When you need a setting to hold for every run or every person, put it in `settings.json`.
- When you put a real value here, first add an ignore line for this file, so it does not reach git.
