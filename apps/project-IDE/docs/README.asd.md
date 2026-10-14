This is the ASD-STE100 version of `README.md`. `README.md` is the source. If the two documents are different, use `README.md`.

# The project IDE

## In short

The project IDE is the window of the owner on the Agent OS. The owner builds the system by vibecoding. The owner tells what they want in plain words, and AI writes the plans, the docs and the code.

The IDE shows the full project as one tree of all folders and files. The owner can click each folder and each file. For each item, the IDE tells what the item is, how it works, what it contains and which questions are open.

The owner reads, edits, comments, asks and deletes on the page. AI then puts all the work of the owner into the files. The same tree gives each AI the full context that it must have to make exact changes.

The IDE operates now. The page is published on claude.ai, and the owner uses it. The build and the checks operate. The server puts Claude Code behind the page. The server is written, and we tested it on a copy of the repository.

The completion of the IDE is stage one of the project. Stage one has three tasks:

1. Make a view for each type of file.
2. Make the metadata correct on each item.
3. Show a tab only for a metadata file that exists.

This document is the full manual of the IDE. It gives each part of the page and how to use it. It gives the three locations where the page operates. It tells how the build makes the page and how the checks examine it. It tells how the work of the owner goes back into the files. It gives the metadata files behind the tabs. It tells how to operate the IDE on a server. It tells where each part is now and where each part goes later.

The vision tells why the IDE exists and how it must operate. The vision is `apps/project-IDE/docs/vision.md`.

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

| Part | What it is for | Where it is now, while we plan | Where it goes in the final layout |
|---|---|---|---|
| The page | The tree, the tabs, edits, notes, questions, the ask box | `vision/explorer/file-tree-explorer.html` | `apps/project-IDE/current-ui/file-tree-explorer.html` |
| The page data | All the data that the page shows. The build makes it from the repository. | `vision/file-tree.data.json`, with a copy in `vision/explorer/` | `apps/project-IDE/current-ui/file-tree.data.json` |
| The text of the real files | The text of each real file. The page loads it when the owner opens the file. | `vision/explorer/real-files.json` | Next to the page data |
| The build scripts | They make the data, keep the files the same as their drafts and metadata, and examine the page | `vision/tools/` | `agents/system/.claude/skills/ide-build/scripts/` |
| The kept page edits | Values that the owner set on the page. The build applies them. | `vision/tools/overrides.json` | `apps/project-IDE/data/overrides.json` |
| The tree notes and the knowledge | One section for each file and folder; topic notes, decisions, inputs, changelog | `vision/docs/` | `apps/project-IDE/data/` and `agents/system/docs/` |
| The How it works files and the Details files | One explanation file and one details file for each item | `vision/tree/agent-os/...`, with a copy next to each item on the disk | Next to each item |
| The server | The page on the machine of the owner, with Claude Code behind it | `vision/server/` | `apps/project-IDE/server/` |
| The page store on the server | The notes, edits and messages of the owner, as JSON files | `vision/page-store/` | `apps/project-IDE/data/page-store/` |
| The project IDE agent and its skills | They build the page and put the work of the owner back into the files | `vision/.claude/agents/`, `vision/.claude/skills/ide-build/`, `ide-sync/` | `agents/system/.claude/agents/`, `agents/system/.claude/skills/` |

The parts connect in one loop:

1. The build reads the repository and writes the page data.
2. The page shows the data.
3. The owner works on the page. The page keeps all the work in its store immediately.
4. The owner pushes Apply changes, or the owner says "sync the file tree".
5. The project IDE agent reads the store. It writes each edit into its file. It records each note and each request as an owner input. It removes the deleted items. It builds the page again.
6. The knowledge base agent puts the new inputs into the docs and updates the explanations.
7. The build makes the page one more time.

On the server of the owner, the loop is shorter. The edits go into the files immediately, and the requests start immediately.

## How it is laid out

While we plan the system, the IDE operates from the planning folder `vision/`. The build makes the copies of its files in other locations of the repository. This is the final layout:

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
    ├── sources/                  the notes behind each doc for people
    ├── page-store/               on the server: the page's notes, edits and messages
    ├── overrides.json            the owner's page edits kept in the page data
    ├── memory/, plans/, archive/ working notes, change plans, retired files
