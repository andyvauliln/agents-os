---
about: agent-os/apps/project-IDE/data/inputs/YYYY-MM-DD-HHMM-[topic].md
basis: 674b4c90b427
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# YYYY-MM-DD-HHMM-[topic].md

## What it is

The name pattern for one owner input file, named by its date, time and topic. Each holds a header (id, time, channel, categories, one-line summary), the owner's words unchanged, and a list of what it was processed into. When the input is a question, the answer is stored in the same file. The knowledge base agent writes it on receipt.

## Who looks after it

It is written by knowledge-base-agent, knowledge-intake and ide-sync.

## When and how it changes

It changes when a real input file is made each time the owner says something; its raw text never changes after that. It is a name pattern, not a real item: it tells what each item made from it will hold.

## Who uses it, and when

It is read by knowledge-base-agent and every AI session when a summary is unclear.

## Where it is mentioned

It is described in `apps/project-IDE/data/inputs/index.json`, `apps/project-IDE/data/inputs/README.md` and its folder's How it works file `apps/project-IDE/data/inputs/inputs.index.md`.

## Related knowledge

It is written by `agents/system/.claude/skills/knowledge-intake/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules") and `docs/metadata.md` (section "Owner inputs").

## Keep in mind

- When you store an input, copy the owner's words exactly and never edit them later; corrections go into the docs.
- When the input is a question, store the answer in the same file under `## Answer`: the answer is knowledge too.
