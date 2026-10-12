# The project IDE: vision

## In short

The project IDE is the owner's window on the Agent OS. The owner builds the system by vibecoding: they say what they want in plain words, and AI writes the plans, the docs and the code. That work quickly becomes too large to hold in one head, so the IDE shows the whole project as one clickable tree of every folder and file, and next to each one says what it is, how it works, what it holds and what is still open. The owner reads, edits, comments, asks and deletes right there, and AI brings everything they leave back into the files. The same tree, with the same explanations, gives every AI that works on the project the full context it needs to change things precisely.

## What it is for and who uses it

The IDE has two kinds of users.

- **The owner.** They use it to understand the project, watch it change, steer it and later analyse how the system is doing. They do not need to open a terminal or read code to know what exists and why: every item explains itself in plain words, and every change they want can be said or typed next to the item it is about.
- **Every AI working on the project.** Before an AI changes a file, it needs to know what the file is for, what depends on it, what must change with it and which rules from the levels above apply to it. The IDE gathers exactly that for every item, so a change lands everywhere it should and nothing is broken by accident.

## Why we have it

Without it, a project built by AI drifts away from its owner. Files appear that nobody asked for, explanations go stale, and the owner learns about a change only when something stops working. A plain folder listing does not help: it shows names, not purposes.

The IDE fixes this with three promises:

1. **The tree on the page is the real project.** It shows exactly the files that are in the repository, nothing invented and nothing missing. Planned items that do not exist yet are hidden unless the owner asks to see them.
2. **Every item explains itself.** Each file and folder has its own short explanation, written for someone who sees the project for the first time, and its own record of details: who writes it, who reads it, what it relates to and what must change with it.
3. **Nothing the owner writes is lost.** Every note, edit, question and deletion is saved the moment it is made, and AI later carries it into the files word for word.

## How it should work for us

The owner opens the page and finds any item by clicking through the tree or by typing part of a name, a path or a file type. An item opens on its explanation. From there the owner can read the file itself, which opens like a page of a book when it is a document, see an example of what the file should hold, read and answer its open questions, and look at its details.

When the owner wants something changed, they have three ways to say it:

- **Edit in place.** A double-click on a paragraph of a document opens that paragraph for editing; the whole file can be edited too.
- **Leave a note.** A comment on one line, or on the whole file or folder.
- **Ask.** A box under every item takes a question or a request in plain words. A question gets an answer, which is kept with the item. A request gets a draft of the changes, which the owner checks and saves.

Everything the owner does is marked "changed". When they are ready, one button at the top, Apply changes, hands it all to AI: AI writes the edits into their files, files every note and request as an owner input, cleans up what was deleted, rebuilds the page and shows the new tree.

The IDE works in three places. Published on claude.ai, it keeps the owner's work in its own store and AI brings it in when asked. On the owner's own server, Claude Code works behind it: edits go straight into the files, requests run at once, and the owner watches each step and approves the risky ones. Opened anywhere else, it only shows the project and says so.

The rules are the same as everywhere in the Agent OS. Only the owner decides; what AI adds is marked as a proposal until they agree. No secret value is ever shown or stored: a keys file shows only the names of its keys. Every change is filed and committed, so it can be traced and undone.

## Where it stands and what comes next

The IDE works today. The page, its build, its checks and the way back into the files are written, and the owner uses the page on claude.ai. The server with Claude Code behind it is written and was tested on a copy of the repository. The tree on the page matches the repository file for file, and every file and folder has its explanation file and its details file on disk.

Finishing the IDE is the first stage of the whole project, and three things are still open in it:

1. **A view for every kind of file.** Today a few kinds have their own tabs, such as an agent's jobs and links or the key names of a keys file. Every kind of file should get a view made for it, such as one view shared by every skill.
2. **Correct metadata everywhere.** Every file and folder has its details file, but most are still empty templates. Each must be filled in truthfully, and the explanation files kept current.
3. **Tabs that are real files.** Every tab on an item should show a real file next to it, such as its example and its open questions, and a tab should appear only when its file exists. The main docs come first.

After that, the IDE grows with the system: views for new kinds of files, more statuses when the owner asks for them, and the same window on the agents once they run.

## Open questions

- Should a routine check the page on a schedule and bring in the owner's changes without the Apply changes button? It would save a step, but changes would reach the files without the owner's go.
- When the owner works on their server, how should the page published on claude.ai learn about it? Today each copy is rebuilt from the repository on its own.
- Which statuses beyond "changed" should the page show, and when? Today it shows only that one, on purpose.

## Going deeper

The README describes every part of the IDE exactly: the page and each of its tabs, how it is built and checked, how the owner's work comes back into the files, the server, the settings and where every file lives. It is at `apps/project-IDE/docs/README.md`.