```

Each file and each folder in this layout has its How it works file and its Details file next to it. This rule applies to all the repository. The project IDE agent and its two skills are in `agents/system/.claude/`, with the other helpers of the system. The build scripts are in the `ide-build` skill.

Now the repository has these folders. It also has copies of the page, the server files and the build scripts. But the working sources are still in `vision/`:

- The page is in `vision/explorer/`.
- The scripts are in `vision/tools/`.
- The server is in `vision/server/`.
- The tree notes and the knowledge are in `vision/docs/`.

The copy of the page data in `apps/project-IDE/current-ui/` is empty. The build does not write to it yet. When the planning stops, the sources move into the final layout. Then the paths in the server settings and in the scripts change.

## The page

The page is one HTML file, `file-tree-explorer.html`. It reads one data file, `file-tree.data.json`. The page does not need a build step. It does not load code from other locations. It loads only its fonts.

The page has three areas:

- The header, at the top.
- The tree, on the left side.
- The sheet of the selected item, on the right side. The ask box is under the sheet.

### The header

- **The title and the version line.** The version line shows the version of the tree notes and the number of items. Then it shows where the page operates: "on your server", "view only", or no text on claude.ai.
- **Apply changes.** This button shows when the page has changed items. It shows the number of changed items. It opens a short confirmation. Then it puts all the changes into the files (refer to "The changed mark and Apply changes"). While a request waits, the button shows "Applying changes", and you cannot push it again.
- **The filter.** When you type, the tree shows only the items that agree with the text:
  - A number, for example `27` or `[27]`, finds items by their number in the tree notes.
  - A text with `*` finds names that agree with the pattern, for example `*.json`.
  - A text with `/` finds paths, for example `agents/system/`.
  - Other text finds a part of a name. For example, `.md` finds all Markdown files.

  The folders above each found item open automatically. A line under the tabs gives the number of found items. A button on that line removes the filter.

### The tree

- **All and Changed.** All shows the full tree. Changed shows only the items that are changed since the last sync. Each item shows the reason.
- **The metadata switch.** When the switch is on, each file shows its two metadata files as rows below it. These are the How it works file (`vision.index.md` for `vision.md`) and the Details file (`vision.meta.json`). Each folder shows its two metadata files first, in the folder. When you click a metadata row, the related tab of its item opens. When the switch is off, the tree does not show metadata files. This includes the real metadata files on the disk. The switch is on by default.
- **The empty filter.** When the filter is on, the tree shows only the files that have no text yet. Each of these files has the mark "empty". The tree always shows the files on the disk.
- **The rows.** Each row has an icon and the name. If applicable, a row also has a "changed" tag and the number of the item in the tree notes. The icon shows a folder, a file or a link. When you click a closed folder one time, it opens and you select it. The arrow keys move in the tree. They also open and close folders. The browser keeps the open folders and the selected item. The address of the page contains the selected item. Thus a link opens the same item.
- **Deleted items.** A deleted item stays in its location until the next sync. A line goes through its name.

### The sheet of an item

The top of the sheet shows these data:

- The path, with a link to each folder above the item.
- The number and the name of the item.
- A "Changed" chip with the reason, if the item is changed.
- The type of the item: file, folder, file link or folder link.
- A Delete button. All items have it, but not the top item.
- One line that tells what the item is for.

The tabs of the item are below these data.

### The tabs

The first tab is always How it works. The last tab is always Details. Between them, a file has File, Example and Questions. A folder has Contents and Questions. Some items have more tabs.

- **How it works.** This tab shows the explanation of the item. The page reads it from the file of the item: `vision.index.md` next to `vision.md`, or `configs/configs.index.md` in a folder. The name of that file is at the top, with an Edit button.
  - Items in the new format show fixed headings: What it is, Who looks after it, When and how it changes, Who uses it and when, Where it is mentioned, Related knowledge. Then they show a short "Keep in mind" list.
  - Items in the old format show one Summary. They also show the knowledge that applies to the item directly and from the folders above. They show the notes of the item from the tree notes, and the owner inputs that had an effect on the item.
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
- **Questions.** This tab shows the open questions about the item. Each question has a Discuss button. This button starts a conversation in the ask box. The tab also shows the questions that have an answer on the page, with their answers. A folder also shows the open questions of the files in it.
- **Details.** This tab shows the Details file of the item, `vision.meta.json`, as it is. The Details file contains these data:
  - What the item is, and its state.
  - If it is in git, if it is secret, and if a script makes it.
  - Who writes it, who reads it, and when it changes.
  - Its related items, and what must change with it.
  - What it gets from the levels above.
  - Its sources, features and views, and its number in the tree.

  Now most Details files are empty templates.
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
- **Edit in place.** Double-click a paragraph, a heading, a list or a table. On a phone, tap the block two times. You can then type in the block. The block keeps its appearance. Ctrl+B makes text bold and Ctrl+I makes text italic. To write only those lines into the file, push Save or Ctrl+Enter, or click outside the block. The page changes the block back to Markdown. To see the Markdown source of the block, push Markdown. To stop without a change, push Esc or Cancel. This also operates in full screen.
- **Edit.** This button opens the full file in an editor with numbered lines. Long lines go onto the next line at the edge of the screen. To save, push Save file or Ctrl+S. To stop, push Cancel.

The page records each save with the old text. Thus you can undo the save from How it works.

On the server of the owner, the file on the disk changes immediately. On claude.ai, the edit waits in the store of the page until the next sync.

After a save on claude.ai, the page also examines the related items. These are the parent folders and the items that refer to this item. If a related item must change, the page saves the change as "Related updates". You can undo all of these updates with one click. The page never changes the text of a different file. It never changes a How it works explanation.

### Notes

You can put a note (a comment) on one line. Use the line numbers. You can also put a note on the full file or folder. Use the "Comment on" button.

Each note keeps the text of its line. Thus the note stays on the correct line when the file changes. If the line is not there, the note tells you.

You can resolve, open again or delete a note. The page does not show resolved notes until you ask for them.

At the sync, the agent applies a note that asks for a change. Each other open note becomes an open question on the item.

### The ask box

Each item has a box below its sheet. You can type a question or a request about the item in the box.

- To send, push Enter.
- To add a line, push Shift+Enter.
- Each item keeps its own conversation in the browser. To remove it, push Clear.
- The page also keeps each message and its answer in its store as an owner input. Thus they go into the files at the next sync.

On claude.ai, the page asks Claude directly. You can select the model: Most capable, Balanced or Fastest. Claude reads the item, the knowledge that applies to it and its related items. Then Claude gives one of these replies:

- **An answer.** If the answer is permanent, the page also keeps it on the Questions tab of the item.
- **A draft.** If you ask for a change, the reply is a draft card. The card shows each item that changes. For each item, it shows each field that changes, with the old value and the new value.
  - To apply the draft immediately, push Save or type "save". The page marks the changed items.
  - To remove the draft, push Discard.
  - To change the draft first, ask more.
  - The card shows a new file, a new folder or a removal with a tag.
- **Save or discard.** Claude can also save or remove a draft when you tell it to do so in words.

On the server of the owner, the box sends the request to Claude Code in the repository (refer to "The server"). The page has no model selection. The server settings select the model. The conversation shows these data:

- Each step that Claude Code does.
- Each step that waits for the owner, with an Allow button and a Refuse button.
- The answer, with its cost, its time and the number of changed files.

A second message in the same box continues the same conversation. Stop stops the request. When files change, the tree loads again.

On the server, a microphone button is next to the box. It records for a maximum of five minutes, with a timer. The server changes the recording into text. The page adds the text to the box. Examine the text before you send it.

In other locations, the box tells you that the page only shows the files. A message goes to no one.

### Adding a file or folder

The Contents tab of a folder has "Add a file or folder". To add an item, do these steps:

1. Push "Add a file or folder".
2. Type the name. For a folder, put `/` at the end of the name.
3. Select the type.
4. Type one or two sentences about what the item is for.
5. Push Add.

The new item shows in the tree immediately. The page marks it as changed. At the sync, the item gets its number, its section in the tree notes and its How it works file. The item stays proposed until the owner agrees.

### Deleting and bringing back

The Delete button is next to the name of the item. It opens a short form. The form tells what the agent deletes. For a folder, it gives the number of items in the folder. The form has a box for an optional note to Claude. For example, the note can tell what to move or keep first. On the server, the note box also has the microphone button.

When you push "Delete and clean up", these things occur:

- **On the server of the owner,** Claude Code starts immediately, in the conversation of that item.
  1. It deletes that item and its metadata files. It does not ask for a second click for this step.
  2. It removes the item from these parts of the project: the tree notes, the links to it, the references to it in other files, the How it works of the parent, and the knowledge map.
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

The browser is not the only location for data that the owner must keep. The page keeps notes, edits and messages in its store.

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

## What the page reads

`file-tree.data.json` is the only data of the page. A script makes it. Do not edit it or merge it by hand.

The top level of the data contains:

- The version of the data and the version of the tree notes.
- The time of the build.
- The top item.
- The decisions.
- The knowledge entries, each with the items that it applies to.
- The owner inputs, by identifier.
- The docs, the feature areas and the retired numbers.
- The list of items.

Each item contains:

- Its identifier. An item in the tree notes has an identifier like `n-53.4.2`. A real file that the build found on the disk has an identifier like `r-...`.
- Its number, name, path, type, parent and children.
- If it is a link. If it is on the disk, or if the scan found it.
- What it is for, and its summary.
- Its How it works text and the path of its How it works file.
- Its Details and the path of its Details file.
- The family name for its metadata files.
- Its text, or a note that the text loads later, and the source file of the text.
- Its example, its field guide and its other tabs.
- Its open questions and the questions with answers.
- The knowledge that applies to it.

`real-files.json` is next to the data. It contains the text of each real file that the build found on the disk. The page loads it the first time that you open such a file. Thus the page stays small. On the server, the server reads the text from the disk again for each request.

## How the page is built and checked

The `ide-build` skill makes the page data from the repository, examines it and publishes it. It operates at these times:

- After each round that changed the tree notes, a doc, a draft or a How it works file.
- After a pull that brought changes.
- As the last step of each sync.

These are its scripts. All are Python with the standard library, but not the page check:

| Script | What it does |
|---|---|
| `parse.py` | It reads the tree notes, the feature map and the decisions into a list of items. |
| `enrich.py` | It adds the drafts, examples, knowledge, How it works files, Details files and the other tabs. It adds each real file in git below each folder that exists. It applies the kept page edits of the owner. It writes the page data and `real-files.json`. You give it the next data version. |
| `tabs.py` | It makes the field guides and the other tables (keys, jobs, links, tests, capabilities). `enrich.py` uses it. |
| `materialize.py` | It keeps the files on the disk the same as their sources in `vision/`. It copies each draft to its real file. It copies the How it works and Details files next to each item. It gives empty metadata files to all other items. It does not make files from the plan. |
| `index_files.py` | It knows the location of each How it works file and each Details file. It reads and writes them. It makes the missing Details files. |
| `build_map.py` | It makes the knowledge map and examines the How it works files. It finds the missing files and the stale files (children first). It gives the context to write one file. It confirms a file. It writes many files at one time. It finds orphans (files whose item is gone). |
| `check_page.js` | It opens the page at the width of a desktop and at the width of a phone, with a substitute for the artifact runtime. It fails on a page error, on a missing tab, or if the page is wider than the phone. It needs Node and Playwright with Chromium. |

Do the build in this sequence:

1. Put the final page in its location first. The page shows its own source.
2. Parse the tree notes. Then run `enrich.py` with the next data version.
3. Run `materialize.py`. If it made new files, run `enrich.py` again.
4. Copy the data next to the page.
5. Run `build_map.py`. Do this until it tells you that all How it works files are fresh, none are missing, and there are no orphans. Give the stale files to the `file-index` skill of the knowledge base agent.
6. Run `check_page.js` on the top item, on the README and on each item that the round changed. Look at the screenshots of each change to the page itself. The script must show "page ok".
7. Make sure that the tree is equal to the files in git. The items of the page must be the paths that `git ls-files` gives, and the local `.env` files. Now we do this check path by path when the tree changes. There is no script for it yet.
8. Publish at the same link. Put the data and `real-files.json` next to the page.
9. Tell the owner in plain words what changed on the page.

The build never makes a status. An item is decided, but not if its notes tell that it is proposed. Each new item that an agent adds is proposed until the owner agrees. The data never contains a secret value.

## How the owner's work comes back

The page keeps all the work immediately. Thus the owner never waits. On claude.ai, the files change only at a sync. On the server, edits to a file and to How it works go into the files immediately.

The store of the page has three collections:

| Collection | One document for each | What it contains |
|---|---|---|
| `inputs` | Message from the page | The text. The item and the path where the owner sent it. Its type: question, answer, change, discard, delete, restore or apply. The answer of the page. Its status: `new` until a sync records it. An apply request also contains the number of items, the items, and if it went to Claude. |
| `nodes` | Item that the owner changed | The last value of each edited field (`content` for the text, `how_md` for How it works). The line comments, with the text of their lines. The questions with answers. A new item. A deletion, with the old item, the note of the owner and who does the cleanup. The mark of a server request that changed the item. |
| `changes` | Save | The history: the time, the person, the words of the owner, and for each item each field before and after. It also tells if someone did an undo. The agent never folds or removes this history. |

On claude.ai, these collections are in the store of the artifact. The agent reads them with the artifact data tool, on the link of the page. On the server, each document is one JSON file: `page-store/<collection>/<id>.json`.

The `ide-sync` skill puts them back into the files. It operates when the owner pushes Apply changes or says "sync the file tree". It always operates before `ide-build`. Do these steps:

1. Make a list of each new input and each changed item.
2. Record each one as an owner input, word for word, with its item. A message and the answer of the page are one input.
3. Write the edits into their files:
   - Write the text of a file into that file.
   - Write How it works into the `.index.md` of the item, word for word. Set the owner as the writer.
   - Write a new item into the tree notes, with its How it works file.
   - Write each other field into the kept page edits.
   - Remove a deleted item from the project. Obey the note of the owner.
4. Do the requests of the owner. Record each answer with its input.
5. Give the recorded inputs to the knowledge base agent. It puts them into the notes and the docs, and it updates the explanations.
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

The rule is: a tab shows only when its file exists, and the tab shows that file. Now the page still shows Example and Questions on each file, from the tree notes. The change to real files is stage one work.

While we plan, the How it works files and the Details files are in the mirror `vision/tree/agent-os/...`, or next to a draft in `vision/`. The build copies them next to each item on the disk.

## The server

`server/` operates the same page on the machine of the owner, with Claude Code behind the request box.

You must have these items:

- The repository on the server, with permission to push.
- Python 3.10 or a newer version.
- Node.
- Claude Code and its SDK: `npm install -g @anthropic-ai/claude-code` and `pip install claude-agent-sdk`.
- A sign-in for Claude Code. Put the key `ANTHROPIC_API_KEY` in the keys file `.secrets/test/.env`, or sign in to Claude Code one time with `claude` in a terminal.
- For voice, the key `GROQ_API_KEY` in the same keys file.

If the SDK is not installed, the page operates, but the request box is off. If the Groq key is not there, the microphone button does not show.

To start the server, do these steps:

1. Go to the top of the repository.
2. While we plan, type `python3 vision/server/server.py`. Later, type `python3 apps/project-IDE/server/server.py`.
3. On your computer, open a tunnel: `ssh -N -L 8765:127.0.0.1:8765 you@your-server`.
4. Open `http://127.0.0.1:8765/` in the browser.
5. Make sure that the header shows "on your server".

