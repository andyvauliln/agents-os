# The project IDE

## In short

The project IDE is the owner's window on the Agent OS. The owner builds the system by vibecoding: they say what they want in plain words, and AI writes the plans, the docs and the code. The IDE shows the whole project as one clickable tree of every folder and file, and next to each one says what it is, how it works, what it holds and what is still open. The owner reads, edits, comments, asks and deletes there, and AI brings everything they leave back into the files. The same tree gives every AI working on the project the full context it needs to change things precisely.

The IDE works today: the page is published on claude.ai and in use, its build and checks run, and the server that puts Claude Code behind the page is written and was tested on a copy of the repository. Finishing it is stage one of the project: a view for every kind of file, correct metadata on every item, and a tab for each metadata file that really exists.

This document is the full manual of the IDE: every part of the page and how to use it, the three places it runs, how it is built and checked, how the owner's work comes back into the files, the metadata files behind its tabs, how to run it on a server, and where every part lives now and later. Why the IDE exists and how it should behave are in its vision, `apps/project-IDE/docs/vision.md`.

## The IDE at a glance

```text
          the repository (git)
   tree notes · docs · drafts · every real file · How it works and Details files
                    │
                    │  ide-build: parse, enrich, materialize, check, publish
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
                          voice ─► Groq (voice.py)
                    │
                    │  ide-sync: every note, edit, deletion and request back into the files
                    ▼
          the repository again, then ide-build
```

| Part | What it is for | Where it lives while we plan | Where it lives in the finished layout |
|---|---|---|---|
| The page | The tree, the tabs, editing, notes, questions, the ask box | `vision/explorer/file-tree-explorer.html` | `apps/project-IDE/current-ui/file-tree-explorer.html` |
| The page data | Everything the page shows, built from the repository | `vision/file-tree.data.json`, copied to `vision/explorer/` | `apps/project-IDE/current-ui/file-tree.data.json` |
| The real files' texts | The text of every real file, loaded when one is opened | `vision/explorer/real-files.json` | next to the page data |
| The build scripts | Build the data, keep files in step with their drafts and metadata, check the page | `vision/tools/` | `agents/system/.claude/skills/ide-build/scripts/` |
| The owner's page edits kept in the data | Values the owner set on the page that the build applies on top | `vision/tools/overrides.json` | `apps/project-IDE/data/overrides.json` |
| The tree notes and the knowledge | One section per file and folder; decisions, inputs, changelog | `vision/docs/` | `apps/project-IDE/data/` |
| How it works and Details files | One explanation and one details file per item | `vision/tree/agent-os/...`, copied next to each item on disk | next to each item |
| The server | The page on the owner's machine with Claude Code behind it | `vision/server/` | `apps/project-IDE/server/` |
| The page store on the server | The owner's notes, edits and messages as JSON files | `vision/page-store/` | `apps/project-IDE/data/page-store/` |
| The project IDE agent and its skills | Build the page, bring the owner's work back | `vision/.claude/agents/`, `vision/.claude/skills/ide-build/`, `ide-sync/` | `agents/system/.claude/agents/`, `agents/system/.claude/skills/` |

The parts connect in one loop. The build reads the repository and writes the page data. The page shows it. The owner works on the page, and everything they do is saved at once in the page's store. When the owner presses Apply changes or says "sync the file tree", the project IDE agent reads the store, writes every edit into its file, files every note and request as an owner input, cleans up what was deleted and rebuilds the page. The knowledge base agent then sorts the new inputs into the docs and refreshes the explanations, and the page is rebuilt once more. On the owner's server the loop is shorter: edits go straight into the files, and requests run at once.

## How it is laid out

While the system is planned, the IDE runs from the planning folder `vision/`, and the copies of its files elsewhere in the repository are made by the build. The finished layout is:

