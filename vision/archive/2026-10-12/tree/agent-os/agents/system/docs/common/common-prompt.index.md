---
about: agent-os/agents/system/docs/common/common-prompt.md
node: n-2.17.3
basis: 80465d2de0dc
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# common-prompt.md

## Summary

The base prompt every agent's `.claude/CLAUDE.md` builds on, plus a level part (system manager or domain owner) and a domain's own layer for its levels. It says who the agent is, what to read first, the rules (own files only, outside actions only through scripts that check the mode and the stop switch, changes as new test versions), links and relink, safety musts and reporting. It is mostly proposed; how the base gets into each `CLAUDE.md` is open.

## Keep in mind

- When you want to change this prompt, propose it as "pending owner" in `decisions.md`; it changes only with the owner's approval (proposed rule).