To stop the server, push Ctrl+C.

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
- `claude_bridge.py` does each request (`api/agent`) as a Claude Code session. The session starts in the folder that the settings give. The program sends each step to the page. It examines each step first:
  - It refuses each step that touches the keys folder.
  - It permits the deletion of the item that the owner deleted.
  - A file outside the repository waits for Allow or Refuse from the owner.
  - A tool or a command that is not on the allow list waits for Allow or Refuse from the owner.
  - If no one answers in fifteen minutes, it refuses the step.

  Claude Code must obey the `CLAUDE.md` of the system. It must record the request, complete the round and never push. The program records each request with its steps, answer, cost and time.
- `voice.py` gets a recording (`api/voice`). It sends the recording to the speech-to-text models of Groq, in sequence. If a model has a rate limit or an error, it uses the next model. It sends back the text. It does not keep the recording. The Groq key never goes to Claude Code or to the page.

The settings are in `server.config.json`. The file contains only the names of keys, never their values.

| Setting | What it does |
|---|---|
| `repo` | The top of the repository, relative to the folder of the server |
| `host`, `port` | Where the server listens. Only the address of the machine is permitted. |
| `page_dir`, `page`, `data` | The page and its data file |
| `store_dir` | The location of the page store |
| `write_through` | Writes edits to a file and to How it works directly into their files |
| `log_dir` | The location of the request records |
| `planning_dir` | While we plan, the folder that contains the drafts and the How it works files |
| `secrets.file`, `secrets.keys` | The keys file and the names of the keys to read from it |
| `voice` | The Groq address, the models in sequence, the key name, the limit of five minutes, the language |
| `claude.cwd` | Where Claude Code starts |
| `claude.model` | The model. If it is empty, Claude Code uses its default model. |
| `claude.max_turns`, `claude.max_budget_usd`, `claude.approval_timeout_s` | The limits for one request |
| `claude.allow` | The tools and commands that Claude Code can use without a question |
| `claude.ask_owner` | Words in a command that always wait for a click from the owner: push, reset, rebase, clean, delete, permission changes, installs, network tools |
| `claude.never` | Paths that nothing can touch: the keys folder |

