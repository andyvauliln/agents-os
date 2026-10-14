# Metadata

This document tells you all of the metadata logic of the Agent OS. It is written in ASD-STE100. It tells how the metadata works in the new system, without the planning folder `vision/`. Section 15 tells which parts are not built yet.

## 1. What metadata is

1. Metadata is information about a file or a folder. It is not the content of that file or folder.
2. Each file and each folder in the repository is an "item".
3. Each item has its metadata in small files next to it. These files are "metadata files".
4. The metadata files tell what the item is, how it works, who changes it, and which other items must change with it.
5. The metadata files are the only source of this information. There is no other list of items and no other plan of the tree.

## 2. Why the system needs metadata

1. You can understand each part of the project in one read. You do not have to read the code or all the docs.
2. Each AI agent gets the full context of an item before it changes that item.
3. After a change, the agent knows which related items it must also update.
4. The File Tree page shows the metadata of each item as tabs. Thus you can examine, edit and control the full system from one page.

## 3. The metadata files of an item

| File (for the item `vision.md`) | Tab on the page | What it contains | Which items have it |
|---|---|---|---|
| `vision.index.md` | How it works | The explanation of the item, in plain words | All items |
| `vision.meta.json` | Details | The facts about the item, as JSON | All items |
| `vision.example.md` | Example | The structure of the item: its parts and what goes in each part | Only items that need it |
| `vision.questions.md` | Questions | The open questions for the owner about the item | Only items that need it |
| `README.asd.md` (next to `README.md`) | ASD-STE100 | The README again, in ASD-STE100 | Each `README.md` of the doc levels |
| `.env.example` (next to `.env`) | Example | The key names of a keys file, with no values | Each `.env` file |
| `vision.{type}.{name}.view.html` | its own tab | A special view for one kind of file | Not built yet |

Rules:

1. Each file and each folder has a How it works file and a Details file. There is no exception outside `vision/`.
2. The Example file and the Questions file exist only when somebody wrote them.
3. The page shows a tab only when its file exists. The tab shows that file as it is.
4. A metadata file has no metadata files of its own. The only exception is `README.asd.md`. It is a doc, so it has its own metadata files (the family name is `README.asd`).

## 4. How the names are made

1. The "family name" of an item is the name that its metadata files use.
2. For a file, the family name is the file name without its last extension. Example: `vision.md` has the family name `vision`.
3. For a folder, the family name is the folder name. The metadata files of a folder are inside that folder. Example: `configs/configs.index.md`.
4. A file name with no extension stays whole. Example: `.gitignore` has `.gitignore.index.md`.
5. Two files can have the same family name, for example `run.js` and `run.py`. Then each file keeps its extension: `run.js.index.md` and `run.py.index.md`.
6. A file can have the same family name as its folder, for example `server/server.py`. Then the file keeps its extension: `server.py.index.md`.
7. The top of the repository has `agent-os.index.md` and `agent-os.meta.json`.
8. A name pattern, for example `[agent-name]/`, has metadata files that tell about the pattern.
9. In a family name, `|` becomes `-`, and `, ` becomes `+`.
10. These endings are only for metadata files: `.index.md`, `.meta.json`, `.example.md`, `.questions.md`, `.asd.md`, `.view.html`. Do not use them for other files.

## 5. The How it works file (`x.index.md`)

### 5.1 What it tells

It tells a person who sees the project for the first time what the item is and how it works now. Each agent reads the How it works file of a folder before it works in that folder.

### 5.2 Its parts

1. The front matter at the top, between two `---` lines:
   - `about`: the path of the item from the top. The path starts with `agent-os/`.
   - `node`: the identifier of the item on the page.
   - `written`: the date and time of the last change.
   - `by`: who made the last change. This is an agent name, or `owner`.
   - `basis` and `confirmed`: the build script sets these two fields. Do not write them by hand (see section 9).
2. The title: the name of the item.
3. Six headings, always in this order:
   1. What it is
   2. Who looks after it
   3. When and how it changes
   4. Who uses it, and when
   5. Where it is mentioned
   6. Related knowledge
4. The heading "Keep in mind", at the end. It has zero to four lines. Each line has this form: "When you do X, do Y." Write only rules that a person would otherwise do incorrectly.

### 5.3 Its length

| Item | Length |
|---|---|
| A file | One to four sentences under each heading |
| A folder | It gives a summary of its children. It names the two to four most important children. |
| The top folders and the top of the repository | Maximum 200 words in each section |

### 5.4 What it must not contain

1. No decision codes, no input codes and no hashes.
2. No history. It tells how the item is now.
3. No other headings.

### 5.5 How a folder's file is made

