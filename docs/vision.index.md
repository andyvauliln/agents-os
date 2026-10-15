---
about: agent-os/docs/vision.md
basis: a1da7494cdba
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# vision.md

## What it is

The top doc of the whole project, read first: what the Agent OS is and why, how the owner builds it by vibecoding with the project IDE as their window, the concept, how a round of work goes, the rules the project follows, examples, the stages and the open questions. It ends by pointing to the project README.

## Who looks after it

The knowledge base agent, with the `vision-doc` skill. The owner can also change it on the File Tree page.

## When and how it changes

When an input changes the project's goals, its way of working, its levels, its stage, a rule, an idea or an open question. The agent finds the sections the input touches, rewrites them so the doc still reads as one story, moves answered questions into their sections, and then brings the README, its ASD-STE100 version and the rebuild prompt in line, in that order.

## Who uses it, and when

The owner and anyone they share the project with, first. Claude Code started in the system folder reads it first of all docs, from its entry file. The knowledge base agent reads it before writing the other project docs.

## Where it is mentioned

`agents/system/CLAUDE.md` (first in the reading list), the project README's "In short", the project rebuild prompt, the system vision, which sums it up, and the `vision-doc` skill.

## Related knowledge

The project README describes every part it names by what it does, with exact paths; the rebuild prompt states it as instructions; the system vision goes deeper into how the agents work. The owner's inputs and the decisions in `apps/project-IDE/data/` are what it rests on.

## Keep in mind

- When you write it, stay high: no paths except the README's path at the end.
- When an idea or a default is ours, call it an idea or still open; only the owner decides.
- When the stage changes, update "Where we are and what comes next" and the README's stages in the same round.
