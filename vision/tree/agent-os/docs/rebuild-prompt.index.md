---
about: agent-os/docs/rebuild-prompt.md
node: n-57.4
basis: 0cac8276f67e
written: 2026-10-12T00:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-12T15:40:56Z
---
# rebuild-prompt.md

## What it is

The prompt an AI coding agent follows to build the repository's top level again from an empty repository: the root files, `.gitignore`, the keys folder without any key value, the project docs and the top folders with their metadata, then each level through its own rebuild prompt, in order, ending with the checks that prove it is the same.

## Who looks after it

The knowledge base agent, with the `rebuild-prompt-doc` skill. The owner can also change it on the File Tree page.

## When and how it changes

After every change to the top level's design, last of the project docs, after the vision, the README and its ASD-STE100 version. The agent updates the tree, the parts, the build order, the checks and "Do not build"; a point the owner decides leaves "Do not build" and goes into its part.

## Who uses it, and when

An AI agent rebuilding the repository or checking it against its spec; the owner, to check nothing is missing.

## Where it is mentioned

The project README, the `rebuild-prompt-doc` skill, and the rebuild prompts of the levels below, which it lists in build order: the system, the apps with the project IDE, and trading.

## Related knowledge

It must agree with the project vision and README and use their names. The tree notes in `vision/docs/file-tree.md` give the exact paths; the lower prompts build everything inside their own folders.

## Keep in mind

- When you write it, never give a key value; key names only.
- When a point is open, put it under "Do not build" with what to leave in its place.
- When you add a level, add its prompt to the build order here.
