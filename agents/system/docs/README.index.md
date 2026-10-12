---
about: agent-os/agents/system/docs/README.md
node: n-2.1
basis: eec9264e4a3c
written: 2026-10-06T21:56:21Z
by: knowledge-base-agent
confirmed: 2026-10-09T09:57:03Z
---
# README.md

## What it is

The full, long description of how the whole Agent OS works, read after the vision by anyone who wants a deeper and exact understanding, people and AI alike. It describes every main part of the system: what it is, what it holds, what it takes from and gives to the other parts, and when and where it runs. Each part ends with the path to that part's own docs. It never describes the logic inside an agent.

## Who looks after it

The knowledge base agent writes and keeps it, following the README skill (`readme-doc`), which sets its sections, its length and how it is written. The owner can also change it on this page; the agent then folds the change in.

## When and how it changes

- After every message, answer or change that touches a part of the system, after the vision and before the rebuild prompt.
- The agent saves the message first, finds the parts it touches and rewrites those passages, so each part still reads as one current description.
- "Still open in the design" and the table of where each part's docs are get checked every time: a settled detail moves into its part, and every path must be real.
- If the short description of the project changes, the front page of the repo is brought in line too.

## Who uses it, and when

- Anyone who has read the vision and wants to know exactly how the system works and where everything is.
- The owner, to check the whole picture after a round of changes.
- Every agent, before it works on a part of the system it does not know yet.
- The knowledge base agent, before it writes the rebuild prompt, so names and facts stay the same.

## Where it is mentioned

- The vision's last section, which sends readers here to go deeper.
- The short front page at the root of the repo.
- The `CLAUDE.md` in the system's `.claude/` folder, as the second thing to read.
- The knowledge base agent's instructions, the README skill and the rebuild prompt's skill.
- The README of every domain, strategy and trading agent, which does the same for its own parts.
- This file tree.

## Related knowledge

- The vision explains why the system exists, its concept, how it should behave and its business logic; the README describes the parts that do it, in the same words.
- The rebuild prompt turns the same description into exact instructions an AI can rebuild the system from.
- Each part's own docs go deeper into that part, including the logic inside agents, which the README leaves out.
- The file tree describes every single folder and file. Behind it all sit the owner's messages and decisions, kept in the knowledge base agent's notes.

## Keep in mind

- When you add or change a part of the system, give it its section here with the path to its own docs.
- When you are about to explain how an agent decides, stop: that belongs in the agent's own docs.
- When a path changes, fix it in its part and in the table in the same round.
- When something is only an idea, say so; never present it as decided.
- When a domain's, strategy's or agent's own docs change, check whether this doc needs the change too: updates climb to the top.