1. A folder's How it works file is made from the How it works files of its children.
2. Thus you write the files from the bottom to the top: first the children, then the folder.
3. The top file gives a summary of the full project.
4. A folder's file must agree with its children. If they do not agree, the children are correct. Write the folder's file again.

## 6. The Details file (`x.meta.json`)

### 6.1 What it tells

It contains all the facts about the item that are not its content and not its explanation. It is for agents and for the page. The Details tab shows these facts in plain words. The related files show as links.

### 6.2 Its fields

Keep all the fields, in this order.

| Field | Type | What it contains |
|---|---|---|
| `schema_version` | number | The version of this list of fields. Now it is `1`. |
| `about` | text | What the item is for, in one line. The page shows it below the title. |
| `kind` | text | `file`, `folder`, `file link` or `folder link`. |
| `state` | text | `written`, `empty`, `stage two` or `name pattern`. |
| `status` | text | `decided` (the owner decided it), `proposed` (an idea of an agent, not yet approved by the owner) or `idea`. |
| `git` | text | `tracked`, or `ignored` (the item is only on the machine, for example a `.env` file). |
| `secret` | true, false or null | `true` when the item contains key values. Never read, show or copy such an item. |
| `generated_by` | text or null | The script that makes the item. Do not edit a generated item by hand. `null` when a person or an agent writes it. |
| `writers` | list | The persons, agents and scripts that write or change the item. |
| `readers` | list | The persons, agents and scripts that read the item. |
| `changes_when` | text | The events that change the item. |
| `related` | list of `{path, how}` | The related items, and the relation to each. The relations are: `reads`, `read by`, `writes`, `written by`, `links to`, `same format as`, `built from`, `documented in`, `checked by`, `tested by`, `summed up in`. |
| `sources` | `{decisions, inputs, notes}` | Where the knowledge about the item comes from: the decision codes, the owner input codes and the notes. Codes are permitted here. |
| `update_with` | list of `{path, how}` | The items that must change when this item changes, and how to change each one. |
| `inherits` | list | The knowledge from the folders above that applies to this item. A script fills this field. Do not fill it by hand. |
| `features` | list | The features that the item helps to supply. |
| `views` | list | The special views that apply to the item. |
| `how_it_works` | object | The check data of the How it works file. It is empty now (see section 15). |
| `tree_number` | text | An old number of the item, only for agents. It is empty when the item has none. |

### 6.3 An empty Details file

A Details file can contain only `{}` until somebody writes it. The item still has its file.

## 7. The other metadata files

### 7.1 Example (`x.example.md`)

1. For a doc: the headings of the doc, in order. Each heading has one line that tells what goes below it.
2. For a settings file: each field, with an example value and its meaning.
3. A folder has no Example file.
4. For a `.env` file, the Example is `.env.example`. It contains only the key names, in the same groups as the real file. Each name has a comment. All values are empty. Write it from `secrets.index.json`. Never open a `.env` file to write it.

### 7.2 Questions (`x.questions.md`)

1. Each open question for the owner about the item.
2. Each question has one sentence that tells why it is important.
3. When the owner gives an answer, put the answer into the docs and the metadata. Then remove the question from the file.
4. When there are no questions, the file says "None open."

### 7.3 ASD-STE100 (`README.asd.md`)

1. It is the README next to it, with the same content and sections, in ASD-STE100.
2. The README is the source. When the two do not agree, write `README.asd.md` again.
3. Write it immediately after each change to its README.

## 8. When a metadata file becomes stale

A metadata file is "stale" when it does not agree with its item any more.

| Metadata file | It becomes stale when |
|---|---|
| How it works | The content of the item changed. The knowledge that applies to the item changed. The How it works file of a child changed. The owner edited it on the page. |
| Details | The item was moved, renamed, made or emptied. Its writers or readers changed. A related item changed. A decision or an owner input changed it. |
| Example | The structure of the item changed. The outline in the skill of the doc changed. For `.env.example`: a key name was added, changed or removed. |
| Questions | The owner answered a question. A new question came up. |
| `README.asd.md` | Its README changed. |

## 9. How the build finds stale How it works files

1. For each item, the build script `build_map.py` calculates a "basis". The basis is a hash of these data:
   - the content of the item;
   - the knowledge that applies to the item;
   - the How it works files of the children of the item.
2. The script compares the new basis with the `basis` field in the front matter.
   - The same: the file is "fresh".
   - Different: the file is "stale".
   - No file: the file is "missing".
3. `build_map.py --stale` lists the stale and missing files. It lists the children before the folders.
4. When a child's How it works file changes, its folder becomes stale. Thus a change goes up from the bottom to the top. This is the "ripple".
5. If a stale file is still correct, confirm it: `build_map.py --confirm <id>`. This writes the new basis and the `confirmed` time. Then the parent folder does not become stale because of this file. Thus the ripple stops.
6. `build_map.py --orphans` lists metadata files whose item does not exist any more. Remove each orphan, or move it to the archive.

