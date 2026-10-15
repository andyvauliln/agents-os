This is the ASD-STE100 version of `README.md`. `README.md` is the source. If the two documents are different, use `README.md`.

# The project IDE

## In short

The project IDE is the window of the owner on the Agent OS. The owner builds the system by vibecoding. The owner tells what they want in plain words, and AI writes the plans, the docs and the code.

The IDE shows the full project as one tree of all folders and files. The owner can click each folder and each file. For each item, the IDE tells what the item is, how it works, what it contains and which questions are open.

The owner reads, edits, comments, asks and deletes on the page. AI then puts all the work of the owner into the files. The same tree gives each AI the full context that it must have to make exact changes.

The IDE operates now. The page is published on claude.ai, and the owner uses it. The build and the checks operate. The server puts Claude Code behind the page. The server operates on the server of the owner. A service starts it when the machine starts.

The completion of the IDE is stage one of the project. Stage one has three tasks:

1. Make a view for each type of file.
2. Make the metadata correct on each item.
3. Show a tab only for a metadata file that exists.

This document is the full manual of the IDE. It gives each part of the page and how to use it. It gives the Notes and runs panel and the page of each run. It gives the three locations where the page operates. It tells how the build makes the page and how the checks examine it. It tells how the work of the owner goes back into the files. It gives the metadata files behind the tabs. It tells how to operate the IDE on a server. It tells where each part is now and where each part goes later.

The vision tells why the IDE exists and how it must operate. The vision is `apps/project-IDE/docs/vision.md`.

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

| Part | What it is for | Where it is |
|---|---|---|
| The page | The tree, the tabs, edits, notes, questions, the ask box | `apps/project-IDE/current-ui/file-tree-explorer.html` |
| The page data | All the data that the page shows. The build makes it from the repository. | `apps/project-IDE/current-ui/file-tree.data.json` |
| The text of the files | The text of each file. The page loads it when the owner opens the file. | `apps/project-IDE/current-ui/real-files.json` |
| The build scripts | They make the data, give metadata files to new items, and examine the How it works files, the tree and the page | `agents/system/.claude/skills/ide-build/scripts/` |
| The kept edits of the extra tables | Values that the owner set on the page. The build applies them. | `apps/project-IDE/data/overrides.json` |
| The records | Each owner input, the decisions, the changelog and the plans | `apps/project-IDE/data/` |
| The How it works files and the Details files | One explanation file and one details file for each item | Next to each item |
| The server | The page on the machine of the owner, with Claude Code behind it | `apps/project-IDE/server/` |
| The page store on the server | The comments, edits, messages and notes of the owner, as JSON files | `apps/project-IDE/data/page-store/` |
| Notes and runs | One panel on the server page shows each note and each Claude Code run. Each run has its own page. | The page, with `notes.py`, `runs.py`, `run_summary.py` and `worktrees.py` in `apps/project-IDE/server/` |
| The run records | The status, notes, branch, summary and tags of each run. Git does not keep them. | `agents/system/logs/subagents/project-ide-agent/runs/` |
| The project IDE agent and its skills | They build the page and put the work of the owner back into the files | `agents/system/.claude/agents/`, `agents/system/.claude/skills/` |

The parts connect in one loop:

1. The build reads the repository and writes the page data.
2. The page shows the data.
3. The owner works on the page. The page keeps all the work in its store immediately.
4. The owner pushes Apply changes, or the owner says "sync the file tree".
5. The project IDE agent reads the store. It writes each edit into its file. It records each note and each request as an owner input. It removes the deleted items. It builds the page again.
6. The knowledge base agent puts the new inputs into the docs and updates the explanations.
7. The build makes the page one more time.

On the server of the owner, the loop is shorter. The edits go into the files immediately. Each message or note starts a run immediately, on its own branch. When the run is done, the server merges the branch into `main`.

## How it is laid out

Each file of the IDE is its own source. Edit it where it is. This is the layout:

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

Two scripts at the top of the repository install and start the server. You run `init.sh` one time. You run `start.sh` for each start. Each run from the page operates in its own checkout in `.worktrees/` at the top of the repository. Git ignores this folder. Each file and each folder in this layout has its How it works file and its Details file next to it. This rule applies to all the repository. The project IDE agent and its two skills are in `agents/system/.claude/`, with the other helpers of the system. The build scripts are in the `ide-build` skill.

## The page

The page is one HTML file, `file-tree-explorer.html`. It reads one data file, `file-tree.data.json`. The page does not need a build step. It does not load code from other locations. It loads only its fonts.

The page has three areas:

- The header, at the top.
- The tree, on the left side.
- The sheet of the selected item, on the right side. The ask box is under the sheet.

### The header

- **The title and the version line.** The version line shows the version of the page data and the number of items. Then it shows where the page operates: "on your server", "view only", or no text on claude.ai.
- **Notes and runs.** This button shows only on the server of the owner. It opens and closes the panel of notes and runs under the header (refer to "Notes and runs"). It shows the number of notes and runs that are at work. When a run waits for the owner, it shows "N need you" in red.
- **Apply changes.** This button shows when the page has changed items. It shows the number of changed items. It opens a short confirmation. Then it puts all the changes into the files (refer to "The changed mark and Apply changes"). While a request waits, the button shows "Applying changes", and you cannot push it again.
- **The filter.** When you type, the tree shows only the items that agree with the text:
  - A text with `*` finds names that agree with the pattern, for example `*.json`.
  - A text with `/` finds paths, for example `agents/system/`.
  - Other text finds a part of a name. For example, `.md` finds all Markdown files.

  The folders above each found item open automatically. A line under the tabs gives the number of found items. A button on that line removes the filter.

### The tree