```text
apps/project-IDE/
├── docs/                         the IDE's own docs
│   ├── vision.md                 what the IDE is for and why
│   ├── README.md                 this manual
│   ├── README.asd.md             this manual in ASD-STE100
│   └── rebuild-prompt.md         how an AI builds the IDE again exactly
├── current-ui/                   the page, as published on claude.ai
│   ├── file-tree-explorer.html   the page itself, one file
│   └── file-tree.data.json       its data; built, never edited or merged by hand
├── server/                       the same page on the owner's server
│   ├── README.md                 how to start it and reach it safely
│   ├── server.py                 the web service: page, store, write-through, request box
│   ├── claude_bridge.py          runs each request as a Claude Code session
│   ├── voice.py                  turns a recording into text through Groq
│   └── server.config.json        address, paths, limits, what Claude Code may do
└── data/                         this project's knowledge and what the page is built from
    ├── README.md                 how the knowledge is kept
    ├── file-tree.md              the tree notes: one numbered section per file and folder
    ├── inputs/                   every owner input, word for word, with index.json
    ├── decisions.md, changelog.md
    ├── knowledge-map.json        which knowledge applies to which item
    ├── sources/                  earlier knowledge notes, kept; not used now
    ├── page-store/               on the server: the page's notes, edits and messages
    ├── overrides.json            the owner's page edits kept in the page data
    ├── memory/, plans/, archive/ working notes, change plans, retired files
```

Every file and folder in it has its How it works file and its Details file next to it, as everywhere in the repository. The project IDE agent and the two skills live with the system's other helpers in `agents/system/.claude/`, and the build scripts inside the `ide-build` skill.

Today the repository already holds these folders and copies of the page, the server files and the build scripts, but the working sources are still in `vision/`: the page in `vision/explorer/`, the scripts in `vision/tools/`, the server in `vision/server/`, and the tree notes and knowledge in `vision/docs/`. The copy of the page data in `apps/project-IDE/current-ui/` is an empty placeholder until the build writes there. When planning ends, the sources move into the finished layout and the paths in the server settings and the scripts change with them.

## The page

The page is one HTML file, `file-tree-explorer.html`, that reads one data file, `file-tree.data.json`. It needs no build step of its own and loads no code from outside, only its fonts. It has a header, the tree on the left, and on the right the sheet of the selected item with the ask box pinned under it.

### The header

- **The title and the version line.** The version line shows the version of the tree notes and the number of items, and then where the page runs: "on your server", "view only", or nothing on claude.ai.
- **Apply changes.** Shown when something on the page is marked changed, with the count. It opens a short confirmation and then carries every change into the files (see "Apply changes" below). While a request waits, it reads "Applying changes" and cannot be pressed again.
- **The filter.** Typing filters the tree as you type. A number such as `27` or `[27]` finds items by their number in the tree notes; a text with `*` matches names as a pattern (`*.json`); a text with `/` matches paths (`agents/system/`); anything else matches part of a name, so `.md` finds every Markdown file. The folders on the way to each match open by themselves, and a line under the tabs says how many items match, with a button to clear the filter.

### The tree

- **All and Changed.** All shows the whole tree. Changed shows only the items marked changed since the last sync, with the reason on each.
- **The metadata switch.** On, every file shows its two metadata files as rows right under it, its How it works file (`vision.index.md` for `vision.md`) and its Details file (`vision.meta.json`), and every folder shows its own first inside it. Clicking one opens that tab of its item. Off, they are hidden, including the real ones found on disk. It is on by default.
- **The empty filter.** On, the tree shows only the files with nothing written in them yet, each marked "empty", with the folders that hold them. The tree itself is always the files on disk; nothing that is only planned is shown.
- **The rows.** A folder icon, a file icon or a link icon, the name, a "changed" tag when it applies, and the item's number in the tree notes when it has one. A first click on a closed folder opens it and selects it. The arrow keys move through the tree and open or close folders. The open folders and the selected item are remembered in the browser, and the address of the page carries the selected item, so a link opens the same item.
- **Deleted items** stay in their place, struck through, until the next sync.

### The sheet of an item

The top of the sheet shows the path as links to each folder above, the item's number and name, a "Changed" chip with the reason when it is marked, its kind (file, folder, file link or folder link), a Delete button for every item but the top, and one line on what the item is for. Under that are its tabs.

### The tabs

