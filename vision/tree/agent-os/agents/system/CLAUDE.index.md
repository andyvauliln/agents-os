---
about: agent-os/agents/system/CLAUDE.md
node: n-10.20
basis: 910e05691f8f
written: 2026-10-14T12:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-12T15:40:56Z
---
# CLAUDE.md

## Summary

The first file Claude Code reads when the owner starts it in agents/system/, and the system manager's instructions. It says what the Agent OS is and that the project is at stage one (finish the project IDE, make every metadata file correct, finish the docs at the project, system, trading and apps levels; prediction-market waits for stage two). It gives the docs to read in order: project vision and README, system vision and README, the plain file tree, the IDE README. Then the lasting rules (the new version keeps no memory folder; the rules live here), the steps after every input or update, and a table of which change makes which doc stale and which skill writes it. It is kept with the skill claude-md-doc.

## Keep in mind

- When the layout, the read order, the rules or the way of syncing change, update this file in the same round.
- When you add a rule that limits outside actions, put the hard limit in code, in the scripts that act, not only in this prompt.
- When you change something every level should follow (role, read order, rules, safety), change the common prompt too, not just this file.
- When the stage changes, rewrite the stage section first; the reading list follows it.
- When a request asks for a change, write its plan first; only questions and small fixes go without one.
