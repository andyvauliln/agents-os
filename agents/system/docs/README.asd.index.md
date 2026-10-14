---
about: agent-os/agents/system/docs/README.asd.md
basis: 196f8a57e292
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# README.asd.md

## What it is

The system's README again, in ASD-STE100 Simplified Technical English. It has the same content and the same section order as `README.md`, in short sentences: descriptive ones at most 25 words, procedural ones at most 20, active voice, present tense, one word for one meaning, numbered steps for procedures. Its first line says that `README.md` is the source.

## Who looks after it

The knowledge base agent writes it right after the README. The planned skill `readme-asd-doc` will hold its rules; until it exists, the rules are in the README's own skill and in this note.

## When and how it changes

It changes every time `README.md` changes. The agent rewrites the matching sections and checks sentence and paragraph lengths. It never adds a fact the README does not have.

## Who uses it, and when

The owner reads it to compare with the README and to check that the README says things clearly. Agents read the README, not this file.

## Where it is mentioned

`agents/system/CLAUDE.md` says every README has an ASD-STE100 twin; the rebuild prompt lists it among the four docs; the File Tree page shows it as its own tab beside the README.

## Related knowledge

The source is `README.md` in this folder. Every level has the same pair: the project's, trading's and the apps' READMEs each have a `README.asd.md`.

## Keep in mind

- When the two differ, `README.md` is correct: fix this file.
- When you write here, use the README's names exactly; do not invent synonyms.
- When a sentence runs over the limit, split it or make a list.
