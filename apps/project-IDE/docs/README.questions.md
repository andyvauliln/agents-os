# Questions: README.md

## Open questions for the owner

- **Do we keep this README as one long manual, or move the page manual into its own file?** The skill sets 500 to 2,000 words for the README of an app. You asked for the full documentation of the IDE, thus this README has approximately 6,800 words. The answer decides where readers look for how to use the page.
- **Do the shared views go in `apps/project-IDE/views/`, with a `views.json` list?** We propose this. The answer decides where each custom view goes in stage one.

## The owner's questions

### 2026-09-29: Where do I select the model and the effort?

> i still not see where i can choose effort and better use only last one in a drop down, fable, opus 5.5 sonet 5.5 haiku

The page on claude.ai cannot select a named model or an effort level. It can only ask for one of three levels: Most capable, Balanced or Fastest. The platform then selects the model. This selection is next to the ask box.

On the owner's server, the page has no model selection. The setting `claude.model` in `server.config.json` selects the model. When it is empty, Claude Code uses its default.

Docs improved: none, the answer was already in apps/project-IDE/docs/README.md (the ask box and the server settings).

### 2026-09-30: How does "changed" work, and when does a sync occur?

> and how changed works, since the last sync and when and how we do sync?

The "changed" mark is on each item that a request from the page touched. Such a request is an edit, a note, an added or deleted item, or a waiting request. The Changed tab lists these items until the next sync.

A sync occurs when the owner pushes Apply changes at the top of the page, or says "sync the file tree". Then these steps occur:

1. `ide-sync` writes all changes into the files. It records each message as an owner input.
2. `ide-build` builds the page again and publishes it.
3. The marks are removed.

On the owner's server, the page writes file edits and How it works edits into the files at once.

This changed later: the first Changed view had the labels NEW, EDITED, REMOVED and COMMENTS. It became the one "changed" mark. The Apply changes button came after.

Docs improved: none, the answer was already in apps/project-IDE/docs/README.md (the "changed" mark and Apply changes).

### 2026-10-05: Does a file edit update the claude.ai page?

> and we now can edit this and after it ll update artefact that i can open it here or how it's works?

The claude.ai link shows the last published version. It changes only when the page is published again to the same link. That publish keeps the waiting notes of the owner.

The `ide-build` skill publishes the page at the end of each round. How the claude.ai page gets the work done on the server is still open.

Docs improved: none, the answer was already in apps/project-IDE/docs/README.md (the three places the page runs, and "Still open in the design").

### 2026-10-13: Can I edit a block as it shows?

> can we when we edit file block in ide  not change format to md again for editing, just same box but just edit there

Yes. Do these steps:

1. In the Read view, double-click the block. On a phone, tap it two times. The block becomes editable where it is, and it looks the same as when you read it.
2. Push Save or Ctrl+Enter, or click outside the block. The page changes the block back into Markdown and writes only those lines.

A Markdown button opens the source lines. The front matter always opens as source.

Docs improved: none, the answer was already in apps/project-IDE/docs/README.md (reading and editing a document).

### 2026-10-13: What decides if a file is planned or not planned?

> what logic we currently have around planed not planed files

Today nothing decides this. The page and the build know only the files on disk. Nothing comes from a plan, and the "planned" switch is removed.

A file that has no text yet has the mark "empty". The "empty" filter shows only these files.

This changed later: at the time of the question, planned items came from the tree notes, and found items came from the disk. On the same day, the owner had all logic about planned items removed.

Docs improved: none, the answer was already in apps/project-IDE/docs/README.md (the empty filter) and agents/system/CLAUDE.md (the rules).

### 2026-10-14: Terminal or page?

> what is a differnce if exist when we ll run agent from terminal claude code and when we make notes on ui?

It is the same Claude Code, with the same `CLAUDE.md`, skills and files.

In the terminal:

1. Claude Code records the input and does the round as `CLAUDE.md` tells.
2. You name the item yourself.
3. It asks you in the terminal before risky steps.

On the page:

1. Each note is tied to one item.
2. The page saves it word for word at once, with a history and undo.
3. The item has the mark "changed" until the sync.
4. On the server, the request box runs the same Claude Code, with Allow and Refuse.

Use the page for one item. Use the terminal for work on many items. Terminal work shows on the page only after the next page build.

Docs improved: apps/project-IDE/docs/README.md, apps/project-IDE/docs/README.asd.md.