While we plan, the settings point to `vision/`:

- The page is in `vision/explorer/`.
- The store is in `vision/page-store/`.
- The records are in `vision/logs/project-ide-agent/`.
- Claude Code starts in `vision/`. There it loads the planning copy of the agents, skills and `CLAUDE.md` of the system.

In the final layout, Claude Code starts in `agents/system/`. Thus it loads the `CLAUDE.md`, the agents and the skills of the system as its own.

## Who looks after it

- **The project IDE agent,** `agents/system/.claude/agents/project-ide-agent.md`, does these tasks:
  - It builds and publishes the page (`ide-build`).
  - It puts the work of the owner on the page back into the files (`ide-sync`).
  - It does the requests of the owner from the page.
  - It deletes items fully.

  On the server, it can be the Claude Code session behind the box. It never edits the page data by hand. It never loses the words of the owner. It never puts a secret value in any location. It never pushes without a click from the owner.
- **The knowledge base agent** keeps the knowledge. It writes the docs and each How it works file (`file-index`). If the two agents do not agree about a file, the files and the notes are correct. The agent builds the page again from them.
- **The owner** can change all items on the page. The agents keep the edits of the owner to How it works word for word.

## Tests and checks

- Before each publication, `check_page.js` must show "page ok" at the width of a desktop and of a phone.
- `build_map.py` must tell you that all How it works files are fresh, none are missing, and there are no orphans.
- The tree must be equal to the files in git.
- After a sync, each new input from the page must be in the inputs folder with its answer. Each How it works edit must be in its file, word for word. The store must contain only the history and the items that the agent kept intentionally.
- We tested the server on a copy of the repository. We tested these functions: the store as files, the write to the files, a real Claude Code request, Allow and Refuse, a deletion with a note, and a restore.

## Where each part's docs are

| Part | Its docs | What they add |
|---|---|---|
| The IDE as a whole | `apps/project-IDE/project-IDE.index.md` | The How it works of the folder |
| The page | `apps/project-IDE/current-ui/file-tree-explorer.index.md` | The How it works of the page |
| The page data | `apps/project-IDE/current-ui/file-tree.data.index.md` | What the data file contains |
| The server | `apps/project-IDE/server/README.md` | Installation, start and safety, step by step |
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
- Make the tabs real files. Show Example and Questions only where `x.example.md` and `x.questions.md` exist. Show an ASD-STE100 tab on a README that has a `README.asd.md`. The page must read each tab from its file.

**Other subjects:**

- Move the working sources from `vision/` into the final layout. Point the server settings and the scripts to the new paths. The copy of `server.config.json` in `apps/project-IDE/server/` still contains the planning paths.
- `materialize.py` is not yet in the copies of the build scripts in `agents/system/.claude/skills/ide-build/scripts/`.
- Write a script that compares the tree with `git ls-files`.
- We propose a routine that examines the page store on a schedule. Then the owner does not have to push Apply changes.
- It is not decided how the page on claude.ai gets the changes from the server.
- Add more statuses than "changed" when the owner asks for them.
