---
about: agent-os/agents/system/docs/vision.md
basis: 915334076110
written: 2026-10-12T00:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# vision.md

## What it is

The system's vision: the first doc to read about the system domain. It says why the Agent OS has a system domain, the concept of agents as a family tree with shared parts, how the system should work step by step, its business logic, examples, what the owner sees and does, where the project stands, its principles, the ideas still being weighed and the open questions.

## Who looks after it

The knowledge base agent writes it with the `vision-doc` skill. The owner can also change it on the File Tree page.

## When and how it changes

It changes when an owner input or a decision changes the goals, the concept, how the system should behave, a business rule or the stage. The agent rewrites the passages it touches so the doc still reads as one story, then brings the README, its ASD-STE100 version and the rebuild prompt in line, in that order, and checks the project's vision above it.

## Who uses it, and when

The owner and anyone new to the system read it first, after the project's vision. `CLAUDE.md` puts it third in its reading list, so every Claude reads it before it works on the system; the knowledge base agent reads it before it writes the system's other docs or a domain's vision.

## Where it is mentioned

`agents/system/CLAUDE.md` lists it under Read first; the system's README and its ASD-STE100 version point to it in their first section; this folder's rebuild prompt says how it is written; the project's README names the system's docs.

## Related knowledge

It sits below the project's vision (`docs/vision.md`) and above trading's vision (`agents/trading/docs/vision.md`). The system's README describes the same things exactly, with paths. It is built from the owner's inputs and the decisions in `vision/docs/`.

## Keep in mind

- When you write here, keep only what holds for the whole system; trading's detail belongs in trading's docs.
- When you state a rule, say whether the owner decided it or it is proposed.
- When the stage changes, update "Where we are and what comes next" and the project's vision too.
- When you name a file, do it only in "Going deeper".
