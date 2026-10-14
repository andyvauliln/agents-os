---
about: agent-os/agents/trading/prediction-market/scripts/relink.system.link.js
node: n-19.3.2
basis: 9879c7134b51
written: 2026-10-01T00:56:32Z
by: summary-worker
confirmed: 2026-10-09T10:03:12Z
---
# relink.system.link.js

## Summary

A file link to the shared `relink` script in the system's `scripts/`. Run from the domain folder as `node scripts/relink.system.link.js`, it relinks only the domain: its file links from the domain's links file and its entry in the system's `subagents.link/` folders. The domain session runs it after editing its links file, and the proposed `PostToolUse` hook runs it too. `create-agent` adds this link at every level below the system.

## Keep in mind

- When you edit the domain's links file, run this and read its report (`+`, `-`, `=`, then `check ok`); fix anything it flags.
