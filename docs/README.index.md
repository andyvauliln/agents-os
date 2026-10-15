---
about: agent-os/docs/README.md
basis: 7f43c7b1bfea
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-15T06:43:18Z
---
# README.md

## What it is

The exact description of the whole repository: every top part, what it holds, how the parts connect, the levels and where each level's docs are, the metadata files, the steps of a round of work and the stages, with the path to each part's own docs.

## Who looks after it

The knowledge base agent, with the `readme-doc` skill. The owner can also change it on the File Tree page.

## When and how it changes

After every input or change that touches a top part of the repository, after the project vision and before the ASD-STE100 version and the rebuild prompt. The agent rewrites the parts touched, checks that every "Its docs" path is real, updates "Still open in the design", and brings the front page in line if "In short" changed.

## Who uses it, and when

Readers after the vision, the owner after each round, Claude Code right after the project vision, and every agent before it works on a part it does not know.

## Where it is mentioned

The project vision's last section, `agents/system/CLAUDE.md`, the front page, `README.asd.md` (its ASD-STE100 version), the project rebuild prompt and the `readme-doc` skill.

## Related knowledge

It uses the vision's words. `README.asd.md` must keep its content and section order. The READMEs of the system, trading, the apps and the project IDE describe their own parts, which this one sums up. The owner's inputs and the decisions in `apps/project-IDE/data/` are behind it.

## Keep in mind

- When you add or move a top folder, add or move its part here and in the table of docs in the same round.
- When this file changes, rewrite `README.asd.md` from it right after.
- When you name a path, check that it exists in the repository.