- **All and Changed.** All shows the full tree. Changed shows only the items that are changed since the last sync. Each item shows the reason.
- **The metadata switch.** When the switch is on, each file shows its two metadata files as rows below it. These are the How it works file (`vision.index.md` for `vision.md`) and the Details file (`vision.meta.json`). Each folder shows its two metadata files first, in the folder. When you click a metadata row, the related tab of its item opens. When the switch is off, the tree does not show metadata files. This includes the real metadata files on the disk. The switch is on by default.
- **The empty filter.** When the filter is on, the tree shows only the files that have no text yet. Each of these files has the mark "empty". The tree always shows the files on the disk.
- **The rows.** Each row has an icon and the name. If applicable, a row also has a "changed" tag. The icon shows a folder, a file or a link. When you click a closed folder one time, it opens and you select it. The arrow keys move in the tree. They also open and close folders. The browser keeps the open folders and the selected item. The address of the page contains the selected item. Thus a link opens the same item.
- **Deleted items.** A deleted item stays in its location until the next sync. A line goes through its name.

### The sheet of an item

The top of the sheet shows these data:

- The path, with a link to each folder above the item.
- The name of the item.
- A "Changed" chip with the reason, if the item is changed.
- The type of the item: file, folder, file link or folder link.
- A Delete button. All items have it, but not the top item.
- One line that tells what the item is for.

The tabs of the item are below these data.

### The tabs

The first tab is always How it works. The last tab is always Details. Between them, a file has File, Example and Questions. A folder has Contents and Questions. Some items have more tabs.

- **How it works.** This tab shows the explanation of the item. The page reads it from the file of the item: `vision.index.md` next to `vision.md`, or `configs/configs.index.md` in a folder. The name of that file is at the top, with an Edit button. The tab shows the file in the Read view, like a Markdown file on the File tab. It has Read and Source, and Full screen. To change the text, push Edit.
  - Items in the new format show fixed headings: What it is, Who looks after it, When and how it changes, Who uses it and when, Where it is mentioned, Related knowledge. Then they show a short "Keep in mind" list.
  - Items in the old format show one Summary.
  - Below the explanation, the tab shows the messages of the owner about the item that wait for the next sync. It also shows each change that the owner made on the page to the item. Each change has an "Undo this change" button.
  - On claude.ai, if an item below this item changed on the page, the page can write a new summary immediately ("Update it now"). The knowledge base agent examines it at the next sync.
- **File.** This tab shows the file as it is now. The page reads the text from the repository. The tab shows the text also when the file is empty. It shows the path and the source of the text.
  - A Markdown file opens in the Read view (refer to "Reading and editing a document").
  - Other files show numbered lines.
  - A long file shows 3,000 lines at one time. A button shows more lines.
  - The page does not show a real file that is larger than 200 KB. The tab tells you to open the file in the repository.
  - A keys file (`.env`) is local only. The page does not read, show or edit its text.
  - For a file that is not written, the tab shows "Write it". If an example exists, it also shows "Start from the example".
  - A link tells which item it points to.
  - The page file shows its own source. The data file shows itself as the page loaded it. You cannot edit the data file.
- **Contents** (folders only). This tab shows a card for each item in the folder. Each card shows the name and what the item is for. The tab has a button to add a file or a folder, and a button to comment on the folder.
- **Example.**
  - For a document, the tab shows the structure of the file: each heading and what goes below it. The page takes this structure from the outline in the skill that writes that type of document.
  - For a settings file, the tab shows a full example. It also shows a table of all fields, with the permitted values, an example and the purpose of each field.
  - A jobs file or a links file makes its example from its own table. The example includes the edits that are not saved.
- **Questions.** This tab shows the Questions file of the item. It shows the file in the Read view, with Read and Source, and Full screen. The file has two parts: the open questions for the owner, and the questions of the owner with their answers. All text is in ASD-STE100. Only the words of the owner stay as the owner wrote them. Below the file, the tab shows the questions that have an answer on the page, with their answers. A folder also shows the open questions of the files in it.
- **Details.** This tab shows the Details file of the item, `vision.meta.json`, as it is. The Details file contains these data:
  - What the item is, and its state.
  - If it is in git, if it is secret, and if a script makes it.
  - Who writes it, who reads it, and when it changes.
  - Its related items, and what must change with it.
  - What it gets from the levels above.
  - Its sources, features and views.

  The Details file of a new item is empty until somebody writes it.
- **More tabs.**
  - The folder of an agent has Overview and Agents. Overview tells what the agent does. Agents shows the agents, workers and skills below it.
  - A jobs file has Jobs. This is a table of all jobs, with the switch, schedule, location, platform and model of each job.
  - A links file has Links.
  - A keys file has Variables. This tab shows the names of the keys and what each key is for. It never shows a value.
  - A tests file has Tests.
  - Some agents have Capabilities.

  You can edit each of these tables. When you save a table, the file changes.

### Reading and editing a document

A Markdown file opens as a page of a book, on white paper or black paper. The page shows the number of words, the time to read and a Contents list of the headings. The reader has these controls:

- **Read and Source.** Read shows the document with its format. Source shows the numbered lines. When you click a line number, a comment form opens for that line.
- **Aa.** This control sets the font (Sans, Legible or Serif) and the size (S, M or L).
- **Light and Dark.** This control sets the paper, white or black. The browser keeps the selection.
- **Full screen.** The document fills the screen. On a wide screen, the Contents list is in a column on the side. A line at the top shows the progress. To close, push Close or Esc.
- **Edit in place.** Double-click a paragraph, a heading, a list or a table. On a phone, tap the block two times. You can then type in the block. The block keeps its appearance. Ctrl+B makes text bold and Ctrl+I makes text italic. To write only those lines into the file, push Save or Ctrl+Enter, or click outside the block. The page changes the block back to Markdown. Sometimes the browser makes a link while you type. For example, a Mac changes a file name such as `x.md` into a web address. The page saves such a link as plain text. To see the Markdown source of the block, push Markdown. To stop without a change, push Esc or Cancel. This also operates in full screen.
- **Edit.** This button opens the full file in an editor with numbered lines. Long lines go onto the next line at the edge of the screen. To save, push Save file or Ctrl+S. To stop, push Cancel.

The page records each save with the old text. Thus you can undo the save from How it works.

On the server of the owner, the file on the disk changes immediately. On claude.ai, the edit waits in the store of the page until the next sync.

