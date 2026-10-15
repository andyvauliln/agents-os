---
about: agent-os/agents/system/.claude/settings.json
basis: 3b4a21d31635
written: 2026-10-15T06:42:40Z
by: knowledge-base-agent
confirmed: 2026-10-15T06:43:18Z
---
# settings.json

## What it is

The shared Claude Code settings for system-level sessions: default model, permissions, environment, hooks, status line and output style. Today it holds only the permissions: it denies reading and editing `.secrets/live/**` and every `.env` file, so no session can see a key value; scripts get keys only through `load-secret`. Proposed additions are `env.AGENT_OS_ENV` (`test` or `live`) and a `PostToolUse` hook that runs relink after a links file is edited. Runs started by `run-job` are meant to take their model from the job or from `configs/models.config.json`.

## Who looks after it

It is written by the owner and an agent through change-plan.

## When and how it changes

It changes when a permission, hook, environment value or default model for system sessions changes; the model, the environment and the relink hook come next.

## Who uses it, and when

It is read by Claude Code started in agents/system/ and the server's Claude Code session behind the page's request box.

## Where it is mentioned

It is described in `agents/system/docs/README.md`, `agents/system/docs/rebuild-prompt.md` and its folder's How it works file `agents/system/.claude/.claude.index.md`.

## Related knowledge

It links to `.secrets/` and `agents/system/configs/models.config.json`. It has the same format as a person's own `settings.local.json`, which git ignores. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Each agent's AI setup"), `agents/system/docs/rebuild-prompt.md` (section "The standard .claude/ folder"), `agents/system/docs/README.md` (section "Keys and secrets") and `agents/system/docs/README.md` (section "Settings and AI models").

## Keep in mind

- When you change the permissions, keep the deny rules for `.secrets/live/**` and `.env`.
- When you set the mode variable, name it `AGENT_OS_ENV`, the name the keys use.
