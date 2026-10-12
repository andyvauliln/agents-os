---
about: agent-os/agents/system/docs/inputs-vision.md
node: n-2.23
written: 2026-10-09T19:45:20Z
by: knowledge-base-agent
---
# inputs-vision.md

## What it is

All of the owner's requirements for the system in one place, taken only from the owner's own messages. Repeated points appear once, and a point the owner later changed appears only in its newest form. It is written in Simplified Technical English (ASD-STE100): short sentences, one rule per line, each rule with its own code, grouped by scope (the system, agent levels, common file rules, configs, runs, self-improvement, docs, the project IDE and more).

## Who looks after it

The knowledge base agent. It is not a proposal list: Claude's own ideas stay out of it.

## When and how it changes

- After every owner input that changes how the system should be.
- A newer input replaces the older rule on the same subject; the old rule is removed, not kept beside it.
- A new subject gets a new rule code in the scope it belongs to.

## Who uses it, and when

- Any AI or person who needs the owner's wishes without reading every message.
- The vision, README and rebuild prompt are checked against it.

## Keep in mind

- Only the owner's words count here. Decisions Claude made as defaults belong in the other docs.