The first tab is always How it works and the last is Details. Between them, a file has File, Example and Questions, and a folder has Contents and Questions. Some items have extra tabs.

- **How it works.** The item's explanation, read from its own file, `vision.index.md` next to `vision.md` or `configs/configs.index.md` inside a folder. The name of that file shows at the top with an Edit button. Like a Markdown file on the File tab, it opens in the Read view with Read and Source and Full screen (below); edits go through the Edit button. Items written in the new format show fixed headings (What it is, Who looks after it, When and how it changes, Who uses it and when, Where it is mentioned, Related knowledge) and a short Keep in mind list; older ones show one Summary, the knowledge that applies to the item directly and from the folders above, the item's own notes from the tree notes, and the owner inputs that shaped it. Under it the tab lists the owner's messages about the item waiting for the next sync and every change made on the page to it, each with an "Undo this change" button. On claude.ai, when something under an item was changed on the page, the page can write a fresh summary at once ("Update it now"); the knowledge base agent checks it at the next sync.
- **File.** The file as it is now: its text, read from the repository, even when it is empty, with its path and where the text came from. A Markdown file opens in the Read view (below); any other file shows numbered lines. A long file shows 3,000 lines at a time with a button for more; a real file over 200 KB is not put on the page, and the tab says to open it in the repository. A keys file (`.env`) is local only: the page never reads, shows or edits its text. A file nobody has written yet offers "Write it" and, when an example exists, "Start from the example". A link says what it points at. The page file shows its own source, and the data file shows itself as the page loaded it, read only.
- **Contents** (folders). A card for each item inside, with its name and what it is for, a button to add a file or folder, and a button to comment on the folder.
- **Example.** For a document, the structure of the file: each heading and what goes under it, taken from the outline in the skill that writes that kind of doc. For a settings file, a full example and a table of every field with its allowed values, an example and what it is for. A jobs or links file builds its example from its own table, unsaved edits included.
- **Questions.** The item's Questions file, in the Read view with Read and Source and Full screen, like a Markdown file: its open questions for the owner, and the owner's own questions with their answers, all in ASD-STE100 apart from the owner's words. Below it, the open questions still kept in the tree notes, each with a Discuss button that starts the conversation in the ask box, and the questions answered on the page with their answers. A folder also lists the open questions of the files inside it.
- **Details.** The item's Details file, `vision.meta.json`, shown as it is. It holds what the item is, its state, whether it is in git, whether it is secret or generated, who writes and reads it, when it changes, what it relates to, what must change with it, what it inherits from the levels above, its sources, features and views, and its number in the tree. Most Details files are still empty templates.
- **Extra tabs.** An agent's folder has Overview and Agents (what the agent does and the agents, workers and skills below it). A jobs file has Jobs, a table of every job with its switch, schedule, place, platform and model. A links file has Links. A keys file has Variables, the names of its keys with what each is for, never a value. A tests file has Tests. Some agents have Capabilities. Each of these is an editable table; saving it updates the file.

### Reading and editing a document

A Markdown file opens as a page of a book, on its own white or black paper, with the word count, the reading time and a Contents list of its headings. The reader's controls:

- **Read and Source.** Read shows the rendered document; Source shows its numbered lines, where a click on a line number opens a comment on that line.
- **Aa.** The font (Sans, Legible or Serif) and the size (S, M or L).
- **Light and Dark.** The paper, white or black, remembered in the browser.
- **Full screen.** The document fills the screen, with the Contents in a side column on a wide screen, a progress line at the top, and Close or Esc to leave.
- **Edit in place.** A double-click on a paragraph, heading, list or table, or two taps on a phone, makes that block editable right where it stands, looking just as it reads: type in it, with Ctrl+B for bold and Ctrl+I for italic. Save, Ctrl+Enter or a click anywhere outside the block turns it back into Markdown and writes only those lines into the file; Esc or Cancel leaves it as it was. A Markdown button switches the block to its source lines when you want them, and the front matter at the top always opens as source. It works in full screen too.
- **Edit.** Opens the whole file in an editor with numbered lines that wrap to the screen. Save file or Ctrl+S saves it; Cancel drops the edit.

