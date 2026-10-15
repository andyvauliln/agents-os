---
about: agent-os/agents/system/.claude/skills/readme-doc/SKILL.md
basis: 4a18dc0700af
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# readme-doc/SKILL.md

## What it is

The skill the knowledge base agent uses to write the README: the full, exact overview of how the whole system works, one section per main part, each ending with the path to that part's own docs, and nothing about the logic inside agents. Its outline lists the sections and the parts, and the File Tree page shows that outline as the README's Example. It sets lengths for each level, gives examples of too vague and too deep, says when the README is updated (after the vision, before the rebuild prompt) and what its How it works panel answers.

## Who looks after it

It is written by the owner and knowledge-base-agent.

## When and how it changes

It changes when the owner changes what a README must hold, its outline, lengths or update order.

## Who uses it, and when

It is read by knowledge-base-agent.

## Where it is mentioned

It is described in its folder's How it works file `agents/system/.claude/skills/readme-doc/readme-doc.index.md`.

## Related knowledge

It writes `agents/system/docs/README.md` and `docs/README.md`. It links to `agents/system/.claude/skills/readme-asd-doc/SKILL.md`. It is read by `agents/system/.claude/agents/knowledge-base-agent.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "When and how to update each doc"), `docs/metadata.md` and `agents/system/docs/README.md` (section "The knowledge base and the docs").

## Keep in mind

- When you describe a part, say what it is, what it holds and what it takes and gives; never how an agent decides.
- When you give a part's docs path, check that it exists in the tree.
- When you change this doc at one level, check the same doc at the level above and climb to the system.