## 10. How to update metadata after a change

Do these steps after each change to an item. The `file-index` skill gives all the details.

1. Before you change an item, read its How it works file and its Details file.
2. Read the How it works files of the folders above it. Use `build_map.py --context <id>` to get the full context.
3. Make the change.
4. Read the `update_with` list in the Details file. Update each item in the list as it tells.
5. Run `build_map.py --stale`.
6. For each stale file, from the children to the top:
   - If it is correct, add its identifier to the confirm list.
   - If it is not correct, write it again. Set `written` to now and `by` to your name. Then confirm it.
7. Update the Details file of each changed item: all the fields must be true now.
8. Update the Example and Questions files where they exist.
9. Do steps 5 to 8 again until `--stale` lists nothing.
10. Run the build of the page (`ide-build`).

## 11. How the build uses the metadata

1. `enrich.py` reads each file that git keeps, and the folders that contain these files. These are the items of the tree. An item that is not on the disk is not in the tree.
2. For each item, `enrich.py` reads its How it works file and its Details file. It also reads the Example, Questions and ASD-STE100 files when they exist.
3. `enrich.py` marks an item as "empty" when it contains nothing yet: 0 bytes, or only `{}` or `[]`. A file with more than 64 bytes is never empty. A `.gitkeep` file and a `.env` file are never marked empty.
4. `enrich.py` writes the page data `file-tree.data.json`. It writes the text of each file into `real-files.json`.
5. `materialize.py` gives an empty How it works file and an empty Details file to each new item. It puts a `.gitkeep` file into each empty folder. It writes the list of all paths into `docs/file-tree.md`.
6. If `materialize.py` made new files, run `enrich.py` again.
7. `build_map.py` checks that all How it works files are fresh, that none is missing, and that there are no orphans.
8. `check_page.js` opens the page and checks each tab.
9. The tree on the page must be the same as the list of files in git.

## 12. How the page shows and changes the metadata

1. Each metadata file shows as a tab of its item.
2. The "metadata" switch shows or hides the metadata files in the tree.
3. The "empty" filter shows only the empty files and their folders.
4. You can edit the How it works file of an item on the page:
   - On claude.ai, the page keeps your edit in its store. You push "Apply changes". Then `ide-sync` writes your edit into the file, word for word. It sets `by` to `owner`.
   - On your server, `server.py` writes your edit into the `x.index.md` file immediately.
5. An agent must never remove your words from a How it works file. When the knowledge changes, the agent changes the text around your words.

## 13. Who does what

| Who | What it does with the metadata |
|---|---|
| The knowledge base agent, with the `file-index` skill | It writes and updates the How it works, Details, Example and Questions files. |
| The `readme-asd-doc` skill | It writes each `README.asd.md`. |
| The project IDE agent, with `ide-build` | It runs the build scripts and publishes the page. |
| The project IDE agent, with `ide-sync` | It writes your page edits into the metadata files. |
| `materialize.py` | It makes the empty metadata files of new items. |
| `build_map.py` | It finds stale, missing and orphan files, and confirms files. |
| The owner | Reads the metadata on the page, edits the How it works files, and answers the questions. |

## 14. Rules

1. Never write a key value into a metadata file. Write only key names.
2. Never open, read or copy a `.env` file.
3. Do not edit a generated file by hand. Make it again with its script.
4. Do not write decision codes or input codes in a How it works, Example or Questions file. Write them only in the Details file.
5. An idea of an agent is `proposed` until the owner says yes.
6. When you add a file or a folder, give it its metadata files in the same round.
7. When you remove or move an item, remove or move its metadata files too.
8. A file without metadata, or metadata without its item, is an error.

## 15. What is not built yet

1. **The mirror in `vision/`.** Now the source of most How it works and Details files is the mirror `vision/tree/agent-os/`. The build copies them next to their items. After the move out of `vision/`, the files next to the items become the source, and the copy stops.
2. **The basis.** Now the basis also uses the tree notes in `vision/docs/file-tree.md`. After the move, the basis uses only the item, its knowledge and its children (section 9).
3. **The page identifier and the number.** Now the identifier comes from the tree notes. After the move, the identifier comes from the path of the item. The old number stays in `tree_number`.
4. **The check field.** The build will move `basis` and `confirmed` from the front matter into the `how_it_works` field of the Details file.
5. **The views.** The special views (`x.{type}.{name}.view.html`) are a plan. No view exists yet.
6. **The prediction-market domain.** It is in stage two. Only its docs folder has metadata files now.
