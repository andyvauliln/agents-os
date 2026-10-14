# Questions: metadata.md

## Open questions for the owner

None open.

## The owner's questions

### 2026-09-30: Is How it works written again on every visit, and is it saved?

> and how does it works "how it works" it ll just generate every time we go this tab? do we save it at all? and in what time then?

No. Each item's How it works is a real file next to it, `x.index.md` beside a file or `f/f.index.md` inside a folder, and the page reads it from there. The knowledge base agent writes it with the `file-index` skill when the item changes, the build marks it stale when the item, its knowledge or its children change, and the owner can edit it on the page. This changed later: at first Claude wrote the text on the first open of the tab and saved it only in the page's store, with a Rewrite button.

### 2026-09-30: Does an edit update the metadata and the folders above?

> if we for example edit file any how and his metadata ll summary for the page and folders updates automaticly?

Not by itself. After a change, `build_map.py --stale` lists every How it works file that is now stale, children first, and the agent rewrites or confirms each one up to the top; it also reads the item's `update_with` list in its Details file and updates those items. On claude.ai the page can write a fresh summary for a folder at once ("Update it now"), and the knowledge base agent checks it at the next sync.

### 2026-09-30: How metadata is made from the owner's inputs

> describe how we currently make metadata to the files and folders after mine inputs

The `knowledge-intake` skill stores the input word for word, finds the knowledge in it, writes it in the right docs and every related place, and records decisions and the changelog. Then the `file-index` skill updates the How it works, Details, Example and Questions files of every changed item, children first, until the build reports none stale. This changed later: at that time the input became text in the tree notes and a build turned that into the page data, with many details written by hand in the build scripts; the tree notes are now being retired.

### 2026-10-05: Why the .index.md files were not next to their files

> and why you not make/moved .index.md files for how it works for now just for readme and vision

They were all made, but in a mirror folder, so none sat next to its file. Today every file and folder outside `vision/` has its How it works file next to it on disk. While we plan, the source is still the mirror in `vision/tree/agent-os/`, and the build copies each file into place.

### 2026-10-06: Why vision.md.index.md has two .md endings

> why for vision index file we have 2 md? vision.md.index.md.

The name kept the whole file name so that two files such as `run.js` and `run.py` could never share one How it works file. Today metadata files are named after the item without its last extension, so it is `vision.index.md`; only a file whose name would clash with a sibling or with its folder keeps its extension, such as `server.py.index.md`.

### 2026-10-06: What other metadata files are needed?

> i don't know what else we need as metadata for files, maybe change log, suggest me

Today an item can have a How it works file (`x.index.md`), a Details file (`x.meta.json`), an Example (`x.example.md`), a Questions file (`x.questions.md`), and next to a README its ASD-STE100 twin. A change log file, a Tests file and custom views (`x.{type}.{name}.view.html`) were proposed and are not built yet.

### 2026-10-06: Is a schema file needed besides the Example?

> about shema.json i think this kind of things we have in a examples or it's suppose to be additonal ?

They overlap: the Example is for reading, and a schema holds the rules a script checks. The proposal was to keep a format file only for config and data files and to build the Example's field notes from it; no schema file exists yet. Today the Example of a settings file lists each field with an example value and its meaning.

### 2026-10-06: Is file-set.md built, or only a doc?

> also tell me about file-set.md, so it's already implemented and part just of documentation?

It was a plan, not built. Since then its naming rule and an empty Details file for every item were built, and the full metadata logic is now in this doc; its other parts (change log, tests and views as files) still wait. The plan stays in the planning area until its content is moved out and it is archived.

### 2026-10-12: Is the metadata in the tree on disk?

> is file metatdata in a disk tree or what?

Yes. Every How it works file and Details file sits next to its item on disk, beside a file or inside a folder. While we plan, the copy in the mirror `vision/tree/agent-os/` is still the source and the build copies it into place; after the move out of `vision/`, the files next to the items become the only source. This changed later: when the owner asked, they lived only in the mirror.

### 2026-10-14: The logic of status, inputs, decisions, questions and the Details fields

> what logic we currently have around An idea of an agent is `proposed` until the owner says yes. this, and about inputs and about decision and about questions, and actuality all fields in metadata object

It is all in this doc, sections 15 to 19. Only the owner decides, and an agent's own idea is "proposed" until the owner says yes; each owner input is one file, word for word, with a row in `index.json`; each decision has a number in `decisions.md`; questions live in each item's Questions file. Most Details files are still empty, and no script reads a field yet.

### 2026-10-14: When does "proposed" happen?

> 1. An agent writes its idea with status `proposed`. It names the idea in its reply to the owner and gives its recommendation. when it's happening i am not unerstand still

Whenever an agent fills a gap the owner did not fill: a plan, a default, or its own idea. It is the same now and in the new version, in the terminal, on the page and in a thread. The owner's yes makes it decided.

### 2026-10-14: When are questions made?

> about question in which stages or when  (now or in new version) we generate questions

There are two types, the same now and in the new version. Open questions for the owner are written by an agent: in a plan (`change-plan`), by the `make-questions` skill (when the owner asks, after a doc or a plan is written, and before a stage ends), while writing a doc, or while changing an item. The owner's own questions are recorded with their answers by `knowledge-intake` in the Questions file of the item. This changed later: when the owner asked, no skill made questions; `make-questions` and the part for the owner's questions came after.

### 2026-10-14: What are the Details fields for?

> and i still not understand purpose of fields

They answer what an agent must know before it changes an item, without reading the whole project: what it is, whether it is safe to change, who works with it, what else must change with it (`update_with`, the most important), why it is so, and which rules from above apply. Today almost none are filled and no script reads them. Keeping only `about`, `status`, `secret`, `generated_by`, `related`, `update_with` and `sources` was proposed and waits for the owner.
