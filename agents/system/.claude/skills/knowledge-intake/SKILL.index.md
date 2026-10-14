---
about: agent-os/agents/system/.claude/skills/knowledge-intake/SKILL.md
basis: f4a07d43cfc5
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# knowledge-intake/SKILL.md

## What it is

The skill the knowledge base agent uses to save and sort one input: an owner message, a change to the system's files, or something a session learned. It keeps the owner's words exactly, with the date and where they came from, works out what is new (a fact, a rule, a decision, an idea, an open question), finds where each piece belongs, writes it there and brings every related file, agent, skill, doc and list in line, the levels above included. Every question the owner asks gets its answer written where they should have found it.

## Who looks after it

It is written by the owner and knowledge-base-agent.

## When and how it changes

It changes when the owner changes how inputs, answers, questions or decisions are filed, or how a change ripples to related files.

## Who uses it, and when

It is read by knowledge-base-agent and ide-sync.

## Where it is mentioned

It is described in its folder's How it works file `agents/system/.claude/skills/knowledge-intake/knowledge-intake.index.md`.

## Related knowledge

It writes `apps/project-IDE/data/inputs/`, `apps/project-IDE/data/decisions.md` and `apps/project-IDE/data/changelog.md`. It links to `agents/system/.claude/skills/file-index/SKILL.md`. It is read by `agents/system/.claude/agents/knowledge-base-agent.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "When and how to update each doc"), `docs/metadata.md` and `agents/system/docs/README.md` (section "The knowledge base and the docs").

## Keep in mind

- When the owner asks a question, save our answer with it and write the explanation into the docs: the answer is knowledge too.
- When a file changes, walk everything that depends on it before you finish.
