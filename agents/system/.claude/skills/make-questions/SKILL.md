---
name: make-questions
description: Analyse one item, a folder or a whole level of the Agent OS and write the questions only the owner can answer - gaps, contradictions, defaults taken without the owner, proposals waiting for a yes - into each item's Questions file, with one sentence on why each matters and a recommended answer. Use it when the owner asks for questions, after a doc or a plan is written, and before a stage is called finished.
---

# Make questions for the owner

The owner decides; agents propose. This skill finds what is still the owner's to decide and puts it where the owner sees it: the "Open questions for the owner" part of the item's Questions file (`x.questions.md`), which the File Tree page shows as the Questions tab. The full logic of the Questions file is in `docs/metadata.md` (Questions).

## When to use it

- The owner asks for questions about an item, a folder or a level.
- After a doc (vision, README, rebuild prompt) is written or rewritten: its open points.
- After a plan is written (`change-plan` writes its choices itself; run this skill for what the plan missed).
- Before a stage is called finished: every item of that stage.

Not for questions the docs can already answer: answer them in the docs instead.

## What to look for

Read the item, its How it works and Details files, its Questions file, the How it works of the folders above, the docs of its level, and the decisions and inputs named in its Details `sources`. Then list:

1. **Gaps**: something the item needs that nobody decided (a name, a limit, a place, who may do what).
2. **Contradictions**: two files, or a file and a decision, that say different things.
3. **Defaults**: a choice an agent made without the owner, still marked proposed.
4. **Proposals waiting**: ideas and plans with status proposed or waiting.
5. **Stale answers**: an owner's question whose recorded answer is no longer true (fix the answer, do not ask again).
6. **The owner's own questions**: read part "The owner's questions" of the item and its neighbours. Many questions on one item, or the same question twice, show a weak doc. Improve that doc as `knowledge-intake` step 6 says, and ask the owner only what the docs cannot answer.

Keep only what the owner must decide. Drop what an agent can settle by reading the docs, and anything already open in the file.

## How to write each question

```markdown
- **<The question, one sentence, in the owner's words where possible>?** <Why it matters, one sentence.> Recommended: <the answer you suggest>. From: <where it came from, e.g. "the plan Leave vision", "the system README", "checking the keys folder">.
```

- Plain words, no decision codes, no input ids, no hashes.
- One question per choice. A yes/no or a pick from two or three options is best.
- At most five new questions per item in one run; put the most important first.
- If the item has no Questions file, create it with both parts ("The owner's questions" says "None recorded yet.").

## Steps

1. Pick the items: the one asked for, or every item of the folder or level, children first.
2. For each item, collect the list above and write the questions into its file.
3. Also write the open points of a doc into its "Still open" part, if the doc has one.
4. Tell the owner in the thread, in a few lines: how many questions, on which items, and the two or three most important ones with your recommendation. Put a choice that changes their goal on a decision card.
5. Rebuild the page (`ide-build`) so the Questions tabs show them.

## Checks

- Every new question has why, a recommendation and where it came from.
- No question duplicates one already open, and none is answerable from the docs.
- No secret value anywhere; no `.env` file was opened.