Every save is recorded with what was there before, so it can be undone from How it works. On the owner's server the file on disk changes at once; on claude.ai the edit waits in the page's store until the next sync. After a save on claude.ai the page also checks related items (the parent folders and the items that mention this one) and saves any update they need as "Related updates", which can be undone in one click; it never changes another file's text or anyone's How it works.

### Notes

A note, or comment, is left on one line (from the line numbers) or on the whole file or folder (the "Comment on" button). Each note keeps the text of its line, so it stays on the right line when the file changes, and says so when that line is gone. A note can be resolved, reopened or deleted; resolved notes are hidden until asked for. At the sync, a note the owner meant as a change is applied, and any other open note becomes an open question on the item.

### The ask box

The box under every item takes a question or a request about that item. Enter sends; Shift+Enter adds a line. Each item keeps its own conversation in the browser, and Clear empties it. Every message and its answer are also saved in the page's store as an owner input, so they reach the files at the next sync.

On claude.ai the page asks Claude itself, with a choice of model: Most capable, Balanced or Fastest. Claude reads the item, the knowledge that applies to it and its related items, and answers in one of three ways:

- **An answer.** A question answered for good is also saved on the item's Questions tab.
- **A draft.** A request for a change comes back as a draft card: every item it changes, and for each one the fields it changes, with a before and after view of each field. Save (or typing "save") applies it at once and marks the items changed; Discard drops it; asking more changes the draft first. A new file or folder and a removal show as such.
- **Save or discard,** when the owner says so in words about a waiting draft.

On the owner's server the box sends the request to Claude Code working in the repository (see "The server"). There is no model choice on the page; the server's settings choose. The chat shows each step Claude Code takes, any step that waits for the owner with Allow and Refuse buttons, then the answer with its cost, its time and how many files changed. A follow-up in the same box continues the same conversation, Stop ends a run, and the tree reloads when files changed. On the server a microphone button sits next to the box: it records up to five minutes with a timer, the server turns the recording into text, and the text is added to the box to check before sending.

Opened anywhere else, the box says that the page only shows the files and that a message reaches no one.

### Adding a file or folder

A folder's Contents tab has "Add a file or folder": a name (ending in `/` for a folder), its type and one or two sentences on what it is for. The new item appears in the tree at once, marked changed. At the sync it gets its number and section in the tree notes and its How it works file, and it stays proposed until the owner agrees.

### Deleting and bringing back

The Delete button next to an item's name opens a short form: what will be deleted (a folder counts the items inside it) and an optional note for Claude, such as what to move or keep first. The note box has the microphone too on the server. "Delete and clean up" then:

- **on the owner's server** starts Claude Code at once in that item's chat. It may delete exactly that item and its metadata files without a second click, then cleans the project of it: its line and section in the tree notes, every link to it and mention of it in other files, the parent's How it works and the knowledge map. It follows the note, files the deletion and commits;
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

The open folders, the selected item and tab, the switches, the Read or Source choice, the reader's paper, font and size, each item's conversation (its last 30 messages) and unsent text in the box. Nothing the owner needs to keep is kept only there: notes, edits and messages go to the page's store.

## The three places the page runs

The page finds out where it is when it loads.

| Place | How the page knows | Where the owner's work is saved | Who answers the box | Apply changes |
|---|---|---|---|---|
| claude.ai, as a published artifact | The artifact runtime is there | The artifact's own store: the collections `nodes`, `changes` and `inputs` | Claude, through the page, with a choice of model | One comment sent to the Claude session watching the page |
| The owner's server | The server answers `api/health` | JSON files in the page store; file and How it works edits also straight into their files | Claude Code in the repository, step by step, with the owner's Allow and Refuse | One Claude Code run in the top folder's chat |
| Anywhere else | Neither answers | Nowhere: the header says "view only" | No one | Hidden |

The published page has one link, https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs, and is always republished at that link, so the owner's work waiting in its store stays where it is. It asks for four runtime capabilities: its store, asking Claude, knowing who views it, and sending a comment to Claude.

