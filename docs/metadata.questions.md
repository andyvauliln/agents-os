# Questions: metadata.md

## Open questions for the owner

- **Does the Details file keep only `about`, `status`, `secret`, `generated_by`, `related`, `update_with` and `sources`?** Almost no field has a value, and no script reads a field yet. A shorter list is easier to keep true. Recommended: fill these seven fields first. Keep the other fields empty until a script reads them. From: the owner's question of 2026-10-14 about the purpose of the fields.

## The owner's questions

### 2026-09-30: Does the page write How it works again at each visit, and does it save it?

> and how does it works "how it works" it ll just generate every time we go this tab? do we save it at all? and in what time then?

No. The How it works text of each item is a real file next to the item. It is `x.index.md` next to a file, or `f/f.index.md` in a folder. The page reads it from there.

1. The knowledge base agent writes it with the `file-index` skill when the item changes.
2. The build marks it stale when the item, its knowledge or its children change.
3. The owner can edit it on the page.

This changed later: at first, Claude wrote the text when you first opened the tab. It saved the text only in the store of the page, with a Rewrite button.

Docs improved: none, the answer was already in docs/metadata.md (sections 5 and 12).

### 2026-09-30: Does an edit update the metadata and the folders above?

> if we for example edit file any how and his metadata ll summary for the page and folders updates automaticly?

Not automatically. After a change, these steps occur:

1. `build_map.py --stale` lists each How it works file that is now stale, children first.
2. The agent writes again or confirms each file, up to the top.
3. The agent reads the `update_with` list in the Details file of the item. It updates those items.

On claude.ai, the page can write a new summary for a folder at once ("Update it now"). The knowledge base agent checks it at the next sync.

Docs improved: none, the answer was already in docs/metadata.md (sections 9 and 10).

### 2026-09-30: How do we make metadata from the owner's inputs?

> describe how we currently make metadata to the files and folders after mine inputs

1. The `knowledge-intake` skill stores the input word for word.
2. It finds the knowledge in the input.
3. It writes that knowledge in the correct docs and in each related location.
4. It records the decisions and the changelog.
5. Then the `file-index` skill updates the How it works, Details, Example and Questions files of each changed item, children first.
6. It continues until the build shows no stale file.

This changed later: at that time, the input became text in the tree notes. A build then made the page data from it. The build scripts had many details that a person wrote by hand. Now we retire the tree notes.

Docs improved: none, the answer was already in docs/metadata.md (sections 10 and 16.3).

### 2026-10-05: Why were the .index.md files not next to their files?

> and why you not make/moved .index.md files for how it works for now just for readme and vision

The agent made all of them, but in a mirror folder. Thus no file was next to its item.

Today each file and folder has its How it works file next to it on disk. That file is the only source. The build copies nothing.

This changed later: until 2026-10-14 the source was a mirror in `vision/tree/agent-os/`, and the build copied each file into its location.

Docs improved: none, the answer was already in docs/metadata.md (sections 3 and 20).

### 2026-10-06: Why does vision.md.index.md have two .md extensions?

> why for vision index file we have 2 md? vision.md.index.md.

The name kept the full file name. Thus two files such as `run.js` and `run.py` could not have the same How it works file.

Today the name of a metadata file is the item name without its last extension. Thus it is `vision.index.md`. A file keeps its extension only when its name is the same as the name of a sibling or its folder. An example is `server.py.index.md`.

Docs improved: none, the answer was already in docs/metadata.md (section 4).

### 2026-10-06: Which other metadata files do we need?

> i don't know what else we need as metadata for files, maybe change log, suggest me

Today an item can have these files:

1. A How it works file (`x.index.md`).
2. A Details file (`x.meta.json`).
3. An Example (`x.example.md`).
4. A Questions file (`x.questions.md`).
5. Next to a README, its ASD-STE100 twin.

An agent proposed a change log file, a Tests file and custom views (`x.{type}.{name}.view.html`). They are not built yet.

Docs improved: docs/metadata.md.

### 2026-10-06: Do we need a schema file in addition to the Example?

> about shema.json i think this kind of things we have in a examples or it's suppose to be additonal ?

They have some of the same content. The Example is for persons to read. A schema holds the rules that a script checks.

The proposal was this: keep a format file only for config and data files, and make the field notes of the Example from it. No schema file exists yet.

Today the Example of a settings file lists each field with an example value and its meaning.

Docs improved: docs/metadata.md.

### 2026-10-06: Is file-set.md built, or is it only a doc?

> also tell me about file-set.md, so it's already implemented and part just of documentation?

It was a plan. It was not built.

After that, its name rule and an empty Details file for each item were built. The full metadata logic is now in this doc. Its other parts still wait: the change log, the tests and the views as files.

The plan stays in the planning area. When its content is moved out, it goes to the archive.

This changed later: on 2026-10-14 the plan moved to `apps/project-IDE/data/plans/file-set.md`.

Docs improved: docs/metadata.md.

### 2026-10-12: Is the metadata in the tree on disk?

> is file metatdata in a disk tree or what?

Yes. Each How it works file and each Details file is next to its item on disk. It is next to a file, or in a folder.

The files next to the items are the only source. The build copies nothing.

This changed later: at the time of the question, the files were only in the mirror. Until 2026-10-14 the mirror `vision/tree/agent-os/` was the source, and the build copied each file into its location.

Docs improved: none, the answer was already in docs/metadata.md (sections 1, 3 and 20).

### 2026-10-14: The logic of status, inputs, decisions, questions and the Details fields

> what logic we currently have around An idea of an agent is `proposed` until the owner says yes. this, and about inputs and about decision and about questions, and actuality all fields in metadata object

All of it is in this doc, sections 15 to 19:

1. Only the owner decides. The idea of an agent is "proposed" until the owner says yes.
2. Each owner input is one file, word for word, with a row in `index.json`.
3. Each decision has a number in `decisions.md`.
4. The questions are in the Questions file of each item.

Most Details files are still empty. No script reads a field yet.

Docs improved: docs/metadata.md.

### 2026-10-14: When does "proposed" occur?

> 1. An agent writes its idea with status `proposed`. It names the idea in its reply to the owner and gives its recommendation. when it's happening i am not unerstand still

It occurs each time an agent fills a gap that the owner did not fill. The gap can be a plan, a default, or the idea of the agent.

It is the same now and in the new version. It is the same in the terminal, on the page and in a thread. When the owner says yes, the item is decided.

Docs improved: docs/metadata.md.

### 2026-10-14: When do agents make questions?

> about question in which stages or when  (now or in new version) we generate questions

There are two types. They are the same now and in the new version.

An agent writes the open questions for the owner at these times:

1. In a plan (`change-plan`).
2. With the `make-questions` skill: when the owner asks, after a doc or a plan is written, and before a stage ends.
3. While it writes a doc.
4. While it changes an item.

The `knowledge-intake` skill records the questions of the owner, with their answers, in the Questions file of the item.

This changed later: at the time of the question, no skill made questions. `make-questions` and the part for the owner's questions came after.

Docs improved: docs/metadata.md.

### 2026-10-14: What are the Details fields for?

> and i still not understand purpose of fields

They tell an agent what it must know before it changes an item. The agent does not have to read the full project. The fields tell:

1. What the item is.
2. If it is safe to change.
3. Who works with it.
4. What else must change with it (`update_with`). This is the most important field.
5. Why it is as it is.
6. Which rules from the levels above apply.

Today almost no field has a value, and no script reads them. An agent proposed to keep only `about`, `status`, `secret`, `generated_by`, `related`, `update_with` and `sources`. This proposal waits for the owner.

Docs improved: docs/metadata.md.