After a save on claude.ai, the page also examines the related items. These are the parent folders and the items that refer to this item. If a related item must change, the page saves the change as "Related updates". You can undo all of these updates with one click. The page never changes the text of a different file. It never changes a How it works explanation.

### Comments

You can put a comment on one line. Use the line numbers. You can also put a comment on the full file or folder. Use the "Comment on" button.

Each comment keeps the text of its line. Thus the comment stays on the correct line when the file changes. If the line is not there, the comment tells you.

You can resolve, open again or delete a comment. The page does not show resolved comments until you ask for them.

At the sync, the agent applies a comment that asks for a change. Each other open comment becomes an open question on the item.

A comment is not the same as a note in the Notes and runs panel. A comment waits on its item for the sync. A note is for Claude Code, and it goes out as a run.

### The ask box

Each item has a box below its sheet. You can type a question or a request about the item in the box.

- To send, push Enter.
- To add a line, push Shift+Enter.
- Each item keeps its own conversation in the browser. To remove it, push Clear.
- On claude.ai, the page also keeps each message and its answer in its store as an owner input. Thus they go into the files at the next sync. On the server, the run that gets the message records it.

On claude.ai, the page asks Claude directly. You can select the model: Most capable, Balanced or Fastest. Claude reads the item, the knowledge that applies to it and its related items. Then Claude gives one of these replies:

- **An answer.** If the answer is permanent, the page also keeps it on the Questions tab of the item.
- **A draft.** If you ask for a change, the reply is a draft card. The card shows each item that changes. For each item, it shows each field that changes, with the old value and the new value.
  - To apply the draft immediately, push Save or type "save". The page marks the changed items.
  - To remove the draft, push Discard.
  - To change the draft first, ask more.
  - The card shows a new file, a new folder or a removal with a tag.
- **Save or discard.** Claude can also save or remove a draft when you tell it to do so in words.

On the server of the owner, a message in the box becomes a note in the Notes and runs panel. The note goes out immediately as its own run of Claude Code, on its own branch (refer to "Notes and runs"). The page does not keep a second copy of the message as a page input. The page has no model selection. The server settings select the model. The conversation shows these data:

- Each step that Claude Code does.
- Each step that waits for the owner, with an Allow button and a Refuse button.
- The answer, with its cost, its time and the number of changed files.

A second message in the same box continues the same conversation, on the same branch. Stop stops the request. When files change, the tree loads again. The box becomes larger with the text, to a maximum of half the screen.

On the server, a microphone button is next to the box. It records for a maximum of five minutes, with a timer. The recording becomes a note in the panel immediately. The server changes the recording into text and puts the text into the note. Examine and edit the text in the panel.

In other locations, the box tells you that the page only shows the files. A message goes to no one.

### Adding a file or folder

The Contents tab of a folder has "Add a file or folder". To add an item, do these steps:

1. Push "Add a file or folder".
2. Type the name. For a folder, put `/` at the end of the name.
3. Select the type.
4. Type one or two sentences about what the item is for.
5. Push Add.

The new item shows in the tree immediately. The page marks it as changed. At the sync, the agent makes the item on the disk, with its How it works file and its Details file. The item stays proposed until the owner agrees.

### Deleting and bringing back

The Delete button is next to the name of the item. It opens a short form. The form tells what the agent deletes. For a folder, it gives the number of items in the folder. The form has a box for an optional note to Claude. For example, the note can tell what to move or keep first. On the server, the note box also has the microphone button.

When you push "Delete and clean up", these things occur:

- **On the server of the owner,** Claude Code starts immediately, in the conversation of that item.
  1. It deletes that item and its metadata files. It does not ask for a second click for this step.
  2. It removes the item from these parts of the project: the links to it, the references to it in other files, and the How it works of the parent.
  3. It obeys the note.
  4. It records the deletion and commits the change.
- **On claude.ai,** the page marks the item as deleted immediately. The agent removes the item from the project at the next sync.

A deleted item stays in the tree until the sync. A line goes through its name. A message tells what occurs next. The item has a "Bring it back" button (on claude.ai, "Restore it").

On the server, "Bring it back" does the opposite steps. Claude Code restores the item from git. It also puts back all the parts that the cleanup removed.

### The "changed" mark and Apply changes

Now the page shows only one status: changed. This mark shows on each item that a request from the page changed. The mark stays until the next sync. These items get the mark:

- An edited item.
- An item with a note.
- An added item or a deleted item.
- An item with a request that waits in the box.
- On the server, each file that Claude Code changed for a request.

The Changed tab shows a list of these items.

Apply changes is at the top of the page. It puts all these changes into the files. Do these steps:

1. Push Apply changes. Read what occurs.
2. Push "Apply now".

Then these things occur:

- On claude.ai, the page puts one comment on itself and sends it to Claude. The page also keeps the request in its store. The Claude session that monitors the page does the sync and the build. It publishes the new tree. It answers the comment and resolves it. When the request is processed, the open page loads the new tree, or asks the owner to load the page again.
- If no Claude session monitors the page, or if comments are not permitted, the page keeps the request. It tells the owner to say "sync the file tree" in the project chat. You can cancel a request that waits.
- On the server of the owner, the button starts one Claude Code request with the same text. This request shows in the conversation of the top folder. When the request stops, the page loads the tree again.

When the owner says "sync the file tree" in the project chat, the result is the same as the button.

### On a phone

When the screen is narrower than 760 pixels, the page shows one area at a time. First it shows the tree. Then it shows the sheet of the item, with a "‹ Tree" button to go back.

No part of the page can be wider than the screen. In the reader, two taps on a block start an edit. This is the same as a double-click on a computer. The reader hides the labels of its buttons to save space.

### What the page keeps in the browser

The browser keeps these data:

- The open folders.
- The selected item and tab.
- The switches.
- The selection of Read or Source.
- The paper, font and size of the reader.
- The conversation of each item (its last 30 messages).
- Text in the box that you did not send.
- On the server, the open or closed state of the Notes and runs panel, and the send options.

The browser is not the only location for data that the owner must keep. The page keeps comments, edits, messages and notes in its store.

## Notes and runs