**The page or the terminal.** Both reach the same Claude Code, with the same `CLAUDE.md`, skills and files. In the terminal the owner starts Claude Code in `agents/system/` and names the item themselves; it files their words and does the round as `CLAUDE.md` says, and asks in the terminal before a risky step. On the page every note and message is tied to one item, saved word for word at once with its history and undo, and marked changed until the sync; on the server the request box runs the same Claude Code, with Allow and Refuse. The page suits work on one item, the terminal wide work across many. Work done in the terminal shows on the page only after the next rebuild.

## What the page reads

`file-tree.data.json` is the page's only data. It is built, never edited or merged by hand. Its top level holds the version of the data and of the tree notes, when it was built, the root item, the decisions, the knowledge entries with the items each applies to, the owner inputs by id, the docs, the feature areas, the retired numbers, and the list of items. Each item carries its id (`n-53.4.2` for an item in the tree notes, `r-...` for a real file the build found on disk), its number, name, path, type, parent and children, whether it is a link, whether it exists on disk or was found by the scan, what it is for and its summary, its How it works text and the path of its How it works file, its Details and the path of its Details file, its family name for those files, its text or a note that the text loads later, the file the text came from, its example, its field guide, its extra tabs, its open questions and answered questions, and the knowledge that applies to it.

`real-files.json` sits next to it and maps each real file found on disk to its text. The page loads it the first time such a file is opened, so the page itself stays small. On the server it is read fresh from disk on every request.

## How the page is built and checked

The `ide-build` skill turns the repository into the page data, checks it and publishes it. It runs after every round that changed the tree notes, a doc, a draft or a How it works file, after a pull that brought changes, and as the last step of every sync. Its scripts, all Python with the standard library except the page check:

| Script | What it does |
|---|---|
| `parse.py` | Reads the tree notes, the feature map and the decisions into a list of items. |
| `enrich.py` | Adds the drafts, examples, knowledge, How it works and Details files and the extra tabs, lists every real file in git under each folder that exists, applies the owner's kept page edits, and writes the page data and `real-files.json`. It is given the next data version. |
| `tabs.py` | The field guides and the extra tables (keys, jobs, links, tests, capabilities), used by `enrich.py`. |
| `materialize.py` | Keeps files on disk in step with their sources in `vision/`: copies drafts over their real files, copies each item's How it works and Details next to it, gives every other file and folder empty metadata files, keeps a `.gitkeep` in empty folders, writes `docs/file-tree.md`. It makes nothing from the plan. |
| `index_files.py` | Knows where every How it works and Details file lives, reads and writes them, and makes missing Details files. |
| `build_map.py` | Builds the knowledge map and checks the How it works files: which are missing or stale (children first), the context for writing one, confirming one, writing many at once, and orphans whose item is gone. |
| `check_page.js` | Opens the page at a desktop width and a phone width with a stand-in for the artifact runtime and fails on a page error, a missing tab or a page wider than the phone. Needs Node and Playwright with Chromium. |

The build, in order:

1. Put the finished page in place first, because the page shows its own source.
2. Parse the tree notes, then enrich with the next data version.
3. Run `materialize.py`, then enrich again if it made new files.
4. Copy the data next to the page.
5. Run `build_map.py` until it reports every How it works file fresh, none missing, no orphans; hand stale ones to the knowledge base agent's `file-index` skill.
6. Run `check_page.js` on the top item, the README and every item the round changed, and look at the screenshots of anything changed on the page itself. It must print "page ok".
7. Check that the tree equals the files in git: the page's items are exactly the paths `git ls-files` lists, plus the local `.env` files. Today this is checked path by path when the tree changes; there is no script for it yet.
8. Publish at the same link, with the data and `real-files.json` next to the page.
9. Report in plain words what the owner will see changed.

The build never invents a status: an item is decided unless its notes say proposed, and anything new an agent adds is proposed until the owner agrees. No secret value is ever in the data.

## How the owner's work comes back

The page saves everything at once, so the owner never waits; the files change only at a sync (on claude.ai) or at once (on the server, for file and How it works edits). The page's store has three collections:

