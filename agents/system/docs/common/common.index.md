---
about: agent-os/agents/system/docs/common/
node: n-2.17
basis: 6edfe47d315e
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# common/

## Summary

Knowledge shared by every agent, written once and read by all, so no agent folder repeats it. It holds how one agent works inside (`agent-architecture.md`), the mechanics all agents share such as triggers, modes, the stop switch, links and config merging (`shared-mechanics.md`), the base prompt every `CLAUDE.md` builds on (`common-prompt.md`), and the templates self-improvement helpers are built from (`self-improvement-templates.md`). A domain adds its own layer in its own docs. Every agent links the docs it needs into its own `docs/`. Much of it is still proposed, and so is the rule that changes to the common prompt need the owner's approval.

## Keep in mind

- When an agent needs one of these docs, link that file into its own `docs/` through its links file; never copy it.
