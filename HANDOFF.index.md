---
about: agent-os/HANDOFF.md
basis: 1dfd7b76e111
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-15T07:11:37Z
---
# HANDOFF.md

## What it is

A planning-time note at the top of the repository that tells a new session how to pick the planning work up: pull `main`, start Claude Code in `agents/system/`, where it reads `agents/system/CLAUDE.md` first, then the docs in the order that file gives. It also says how to start the File Tree page on the owner's server, how to rebuild the page, where things stand and the rules to keep. When the owner asks "can we continue?", this is the place that says how.

## Who looks after it

The agent that ends a stretch of planning work writes it by hand, so the next session can start. The owner can also change it on the File Tree page.

## When and how it changes

At the end of a planning stretch, or when the way to start a session changes. It is not rebuilt by a script. Its "Where things stand" part is a snapshot of its date; the changelog and the docs are newer when they disagree.

## Who uses it, and when

Whoever picks the work up in a new session, person or AI, before the first round. `agents/system/CLAUDE.md` is the entry point Claude Code loads; this note explains how to get there and what was going on.

## Where it is mentioned

The project README and its ASD-STE100 twin, the project rebuild prompt (which copies it only when the owner hands it over), and the cloud project's memory.

## Related knowledge

Whether this note is still needed once `agents/system/CLAUDE.md` is the only entry point is open for the owner.

## Keep in mind

- When the way to start a session or to run the page changes, update this note in the same round.
- When it disagrees with `agents/system/CLAUDE.md`, the latter is right; fix this note.
