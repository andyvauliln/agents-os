# The project IDE

## In short

The project IDE is the owner's window on the Agent OS. The owner builds the system by vibecoding: they say what they want in plain words, and AI writes the plans, the docs and the code. The IDE shows the whole project as one clickable tree of every folder and file, and next to each one says what it is, how it works, what it holds and what is still open. The owner reads, edits, comments, asks and deletes there, and AI brings everything they leave back into the files. The same tree gives every AI working on the project the full context it needs to change things precisely.

The IDE works today: the page is published on claude.ai and in use, its build and checks run, and the server that puts Claude Code behind the page runs on the owner's server, where a service starts it when the machine boots. Finishing it is stage one of the project: a view for every kind of file, correct metadata on every item, and a tab for each metadata file that really exists.

This document is the full manual of the IDE: every part of the page and how to use it, the Notes and runs panel and the page of each run, the three places it runs, how it is built and checked, how the owner's work comes back into the files, the metadata files behind its tabs, how to run it on a server, and where every part lives now and later. Why the IDE exists and how it should behave are in its vision, `apps/project-IDE/docs/vision.md`.

## The IDE at a glance

```text
          the repository (git)
   every file · the How it works, Details and other metadata files next to it
                    │
                    │  ide-build: materialize, check, enrich, check the tree, publish
                    ▼
   file-tree.data.json + real-files.json ──►  THE PAGE  file-tree-explorer.html
                                               │      │        │
                         on claude.ai ◄────────┘      │        └────────► anywhere else
              its own store (nodes, changes, inputs)  │                   view only
              Apply changes = one comment to Claude   │
                                                      ▼
                                   on the owner's server: server.py
                          store as files · write-through into the files
                          request box ─► Claude Code (claude_bridge.py)
                          Notes and runs panel ─► notes, runs, summaries
                          each page run on its own branch (worktrees.py)
                          voice ─► Groq (voice.py)
                    │
                    │  ide-sync: every note, edit, deletion and request back into the files
                    ▼
          the repository again, then ide-build
```

| Part | What it is for | Where it lives |
|---|---|---|
| The page | The tree, the tabs, editing, notes, questions, the ask box | `apps/project-IDE/current-ui/file-tree-explorer.html` |
| The page data | Everything the page shows, built from the repository | `apps/project-IDE/current-ui/file-tree.data.json` |
| The real files' texts | The text of every file, loaded when one is opened | `apps/project-IDE/current-ui/real-files.json` |
| The build scripts | Build the data, give new items their metadata files, check the How it works files, the tree and the page | `agents/system/.claude/skills/ide-build/scripts/` |
| The owner's kept edits of the extra tables | Values the owner set on the page that the build applies on top | `apps/project-IDE/data/overrides.json` |
| The records | Every owner input, the decisions, the changelog, the plans | `apps/project-IDE/data/` |
| How it works and Details files | One explanation and one details file per item | next to each item |
| The server | The page on the owner's machine with Claude Code behind it | `apps/project-IDE/server/` |
| The page store on the server | The owner's comments, edits, messages and notes as JSON files | `apps/project-IDE/data/page-store/` |
| Notes and runs | Every note and every Claude Code run in one panel on the server page, each run with its own page | the page, with `notes.py`, `runs.py`, `run_summary.py` and `worktrees.py` in `apps/project-IDE/server/` |
| The run records | Each run's status, notes, branch, summary and tags (out of git) | `agents/system/logs/subagents/project-ide-agent/runs/` |
| The project IDE agent and its skills | Build the page, bring the owner's work back | `agents/system/.claude/agents/`, `agents/system/.claude/skills/` |

The parts connect in one loop. The build reads the repository and writes the page data. The page shows it. The owner works on the page, and everything they do is saved at once in the page's store. When the owner presses Apply changes or says "sync the file tree", the project IDE agent reads the store, writes every edit into its file, files every note and request as an owner input, cleans up what was deleted and rebuilds the page. The knowledge base agent then sorts the new inputs into the docs and refreshes the explanations, and the page is rebuilt once more. On the owner's server the loop is shorter: edits go straight into the files, and each message or note runs at once on its own branch, which the server merges into `main` when the run is done.

## How it is laid out

Every file of the IDE is its own source and is edited where it is. The layout:

```text
apps/project-IDE/
├── docs/                         the IDE's own docs
│   ├── vision.md                 what the IDE is for and why
│   ├── README.md                 this manual
│   ├── README.asd.md             this manual in ASD-STE100
│   └── rebuild-prompt.md         how an AI builds the IDE again exactly
├── current-ui/                   the page, as published on claude.ai
│   ├── file-tree-explorer.html   the page itself, one file
│   ├── file-tree.data.json       its data; built, never edited or merged by hand
│   └── real-files.json           the text of every file; built
├── server/                       the same page on the owner's server
│   ├── README.md                 how to start it and reach it safely
│   ├── server.py                 the web service: page, store, write-through, request box, panel routes
│   ├── claude_bridge.py          runs each request as a Claude Code session
│   ├── notes.py                  notes and run records, statuses, sending notes as one run
│   ├── runs.py                   reads Claude Code's transcripts into runs with every step
│   ├── run_summary.py            each run's summary in ASD-STE100 and its tags
│   ├── worktrees.py              each page run's branch and worktree, and its merge into main
│   ├── voice.py                  turns a recording into text through Groq
│   └── server.config.json        address, paths, limits, what Claude Code may do
└── data/                         this project's records
    ├── README.md                 what the records are and how they are kept
    ├── inputs/                   every owner input, word for word, with index.json
    ├── decisions.md, changelog.md
    ├── plans/, archive/          change plans with index.json, retired files
    ├── page-store/               on the server: the page's comments, edits, messages and notes
    └── overrides.json            the owner's kept edits of the extra tables
```