It is easy to lose a request that you say or type. The request goes into the conversation of one item. When a run stops, its steps go from view after the page loads again. On the server of the owner, the page keeps all of them in view.

Each note that the owner makes for Claude Code is one row in one panel. Each Claude Code run in this repository is also one row, from the page or from a terminal. The owner sees what waits, what operates and what is done. The owner can send many notes as one run. The owner can open each run and see what it did. The panel is only on the server page. On claude.ai and in other locations, the page does not show its button.

**The panel.** The Notes and runs button in the header opens the panel under the header. The page keeps the open or closed state. The panel has three tabs: All, Notes and Runs. It also has Refresh and Hide. The rows that need the owner are first. Then come the rows that are at work. Then come the other rows, the newest first. The panel shows ten rows at a time. A line shows, for example, "10 of 34". Show more shows ten more rows.

**How to make a note.** A note is a text that the owner types or says for Claude Code on the server page. There are four ways to make a note:

- Type in the box at the top of the panel. The box becomes larger with the text. To add the note, push Ctrl+Enter or Add note.
- Type a message in the ask box under an item. The message becomes a note, and the note goes out immediately as its own run.
- Push a microphone, in the panel or in the ask box. The recording becomes a note immediately, with the status transcribing. The server changes it into text. Then the owner edits the text in the panel.
- Select text on the sheet of an item. A small bar shows "Record about this" and "Note". The note keeps the selected text, its line, the tab and the item.

**The row of a note** shows these data: a checkbox, the status, the item, tags, the time and the text. When the checkbox is clear, Send all does not send the note. A click on the item opens it. The tags are, for example, "selection · line 12" and "voice".

The buttons of a note change with its status:

- Send after transcript, while the status is transcribing. The note then goes out automatically when its text is there.
- Edit, with Save and Cancel.
- Send.
- Open run.
- Cancel.
- Delete.
- Details.

Details show where the note came from: the ask box, the panel or a selection. They also show the item, the tab, the line and the selected text. They tell if the owner typed or said the note. They give the time, the page version and the run. They give the commit that the note was sent from and the commit in `main` that contains it. After a send, the row shows a line such as "sent at 3f2a1c9 · page v75 → in main at 8b0d2e4 · page v76".

**The statuses** are the same for notes and runs:

| Status | What it means |
|---|---|
| transcribing | The server changes the recording into text. |
| ready | The text is there. The owner can edit it, send it or keep it. |
| queued | It goes out automatically when its text is there. |
| sending | It goes to Claude Code now. |
| planning | Its run writes a plan before it builds. |
| working | Its run does the work. |
| need human | The run cannot continue without the owner. An Allow or Refuse waits, or the run asks a question. These rows are first. |
| need manual test | The run is done. It tells what a person must try. |
| done | The run is done, and its branch is ready. The branch is not in `main` yet. |
| in main | Its branch is merged into `main`. |
| failed | The recording or the run failed. The row tells why. |
| cancelled | The owner stopped it. |

A run tells how it stopped. The last line of its answer is "STATUS: done". It can also be "STATUS: need manual test:" with what to try, or "STATUS: need human:" with what it needs. When the server starts again, the notes and runs that were at work become failed.

**How to send.** Send all is at the bottom of the panel. It sends all the checked notes that are ready, together, as one run. Each note goes with its source and its selected text. Thus Claude Code knows the item of each note.

A folded line above Send all shows "Options: local · auto merge · related tests · bug check · report". It opens the send options. The page keeps them. The send options are:

- **Where:** Local makes a branch on this server. Cloud shows, but it is off. It comes later.
- **Merge:** Auto merge merges into `main` when the run is done. Ask me waits for the button of the owner.
- **Tests:** Related runs the build checks and the tests of the changed parts. The other values are All and None.
- **Check for bugs:** the run examines its own changes before it stops.
- **Report:** the run gives a short report at the end. The report tells what the owner asked, what changed, the checks and what is not done.

The defaults are Local, Auto merge, Related, Check for bugs on and Report on.

**Each run from the page operates on its own branch.** Without this rule, two runs at the same time change the same files. Also, a run that is not complete changes the files that the page shows.

For each run with notes, the server makes a branch with the name `ide/<date>-<subject>`. The branch starts from the last commit of `main`. The run gets its own checkout in `.worktrees/<run>/`. Claude Code operates and commits there. A second message from the same conversation continues on the same branch.

The server merges the branch in two cases: the run is done and the option is Auto merge, or the owner pushes Merge into main. Then the server does these steps:

1. It brings the branch up to date with `main`.
2. It moves `main` forward on the server.
3. It builds the page again.
4. It sets the notes and the run to in main.

The built files are different on each branch. These files are the page data, `real-files.json` and `docs/file-tree.md`. When a conflict is only in these files, the server builds them again. A conflict in a different file stops the merge with the status need human. The server does not push to GitHub.

The branch starts from the last commit. Thus page edits that are not committed yet are not in the branch. Delete and Apply changes still operate in the repository itself, not on a branch.

**The row of a run** shows these data: the status, the title, the tags, the source (page or terminal), the branch, the number of steps, the cost or the largest context, the time and the number of notes. Page runs show the cost. Terminal runs show the largest context. A click on the title opens the page of the run, and the panel closes. A run at work has Stop. A page run that is done and has a branch has Merge into main.

**Where the data is.** Each note is a small file in the `notes/` folder of the page store. Each run has a record in the log folder of the project IDE agent. Git does not keep the notes or the records. The run that gets a note records its words as an owner input, word for word.

A terminal run does not need a record. The server reads it from the transcripts of Claude Code for this repository. A terminal run is live while its transcript changed in the last 90 seconds. Terminal runs show no cost, because their transcripts do not contain a cost.

## The page of a run

Each run has its own page, from the page or from a terminal. The page of the run opens at the address `#run/<id>`. It fills the full page. The tree is hidden, the run uses the full width, and the full page scrolls as one. The ask box is hidden. "‹ Back" goes back to the tree and the item. The page of a run at work loads again each four seconds.

The top shows these data: the title, the status, page or terminal, the tags and the start folder. It also shows the branch, the start time, the length, the model, the cost, the largest context, the written tokens and the number of steps.

