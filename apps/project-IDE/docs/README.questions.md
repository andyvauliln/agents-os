# Questions: README.md

## Open questions for the owner

- The skill sets 500 to 2,000 words for an app's README; you asked for the full documentation of the IDE, so this one is about 6,800 words. Keep it as one long manual, or split the page manual into its own file? It decides where readers look for how to use the page.
- Where should shared views live: `apps/project-IDE/views/` with a `views.json` list, as proposed? It decides where every custom view is written in stage one.
- When the working sources leave `vision/`, may we move the page, server and scripts into `apps/project-IDE/` and `agents/system/.claude/skills/ide-build/scripts/` in one round, with the server starting Claude Code in `agents/system/`? Until then the copies there are not the ones that run.
- Should the build get a script that compares the tree with `git ls-files` and fails on any difference? Today this check is done by hand.

## The owner's questions

### 2026-09-29: Where to choose the model and the effort

> i still not see where i can choose effort and better use only last one in a drop down, fable, opus 5.5 sonet 5.5 haiku

The page on claude.ai cannot pick a named model or an effort level: it can only ask for one of three levels, Most capable, Balanced or Fastest, and the platform chooses the model. That choice sits with the ask box. On the owner's server the page has no model choice; the setting `claude.model` in `server.config.json` chooses, and empty means Claude Code's default.

### 2026-09-30: How Changed works and when a sync happens

> and how changed works, since the last sync and when and how we do sync?

The "changed" mark is on every item a request from the page touched (an edit, a note, an added or deleted item, a waiting request), and the Changed tab lists them until the next sync. A sync happens when the owner presses Apply changes at the top of the page or says "sync the file tree": `ide-sync` writes everything into the files and files each message as an owner input, then `ide-build` rebuilds and publishes the page, and the marks are cleared. On the owner's server, file and How it works edits go into the files at once. This changed later: the first Changed view with its NEW, EDITED, REMOVED and COMMENTS labels became the one "changed" mark, and the Apply changes button was added.

### 2026-10-05: Does editing the files update the claude.ai page?

> and we now can edit this and after it ll update artefact that i can open it here or how it's works?

The claude.ai link shows what was last published, and it changes only when the page is published again to the same link, which keeps the owner's waiting notes. The `ide-build` skill publishes it at the end of every round. How the claude.ai page gets updated after work done on the server is still open.

### 2026-10-13: Can a block be edited as it looks?

> can we when we edit file block in ide  not change format to md again for editing, just same box but just edit there

Yes. A double-click in the Read view, or two taps on a phone, makes the block editable where it stands, looking as it reads. Save, Ctrl+Enter or a click outside the block turns it back into Markdown and writes only those lines; a Markdown button opens the source lines, and the front matter always opens as source.

### 2026-10-13: What decides planned and not planned files?

> what logic we currently have around planed not planed files

Today nothing does: the page and the build know only the files on disk, nothing is created from a plan, and the "planned" switch is gone. A file with nothing written in it yet is marked "empty", and the "empty" filter shows only those files. This changed later: when asked, planned items came from the tree notes and found items from the disk; the same day the owner had all logic about planned items removed.

### 2026-10-14: Terminal or page?

> what is a differnce if exist when we ll run agent from terminal claude code and when we make notes on ui?

It is the same Claude Code with the same `CLAUDE.md`, skills and files. In the terminal it files the input and does the round by following `CLAUDE.md`, you name the item yourself, and it asks in the terminal before risky steps. On the page every note is tied to one item, saved word for word at once with a history and undo, and marked "changed" until the sync; on the server the request box runs the same Claude Code with Allow and Refuse. Use the page for one item and the terminal for wide work; terminal work shows on the page only after the next rebuild.
