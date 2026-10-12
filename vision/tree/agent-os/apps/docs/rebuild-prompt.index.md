---
about: agent-os/apps/docs/rebuild-prompt.md
node: n-43.1.4
written: 2026-10-12T00:00:00Z
by: knowledge-base-agent
---
# rebuild-prompt.md

## What it is

The prompt an AI coding agent follows to build the `apps/` folder again: its tree, the metadata format, the rules for research clones and forks, the build order, the checks and what not to build. It builds only the apps folder itself and hands each app to that app's own rebuild prompt, starting with the project IDE's.

## Who looks after it

The knowledge base agent, with the `rebuild-prompt-doc` skill and its outline for an app. The owner can read and change it.

## When and how it changes

After every change to the design of `apps/`, last of the four apps docs. The agent updates the tree, the parts, the build order, the checks and "Do not build"; a point the owner decides moves out of "Do not build" into its part.

## Who uses it, and when

An AI agent rebuilding the repository, called from the system's rebuild prompt; an agent checking that `apps/` still matches its spec; the owner, to check nothing is missing.

## Where it is mentioned

The system's rebuild prompt lists it in its build order; the apps README lists it; it points down to `apps/project-IDE/docs/rebuild-prompt.md`.

## Related knowledge

It uses the same names as the apps vision and README; the tree notes and the conventions for apps give its paths and rules; the IDE's own prompt builds the IDE's files.

## Keep in mind

- When you write it, never put a key value or a live setting in it.
- When the IDE's own prompt is empty, say how to fall back to the system prompt's IDE parts.