The page of a run has these buttons:

- Stop.
- Merge into main.
- Discard the branch. This removes the branch, without a merge.
- Make PR and Make PR and merge. These buttons show, but they are off. Pull requests come in a later step.
- Copy. This gives `claude --resume <session>`, to continue the run in a terminal.

The page of a run has these sections:

- **Summary.** It has four to ten sentences in ASD-STE100 and one to four tags. Claude Haiku writes them after each page run. It also writes them in the background for terminal runs that are done. Each summary costs about half a cent to one cent. Write it again asks for a new summary. The tags come from a fixed list: question, change, fix, docs, ui, server, setup, sync, plan, research, delete, failed, waiting. Haiku makes a new tag only when no tag in the list applies.
- **Request** and **Answer.** The first message and the last answer, in full.
- **Notes.** The notes of the run, with the source of each note.
- **Send options.** The options of the send.
- **Git.** The commit of the send and the commit in `main`. The branch and its commits. The changed files, with links to their items. The commits during the run. The current branch of the repository and its files that are not committed.
- **What it used.** Chips for the types of steps, the tools, skills, subagents, MCP servers, plugins, workflows and web pages. The files that it read and edited. A click on a chip shows only those steps.
- **Checks and tests.** The build checks and the tests of the run, with their results.
- **Plan.** The plan of the run, if the run wrote one.
- **Steps.** One row for each step, in sequence. Each row has an icon for the type of step: prompt, notification, text, read, edit, command, skill, subagent, MCP, web, workflow or other tool. It also has a summary of one line, the time, the duration and a small bar. The bar shows how much context the model had at that step. Click a row to see the input and the output of the step. A long text shows its start. "Show all of it" shows the remaining text. The step of a subagent opens into the steps of that subagent. Open all and Close all open or close all rows.

## The three places the page runs

The page finds its location when it loads.

| Location | How the page finds it | Where the page keeps the work of the owner | Who answers the box | Apply changes |
|---|---|---|---|---|
| claude.ai, as a published artifact | The artifact runtime is there | The store of the artifact: the collections `nodes`, `changes` and `inputs` | Claude, through the page. You can select the model. | One comment to the Claude session that monitors the page |
| The server of the owner | The server answers `api/health` | JSON files in the page store. Edits to a file and to How it works also go directly into their files. | Claude Code in the repository, step by step, with Allow and Refuse from the owner | One Claude Code request in the conversation of the top folder |
| A different location | No answer from the two | No location. The header shows "view only". | No one | Not shown |

The published page has one link: https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs. The agent always publishes the page again at this link. Thus the work of the owner in the store stays in its location.

The page asks for four runtime capabilities:

- Its store.
- Questions to Claude.
- The identity of the viewer.
- Comments to Claude.

**The page or the terminal.** The page and the terminal use the same Claude Code. They use the same `CLAUDE.md`, the same skills and the same files. In the terminal, the owner starts Claude Code in `agents/system/`. The owner gives the name of the item. Claude Code records the words of the owner and does the round as `CLAUDE.md` tells. Before a risky step, it asks the owner in the terminal. On the page, each note and each message is about one item. The page keeps it immediately, word for word, with its history and an undo. The item shows "changed" until the sync. On the server, the request box starts the same Claude Code, with Allow and Refuse. Use the page for work on one item. Use the terminal for work on many items. The tree shows work from the terminal only after the next build. But the run from the terminal shows immediately in the Notes and runs panel on the server, with its own page. A run from the page operates on its own branch. It goes into `main` when the server merges it. A run in the terminal operates where the owner started it.

## What the page reads

`file-tree.data.json` is the only data of the page. A script makes it. Do not edit it or merge it by hand.

The top level of the data contains:

- The version of the data.
- The time of the build.
- The top item.
- The decisions.
- The list of items.

Each item contains:

- Its identifier. The identifier is the path of the item from the top of the repository, for example `docs/README.md`. The identifier of the top is `agent-os`.
- Its name, path, type, parent and children.
- If it is a link, and its status.
- What it is for, from its Details file.
- Its How it works text, the state of that file and its path.
- Its Details and the path of its Details file.
- A note that its text loads later, and the source file of the text.
- Its example, its field guide and its other tabs.

`real-files.json` is next to the data. It contains the text of each file. The page loads it the first time that you open such a file. Thus the page stays small. On the server, the server reads the text from the disk again for each request.

## How the page is built and checked

The `ide-build` skill makes the page data from the repository, examines it and publishes it. Its only source is the files on the disk and the metadata files next to them. It reads no notes and it copies nothing. It operates at these times:

- After each round that changed a file, a folder or a metadata file.
- After a pull that brought changes.
- As the last step of each sync.

Its scripts are in `agents/system/.claude/skills/ide-build/scripts/`. All are Python with the standard library, but not the page check:

| Script | What it does |
|---|---|
| `index_files.py` | It lists the items: each file in git, the folders that contain them, and the local `.env` files. It does not read the `.env` files. It knows the location of each How it works file and each Details file. It reads and writes them. |
| `materialize.py` | It gives empty How it works and Details files to each new item. It keeps a `.gitkeep` in empty folders. It writes `docs/file-tree.md`. It copies nothing. |
| `build_map.py` | It examines the How it works files against their items. It finds the missing files and the stale files (children first), and the files that are still empty. It gives the context to write one file. It confirms a file. It writes many files at one time. It finds orphans (files whose item is gone). |
| `enrich.py` | It reads each item with its metadata files and other tabs. It applies the kept edits of the owner to the extra tables. It writes the page data and `real-files.json`. You give it the next data version. |
| `tabs.py` | It makes the field guides and the other tables (keys, jobs, links, tests, capabilities). `enrich.py` uses it. |
| `check_tree.py` | It makes sure that the items of the page are the files in git and their folders, and the local `.env` files. |
| `check_page.js` | It opens the page at the width of a desktop and at the width of a phone, with a substitute for the artifact runtime. It fails on a page error, on a missing tab, on an address that does not open its item, or if the page is wider than the phone. It needs Node and Playwright with Chromium. |

