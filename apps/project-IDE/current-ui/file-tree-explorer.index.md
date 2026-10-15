---
about: agent-os/apps/project-IDE/current-ui/file-tree-explorer.html
basis: 041236ec6f65
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# file-tree-explorer.html

## What it is

The page itself: the tree of every folder and file with search and filters. The tree is exactly the files git keeps and the folders that hold them, plus the two local-only `.env` files, and each item's id is its path, so the address of the page opens that item; nothing only planned is shown, a file with nothing written yet is marked "empty", and every build checks that the page tree equals the files in git, so a pulled repository and the rebuilt page show the same tree. For each item it shows its tabs: How it works, File, Example, Questions, extra tabs such as jobs, links, tests or key names, and Details. Every file shows its two metadata files as rows right under it, its How it works (`vision.index.md` for `vision.md`) and its Details (`vision.meta.json`, empty for now), and every folder shows its own first inside it; clicking one opens that tab, and the metadata switch above the tree hides or shows them. Folders start closed below the top levels; a first click on a closed folder opens it, and the search opens the folders on the way to each match. Every file and folder except the top has a Delete button next to its name: it opens a short form with an optional note for Claude, and the deletion runs the agent, which removes the item and cleans the project of it. A deleted item stays in the tree, struck through, until the next sync, and can be brought back. For now the page shows one status, "changed": a tag on whatever a request from the page touched (an edit, a note, an added or deleted item, a request in the box, a file Claude Code changed), listed on the Changed tab until the next sync. Its own File tab shows this source, the same file that is published, so the finished page is put in place before the data is built. It works in three places. On claude.ai it saves the owner's edits, notes, deletions and questions at once in its own store, and they reach the files at the next sync. An Apply changes button at the top, with the number of changed items, starts that sync: it sends Claude one comment on the page, and when Claude has applied the changes and published the new tree, the open page shows it. If no Claude is watching the page, the request is kept and the owner is asked to say "sync the file tree" in the project chat. On the owner's server it finds the server's service next to it, saves into the repository, writes edits straight into their files and sends requests, deletions and Apply changes to Claude Code. Served anywhere else it is view only and says so in its header. On the owner's server, the request box and the delete note box have a microphone button: it records up to 5 minutes, the server turns the recording into text, and the text is added to the box to check and send; on claude.ai the button is hidden.

## Who looks after it

It is written by project-ide-agent; ide-build; and the owner, by request on the page.

## When and how it changes

It changes when the owner asks for a change to the page.

## Who uses it, and when

It is read by the owner, `apps/project-IDE/server/server.py`, `agents/system/.claude/skills/ide-build/scripts/check_page.js` and `agents/system/.claude/skills/ide-build/scripts/enrich.py`.

## Where it is mentioned

It is described in `apps/project-IDE/docs/README.md`, `apps/project-IDE/docs/rebuild-prompt.md` and its folder's How it works file `apps/project-IDE/current-ui/current-ui.index.md`.

## Related knowledge

It reads `apps/project-IDE/current-ui/file-tree.data.json`. It is read by `apps/project-IDE/server/server.py` and `agents/system/.claude/skills/ide-build/scripts/enrich.py`. It is checked by `agents/system/.claude/skills/ide-build/scripts/check_page.js`. It is written by `agents/system/.claude/skills/ide-build/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `apps/docs/README.md` (section "The project IDE") and `apps/project-IDE/docs/README.md` (section "The page").

## Keep in mind

- The page shows only the "changed" status for now; new statuses come only when the owner asks for them.
