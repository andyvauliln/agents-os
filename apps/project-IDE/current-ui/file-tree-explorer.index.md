---
about: agent-os/apps/project-IDE/current-ui/file-tree-explorer.html
node: n-53.1.1
basis: bbd24314cede
written: 2026-10-07T09:33:30Z
by: knowledge-base-agent
confirmed: 2026-10-09T10:30:32Z
---
# file-tree-explorer.html

## Summary

The page itself: the tree of every folder and file with search and filters, and for each item its tabs: How it works, File, Example, Questions, extra tabs such as jobs, links, tests or key names, and Details. Every file shows its two metadata files as rows right under it, its How it works (`vision.index.md` for `vision.md`) and its Details (`vision.meta.json`, empty for now), and every folder shows its own first inside it; clicking one opens that tab, and the metadata switch above the tree hides or shows them. Folders start closed below the top levels; a first click on a closed folder opens it, and the search opens the folders on the way to each match. Every file and folder except the top has a Delete button next to its name: it opens a short form with an optional note for Claude, and the deletion runs the agent, which removes the item and cleans the project of it. A deleted item stays in the tree, struck through, until the next sync, and can be brought back. For now the page shows one status, "changed": a tag on whatever a request from the page touched (an edit, a note, an added or deleted item, a request in the box, a file Claude Code changed), listed on the Changed tab until the next sync. Its own File tab shows this source, the same file that is published, so the finished page is put in place before the data is built. It works in three places. On claude.ai it saves the owner's edits, notes, deletions and questions at once in its own store, and they reach the files at the next sync. An Apply changes button at the top, with the number of changed items, starts that sync: it sends Claude one comment on the page, and when Claude has applied the changes and published the new tree, the open page shows it. If no Claude is watching the page, the request is kept and the owner is asked to say "sync the file tree" in the project chat. On the owner's server it finds the server's service next to it, saves into the repository, writes edits straight into their files and sends requests, deletions and Apply changes to Claude Code. Served anywhere else it is view only and says so in its header. On the owner's server, the request box and the delete note box have a microphone button: it records up to 5 minutes, the server turns the recording into text, and the text is added to the box to check and send; on claude.ai the button is hidden.

## Keep in mind

- The page shows only the "changed" status for now; new statuses come only when the owner asks for them.