| Collection | One document per | What it holds |
|---|---|---|
| `inputs` | message sent from the page | The text, the item and path it was sent on, its kind (question, answer, change, discard, delete, restore or apply), the answer the page gave, and its status: `new` until a sync files it. An apply request also holds the count, the items and whether it reached Claude. |
| `nodes` | item the owner touched | The latest value of each edited field (`content` for the text, `how_md` for How it works), line comments with their line's text, answered questions, a new item, a deletion with what the item was, the owner's note and who cleans up, and the mark of a server request that changed it. |
| `changes` | save | The history: when, by whom, the owner's words, and for each item every field before and after, and whether it was undone. It is never folded or cleared. |

On claude.ai these live in the artifact's store and are read through the artifact data tool on the page's link. On the server each document is one JSON file, `page-store/<collection>/<id>.json`.

The `ide-sync` skill brings them back. It runs when the owner presses Apply changes or says "sync the file tree", and always before `ide-build`:

1. List every new input and every touched item.
2. Save each as an owner input, word for word, with the item it was left on; a message and the answer the page gave are one input.
3. Write the edits into their files: a file's text into that file, How it works into the item's `.index.md` word for word with the owner as its writer, a new item into the tree notes with its How it works file, any other field into the kept page edits. A deleted item is cleaned out of the project, following the owner's note.
4. Run the requests the owner sent and file each answer with its input.
5. Hand the saved inputs to the knowledge base agent, which sorts them into the notes and docs and refreshes the explanations.
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

Every item has its How it works and Details files today. The example and questions files are being written now for the main docs and the keys files only; other files get them later, when they need them. The rule is that a tab shows only when its file exists and shows that file; today the page still shows Example and Questions on every file, built from the tree notes, and moving them onto real files is stage one work. While we plan, the How it works and Details files are kept in the mirror `vision/tree/agent-os/...` (or next to a draft in `vision/`), and the build copies them next to each item on disk.

## The server

`server/` runs the same page on the owner's own machine, with Claude Code behind its request box.

**What it needs:** the repository cloned on the server with a way to push; Python 3.10 or newer; Node; Claude Code and its SDK (`npm install -g @anthropic-ai/claude-code` and `pip install claude-agent-sdk`); a way for Claude Code to sign in, either the key `ANTHROPIC_API_KEY` in the keys file `.secrets/test/.env` or signing Claude Code in once with `claude` in a terminal; and for voice, the key `GROQ_API_KEY` in the same keys file. Without the SDK the page still works and only the request box is off; without the Groq key the microphone stays hidden.

**How to start it,** from the top of the repository: `python3 vision/server/server.py` while we plan (later `python3 apps/project-IDE/server/server.py`). It listens only on the machine itself, at `127.0.0.1:8765`, and refuses any other address. From your own computer, open a tunnel with `ssh -N -L 8765:127.0.0.1:8765 you@your-server` and open `http://127.0.0.1:8765/`. The header says "on your server" when the page found the service. Ctrl+C stops it. Never open the port to the internet: whoever reaches the page can make Claude Code change files and run commands. The server also refuses requests whose address or origin is not the machine's own.

**What it does:**

- `server.py` serves the page, its data and `real-files.json` read fresh from disk; answers `api/health`; keeps the page store as JSON files (`api/store/<collection>`); writes an edit to a file's text straight into the file the page showed, and into the real file made from a draft, and an edit to How it works into the item's `.index.md` (and its copy on disk), with the owner as its writer; never writes back a text the page showed only in part, and never writes again a field it already wrote, so it cannot undo what Claude Code changed since. An edit to a planned file nobody has written yet waits in the store until the sync.
- `claude_bridge.py` runs each request (`api/agent`) as a Claude Code session in the folder the settings name, streams its steps to the page, and checks every step first: anything touching the keys folder is refused; deleting exactly the item the owner deleted goes ahead; a file outside the repository, or a tool or command not on the allow list, waits for the owner's Allow or Refuse, and a question nobody answers is refused after fifteen minutes. Claude Code is told to follow the system's `CLAUDE.md`, file the request, finish the round and never push. Each run is logged with its steps, answer, cost and time.
- `voice.py` takes a recording (`api/voice`), sends it to Groq's speech-to-text models in order, skips a model that hits its rate limit or fails, and returns the text. The recording is not kept, and the Groq key never reaches Claude Code or the page.

