---
name: ide-sync
description: Bring back everything the owner left on the File Tree page (messages, notes, file edits, How it works edits, new, moved or deleted items, requests) into the repository, so nothing they wrote is lost and the page can be rebuilt from the files. Use it when the owner presses Apply changes at the top of the page or says "sync the file tree", before ide-build.
---

# IDE sync: from the page back to the files

The owner works on the File Tree page: they edit a file's text or its How it works, comment on a line, add or remove an item, and send messages or requests. The page saves all of it at once in its own store, so the owner never waits, but the files do not change until a sync. This skill folds what is waiting into the files. Afterwards `ide-build` rebuilds the page from the files.

A sync starts when the owner asks for it: they press **Apply changes** at the top of the page, or say "sync the file tree". On claude.ai the button posts one comment on the page and sends it to Claude, which wakes the Claude watching the page; when no Claude is watching, the page saves the request and tells the owner to say "sync the file tree" in the project chat. On the owner's server the button starts a Claude Code run with the same request, shown in the chat of the top folder.

## What waits on the page

The page's store has three collections:

| Collection | What a document holds |
|---|---|
| `inputs` | A message sent on the page, with its kind (question, answer, change, discard; `delete` and `restore` for the Delete and Bring back buttons, with the owner's `note`; `apply` for the Apply changes button, with `count` and `items` (what was marked changed), `sent_to_claude`, the comment's `thread`, or `not_sent` with the reason), the answer given on the page and its status (`new` until a sync files it). |
| `nodes` | One document per item the owner touched: `fields` (the latest value of each field edited, such as `content` for the file's text and `how_md` for its How it works), `comments` (line comments with the line's text), `qa`, `new_node` for an item added on the page, `deleted` with `was` (what the item was), `delete_note` and `cleanup` (`sync`, or `claude-code` when Claude Code on the server already cleaned up), and `worked` (the item was changed by a request from the page). |
| `changes` | The history of every edit, with before and after. It stays as the history and is never folded or deleted. |

Read them with the artifact data tool on the page's link, https://claude.ai/artifact/72v2Uppt6jpfXLCjKNX9xs. On the owner's server the same documents are files, one per document, in `apps/project-IDE/data/page-store/<collection>/<id>.json`: read them there, and clear a folded one by setting its `status` or deleting its file. Edits to a file's text and to How it works made on the server page are already in their files; check them and confirm them.

## Steps

1. **List** every `inputs` document with status `new` and every `nodes` document with fields, comments, `deleted`, `new_node` or `worked`.
2. **Save each as an input,** word for word, with the item it was left on: the first step of `knowledge-intake`. A page message and the answer the page gave are one input. An edit is an input too: its text is the new value.
3. **Write the edits into their files:**
   - an edit to a file's text goes into that file (while we plan: its draft; for a file nobody has written yet: `overrides.json` as `content`);
   - an edit to How it works goes into the item's `.index.md` word for word, with `by: owner` and the time, then `build_map.py --confirm <id>`;
   - a new item gets its number and a line in the tree notes, a section, and its How it works file, marked proposed until the owner says otherwise;
   - a deleted item is cleaned out of the project as in "Deleting an item" below, keeping the owner's note in mind; when its `cleanup` is `claude-code`, Claude Code already did it on the server, so only check it;
   - any other field goes into `overrides.json` under the item's number;
   - an open line comment is applied when the owner asked for the change, otherwise it becomes an open question in the item's section.
4. **Run the requests** the owner sent from the page, such as a question to answer or a file to add. File each answer with its input.
5. **Hand over the knowledge.** List the saved inputs for the knowledge base agent, which sorts them into the notes, decisions and docs and refreshes the How it works files.
6. **Rebuild and publish** with `ide-build`.
7. **Clear what was folded:** mark each filed `inputs` document processed and delete the folded `nodes` documents, which also clears the "changed" marks on the page. Leave `changes` alone. Clear nothing that is not yet in a file.
8. **Report** to the owner in two to five plain lines: what was brought in, what changed on the page, and any question only they can answer.

## Started by Apply changes

When the round was started by the Apply changes button, finish it in this order, so the page the owner has open shows the new tree:

1. Do steps 1 to 6 as above: every waiting item, and the publish of the new page.
2. Clear what was folded (step 7), and mark the `apply` input processed **last**, with `processed_at` and `processed_into`. The open page watches that input: when it turns processed, the page loads the new tree, or asks the owner to reload.
3. On claude.ai, answer the comment the button posted (the artifact comments tool, in its thread) in one or two plain lines: what was applied and anything left for the owner. Then resolve the thread. On the server, the answer is the run's last message.

A comment that reaches you from the page but is not from the Apply changes button is a message like any other: file it and answer it in its thread.

## Deleting an item

The owner deletes a file or folder with the Delete button on the page and may write a note for Claude with it. On the owner's server Claude Code does the deletion at once; on claude.ai it waits for this sync. Either way it is one round:

1. **Read the note first** and follow it: it says what to keep, move or leave before anything goes.
2. **Delete the item from the repository:** the file, or the folder with everything inside it, and its How it works and Details files (`vision.index.md` and `vision.meta.json` next to `vision.md`; a folder's sit inside it). An item that was only planned has no files, so there is nothing to delete here.
3. **Clean the project of it:**
   - its line and section in the tree notes; its number is retired and never reused;
   - every link file that points to it, and its rows in the links and workers files;
   - mentions in other files and in How it works files: remove them, or reword the sentence so it still reads well;
   - the parent folder's How it works file when it lists the item, and the item's entries in the knowledge map.
   Earlier inputs and decisions that mention it stay as they are: they are the history.
4. **File it:** the deletion and the note go in word for word as one input (`knowledge-intake`), with a line in the changelog saying what was deleted and why. Then rebuild with `ide-build` and commit.
5. **Report** in one or two plain lines what was deleted and what else changed, and anything the note asked for that could not be done.

Delete nothing beyond the item without asking: a file that only mentions it is edited, never deleted. Bringing an item back ("Bring it back" on the page) is the same round in reverse: restore the files from git and put back what the cleanup removed.

## The "changed" mark

For now the page has one status: changed. Every request from the page marks what it touched until the next sync: an edit, a note, a new or deleted item, a request in the box, and on the server every file Claude Code changed for a request (saved as `worked` in that item's `nodes` document). The sync clears the marks when it deletes the folded documents. More statuses may come later.

## Rules

- The owner's words are never changed and never dropped. If a later rewrite of a How it works file would lose an owner edit, write around it and say so in your report.
- Nothing is cleared from the page before it is in a file.
- An edit that contradicts something the owner decided earlier is not applied silently: ask the owner.
- No secret values: if the owner pasted a key on the page, do not copy it anywhere; tell them to put it in the keys file on their machine and remove it from the page.

## Checks

- Every `new` input on the page is in the inputs folder, with its answer.
- Every How it works edit is in its `.index.md`, word for word, and confirmed.
- After the rebuild, the page shows each edit from the files, and the page store holds only `changes` and what was not folded on purpose.
- A round started by Apply changes ends with its `apply` input processed and, on claude.ai, its comment answered and resolved.
