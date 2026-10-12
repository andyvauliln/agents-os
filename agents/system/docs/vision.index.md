---
about: agent-os/agents/system/docs/vision.md
node: n-2.2
basis: 4613e386242d
written: 2026-10-07T19:21:01Z
by: knowledge-base-agent
confirmed: 2026-10-09T09:57:03Z
---
# vision.md

## What it is

The top-level doc, the first one anyone reads: what we are building and why, the concept, how the system should work, the business logic (how it turns ideas into results and decides what to keep), a few worked examples, where the project stands and what is still open. Mostly for people, and every agent reads it for the high-level view. From here the reader goes deeper, into the README.

## Who looks after it

The knowledge base agent writes and updates it, following the vision skill (`vision-doc`), which sets its sections, its length and how it is written. The owner can also change it on this page; the agent then folds the change in.

## When and how it changes

- After every owner message, answer or change that touches the goals, the concept, how the system should work, the business rules, the plans, a principle, an idea or an open question.
- The agent saves the message first, finds the sections it touches and rewrites those passages, so the doc still reads as one story about today.
- An answered question leaves "Open questions" and the answer moves into the section it belongs to. An idea the owner accepts moves out of "Ideas we are still weighing" the same way.
- Then the README and the rebuild prompt are brought in line, in that order.

## Who uses it, and when

- Everyone new to the project reads it first, technical or not.
- The owner reads it to check that the system is still what they want to build.
- Every agent can read it as background on what the system is trying to achieve and why.
- The knowledge base agent reads it before writing the other docs, so they all agree with it.

## Where it is mentioned

- The `CLAUDE.md` in the system's `.claude/` folder, as the first thing to read.
- The README, which opens by sending readers here for the why.
- The knowledge base agent's instructions and the vision skill.
- The vision of every domain and of the levels each domain defines, which builds on this one and only adds what is different.
- This file tree.

## Related knowledge

- The README describes every part of the system exactly and where each part's docs are; the vision stays above it, with no folders or files.
- The rebuild prompt holds the exact spec; its short description of the system uses the vision's words.
- The glossary explains the words it uses, and the roadmap holds the detailed plan behind "What comes next".
- Behind it sit the owner's messages and decisions, kept in the knowledge base agent's notes.

## Keep in mind

- When you update it, state facts as they are now, with no "who said what, when".
- When something is only an idea, keep it under "Ideas we are still weighing" until the owner decides.
- When you add an example, use only rules that are decided.
- When you are about to name a folder or a file, stop: that belongs in the README.
- When a domain's, strategy's or agent's own docs change, check whether this doc needs the change too: updates climb to the top.
