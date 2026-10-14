---
about: agent-os/agents/system/.claude/rules/[topic].md
basis: 674b4c90b427
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# [topic].md

## What it is

The pattern for a system-level rule: one Markdown file per topic, named after it. Its `paths:` frontmatter lists globs, and the rule is loaded only when matching files are read. No concrete system rule is named yet; the frontmatter details are a proposal.

## Who looks after it

It is written by the owner or an agent through change-plan, when a real rule is made.

## When and how it changes

It changes when the rule format changes, or a real rule replaces the pattern. It is a name pattern, not a real item: it tells what each item made from it will hold. It is a proposal of an agent, not yet approved by the owner.

## Who uses it, and when

It is read by Claude Code started in agents/system/.

## Where it is mentioned

It is described in `agents/system/.claude/rules/`, `agents/system/docs/rebuild-prompt.md` and its folder's How it works file `agents/system/.claude/rules/rules.index.md`.

## Related knowledge

The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `agents/system/docs/README.md` (section "Each agent's AI setup") and `agents/system/docs/rebuild-prompt.md` (section "The standard .claude/ folder").

## Keep in mind


