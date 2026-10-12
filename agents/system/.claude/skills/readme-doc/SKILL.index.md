---
about: agent-os/agents/system/.claude/skills/readme-doc/SKILL.md
node: n-10.1.2.4
basis: 48cb69c73630
written: 2026-10-06T21:56:21Z
by: knowledge-base-agent
confirmed: 2026-10-07T19:02:04Z
---
# readme-doc/SKILL.md

## Summary

The skill the knowledge base agent uses to write the README: the full, exact overview of how the whole system works, one section per main part, each ending with the path to that part's own docs, and nothing about the logic inside agents. Its outline lists the sections and the parts, and the File Tree page shows that outline as the README's Example. It sets lengths for each level, gives examples of too vague and too deep, says when the README is updated (after the vision, before the rebuild prompt) and what its How it works panel answers.

## Keep in mind

- When you describe a part, say what it is, what it holds and what it takes and gives; never how an agent decides.
- When you give a part's docs path, check that it exists in the tree.
- When you change this doc at one level, check the same doc at the level above and climb to the system.
