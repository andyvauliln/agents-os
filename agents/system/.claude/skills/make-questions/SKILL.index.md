---
about: agent-os/agents/system/.claude/skills/make-questions/SKILL.md
basis: 0d93cb0f0146
confirmed: 2026-10-14T15:07:13Z
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
---
# make-questions/SKILL.md

## What it is

The skill that finds what only the owner can answer. It reads one item, a folder or a whole level, and looks for gaps, contradictions, defaults an agent took without the owner, proposals still waiting for a yes, and recorded answers that are no longer true. It also reads the owner's own past questions: many questions on one item show a weak doc, and the skill improves that doc before it asks anything. Each question it writes goes into the item's Questions file, part "Open questions for the owner", with one sentence on why it matters and a recommended answer, at most five per item. Then it tells the owner the count and the most important ones, and rebuilds the page.

## Who looks after it

It is written by the owner and knowledge-base-agent.

## When and how it changes

It changes when the owner changes how open questions are found, written or answered.

## Who uses it, and when

It is read by knowledge-base-agent, change-plan and every AI that finishes a doc or a plan.

## Where it is mentioned

It is described in `docs/metadata.md` and its folder's How it works file `agents/system/.claude/skills/make-questions/make-questions.index.md`.

## Related knowledge

It links to `agents/system/.claude/skills/knowledge-intake/SKILL.md`. It is read by `agents/system/.claude/skills/change-plan/SKILL.md` and `agents/system/CLAUDE.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "When and how to update each doc"), `docs/metadata.md` and `agents/system/docs/README.md` (section "The knowledge base and the docs").

## Keep in mind

- Ask only what the docs cannot answer; fix a weak doc instead of asking.
- Give every question a recommendation, so the owner can answer with one word.
- When the owner answers, the answer goes into the docs and the question leaves the file.
