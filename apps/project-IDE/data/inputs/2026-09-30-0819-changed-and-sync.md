# in-20260930-0819: How Changed and sync work
- At: 2026-09-30T08:19:33Z · Where: thread: Interactive file tree UI · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxMc6BiUPmg1jZQL6JZimjhw
- Categories: question, ui, process
- Summary: The owner asked how the Changed view works, what since the last sync means, and when and how a sync happens.

## Raw input
~~~text
and how changed works, since the last sync and when and how we do sync?
~~~

## Answer (given in chat)
~~~text
**How Changed works.** The page compares every save made on it with the data file it was last published with. A file appears under Changed if:
- **NEW:** it was added on the page.
- **EDITED:** any of its fields or its content now differ from the data file.
- **REMOVED:** it was removed on the page.
- **COMMENTS:** it has open comments.

It updates live. If you undo a change so the file matches the data file again, it drops off the list.

**What "since the last sync" means.** A sync writes the page's changes into the data file and clears those saved records. So right after a sync, Changed is back to 0.

**When a sync happens.** Only when you say "sync the file tree", here or in the project chat. The page can't trigger it on its own, because the direct connection to me was blocked earlier. On a sync I:
1. Read everything saved on the page: edits, new and removed files, comments, and answered questions.
2. Write it into file-tree.md. The version goes up and a changelog line is added. Decisions get a D-number and new files get an [n] number.
3. Record the final values in overrides.json, so later rebuilds keep them.
4. Rebuild the data file and republish the page, which clears the Changed list.

The history of changes stays under Notes & rules. I apply the comments you tell me to apply and turn the rest into open questions. Edited file contents are kept in the plan only; nothing is written to the repo until you ask.

If you'd like, I can also run the sync on a schedule, for example every evening.
~~~

## Processed into
- answered in chat
