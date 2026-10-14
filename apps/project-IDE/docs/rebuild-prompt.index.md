---
about: agent-os/apps/project-IDE/docs/rebuild-prompt.md
basis: 520aeed75fd2
written: 2026-10-12T00:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# rebuild-prompt.md

## What it is

The prompt an AI coding agent follows to build the project IDE again exactly: the folder tree, the page's features and store format, the data format, every build script with its options, the sync, the server's routes, settings and safety checks, the agent, the build order, the acceptance checks and what not to build yet. It builds only the IDE's own folder and its agent, skills and scripts, assuming the levels above exist.

## Who looks after it

The knowledge base agent writes it with the `rebuild-prompt-doc` skill, last of the IDE's docs. The owner can read it to check that nothing is missing.

## When and how it changes

After every change to the IDE's design, after the vision, the README and its ASD-STE100 version. The agent updates the parts the change touches and always checks the tree, the build order, the acceptance checks and Do not build. A stage one item that gets built leaves Do not build and goes into its part.

## Who uses it, and when

An AI agent rebuilding the IDE or checking it against its spec; the project IDE agent before changing the page, the scripts or the server; the owner, to check it.

## Where it is mentioned

The IDE's README lists it in its table of docs. The system's and the apps' rebuild prompts list it among the apps to build. The `rebuild-prompt-doc` skill names its outline for an app.

## Related knowledge

It must match the page, the scripts in `vision/tools/`, the server in `vision/server/`, the `ide-build` and `ide-sync` skills, the project IDE agent and the IDE's README. Paths and keys come from those files, character for character.

## Keep in mind

- When you write about a key, write its name only, never its value.
- When you change a server setting, a route, the store format or a script option, change it here the same round.
- When a point is still open, list it under Do not build instead of describing it as built.
