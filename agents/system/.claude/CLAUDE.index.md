---
about: agent-os/agents/system/.claude/CLAUDE.md
node: n-10.1.5
basis: 9e16f6cffae1
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# CLAUDE.md

## Summary

The first file any AI session reads when it works on the project, and the system manager's instructions. Claude Code loads it by itself in the system folder; a session started at the top of the repository reads it first by hand. It says what the Agent OS is for, what to read first, where things are, the rules and how a round works, and ends with the system manager's job: oversee the domains, the system's health and its development.

## Keep in mind

- When the layout, the read order, the rules or the way of syncing change, update this file in the same round.
- When you add a rule that limits outside actions, put the hard limit in code, in the scripts that act, not only in this prompt.
- When you change something every level should follow (role, read order, rules, safety), change the common prompt too, not just this file.
- When a request asks for a change, write its plan first; only questions and small fixes go without one.