Do the build in this sequence:

1. Put the final page in its location first. The page shows its own source.
2. Run `materialize.py`.
3. Run `build_map.py --stale`. Give the stale How it works files to the `file-index` skill of the knowledge base agent, or confirm the files that are still correct.
4. Run `enrich.py` with the next data version. Run `materialize.py` again. If it made files, examine and run `enrich.py` again.
5. Run `build_map.py`. All How it works files must be fresh, none can be missing, and there must be no orphans.
6. Run `check_tree.py`. It must show "tree ok".
7. Run `check_page.js` on the top item, on the README and on each item that the round changed. Look at the screenshots of each change to the page itself. The script must show "page ok".
8. Publish at the same link. Put the data and `real-files.json` next to the page.
9. Tell the owner in plain words what changed on the page.

The build never makes a status. An item is decided, but not if its Details file tells that it is proposed or an idea. Each new item that an agent adds is proposed until the owner agrees. The data never contains a secret value.

## How the owner's work comes back

The page keeps all the work immediately. Thus the owner never waits. On claude.ai, the files change only at a sync. On the server, edits to a file and to How it works go into the files immediately.

The store of the page has three collections:

| Collection | One document for each | What it contains |
|---|---|---|
| `inputs` | Message from the page | The text. The item and the path where the owner sent it. Its type: question, answer, change, discard, delete, restore or apply. The answer of the page. Its status: `new` until a sync records it. An apply request also contains the number of items, the items, and if it went to Claude. |
| `nodes` | Item that the owner changed | The last value of each edited field (`content` for the text, `how_md` for How it works). The line comments, with the text of their lines. The questions with answers. A new item. A deletion, with the old item, the note of the owner and who does the cleanup. The mark of a server request that changed the item. |
| `changes` | Save | The history: the time, the person, the words of the owner, and for each item each field before and after. It also tells if someone did an undo. The agent never folds or removes this history. |

On claude.ai, these collections are in the store of the artifact. The agent reads them with the artifact data tool, on the link of the page. On the server, each document is one JSON file: `page-store/<collection>/<id>.json`. The server also keeps the notes of the Notes and runs panel there, one file for each note, in `page-store/notes/`. Git ignores this folder. The notes do not wait for a sync. The run that gets a note records its words as an owner input. Thus a sync examines only the notes that are ready and not sent.

The `ide-sync` skill puts them back into the files. It operates when the owner pushes Apply changes or says "sync the file tree". It always operates before `ide-build`. Do these steps:

1. Make a list of each new input and each changed item.
2. Record each one as an owner input, word for word, with its item. A message and the answer of the page are one input.
3. Write the edits into their files:
   - Write the text of a file into that file.
   - Write How it works into the `.index.md` of the item, word for word. Set the owner as the writer.
   - Make a new item on the disk, with its How it works file and its Details file.
   - Write each edit of an extra table into the kept page edits.
   - Remove a deleted item from the project. Obey the note of the owner.
4. Do the requests of the owner. Record each answer with its input.
5. Give the recorded inputs to the knowledge base agent. It puts them into the docs and the metadata files, and it updates the explanations.
6. Build and publish the page with `ide-build`.
7. Remove what is in the files now:
   - Mark each recorded input as processed.
   - Delete the folded item documents. This removes the "changed" marks.
   - For a round from Apply changes, mark its apply request as processed last. Thus the open page shows the new tree. Then answer the page comment and resolve it.
8. Tell the owner the result in two to five plain lines.

Obey these rules:

- Do not remove anything before it is in a file.
- Do not change or lose the words of the owner.
- If an edit is different from an earlier decision, ask the owner.
- If the owner put a key on the page, do not copy it to any location.

## The metadata files and the tabs

Each file and each folder has metadata files next to it. Their names are the name of the item without its extension.

| File | Tab | What it contains |
|---|---|---|
| `vision.index.md` | How it works | The plain explanation, below fixed headings. Its front matter tells what it explains, its item, when it was written and who wrote it. |
| `vision.meta.json` | Details | The details of the item as JSON (the fields in the Details tab above) |
| `vision.example.md` | Example | The structure of the file: its headings and one line about what goes below each |
| `vision.questions.md` | Questions | The open questions for the owner, and the questions that the owner asked about the file, with their answers |
| `vision.{type}.{name}.view.html` | Its own tab | A custom view for that type of file. This is proposed. It is not built. |

These rules apply to the names:

- A folder keeps its metadata files in it (`configs/configs.index.md`).
- A name without an extension stays complete (`.gitignore.index.md`).
- If a name is the same as the name of a sibling or of its folder, the file keeps its extension. Now only `apps/project-IDE/server/server.py` has this name: `server.py.index.md`.
- A metadata file has no metadata files.

Now each item has its How it works file and its Details file. The example files and the questions files are being written now, for the main docs and the keys files only. Other files get them later, when they need them.

The rule is: a tab shows only when its file exists, and the tab shows that file.

Each metadata file is its own source. Edit it where it is, next to its item. The build only gives empty How it works and Details files to a new item.

## The server

`server/` operates the same page on the machine of the owner, with Claude Code behind the request box.

You must have these items:

- The repository on the server, with permission to push.
- Python 3.10 or a newer version.
- Node.
- Claude Code: `npm install -g @anthropic-ai/claude-code`.
- The Python SDK `claude-agent-sdk`. `./init.sh` installs it into `.venv/` at the top of the repository. Git ignores `.venv/`.
- A sign-in for Claude Code. Put the key `ANTHROPIC_API_KEY` in the keys file `.secrets/test/.env`, or sign in to Claude Code one time with `claude` in a terminal.
- For voice, the key `GROQ_API_KEY` in the same keys file.

If the SDK is not installed, the page operates, but the request box is off. If the Groq key is not there, the microphone button does not show.

To install the server one time, do these steps:

1. Go to the top of the repository.
2. Type `./init.sh`.

`./init.sh` does these tasks:

