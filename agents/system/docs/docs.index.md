---
about: agent-os/agents/system/docs/
basis: 125905a6db43
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# docs/

## What it is

The system domain's docs: four docs about the system, read in order. `vision.md` says why and how the system should work; `README.md` maps every part exactly with the path to its docs; `README.asd.md` is the README again in ASD-STE100 for the owner to compare; `rebuild-prompt.md` is the spec an AI rebuilds `agents/system/` from. Next to each sit its notes, an outline (`x.example.md`) and its open questions (`x.questions.md`). `subagents.link/` holds one folder link per domain's docs.

## Who looks after it

The knowledge base agent writes the four docs; the owner can edit them on the File Tree page; `relink` makes the child links.

## When and how it changes

After every owner input or change that touches the system, the docs are updated in the order vision, README, README.asd, rebuild prompt.

## Who uses it, and when

The owner, every Claude that works on the system (through `CLAUDE.md`'s reading list), and the system manager when it reads its domains' docs through `subagents.link/`.

## Where it is mentioned

`agents/system/CLAUDE.md` (Read first, and the table of docs); the project's README; the rebuild prompts of the project and of the system.

## Related knowledge

The project's docs are in `docs/`; trading's in `agents/trading/docs/`; the apps' in `apps/docs/` and `apps/project-IDE/docs/`. The records the docs are built from (the owner's inputs and the decisions) are in `apps/project-IDE/data/`.

## Keep in mind

- When a lower level's docs change, check these four, then the project's.
- When you add a doc here, list it in the README and the rebuild prompt.
- When you write for people, use no reference numbers, ids or decision codes.