**Its settings,** `server.config.json`, hold no key values, only key names:

| Setting | What it does |
|---|---|
| `repo` | The top of the repository, relative to the server's folder |
| `host`, `port` | Where it listens; only the machine's own address |
| `page_dir`, `page`, `data` | The page and its data file |
| `store_dir` | Where the page store is kept |
| `write_through` | Write file and How it works edits straight into their files |
| `log_dir` | Where each request is logged |
| `planning_dir` | While we plan, the folder holding the drafts and How it works files |
| `secrets.file`, `secrets.keys` | The keys file and the key names read from it |
| `voice` | The Groq address, the models in order, the key name, the five-minute limit, the language |
| `claude.cwd` | Where Claude Code starts |
| `claude.model` | Which model; empty means Claude Code's default |
| `claude.max_turns`, `claude.max_budget_usd`, `claude.approval_timeout_s` | Limits for one request |
| `claude.allow` | Tools and commands Claude Code may use without asking |
| `claude.ask_owner` | Words in a command that always wait for the owner's click: push, reset, rebase, clean, delete, permission changes, installs, network tools |
| `claude.never` | Paths nothing may touch: the keys folder |

While we plan, the settings point at `vision/`: the page in `vision/explorer/`, the store in `vision/page-store/`, the logs in `vision/logs/project-ide-agent/`, and Claude Code started in `vision/`, where the planning copy of the system's agents, skills and `CLAUDE.md` loads. In the finished layout Claude Code starts in `agents/system/`, so the system's `CLAUDE.md`, agents and skills load as its own.

## Who looks after it

- **The project IDE agent,** `agents/system/.claude/agents/project-ide-agent.md`, builds and publishes the page (`ide-build`), brings back what the owner left on it (`ide-sync`), runs the owner's requests from the page and deletes cleanly. On the server it may be the Claude Code session behind the box. It never edits the page data by hand, never loses the owner's words, never puts a secret value anywhere and never pushes without the owner's click.
- **The knowledge base agent** keeps the knowledge and writes the docs and every How it works file (`file-index`). When the two disagree about what a file says, the files and the notes win, and the page is rebuilt from them.
- **The owner** can change anything on the page; their edits to How it works are kept word for word.

## Tests and checks

- `check_page.js` must print "page ok" at a desktop and a phone width before every publish.
- `build_map.py` must report every How it works file fresh, none missing, no orphans.
- The tree must equal the files in git.
- After a sync, every new input from the page is in the inputs folder with its answer, every How it works edit is in its file word for word, and the store holds only the history and what was kept on purpose.
- The server was tested on a copy of the repository: the store as files, write-through, a real Claude Code request, Allow and Refuse, a delete with a note and a bring-back.

## Where each part's docs are

| Part | Its docs | What they add |
|---|---|---|
| The IDE as a whole | `apps/project-IDE/project-IDE.index.md` | The folder's How it works |
| The page | `apps/project-IDE/current-ui/file-tree-explorer.index.md` | The page's How it works |
| The page data | `apps/project-IDE/current-ui/file-tree.data.index.md` | What the data file holds |
| The server | `apps/project-IDE/server/README.md` | Setup, start and safety, step by step |
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
- Tabs as real files: Example and Questions shown only where `x.example.md` and `x.questions.md` exist, an ASD-STE100 tab on a README that has `README.asd.md`, and the page reading each tab from its file.

**Other details:**

- Moving the working sources out of `vision/` into the finished layout, and pointing the server's settings and the scripts at it. The copy of `server.config.json` in `apps/project-IDE/server/` still holds the planning paths.
- `materialize.py` is not yet among the copies of the build scripts in `agents/system/.claude/skills/ide-build/scripts/`.
- A script that checks the tree against `git ls-files`.
- A routine that checks the page store on a schedule, so Apply changes is not needed (proposed).
- How the page published on claude.ai is updated after work on the server.
- More statuses than "changed", when the owner asks for them.