- It examines the tools: git, curl, Python 3.10 or a newer version, Node and Claude Code.
- It makes `.venv/` with the SDK.
- It installs the systemd user service `project-ide`. The service starts the IDE when the machine starts. Lingering is on, so the service starts before a person logs in.
- At the end, it runs `./start.sh`.

You can run `./init.sh` again safely. `./init.sh --no-service` does not install the service.

To start or restart the IDE, type `./start.sh` at the top of the repository. `./start.sh` does four steps:

1. **Sync.** It gets the new commits from GitHub. If the branch is behind, it puts back the three built files: the page data, `real-files.json` and `docs/file-tree.md`. Then it moves the branch forward. It does this only if no other file has local changes and there are no local commits. If not, it does not pull, and it shows a warning. It never merges, stashes or pushes. It also tells how many items on the page have the "changed" mark. It does not sync these items. Apply changes or "sync the file tree" starts a Claude Code run for the sync.
2. **Stop.** It stops the service. It also stops a server that a person started by hand. It stops only a process that runs `apps/project-IDE/server/server.py`. It never stops another program on the port.
3. **Rebuild.** It runs `rebuild.py` from the build scripts. The page data gets a new data version only if a change occurred. Thus a restart without a change keeps git clean. `rebuild.py` writes no How it works file and publishes nothing.
4. **Start.** It starts the service. If there is no service, it starts a background process. It shows the output. It waits a maximum of two minutes for an answer from `api/health`. Then it shows the address and the tunnel command.

Other commands:

- `./start.sh --no-pull` does not do the sync.
- `./start.sh stop` stops the IDE.
- `./start.sh status` shows the state of the IDE.
- `./start.sh logs` shows the output of the IDE while it operates.
- `./start.sh serve` is the command that the service runs. It does the sync, the stop and the rebuild. Then it runs the server in the foreground.

If there is no service, the output and the process id go to `agents/system/logs/services/project-ide/`. Git ignores this folder.

The owner decided that these scripts start the IDE when the machine starts. Some details are a proposal. The owner did not decide them:

- the name of the service;
- the rule that a pull occurs only if the branch can move forward cleanly;
- the report of the items that wait on the page, instead of a sync;
- `.venv/` for the SDK.

You can also start the server by hand when the service is stopped. Type `python3 apps/project-IDE/server/server.py`. To stop it, push Ctrl+C.

To get access to the page from your computer, do these steps:

1. On your computer, open a tunnel: `ssh -N -L 8765:127.0.0.1:8765 you@your-server`.
2. Open `http://127.0.0.1:8765/` in the browser.
3. Make sure that the header shows "on your server".

WARNING: Do not open the port to the internet. A person who can get access to the page can make Claude Code change files and run commands.

The server listens only on the address of the machine, `127.0.0.1:8765`. It refuses all other addresses. It also refuses a request if its address or origin is not the address of the machine.

The server has three program files:

- `server.py` does these tasks:
  - It sends the page, its data and `real-files.json`. It reads the text of the real files from the disk again for each request.
  - It answers `api/health`.
  - It keeps the page store as JSON files (`api/store/<collection>`).
  - It writes an edit to the text of a file directly into the file that the page showed. It also writes the edit into the real file that the build made from a draft.
  - It writes an edit to How it works into the `.index.md` of the item, and into its copy on the disk. It sets the owner as the writer.
  - It never writes back a text that the page showed only in part.
  - It never writes again a field that it wrote before. Thus it cannot undo a change from Claude Code.
  - An edit to a planned file that is not written waits in the store until the sync.
  - It serves the Notes and runs panel: the list of notes and runs, and each note. A note can be made, edited, recorded, sent, cancelled or deleted.
  - It serves each run with its steps, and the full text of a long step. It also does the summary, the merge, the discard and the stop of a run.
  - Its health answer tells if the panel, the defaults of the send options and the summaries are available.
- `claude_bridge.py` does each request (`api/agent`, and each send of notes) as a Claude Code session. A run with notes starts in `.worktrees/<run>/agents/system/`, on its own branch. A Delete run and an Apply changes run start in `agents/system/` of the repository itself. The program sends each step to the page. It examines each step first:
  - It refuses each step that touches the keys folder.
  - It permits the deletion of the item that the owner deleted.
  - A file outside the checkout of the run waits for Allow or Refuse from the owner.
  - A tool or a command that is not on the allow list waits for Allow or Refuse from the owner.
  - If no one answers in fifteen minutes, it refuses the step.

  The program sets the status of the run and its notes while the run continues. It merges when the option is Auto merge. Stop operates also before Claude Code connects. Claude Code must obey the `CLAUDE.md` of the system. It must record the request, complete the round and never push. It must end with its `STATUS:` line. The program records each request with its steps, answer, cost and time.
- `notes.py` keeps the notes and the run records. It sorts the list of the panel. It puts notes together into one request. It reads the `STATUS:` line of a run.
- `runs.py` reads the transcripts of Claude Code for each session that started in the repository, with its subagents. It makes the run list and the page of a run. It does not copy data.
- `run_summary.py` asks Claude Haiku for the summary and the tags of each run. It operates from a folder outside the repository. Thus the call loads no project settings, and it never shows as a run.
- `worktrees.py` makes the branch and the worktree of each run. It merges a branch that is done into `main` on the server, and it builds the page again. It also removes or discards a branch.
- `voice.py` gets a recording: from `api/voice` for the delete note box, or the recording of a note. The server changes the recording of a note into text in the background. It sends the recording to the speech-to-text models of Groq, in sequence. If a model has a rate limit or an error, it uses the next model. It sends back the text. It does not keep the recording. The Groq key never goes to Claude Code or to the page.

The settings are in `server.config.json`. The file contains only the names of keys, never their values.

