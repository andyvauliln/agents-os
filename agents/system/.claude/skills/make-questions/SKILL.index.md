---
about: agent-os/agents/system/.claude/skills/make-questions/SKILL.md
basis: 0d93cb0f0146
confirmed: 2026-10-14T15:07:13Z
---
# make-questions/SKILL.md

## Summary

The skill that finds what only the owner can answer. It reads one item, a folder or a whole level, and looks for gaps, contradictions, defaults an agent took without the owner, proposals still waiting for a yes, and recorded answers that are no longer true. It also reads the owner's own past questions: many questions on one item show a weak doc, and the skill improves that doc before it asks anything. Each question it writes goes into the item's Questions file, part "Open questions for the owner", with one sentence on why it matters and a recommended answer, at most five per item. Then it tells the owner the count and the most important ones, and rebuilds the page.

## Keep in mind

- Ask only what the docs cannot answer; fix a weak doc instead of asking.
- Give every question a recommendation, so the owner can answer with one word.
- When the owner answers, the answer goes into the docs and the question leaves the file.
