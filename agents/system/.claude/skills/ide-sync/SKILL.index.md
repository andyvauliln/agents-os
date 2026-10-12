---
about: agent-os/agents/system/.claude/skills/ide-sync/SKILL.md
node: n-10.1.2.6
basis: 6c27a9a2fddf
written: 2026-10-05T16:17:55Z
by: knowledge-base-agent
confirmed: 2026-10-06T11:55:20Z
---
# ide-sync/SKILL.md

## Summary

The skill for the way back from the page: it reads everything waiting in the page's store (messages, notes, file edits, How it works edits, new or deleted items, requests), saves each word for word as an input, writes edits into their files, folds the rest into the tree notes or the page edits file, runs the requests, rebuilds and republishes the page, and clears only what reached a file, which also clears the page's "changed" marks. It starts when the owner presses Apply changes at the top of the page or says "sync the file tree"; a round started by the button ends by marking that request processed last, so the open page shows the new tree, and by answering and resolving the button's comment. A deletion is one round of its own: read the owner's note first, delete the item and its How it works file, remove its line and section from the tree notes, its links and every mention in other files, file it with the note, rebuild and commit; earlier inputs and decisions stay as history. On claude.ai the store is read with the artifact data tool; on the owner's server it is a folder of JSON files in the repository, and edits and deletions made there are already done, so it checks and confirms them.

## Keep in mind

- When an edit contradicts something the owner decided, ask the owner instead of applying it.
- A file that only mentions a deleted item is edited, never deleted.
