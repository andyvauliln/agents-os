---
about: agent-os/apps/project-IDE/data/inputs/
basis: 2f9410effad2
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-15T09:57:53Z
---
# inputs/

## What it is

The archive of every owner input, word for word, from any channel (project chat, threads, comments on files, the File Tree page), so nothing the owner said is lost and every doc can say where its knowledge came from. Each input is one Markdown file with a header, the raw text and what it was processed into; a question is stored with its answer. `index.json` lists every input with its categories and summary, and `README.md` explains the archive and its categories. The knowledge base agent saves each input on receipt, as the first step of processing it; page messages wait in the page's store until the next sync.

## Who looks after it

It is written by knowledge-base-agent, knowledge-intake and ide-sync.

## When and how it changes

It changes when the owner says anything about the system.

## Who uses it, and when

It is read by knowledge-base-agent and every AI session when a summary is unclear.

## Where it is mentioned

It is described in `apps/project-IDE/data/inputs/README.md`, `apps/project-IDE/data/inputs/index.json`, `docs/metadata.md` and its folder's How it works file `apps/project-IDE/data/data.index.md`.

## Related knowledge

It is written by `agents/system/.claude/skills/knowledge-intake/SKILL.md` and `agents/system/.claude/skills/ide-sync/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules") and `docs/metadata.md` (section "Owner inputs").

## Keep in mind

- When the owner says anything about the system, in any channel, store it here word for word before filing its knowledge.
- When an input is stored, never edit its raw text; corrections go into the docs.
