---
about: agent-os/agents/system/CLAUDE.md
basis: 28ceed9cf88c
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-15T07:11:37Z
---
# CLAUDE.md

## What it is

The first file Claude Code reads when the owner starts it in agents/system/, and the system manager's instructions. It says what the Agent OS is and that the project is at stage one (finish the project IDE, make every metadata file correct, finish the docs at the project, system, trading and apps levels; prediction-market waits for stage two). It gives the docs to read in order: project vision and README, system vision and README, the plain file tree, the IDE README. Then the lasting rules (the new version keeps no memory folder; the rules live here), the steps after every input or update, and a table of which change makes which doc stale and which skill writes it. It is kept with the skill claude-md-doc.

## Who looks after it

It is written by knowledge-base-agent with the claude-md-doc skill; and the owner, on the File Tree page.

## When and how it changes

It changes when the stage, the reading list, a lasting rule, the round of work, the doc table or the system manager's job changes.

## Who uses it, and when

It is read by every Claude Code session started in agents/system/, every request sent from the File Tree page on the owner's server, the system agent and the owner.

## Where it is mentioned

It is described in `agents/system/docs/README.md` (section "The system agent and the shared files") and its folder's How it works file `agents/system/system.index.md`.

## Related knowledge

It links to `docs/vision.md`, `docs/README.md`, `agents/system/docs/vision.md`, `agents/system/docs/README.md`, `docs/file-tree.md`, `docs/metadata.md` and `apps/project-IDE/docs/README.md`. It is written by `agents/system/.claude/skills/claude-md-doc/`. The rules that apply to it come from `docs/README.md`, `docs/metadata.md` and `agents/system/docs/README.md` (section "The system agent and the shared files").

## Keep in mind

- When the layout, the read order, the rules or the way of syncing change, update this file in the same round.
- When you add a rule that limits outside actions, put the hard limit in code, in the scripts that act, not only in this prompt.
- When you change something every level should follow (role, read order, rules, safety), change the common prompt too, not just this file.
- When the stage changes, rewrite the stage section first; the reading list follows it.
- When a request asks for a change, write its plan first; only questions and small fixes go without one.
