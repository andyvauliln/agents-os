---
about: agent-os/apps/project-IDE/data/decisions.md
node: n-2.6
basis: ce974958f067
written: 2026-10-05T13:25:49Z
by: knowledge-base-agent
confirmed: 2026-10-07T14:22:08Z
---
# decisions.md

## Summary

The decision log: an append-only history of what the owner decided, when, why and from which input, so settled questions are not reopened. Each entry has an id, date, decision, reasons, sources and a status (active, partly superseded, superseded); the rule itself lives in a topic doc that points back here. The knowledge base agent records owner decisions while processing an input. It sits with the project's records in `apps/project-IDE/data/`. Self-improvement and support agents may add proposals marked "pending owner", which the owner approves or rejects in the UI.

## Keep in mind

- When you record a decision, write the rule in the topic doc that owns it; this log only says when and why.
- When you propose a change to a shared file or the common prompt, add it here marked "pending owner" and wait for the owner.
- When a decision is replaced, mark the old entry superseded instead of editing or deleting it.