| Setting | What it does |
|---|---|
| `repo` | The top of the repository, relative to the folder of the server |
| `host`, `port` | Where the server listens. Only the address of the machine is permitted. |
| `page_dir`, `page`, `data` | The page and its data file |
| `store_dir` | The location of the page store |
| `write_through` | Writes edits to a file and to How it works directly into their files |
| `log_dir` | The location of the request records |
| `secrets.file`, `secrets.keys` | The keys file and the names of the keys to read from it |
| `voice` | The Groq address, the models in sequence, the key name, the limit of five minutes, the language |
| `claude.cwd` | Where Claude Code starts |
| `claude.model` | The model. If it is empty, Claude Code uses its default model. |
| `claude.max_turns`, `claude.max_budget_usd`, `claude.approval_timeout_s` | The limits for one request |
| `claude.allow` | The tools and commands that Claude Code can use without a question |
| `claude.ask_owner` | Words in a command that always wait for a click from the owner: push, reset, rebase, clean, delete, permission changes, installs, network tools |
| `claude.never` | Paths that nothing can touch: the keys folder |
| `send_options` | The defaults of the send options: where, merge, tests, bug check, report |
| `worktrees.folder`, `worktrees.main` | The location of the checkout of each run (`.worktrees`), and the branch where runs start and merge (`main`) |
| `runs.claude_config_dir`, `runs.live_seconds`, `runs.max_text`, `runs.summary_model` | The location of the transcripts of Claude Code, how long a terminal run is live, how much text of a step comes at one time, and the model for summaries |

The settings point to these locations:

- The page is in `apps/project-IDE/current-ui/`.
- The store is in `apps/project-IDE/data/page-store/`.
- The logs are in `agents/system/logs/subagents/project-ide-agent/`.
- Claude Code starts in `agents/system/`, or in `agents/system/` of the checkout of a run. Thus it loads the `CLAUDE.md`, the agents and the skills of the system as its own.

A How it works edit from the page goes into the `x.index.md` next to its item.

## Who looks after it

- **The project IDE agent,** `agents/system/.claude/agents/project-ide-agent.md`, does these tasks:
  - It builds and publishes the page (`ide-build`).
  - It puts the work of the owner on the page back into the files (`ide-sync`).
  - It does the requests of the owner from the page.
  - It deletes items fully.

  On the server, it can be the Claude Code session behind the box. It never edits the page data by hand. It never loses the words of the owner. It never puts a secret value in any location. It never pushes without a click from the owner.
- **The knowledge base agent** keeps the knowledge. It writes the docs and each How it works file (`file-index`). If the two agents do not agree about a file, the files and their metadata are correct. The agent builds the page again from them.
- **The owner** can change all items on the page. The agents keep the edits of the owner to How it works word for word.

## Tests and checks

- Before each publication, `check_page.js` must show "page ok" at the width of a desktop and of a phone.
- `build_map.py` must tell you that all How it works files are fresh, none are missing, and there are no orphans.
- The tree must be equal to the files in git.
- After a sync, each new input from the page must be in the inputs folder with its answer. Each How it works edit must be in its file, word for word. The store must contain only the history and the items that the agent kept intentionally.
- We tested the server on a copy of the repository. We tested these functions: the store as files, the write to the files, a real Claude Code request, Allow and Refuse, a deletion with a note, and a restore.
- We tested the server on the server of the owner with `./start.sh`. The health check answers. A restart stops the old server and a server that a person started by hand. A second start keeps the data version. The page store saves and reads a note.
- `check_page.js` operates on the server of the owner when the system libraries of Chromium are installed. The command is `sudo npx playwright install-deps chromium`. Only the owner can run it.
- We tested the Notes and runs panel and the page of a run on the server of the owner. `check_page.js` shows "page ok". A browser test of the panel and a page of a run passed: at the width of a desktop in light, and at the width of a phone in dark. No part was wider than the screen. A real run with two notes stopped with done, and the server merged it into `main`. A Stop immediately after a send stopped the run with cancelled, at no cost. The summary of a small run cost less than half a cent.

## Where each part's docs are

| Part | Its docs | What they add |
|---|---|---|
| The IDE as a whole | `apps/project-IDE/project-IDE.index.md` | The How it works of the folder |
| The page | `apps/project-IDE/current-ui/file-tree-explorer.index.md` | The How it works of the page |
| The page data | `apps/project-IDE/current-ui/file-tree.data.index.md` | What the data file contains |
| The server | `apps/project-IDE/server/README.md` | Installation, start with `init.sh` and `start.sh`, notes and runs, the branch of each run, and safety, step by step |
| Notes, runs and their branches | `apps/project-IDE/server/server.index.md` and the How it works files of `notes.py`, `runs.py`, `run_summary.py` and `worktrees.py` next to them | What each file keeps or reads, and who uses it |
| The knowledge and the records | `apps/project-IDE/data/README.md` | How the knowledge is kept: layers, tags, the flow |
| The build | `agents/system/.claude/skills/ide-build/SKILL.md` and `scripts/README.md` | The build steps and the options of each script |
| The sync | `agents/system/.claude/skills/ide-sync/SKILL.md` | Each step from the page back into the files |
| The agent | `agents/system/.claude/agents/project-ide-agent.md` | Its tasks, when it operates and its rules |
| The How it works files | `agents/system/.claude/skills/file-index/SKILL.md` | Their format and how they are kept |
| Rebuilding the IDE | `apps/project-IDE/docs/rebuild-prompt.md` | The exact specification for an AI |

## Still open in the design

**Stage one, the work to complete the IDE:**

- Make a custom view for each type of file. For example, one shared view for all skills. The current other tabs become shared views. The location of the shared views is not decided. We propose `apps/project-IDE/views/`.
- Make the metadata correct on each item. Fill each Details file with correct data. Keep each How it works file current.

**Other subjects:**

- We propose a routine that examines the page store on a schedule. Then the owner does not have to push Apply changes.
- It is not decided how the page on claude.ai gets the changes from the server.
- Add more statuses for items than "changed" when the owner asks for them. Notes and runs have their own statuses.
- Pull requests from a run (Make PR, Make PR and merge) are the next step of the plan for notes and runs. They are not built. It is not decided when to build them. Until then, a merge occurs only on the server, and nothing goes to GitHub.
- The Cloud send option shows, but it is off. A run of notes in a cloud session needs its own plan.
- The branch of a run starts from the last commit of `main`. Thus page edits that are not committed are not in the branch.
- It is not decided if git keeps the run records. Now they stay in the logs folder, out of git. This is a proposal.
