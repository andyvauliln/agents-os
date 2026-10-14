# Questions: SKILL.md

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-05: Does a question with its answer update the knowledge?

> telll me for example i have question you answer me do we update any knowledge from that?

Yes. The agent stores the question and its answer together as one owner input, word for word. It also records them in the Questions file of the item that the question is about.

The answer can add a new fact. Then the agent also writes that fact in these locations:

1. The docs.
2. The decisions.
3. The changelog.
4. The metadata of the items that the fact is about.

The agent also writes the answer into the doc where the owner looked for it.

Docs improved: none, the answer was already in agents/system/.claude/skills/knowledge-intake/SKILL.md (step 6) and docs/metadata.md (section 18.4).
