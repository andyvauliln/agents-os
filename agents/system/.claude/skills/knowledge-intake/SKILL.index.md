---
about: agent-os/agents/system/.claude/skills/knowledge-intake/SKILL.md
node: n-10.1.2.1
basis: 5f71dc5ded5b
written: 2026-10-06T20:55:10Z
by: knowledge-base-agent
confirmed: 2026-10-07T09:34:43Z
---
# knowledge-intake/SKILL.md

## Summary

The skill the knowledge base agent uses to save and sort one input: an owner message, a change to the system's files, or something a session learned. It keeps the owner's words exactly, with the date and where they came from, works out what is new (a fact, a rule, a decision, an idea, an open question), finds where each piece belongs, writes it there and brings every related file, agent, skill, doc and list in line, the levels above included. Every question the owner asks gets its answer written where they should have found it.

## Keep in mind

- When the owner asks a question, save our answer with it and write the explanation into the docs: the answer is knowledge too.
- When a file changes, walk everything that depends on it before you finish.
