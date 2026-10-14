---
about: agent-os/agents/system/docs/how-to/process-an-input.md
node: n-2.11.10
basis: fbf18f3b008a
written: 2026-10-01T00:56:11Z
by: summary-worker
confirmed: 2026-10-07T19:02:04Z
---
# process-an-input.md

## Summary

The runbook that turns any owner input or system change into knowledge; the knowledge agent follows it through its `knowledge-intake` skill. It stores the input word for word (a question with its answer), extracts the knowledge, places each piece in the one doc that owns it, ripples it to everything that states the same thing, records decisions and the changelog, rebuilds the map, refreshes every stale How it works summary and reports a few plain lines to the owner.

## Keep in mind

- When the owner says anything about how the system should be, run it through this flow; nothing is "just chat".
- When you mark a piece of knowledge decided, be sure the owner said it; otherwise it is proposed or open.