Two scripts at the top of the repository set up and start the server: `init.sh`, run once, and `start.sh`, run for every start. Each run from the page works in its own checkout in `.worktrees/` at the top of the repository, which git ignores. Every file and folder in it has its How it works file and its Details file next to it, as everywhere in the repository. The project IDE agent and the two skills live with the system's other helpers in `agents/system/.claude/`, and the build scripts inside the `ide-build` skill.

## The page

The page is one HTML file, `file-tree-explorer.html`, that reads one data file, `file-tree.data.json`. It needs no build step of its own and loads no code from outside, only its fonts. It has a header, the tree on the left, and on the right the sheet of the selected item with the ask box pinned under it.

### The header

- **The title and the version line.** The version line shows the version of the page data and the number of items, and then where the page runs: "on your server", "view only", or nothing on claude.ai.
- **Notes and runs** (on the owner's server only). Opens and closes the panel of notes and runs under the header (see "Notes and runs" below). It shows how many notes and runs are at work, or "N need you" in red when a run waits for the owner.
- **Apply changes.** Shown when something on the page is marked changed, with the count. It opens a short confirmation and then carries every change into the files (see "Apply changes" below). While a request waits, it reads "Applying changes" and cannot be pressed again.
- **The filter.** Typing filters the tree as you type. A text with `*` matches names as a pattern (`*.json`); a text with `/` matches paths (`agents/system/`); anything else matches part of a name, so `.md` finds every Markdown file. The folders on the way to each match open by themselves, and a line under the tabs says how many items match, with a button to clear the filter.

### The tree

- **All and Changed.** All shows the whole tree. Changed shows only the items marked changed since the last sync, with the reason on each.
- **The metadata switch.** On, every file shows its two metadata files as rows right under it, its How it works file (`vision.index.md` for `vision.md`) and its Details file (`vision.meta.json`), and every folder shows its own first inside it. Clicking one opens that tab of its item. Off, they are hidden, including the real ones found on disk. It is on by default.
- **The empty filter.** On, the tree shows only the files with nothing written in them yet, each marked "empty", with the folders that hold them. The tree itself is always the files on disk; nothing that is only planned is shown.
- **The rows.** A folder icon, a file icon or a link icon, the name, and a "changed" tag when it applies. A first click on a closed folder opens it and selects it. The arrow keys move through the tree and open or close folders. The open folders and the selected item are remembered in the browser, and the address of the page carries the selected item, so a link opens the same item.
- **Deleted items** stay in their place, struck through, until the next sync.

### The sheet of an item

The top of the sheet shows the path as links to each folder above, the item's name, a "Changed" chip with the reason when it is marked, its kind (file, folder, file link or folder link), a Delete button for every item but the top, and one line on what the item is for. Under that are its tabs.

### The tabs

The first tab is always How it works and the last is Details. Between them, a file has File, Example and Questions, and a folder has Contents and Questions. Some items have extra tabs.

- **How it works.** The item's explanation, read from its own file, `vision.index.md` next to `vision.md` or `configs/configs.index.md` inside a folder. The name of that file shows at the top with an Edit button. Like a Markdown file on the File tab, it opens in the Read view with Read and Source and Full screen (below); edits go through the Edit button. Items written in the new format show fixed headings (What it is, Who looks after it, When and how it changes, Who uses it and when, Where it is mentioned, Related knowledge) and a short Keep in mind list; older ones show one Summary. Under it the tab lists the owner's messages about the item waiting for the next sync and every change made on the page to it, each with an "Undo this change" button. On claude.ai, when something under an item was changed on the page, the page can write a fresh summary at once ("Update it now"); the knowledge base agent checks it at the next sync.
- **File.** The file as it is now: its text, read from the repository, even when it is empty, with its path and where the text came from. A Markdown file opens in the Read view (below); any other file shows numbered lines. A long file shows 3,000 lines at a time with a button for more; a real file over 200 KB is not put on the page, and the tab says to open it in the repository. A keys file (`.env`) is local only: the page never reads, shows or edits its text. A file nobody has written yet offers "Write it" and, when an example exists, "Start from the example". A link says what it points at. The page file shows its own source, and the data file shows itself as the page loaded it, read only.
- **Contents** (folders). A card for each item inside, with its name and what it is for, a button to add a file or folder, and a button to comment on the folder.
- **Example.** For a document, the structure of the file: each heading and what goes under it, taken from the outline in the skill that writes that kind of doc. For a settings file, a full example and a table of every field with its allowed values, an example and what it is for. A jobs or links file builds its example from its own table, unsaved edits included.
- **Questions.** The item's Questions file, in the Read view with Read and Source and Full screen, like a Markdown file: its open questions for the owner, and the owner's own questions with their answers, all in ASD-STE100 apart from the owner's words. Below it, the questions answered on the page with their answers. A folder also lists the open questions of the files inside it.
- **Details.** The item's Details file, `vision.meta.json`, shown as it is. It holds what the item is, its state, whether it is in git, whether it is secret or generated, who writes and reads it, when it changes, what it relates to, what must change with it, what it inherits from the levels above, its sources, features and views. A new item's Details file is empty until it is written.
- **Extra tabs.** An agent's folder has Overview and Agents (what the agent does and the agents, workers and skills below it). A jobs file has Jobs, a table of every job with its switch, schedule, place, platform and model. A links file has Links. A keys file has Variables, the names of its keys with what each is for, never a value. A tests file has Tests. Some agents have Capabilities. Each of these is an editable table; saving it updates the file.

### Reading and editing a document

A Markdown file opens as a page of a book, on its own white or black paper, with the word count, the reading time and a Contents list of its headings. The reader's controls:

- **Read and Source.** Read shows the rendered document; Source shows its numbered lines, where a click on a line number opens a comment on that line.
- **Aa.** The font (Sans, Legible or Serif) and the size (S, M or L).
- **Light and Dark.** The paper, white or black, remembered in the browser.
- **Full screen.** The document fills the screen, with the Contents in a side column on a wide screen, a progress line at the top, and Close or Esc to leave.
- **Edit in place.** A double-click on a paragraph, heading, list or table, or two taps on a phone, makes that block editable right where it stands, looking just as it reads: type in it, with Ctrl+B for bold and Ctrl+I for italic. Save, Ctrl+Enter or a click anywhere outside the block turns it back into Markdown and writes only those lines into the file; Esc or Cancel leaves it as it was. A link the browser made by itself while typing, such as a file name like `x.md` that a Mac turns into a web address, is saved as plain text. A Markdown button switches the block to its source lines when you want them, and the front matter at the top always opens as source. It works in full screen too.
- **Edit.** Opens the whole file in an editor with numbered lines that wrap to the screen. Save file or Ctrl+S saves it; Cancel drops the edit.

Every save is recorded with what was there before, so it can be undone from How it works. On the owner's server the file on disk changes at once; on claude.ai the edit waits in the page's store until the next sync. After a save on claude.ai the page also checks related items (the parent folders and the items that mention this one) and saves any update they need as "Related updates", which can be undone in one click; it never changes another file's text or anyone's How it works.

### Comments

A comment is left on one line (from the line numbers) or on the whole file or folder (the "Comment on" button). Each comment keeps the text of its line, so it stays on the right line when the file changes, and says so when that line is gone. A comment can be resolved, reopened or deleted; resolved comments are hidden until asked for. At the sync, a comment the owner meant as a change is applied, and any other open comment becomes an open question on the item. A comment is not the same as a note in the Notes and runs panel: a comment waits on its item for the sync, while a note is meant for Claude Code and goes out as a run.

### The ask box

The box under every item takes a question or a request about that item. Enter sends; Shift+Enter adds a line. Each item keeps its own conversation in the browser, and Clear empties it. On claude.ai every message and its answer are also saved in the page's store as an owner input, so they reach the files at the next sync; on the server the run that takes the message files it.

On claude.ai the page asks Claude itself, with a choice of model: Most capable, Balanced or Fastest. Claude reads the item, the knowledge that applies to it and its related items, and answers in one of three ways:

- **An answer.** A question answered for good is also saved on the item's Questions tab.
- **A draft.** A request for a change comes back as a draft card: every item it changes, and for each one the fields it changes, with a before and after view of each field. Save (or typing "save") applies it at once and marks the items changed; Discard drops it; asking more changes the draft first. A new file or folder and a removal show as such.
- **Save or discard,** when the owner says so in words about a waiting draft.

On the owner's server a message in the box becomes a note in the Notes and runs panel and goes out at once as its own run of Claude Code, on its own branch (see "Notes and runs"); no second copy of it is kept as a page input. There is no model choice on the page; the server's settings choose. The chat shows each step Claude Code takes, any step that waits for the owner with Allow and Refuse buttons, then the answer with its cost, its time and how many files changed. A follow-up in the same box continues the same conversation on the same branch, Stop ends a run, and the tree reloads when files changed. The box grows with the text, up to half the screen. A microphone button sits next to it: it records up to five minutes with a timer, and the recording becomes a note in the panel at once, whose text the server writes in and the owner checks and edits there.

Opened anywhere else, the box says that the page only shows the files and that a message reaches no one.

### Adding a file or folder

A folder's Contents tab has "Add a file or folder": a name (ending in `/` for a folder), its type and one or two sentences on what it is for. The new item appears in the tree at once, marked changed. At the sync it is created on disk with its How it works and Details files, and it stays proposed until the owner agrees.

### Deleting and bringing back

The Delete button next to an item's name opens a short form: what will be deleted (a folder counts the items inside it) and an optional note for Claude, such as what to move or keep first. The note box has the microphone too on the server. "Delete and clean up" then:

- **on the owner's server** starts Claude Code at once in that item's chat. It may delete exactly that item and its metadata files without a second click, then cleans the project of it: every link to it and mention of it in other files, and the parent's How it works. It follows the note, files the deletion and commits;
- **on claude.ai** marks the item deleted at once; the cleanup happens at the next sync.

A deleted item stays in the tree, struck through, with a note that says what happens next and a "Bring it back" button (on claude.ai, "Restore it"), until the sync. On the server, bringing it back is the same round in reverse: Claude Code restores it from git and puts back what the cleanup removed.

### The "changed" mark and Apply changes

The page shows one status for now: changed. It marks whatever a request from the page touched until the next sync: an edit, a note, an added or deleted item, a request waiting in the box, and on the server every file Claude Code changed for a request. The Changed tab lists them.

Apply changes, at the top, carries all of them into the files:

1. The owner presses it and reads what will happen, then presses "Apply now".
2. On claude.ai the page posts one comment on itself and sends it to Claude, and saves the request in its store. The Claude session watching the page runs the sync and the build, publishes the new tree, answers the comment and resolves it. When the request is marked processed, the open page loads the new tree, or asks the owner to reload.
3. If no Claude session watches the page, or commenting is not allowed, the page saves the request and asks the owner to say "sync the file tree" in the project chat. A waiting request can be cancelled.
4. On the owner's server the button starts one Claude Code run in the chat of the top folder with the same request, and the page reloads the tree when it ends.

Saying "sync the file tree" in the project chat does the same as the button.

### On a phone

Below a width of 760 pixels the page shows one pane at a time: the tree, then the item's sheet with a "‹ Tree" button to go back. Nothing on the page may be wider than the screen. In the reader, two taps on a block edit it, as a double-click does on a computer, and the labels of the reader's buttons hide to save room.

### What the page remembers in the browser

The open folders, the selected item and tab, the switches, the Read or Source choice, the reader's paper, font and size, each item's conversation (its last 30 messages), unsent text in the box, and on the server whether the Notes and runs panel is open and the send options. Nothing the owner needs to keep is kept only there: comments, edits, messages and notes go to the page's store.

## Notes and runs

A spoken or typed request is easy to lose: it goes into one item's chat, and once a run ends, its steps are gone from view after a reload. On the owner's server the page keeps all of them in sight. Every note the owner makes for Claude Code, and every Claude Code run in this repository, from the page or from a terminal, is one row in one panel. The owner sees what waits, what works and what is done, sends several notes as one run, and opens any run to see what it did. The panel exists only on the server page; on claude.ai and anywhere else its button is hidden.

**The panel.** The Notes and runs button in the header opens it under the header, and the page remembers whether it was open. It has three tabs, All, Notes and Runs, with Refresh and Hide. Rows that need the owner come first, then the rows at work, then the rest, newest first. Ten rows show at a time, with a line such as "10 of 34" and Show more for ten more.

**Making a note.** A note is anything the owner types or says for Claude Code on the server page. There are four ways to make one:

- the box at the top of the panel, which grows with the text; Ctrl+Enter or Add note adds it;
- the ask box under an item, where a message becomes a note that goes out at once as its own run;
- a microphone, in the panel or in the ask box: the recording becomes a note at once, with the status transcribing, and the server turns it into text, which the owner then edits in the panel;
- selecting text on an item's sheet: a small bar shows "Record about this" and "Note", and the note keeps the selected text, its line, the tab and the item.

**A note's row** shows a checkbox (unchecked leaves it out of Send all), its status, the item it is about (a click opens it), tags such as "selection · line 12" and "voice", its time and its text. Its buttons follow its status: Send after transcript while it is still transcribing, so it goes out by itself when its text is in; Edit, with Save and Cancel; Send; Open run; Cancel; Delete; and Details. Details show where the note was made (the ask box, the panel or a selection), the item, the tab, the line, the selected text, whether it was typed or spoken, when it was made, the page version, its run, and the commits it was sent from and merged at. Once sent, the row says, for example, "sent at 3f2a1c9 · page v75 → in main at 8b0d2e4 · page v76".

**The statuses** are the same for notes and runs:

| Status | What it means |
|---|---|
| transcribing | The recording is being turned into text. |
| ready | The text is in. The owner can edit it, send it or leave it. |
| queued | It goes out by itself as soon as its text is in. |
| sending | It is on its way to Claude Code. |
| planning | Its run is writing a plan before it builds. |
| working | Its run is doing the work. |
| need human | The run cannot go on without the owner: an Allow or Refuse waits, or it asks something. These rows come first. |
| need manual test | The run is finished, and says what a person must try. |
| done | The run is finished and its branch is ready, not yet in `main`. |
| in main | Its branch is merged into `main`. |
| failed | The recording or the run failed; the row says why. |
| cancelled | The owner stopped it. |

A run tells how it ended: the last line of its answer is "STATUS: done", "STATUS: need manual test:" with what to try, or "STATUS: need human:" with what it needs. After the server restarts, notes and runs that were at work become failed.

**Sending.** Send all, at the bottom, sends every checked ready note together as one run: each note goes in with where it came from and its selected text, so Claude Code knows which item each one is about. A folded line above it, "Options: local · auto merge · related tests · bug check · report", opens the send options, which the page remembers:

- **Where:** Local, a branch on this server. Cloud is shown but off, for later.
- **Merge:** Auto merge, into `main` as soon as the run ends done, or Ask me, which waits for the owner's button.
- **Tests:** Related (the build checks and the tests of what the run changed), All or None.
- **Check for bugs:** the run reviews its own changes before it ends.
- **Report:** the run ends with a short report of what was asked, what changed, the checks and what is left.

The defaults are Local, Auto merge, Related, Check for bugs on and Report on.

**Each run from the page works on its own branch.** Without that, two runs at once would change the same files, and a half-done run would change the files the page shows. So for every run that carries notes, the server makes a branch named `ide/<date>-<subject>` from the last commit of `main`, with its own checkout in `.worktrees/<run>/`, and Claude Code works and commits there. A follow-up from the same chat continues on the same branch. When the run ends done with Auto merge, or when the owner presses Merge into main on its page, the server brings the branch up to date with `main`, moves `main` forward on the server and rebuilds the page; the notes and the run become in main. The built files (the page data, `real-files.json` and `docs/file-tree.md`) always differ between branches, so a conflict only in them is solved by building them again; any other conflict stops at need human. Nothing is pushed to GitHub. Because the branch starts from the last commit, page edits the owner has not committed yet are not in it. A Delete and Apply changes still work in the repository itself, not on a branch.

**A run's row** shows its status, its title (a click opens its page, and the panel closes to give it room), its tags, whether it came from the page or a terminal, its branch, its number of steps, its cost (page runs) or its largest context (terminal runs), its time and how many notes it carries. A run at work has Stop; a finished page run with a branch has Merge into main.

**Where it is all kept.** Each note is a small file in the page store's `notes/` folder, and each run has a record in the project IDE agent's log folder; git keeps neither. The run that takes a note files its words as an owner input, word for word. Terminal runs need no record to appear: the server reads them from Claude Code's own transcripts of this repository, and a terminal run counts as live while its transcript changed in the last 90 seconds. Terminal runs show no cost, because their transcripts hold none.

## The page of a run

Every run, from the page or from a terminal, has its own page at the address `#run/<id>`. It fills the whole page: the tree hides, the run uses the full width, and the whole page scrolls as one. The ask box hides, and "‹ Back" returns to the tree and the item. A run still at work refreshes every four seconds.

The top shows the title, the status, page or terminal, the tags, the folder it started in, its branch, the start, the length, the model, the cost, the largest context, the tokens written and the number of steps. Its buttons: Stop; Merge into main; Discard the branch, which removes the branch without merging; Make PR and Make PR and merge, shown but off, because pull requests come in a later step; and Copy, which gives `claude --resume <session>` to go on with the run in a terminal.

Below come these sections:

- **Summary:** four to ten sentences in ASD-STE100 and one to four tags, written by Claude Haiku after each page run and in the background for finished terminal runs, for about half a cent to one cent each. Write it again asks for a new one. Tags come from a fixed list (question, change, fix, docs, ui, server, setup, sync, plan, research, delete, failed, waiting); a new tag is made only when none fits.
- **Request** and **Answer:** the first message and the last answer, in full.
- **Notes:** the notes the run carried, with where each came from.
- **Send options:** the options it was sent with.
- **Git:** the commit it was sent from and the one it is in `main` at, its branch and the branch's commits, the files it changed with links to their items, the commits made while it ran, and the repository's current branch and uncommitted files.
- **What it used:** chips for the kinds of steps, the tools, skills, subagents, MCP servers, plugins, workflows and web pages, and the files read and edited. A click on a chip shows only those steps.
- **Checks and tests:** the build checks and tests the run ran, with their results.
- **Plan:** the plan the run wrote, when it wrote one.
- **Steps:** one row per step, in order, with an icon by kind (prompt, notification, text, read, edit, command, skill, subagent, MCP, web, workflow, other tool), a one-line summary, its time and duration, and a small bar for how much context the model had at that step. A row opens to show the step's input and output; a long one shows its start, with "Show all of it" for the rest; a subagent's step opens into the subagent's own steps. Open all and Close all open or close every row.

## The three places the page runs

The page finds out where it is when it loads.

| Place | How the page knows | Where the owner's work is saved | Who answers the box | Apply changes |
|---|---|---|---|---|
| claude.ai, as a published artifact | The artifact runtime is there | The artifact's own store: the collections `nodes`, `changes` and `inputs` | Claude, through the page, with a choice of model | One comment sent to the Claude session watching the page |
| The owner's server | The server answers `api/health` | JSON files in the page store; file and How it works edits also straight into their files | Claude Code in the repository, step by step, with the owner's Allow and Refuse | One Claude Code run in the top folder's chat |
| Anywhere else | Neither answers | Nowhere: the header says "view only" | No one | Hidden |

The published page has one link, https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs, and is always republished at that link, so the owner's work waiting in its store stays where it is. It asks for four runtime capabilities: its store, asking Claude, knowing who views it, and sending a comment to Claude.

**The page or the terminal.** Both reach the same Claude Code, with the same `CLAUDE.md`, skills and files. In the terminal the owner starts Claude Code in `agents/system/` and names the item themselves; it files their words and does the round as `CLAUDE.md` says, and asks in the terminal before a risky step. On the page every note and message is tied to one item, saved word for word at once with its history and undo, and marked changed until the sync; on the server the request box runs the same Claude Code, with Allow and Refuse. The page suits work on one item, the terminal wide work across many. Work done in the terminal shows in the tree only after the next rebuild, but its run shows at once in the Notes and runs panel on the server, with its own page. A run from the page works on its own branch and reaches `main` when it is merged; a run in the terminal works wherever the owner started it.

## What the page reads

`file-tree.data.json` is the page's only data. It is built, never edited or merged by hand. Its top level holds the version of the data, when it was built, the root item, the decisions, and the list of items. Each item carries its id, which is its path from the top of the repository (`docs/README.md`; the top is `agent-os`), its name, path, type, parent and children, whether it is a link, its status, what it is for (from its Details file), its How it works text with the state of that file and its path, its Details and the path of its Details file, a note that its text loads later, the file the text came from, its example, its field guide and its extra tabs.

`real-files.json` sits next to it and maps each real file found on disk to its text. The page loads it the first time such a file is opened, so the page itself stays small. On the server it is read fresh from disk on every request.

## How the page is built and checked

The `ide-build` skill turns the repository into the page data, checks it and publishes it. The files on disk and the metadata files next to them are its only source: it reads no notes and copies nothing. It runs after every round that changed a file, a folder or a metadata file, after a pull that brought changes, and as the last step of every sync. Its scripts are in `agents/system/.claude/skills/ide-build/scripts/`, all Python with the standard library except the page check:

| Script | What it does |
|---|---|
| `index_files.py` | Lists the items: every file git keeps, the folders that hold them, and the local `.env` files, listed but never read. Knows where every How it works and Details file lives, and reads and writes them. |
| `materialize.py` | Gives every new item its empty How it works and Details files, keeps a `.gitkeep` in empty folders and writes `docs/file-tree.md`. It copies nothing. |
| `build_map.py` | Checks the How it works files against their items: which are missing or stale (children first), which are still empty, the context for writing one, confirming one, writing many at once, and orphans whose item is gone. |
| `enrich.py` | Reads every item with its metadata files and extra tabs, applies the owner's kept edits of the extra tables, and writes the page data and `real-files.json`. It is given the next data version. |
| `tabs.py` | The field guides and the extra tables (keys, jobs, links, tests, capabilities), used by `enrich.py`. |
| `check_tree.py` | Checks that the page's items are exactly the files in git and their folders, plus the local `.env` files. |
| `check_page.js` | Opens the page at a desktop width and a phone width with a stand-in for the artifact runtime and fails on a page error, a missing tab, an address that does not open its item, or a page wider than the phone. Needs Node and Playwright with Chromium. |

The build, in order:

1. Put the finished page in place first, because the page shows its own source.
2. Run `materialize.py`.
3. Run `build_map.py --stale`; hand the stale How it works files to the knowledge base agent's `file-index` skill, or confirm the ones still right.
4. Run `enrich.py` with the next data version; run `materialize.py` again, and if it made anything, check and enrich again.
5. Run `build_map.py`: every How it works file fresh, none missing, no orphans.
6. Run `check_tree.py`: it must print "tree ok".
7. Run `check_page.js` on the top item, the README and every item the round changed, and look at the screenshots of anything changed on the page itself. It must print "page ok".
8. Publish at the same link, with the data and `real-files.json` next to the page.
9. Report in plain words what the owner will see changed.

The build never invents a status: an item is decided unless its Details file says proposed or idea, and anything new an agent adds is proposed until the owner agrees. No secret value is ever in the data.

## How the owner's work comes back

The page saves everything at once, so the owner never waits; the files change only at a sync (on claude.ai) or at once (on the server, for file and How it works edits). The page's store has three collections:

| Collection | One document per | What it holds |
|---|---|---|
| `inputs` | message sent from the page | The text, the item and path it was sent on, its kind (question, answer, change, discard, delete, restore or apply), the answer the page gave, and its status: `new` until a sync files it. An apply request also holds the count, the items and whether it reached Claude. |
| `nodes` | item the owner touched | The latest value of each edited field (`content` for the text, `how_md` for How it works), line comments with their line's text, answered questions, a new item, a deletion with what the item was, the owner's note and who cleans up, and the mark of a server request that changed it. |
| `changes` | save | The history: when, by whom, the owner's words, and for each item every field before and after, and whether it was undone. It is never folded or cleared. |

On claude.ai these live in the artifact's store and are read through the artifact data tool on the page's link. On the server each document is one JSON file, `page-store/<collection>/<id>.json`. The server also keeps the notes of the Notes and runs panel there, one file each in `page-store/notes/`, which git ignores. They do not wait for a sync: the run that takes a note files its words as an owner input, so a sync only checks the notes left ready and never sent.

The `ide-sync` skill brings them back. It runs when the owner presses Apply changes or says "sync the file tree", and always before `ide-build`:

1. List every new input and every touched item.
2. Save each as an owner input, word for word, with the item it was left on; a message and the answer the page gave are one input.
3. Write the edits into their files: a file's text into that file, How it works into the item's `.index.md` word for word with the owner as its writer, a new item onto disk with its How it works and Details files, an edit of an extra table into the kept page edits. A deleted item is cleaned out of the project, following the owner's note.
4. Run the requests the owner sent and file each answer with its input.
5. Hand the saved inputs to the knowledge base agent, which sorts them into the docs and metadata files and refreshes the explanations.
6. Rebuild and publish with `ide-build`.
7. Clear what was folded: mark each filed input processed and delete the folded item documents, which clears the "changed" marks. A round started by Apply changes marks its apply request processed last, so the open page shows the new tree, then answers the page comment and resolves it.
8. Report to the owner in two to five plain lines.

Nothing is cleared before it is in a file, the owner's words are never changed or dropped, an edit that contradicts an earlier decision is asked about, and a key pasted on the page is never copied anywhere.

## The metadata files and the tabs

Every file and folder has metadata files next to it, named after the item without its extension:

| File | Tab | What it holds |
|---|---|---|
| `vision.index.md` | How it works | The plain explanation, under fixed headings, with front matter saying what it describes, its item, when and by whom it was written |
| `vision.meta.json` | Details | The item's details as JSON (the fields listed under the Details tab above) |
| `vision.example.md` | Example | The structure of the file: its headings and one line on what goes under each |
| `vision.questions.md` | Questions | The open questions for the owner, and the questions the owner asked about the file with their answers |
| `vision.{type}.{name}.view.html` | its own tab | A custom view for that kind of file (proposed, not built yet) |

A folder keeps its own inside it (`configs/configs.index.md`). A name with no extension stays whole (`.gitignore.index.md`). A file whose name would clash with a sibling's or its folder's keeps its extension; today only `apps/project-IDE/server/server.py` has `server.py.index.md`. A metadata file has no metadata files of its own.

Every item has its How it works and Details files today. The example and questions files are being written now for the main docs and the keys files only; other files get them later, when they need them. A tab shows only when its file exists, and it shows that file. Every metadata file is its own source, edited where it sits next to its item; the build only gives a new item its empty How it works and Details files.

## The server

`server/` runs the same page on the owner's own machine, with Claude Code behind its request box.

**What it needs:** the repository cloned on the server with a way to push; Python 3.10 or newer; Node; Claude Code (`npm install -g @anthropic-ai/claude-code`) and its Python SDK `claude-agent-sdk`, which `./init.sh` installs into `.venv/` at the top of the repository (git ignores that folder); a way for Claude Code to sign in, either the key `ANTHROPIC_API_KEY` in the keys file `.secrets/test/.env` or signing Claude Code in once with `claude` in a terminal; and for voice, the key `GROQ_API_KEY` in the same keys file. Without the SDK the page still works and only the request box is off; without the Groq key the microphone stays hidden.

**How to start it,** from the top of the repository. Run `./init.sh` once: it checks the tools (git, curl, Python 3.10 or newer, Node, Claude Code), makes `.venv/` with the SDK, installs the systemd user service `project-ide` that starts the IDE when the machine boots (with lingering on, so before anyone logs in), and then runs `./start.sh`. It is safe to run again, and `./init.sh --no-service` leaves the service out. After that, `./start.sh` starts or restarts the IDE in four steps:

1. **Sync.** It fetches from GitHub. When the branch is behind, it puts back the three built files (the page data, `real-files.json` and `docs/file-tree.md`) and moves the branch forward, but only when no other file has local changes and there are no local commits; otherwise it skips the pull with a warning. It never merges, stashes or pushes. It also says how many items on the page are marked changed; it does not sync them, since that is a Claude Code run started by Apply changes or "sync the file tree".
2. **Stop.** It stops the service and any server left from a start by hand, but only a process running `apps/project-IDE/server/server.py`, never another program on the port.
3. **Rebuild.** It runs `rebuild.py` from the build scripts: the page data gets a new data version only when something changed, so a restart with no change leaves git clean. It writes no How it works file and publishes nothing.
4. **Start.** It starts the service (or a background process when there is none), shows its output, waits up to two minutes until `api/health` answers, and prints the address and the tunnel command.

`./start.sh --no-pull` skips the sync; `./start.sh stop`, `status` and `logs` stop the IDE, show its state and follow its output; `./start.sh serve` is what the service runs (sync, stop, rebuild, then the server in the foreground). Without the service, the output and the process id go to `agents/system/logs/services/project-ide/`, which git ignores. The start at boot with these scripts is decided; the service's name, the rule to pull only when it is a clean move forward, reporting the waiting page items instead of syncing them, and `.venv/` for the SDK are our proposal. The manual way still works when the service is stopped: `python3 apps/project-IDE/server/server.py`, stopped with Ctrl+C.

The server listens only on the machine itself, at `127.0.0.1:8765`, and refuses any other address. From your own computer, open a tunnel with `ssh -N -L 8765:127.0.0.1:8765 you@your-server` and open `http://127.0.0.1:8765/`. The header says "on your server" when the page found the service. Never open the port to the internet: whoever reaches the page can make Claude Code change files and run commands. The server also refuses requests whose address or origin is not the machine's own.

**What it does:**

- `server.py` serves the page, its data and `real-files.json` read fresh from disk; answers `api/health`; keeps the page store as JSON files (`api/store/<collection>`); writes an edit to a file's text straight into the file the page showed, and into the real file made from a draft, and an edit to How it works into the item's `.index.md` (and its copy on disk), with the owner as its writer; never writes back a text the page showed only in part, and never writes again a field it already wrote, so it cannot undo what Claude Code changed since. An edit to a planned file nobody has written yet waits in the store until the sync. It also serves the Notes and runs panel: the list of notes and runs, each note (made, edited, recorded, sent, cancelled or deleted), each run with its steps and the full text of a long step, and a run's summary, merge, discard and stop. Its health answer says whether the panel, the send options' defaults and the summaries are available.
- `claude_bridge.py` runs each request (`api/agent`, and every send of notes) as a Claude Code session, streams its steps to the page, and checks every step first: anything touching the keys folder is refused; deleting exactly the item the owner deleted goes ahead; a file outside the run's checkout, or a tool or command not on the allow list, waits for the owner's Allow or Refuse, and a question nobody answers is refused after fifteen minutes. A run with notes starts in `.worktrees/<run>/agents/system/` on its own branch; Delete and Apply changes runs start in `agents/system/` of the repository itself. It sets the status of the run and its notes as the run moves, merges on Auto merge, and lets Stop work even before Claude Code has connected. Claude Code is told to follow the system's `CLAUDE.md`, file the request, finish the round, never push and end with its `STATUS:` line. Each run is logged with its steps, answer, cost and time.
- `notes.py` keeps the notes and the run records, sorts the panel's list, combines notes into one request and reads a run's `STATUS:` line.
- `runs.py` reads Claude Code's own transcripts of every session started inside the repository, with its subagents, into the run list and the run page. It copies nothing.
- `run_summary.py` asks Claude Haiku for each run's summary and tags, from a folder outside the repository, so that call loads no project settings and never shows as a run.
- `worktrees.py` makes each run's branch and worktree, merges a finished branch into `main` on the server and rebuilds the page, and removes or discards a branch.
- `voice.py` takes a recording (`api/voice` for the delete note box, or a note's recording, which the server turns into text in the background), sends it to Groq's speech-to-text models in order, skips a model that hits its rate limit or fails, and returns the text. The recording is not kept, and the Groq key never reaches Claude Code or the page.

**Its settings,** `server.config.json`, hold no key values, only key names:

| Setting | What it does |
|---|---|
| `repo` | The top of the repository, relative to the server's folder |
| `host`, `port` | Where it listens; only the machine's own address |
| `page_dir`, `page`, `data` | The page and its data file |
| `store_dir` | Where the page store is kept |
| `write_through` | Write file and How it works edits straight into their files |
| `log_dir` | Where each request is logged |
| `secrets.file`, `secrets.keys` | The keys file and the key names read from it |
| `voice` | The Groq address, the models in order, the key name, the five-minute limit, the language |
| `claude.cwd` | Where Claude Code starts |
| `claude.model` | Which model; empty means Claude Code's default |
| `claude.max_turns`, `claude.max_budget_usd`, `claude.approval_timeout_s` | Limits for one request |
| `claude.allow` | Tools and commands Claude Code may use without asking |
| `claude.ask_owner` | Words in a command that always wait for the owner's click: push, reset, rebase, clean, delete, permission changes, installs, network tools |
| `claude.never` | Paths nothing may touch: the keys folder |
| `send_options` | The defaults of the send options: where, merge, tests, bug check, report |
| `worktrees.folder`, `worktrees.main` | Where each run's checkout goes (`.worktrees`) and the branch runs start from and merge into (`main`) |
| `runs.claude_config_dir`, `runs.live_seconds`, `runs.max_text`, `runs.summary_model` | Where Claude Code's transcripts are, how long a terminal run counts as live, how much of a step's text comes at once, and the model that writes summaries |

The settings point at the page in `apps/project-IDE/current-ui/`, the store in `apps/project-IDE/data/page-store/` and the logs in `agents/system/logs/subagents/project-ide-agent/`. Claude Code starts in `agents/system/`, or in the `agents/system/` of a run's own checkout, so the system's `CLAUDE.md`, agents and skills load as its own. A How it works edit from the page goes into the `x.index.md` next to its item.

## Who looks after it

- **The project IDE agent,** `agents/system/.claude/agents/project-ide-agent.md`, builds and publishes the page (`ide-build`), brings back what the owner left on it (`ide-sync`), runs the owner's requests from the page and deletes cleanly. On the server it may be the Claude Code session behind the box. It never edits the page data by hand, never loses the owner's words, never puts a secret value anywhere and never pushes without the owner's click.
- **The knowledge base agent** keeps the knowledge and writes the docs and every How it works file (`file-index`). When the two disagree about what a file says, the files and their metadata win, and the page is rebuilt from them.
- **The owner** can change anything on the page; their edits to How it works are kept word for word.

## Tests and checks

- `check_page.js` must print "page ok" at a desktop and a phone width before every publish.
- `build_map.py` must report every How it works file fresh, none missing, no orphans.
- The tree must equal the files in git.
- After a sync, every new input from the page is in the inputs folder with its answer, every How it works edit is in its file word for word, and the store holds only the history and what was kept on purpose.
- The server was tested on a copy of the repository: the store as files, write-through, a real Claude Code request, Allow and Refuse, a delete with a note and a bring-back. On the owner's server it was tested with `./start.sh`: the health check answers, a restart stops the old server and a stray one started by hand, a second start keeps the data version, and the page store saves and reads a note. `check_page.js` runs there once Chromium's system libraries are installed with `sudo npx playwright install-deps chromium`, which only the owner can run.
- The Notes and runs panel and the page of a run were tested on the owner's server: `check_page.js` prints "page ok"; a browser test of the panel and a run page at a desktop width in light and a phone width in dark passed, with nothing wider than the screen; a real run with two notes ended done and was merged into `main`; a Stop right after sending ended cancelled at no cost; and the summary of a small run cost less than half a cent.

## Where each part's docs are

| Part | Its docs | What they add |
|---|---|---|
| The IDE as a whole | `apps/project-IDE/project-IDE.index.md` | The folder's How it works |
| The page | `apps/project-IDE/current-ui/file-tree-explorer.index.md` | The page's How it works |
| The page data | `apps/project-IDE/current-ui/file-tree.data.index.md` | What the data file holds |
| The server | `apps/project-IDE/server/README.md` | Setup, start with `init.sh` and `start.sh`, notes and runs, each run's branch, and safety, step by step |
| Notes, runs and their branches | `apps/project-IDE/server/server.index.md` and the How it works files of `notes.py`, `runs.py`, `run_summary.py` and `worktrees.py` next to them | What each file keeps or reads, and who uses it |
| The knowledge and records | `apps/project-IDE/data/README.md` | How the knowledge is kept: layers, tags, the flow |
| The build | `agents/system/.claude/skills/ide-build/SKILL.md` and `scripts/README.md` | The build steps and each script's options |
| The sync | `agents/system/.claude/skills/ide-sync/SKILL.md` | Every step from the page back into the files |
| The agent | `agents/system/.claude/agents/project-ide-agent.md` | Its job, when it runs and its rules |
| The How it works files | `agents/system/.claude/skills/file-index/SKILL.md` | Their format and how they are kept |
| Rebuilding the IDE | `apps/project-IDE/docs/rebuild-prompt.md` | The exact spec for an AI |

## Still open in the design

**Stage one, the work to finish the IDE:**

- A custom view for every kind of file, such as one shared view for every skill; today's extra tabs become shared views. Where shared views live (`apps/project-IDE/views/` is proposed) is not settled.
- Correct metadata on every item: every Details file filled in truthfully, every How it works file current.

**Other details:**

- A routine that checks the page store on a schedule, so Apply changes is not needed (proposed).
- How the page published on claude.ai is updated after work on the server.
- More statuses for items than "changed", when the owner asks for them. Notes and runs have their own statuses.
- Pull requests from a run (Make PR, Make PR and merge): the next step of the notes and runs plan, not built; when to build it is open. Until then a merge happens on the server only and nothing is pushed.
- Running notes in a cloud session (the Cloud send option): shown but off; it needs its own plan.
- A run's branch starts from the last commit of `main`, so page edits not yet committed are not in it.
- Whether the run records ever go into git: today they stay in the logs folder, out of git (proposed).
