---
about: agent-os/agents/system/.claude/skills/ide-sync/SKILL.md
basis: 047a4444f20c
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# ide-sync/SKILL.md

## What it is

The skill for the way back from the page. It reads everything waiting in the page's store (messages, notes, file edits, How it works edits, new or deleted items, requests), saves each word for word as an input in `apps/project-IDE/data/inputs/`, writes edits into their files, applies each note meant as a change and turns any other open note into a question in the item's Questions file, runs the requests, rebuilds and republishes the page, and clears only what reached a file. It starts when the owner presses Apply changes on the page or says "sync the file tree". A deletion is a round of its own: read the owner's note, delete the item and its metadata files, remove every mention in other files, record it with the note and rebuild. On claude.ai the store is read with the artifact data tool; on the owner's server it is a folder of JSON files, and the edits made there are already in the files, so it checks and confirms them.

## Who looks after it

It is written by the owner, project-ide-agent and knowledge-base-agent.

## When and how it changes

It changes when the page's store, the kinds of things the owner can leave on the page, or the delete and Apply changes rounds change.

## Who uses it, and when

It is read by project-ide-agent and the server's Claude Code session.

## Where it is mentioned

It is described in `apps/project-IDE/docs/README.md` and its folder's How it works file `agents/system/.claude/skills/ide-sync/ide-sync.index.md`.

## Related knowledge

It writes `apps/project-IDE/data/`. It reads `agents/system/.claude/skills/knowledge-intake/SKILL.md` and `agents/system/.claude/skills/ide-build/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `agents/system/CLAUDE.md` (section "The File Tree page"), `docs/metadata.md`, `agents/system/docs/README.md` (section "The project IDE"), `apps/project-IDE/docs/README.md` (section "How the page is built and checked") and `apps/project-IDE/docs/README.md` (section "How the owner's work comes back").

## Keep in mind

- When an edit contradicts something the owner decided, ask the owner instead of applying it.
- A file that only mentions a deleted item is edited, never deleted.
