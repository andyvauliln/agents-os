---
about: agent-os/agents/system/docs/rebuild-prompt.md
node: n-2.22
basis: f6ea621dc9a1
written: 2026-10-07T08:58:18Z
by: knowledge-base-agent
confirmed: 2026-10-09T09:57:03Z
---
# rebuild-prompt.md

## What it is

A prompt for an AI coding agent, such as Claude Code. Given this file and an empty repository, the agent builds the top of the repository and the system's own folder exactly: the same folders and files, formats, settings, scripts, helpers, safety rules and project IDE. It then runs the rebuild prompts of the levels below in order, starting with trading's, which lists the prediction-market domain's. It holds nothing about trading itself.

## Who looks after it

The knowledge base agent writes and keeps it, following the rebuild prompt skill (`rebuild-prompt-doc`), which sets its sections, its length and how it is written for AI. The owner can also change it on this page; the agent then folds the change in.

## When and how it changes

- After every change to the system's design, last of all the docs, once the vision and the README are updated.
- The agent finds the sections the change touches and rewrites them, always checking the tree, the build order, the acceptance checks and the list of what not to build.
- A point the owner decides leaves "Do not build" and goes into its part, the tree and the build order.
- Every path and format is taken from the tree notes, never from memory.

## Who uses it, and when

- An AI agent rebuilding the system, or a part of it, from nothing.
- An agent checking whether the system still matches its spec.
- The owner, to check that nothing important is missing.

## Where it is mentioned

- The knowledge base agent's instructions and the rebuild prompt skill.
- The vision and README skills, whose last steps bring it in line.
- The README's description of the knowledge base and the docs.
- This file tree.

## Related knowledge

- The vision gives the purpose; the prompt's short description of the system uses its words.
- The README describes the same parts for reading; the prompt gives them as exact instructions.
- The tree notes and the topic notes on conventions, data and safety are where every exact name and format comes from.

## Keep in mind

- When the design changes, update the prompt in the same round, last.
- When a detail is open, list it under "Do not build"; never let the AI guess it.
- When you write about a key, write its name only, never its value.
- When you name a file, copy its path from the tree notes character for character.
- When a domain's, strategy's or agent's own docs change, check whether this doc needs the change too: updates climb to the top.
