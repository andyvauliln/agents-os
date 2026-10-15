---
about: agent-os/agents/system/.claude/rules/
basis: 4a696fdf0fa3
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# rules/

## What it is

The system level's topic rules: instructions that apply only when certain files are in play. Each rule is a Markdown file, one topic per file, with a `paths:` frontmatter of globs so it loads only when matching files are read; subfolders are allowed. It is part of the standard `.claude/` every level has and holds only the generic placeholder for now; concrete rules come later.

## Who looks after it

It is written by the owner; and knowledge-base-agent, through change-plan.

## When and how it changes

It changes when the first real rule is added, or the standard .claude/ layout changes. It is empty for now.

## Who uses it, and when

It is read by Claude Code started in agents/system/.

## Where it is mentioned

It is described in `agents/system/docs/README.md`, `agents/system/docs/rebuild-prompt.md` and its folder's How it works file `agents/system/.claude/.claude.index.md`.

## Related knowledge

The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Each agent's AI setup") and `agents/system/docs/rebuild-prompt.md` (section "The standard .claude/ folder").

## Keep in mind


