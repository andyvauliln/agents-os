---
about: agent-os/agents/system/docs/common/shared-mechanics.md
node: n-2.17.2
basis: 4e8d55657f1f
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# shared-mechanics.md

## Summary

The mechanics every agent shares, written once: triggers (an important file change cancels the current run and starts a new one; other changes wait), the one central scheduler, test and live modes, going live and the general stop switch, `.link` symlinks and when `relink` runs, logging by source, and the order in which configs merge, with a domain's own config between the global one and the agent's. Still open: log format and retention, and whether symlinks are committed to git.

## Keep in mind

- When you merge configs, let a lower layer only tighten a limit, never loosen it; the stop switch overrides everything (proposed rule).
- When a link must be made or removed, let `relink` do it; nothing links into `.secrets/` or any `.claude/`.
