---
name: claude-md-doc
description: Write and keep agents/system/CLAUDE.md, the file Claude Code reads first when it starts in agents/system/ - what the project is and its current stage, the docs to read in order, the work of the current stage, and the rules, the steps after every input or update and which change makes which doc stale. Use it to write CLAUDE.md the first time, and whenever the stage, the reading list, a rule from memory, the steps of a round, a doc or a skill that writes a doc changes.
---

# CLAUDE.md doc

## What CLAUDE.md is

`agents/system/CLAUDE.md` is the first file Claude Code reads when it starts in `agents/system/`, as it does on the owner's server and behind the request box of the File Tree page. Claude Code loads it by itself. There is no other `CLAUDE.md` at the top of the repository: an agent that starts at the top reads this file first by hand.

After one read, Claude Code knows what the project is, which stage it is at, what to read next and in which order, what work the stage holds, which rules it never breaks, what to do after every input or update, and which doc each change makes stale. It does not repeat the docs: it names them, in the order to read them, and gives only what Claude Code needs before it opens them.

## Who reads it

- Claude Code started in `agents/system/`, at the start of every session.
- Any agent that starts at the top of the repository, by hand, first.
- The owner, to check what every new session is told.

## The structure the owner set

The owner set the order of its parts:

1. What the project is, and its current stage.
2. The reading list, in this order: the project vision, the project README, the system vision, the system README, the file tree, the project IDE docs.
3. The current stage and its work.
4. The things that belong to `CLAUDE.md` itself: the rules from memory, what to do after every input or update, and when and how to update each doc file.

Keep this order. A heading can be worded to fit, but no part moves and no part is left out.

## What to read before writing

- **The current `CLAUDE.md`** and its earlier draft in `vision/archive/2026-10-12/claude-docs/CLAUDE.md`. Keep what is still true.
- **The memory notes** in `vision/.claude/memory/` (`MEMORY.md` is the index). Each rule there that holds for every session goes into the rules.
- **The notes:** the newest decisions, the changelog and the owner's inputs in `vision/docs/`, and the plan of the current round in `vision/plans/`. Newest wins.
- **The project vision and README** (`docs/vision.md`, `docs/README.md`), for the words that say what the project is and its stage.
- **The skills** in `vision/.claude/skills/` and the helper agents in `vision/.claude/agents/`, so each skill named in the update table exists and does what the table says.
- **The real repository** (`git ls-files`), so every path is real.

## Outline

Write `CLAUDE.example.md` next to the file from this outline: it is the file's Example tab on the File Tree page. The page build also reads the block below.

```markdown
# Agent OS

## What this project is
Three to six sentences: the Agent OS, the owner's personal system that runs AI agents of any kind; the repository that holds it; the owner builds it by vibecoding, and the project IDE is their window on the work; the planning area vision/ that holds the notes, drafts and build tools while we plan. Where this file sits and that Claude Code loads it by itself in agents/system/. Paths in this file are from the top of the repository.

Then the current stage in one or two sentences: which stage it is and what is built.

## Read first, in this order
1. docs/vision.md: the project vision.
2. docs/README.md: the project README.
3. agents/system/docs/vision.md: the system vision.
4. agents/system/docs/README.md: the system README.
5. docs/file-tree.md: every path in the repository, plain, without metadata files, built by the IDE build.
6. apps/project-IDE/docs/README.md: the full documentation of the project IDE.
One line for each: what the reader gets from it. Then one line: before you touch a file or folder, read its How it works file next to it, and how to print everything that applies to it.

## The current stage and its work
The stage, its work as a short list in the order the owner gave it, and what is out of scope until the next stage (do not touch it). What comes in the next stage, in one or two lines.

## CLAUDE.md related things

### Rules from memory
The rules every session follows, one line each, taken from the memory notes.

### What to do after every input or update
Numbered steps, from the moment an input arrives to the commit.

### When and how to update each doc
One table: the change, the files it makes stale, the skill that writes each one, in the order to run them.

### Where things are
A short table: what, and its path. Only what a new session needs to find its way.
```

### What each part holds

- **What this project is.** The same words as the "In short" of the project vision. The stage: today stage one, and nothing of the agents is built yet.
- **Read first, in this order.** Exactly the six docs above, in that order. Add a doc to the list only on the owner's word. The How it works line: `vision.index.md` next to `vision.md`, `f/f.index.md` inside a folder, and `python3 vision/tools/build_map.py --context <node>` to print everything that applies to an item, the levels above included.
- **The current stage and its work.** For stage one: finish the project IDE; go through every file and folder; write the custom views; make all metadata correct; finish the docs at the project level, the system domain, trading in general and apps. Out of scope: the prediction-market domain and everything below it, which keep only their folders; that is stage two.
- **Rules from memory.** From `vision/.claude/memory/`, one line each, for example: decided only on the owner's word, and our ideas are "proposed"; never write or read a key value, and never open a `.env` file; docs for people are plain and book-like, with no reference numbers, ids or decision codes; every owner input, every answer to the owner's question and every system change goes through `knowledge-intake`; every change request gets a plan first (`change-plan`); before a change, know the item's whole context, and after it bring everything related in line in the same round; the tree on the page always equals the files on disk, and every planned item is a real file; every file and folder outside `vision/` has its How it works and Details files; one job per code file; generated files are rebuilt, never merged by hand; use only the repository `andyvauliln/trading-oss`; ask before anything hard to undo (deleting, rewriting history, merging into `main` unless the owner allowed it, anything that acts live); show the plan and one example before a big rewrite; call the owner "the owner", and "they".
- **What to do after every input or update.** The steps in "The round" below.
- **When and how to update each doc.** The table in "The update table" below.
- **Where things are.** The knowledge base and notes, the memory, the plans, the drafts of the helper agents and skills, the build tools, the File Tree page and its server, the keys folder, while we plan and where each goes later.

### The round

These are the steps `CLAUDE.md` gives for every input or update:

1. Pull: `git pull` on `main` on the owner's server; in the cloud, bring `origin/main` into the branch first.
2. Store the input word for word with `knowledge-intake` (`vision/docs/inputs/`, with its row in `index.json`), and record decisions and the changelog.
3. If it asks for a change, write a plan with `change-plan` and show it to the owner before you build it. Small fixes need none.
4. Build the change. Work out every related item first, from its Details file (`update_with`) and `build_map.py --context`.
5. Update the docs it makes stale, by the update table: inside a level vision, README, `README.asd.md`, then rebuild prompt; then climb to the parent level; then `CLAUDE.md` if it is stale.
6. Update the metadata files with `file-index`, children before parents.
7. Rebuild and check the page with `ide-build` (this also builds `docs/file-tree.md` and copies the metadata next to each item). If the owner pressed Apply changes or asked for a sync, run `ide-sync` first.
8. Commit with a message that says what changed and which input caused it, push, and open or update the pull request into `main`. Merge only on the owner's word.
9. Tell the owner in two to five plain lines what changed and what only they can answer.

### The update table

| Change | Stale | Skill, in order |
|---|---|---|
| Any owner input, answer or system change | the stored inputs, decisions, changelog | `knowledge-intake` |
| A change request | a plan in `vision/plans/` | `change-plan` |
| The goals, concept, behaviour, business rules, stage, plans, ideas or open questions of a level | that level's `vision.md`, then its README, `README.asd.md` and rebuild prompt where the change reaches them, then the parent level | `vision-doc`, `readme-doc`, `readme-asd-doc`, `rebuild-prompt-doc` |
| A part of a level added, removed, renamed or moved; a format, setting, job, link or docs path changed | that level's `README.md`, then `README.asd.md`, then `rebuild-prompt.md`; the parent's README if it names the part | `readme-doc`, `readme-asd-doc`, `rebuild-prompt-doc` |
| A `README.md` changed | the `README.asd.md` next to it, right after | `readme-asd-doc` |
| Any change to a level's design: tree, names, formats, build order, checks | that level's `rebuild-prompt.md`, last; the parent's list of child prompts | `rebuild-prompt-doc` |
| A file or folder added, moved, renamed or removed | `docs/file-tree.md` (built), the item's metadata files and its parents' How it works | `ide-build`, `file-index` |
| An item's notes, the knowledge that applies to it, or a child's How it works changed | its `.index.md` and `.meta.json` | `file-index` |
| A doc's outline changed in its skill | that doc's `.example.md` at every level | `file-index` |
| A question about an item asked or answered | its `.questions.md`, and the doc where the answer belongs | `knowledge-intake`, `file-index` |
| The owner left notes, edits or deletes on the page | the files they touch, then all of the above | `ide-sync`, then `ide-build` |
| The stage, the reading list, a memory rule, the round, a doc or a doc skill changed | `agents/system/CLAUDE.md` | `claude-md-doc` |

The five doc levels, each with `vision.md`, `README.md`, `README.asd.md` and `rebuild-prompt.md`: the project in `docs/`, the system in `agents/system/docs/`, trading in `agents/trading/docs/`, apps in `apps/docs/`, and one app, such as `apps/project-IDE/docs/`. When every level is written fresh, the order is project, system, apps, the project IDE, trading.

## Length

About 1,000 to 2,000 words. Claude Code loads the whole file into every session, so every line must earn its place. Detail belongs in the docs it names, the skills and the memory notes.

## How to write it

- **For an AI agent**, in the second person and the imperative where it gives an instruction: "Read these in order." Plain sentences.
- **Exact paths**, from the top of the repository, in backticks. Every path is a real file or folder.
- **No reference numbers, decision or input codes, hashes or history.** State the rules as they are now.
- **No key values**, ever: key names only.
- **Status is honest.** Say what is decided and what is proposed; say what is built and what is only designed; name stage two parts as stage two.
- **Same words** as the project vision and README.
- **Do not repeat the docs.** Name a doc and say in one line what the reader gets from it.

## When it goes stale

`CLAUDE.md` is stale when:

- the stage changes, or the work of the current stage changes;
- a doc in the reading list is added, removed, moved or renamed, or the owner changes the order;
- a rule in the memory notes is added, changed or dropped, when it holds for every session;
- the steps of a round change (a new skill in the round, a new check, a new git rule);
- a doc is added at a level, a doc skill is added or renamed, or a change starts to make another doc stale;
- a path in "Where things are" changes, for example when the planning area `vision/` moves into the repository's own folders;
- the project vision changes its "In short".

## Steps

### First build, or a full rebuild

1. Read the sources above.
2. List, in the notes, each rule from memory that holds for every session, and each change that makes a doc stale, with the skill that writes it.
3. Write the four parts in the order the owner set, from that list.
4. Do the checks below.
5. Write or refresh the metadata of `CLAUDE.md` with `file-index`: `CLAUDE.index.md` (How it works), `CLAUDE.meta.json` (Details), `CLAUDE.example.md` (Example, from the outline above) and `CLAUDE.questions.md` (Questions), next to the file.
6. Start a new Claude Code session in `agents/system/` when you can, and ask it what the project is, its stage and what to read first. Its answer must match the file.

### After a change

1. Find the parts that the change touches, by "When it goes stale".
2. Rewrite those lines. Remove what is no longer true. Never add "Update:" notes.
3. If a new doc or skill joined the round, add it to the update table in its place.
4. Do the checks, and refresh the metadata with `file-index` if the structure or the way the file is kept changed.

## Its page on the File Tree

The File Tree page shows a tab only when its file exists. Next to `agents/system/CLAUDE.md`:

- **How it works**, `CLAUDE.index.md`, under the fixed headings of `file-index`: what it is (the first file Claude Code reads in `agents/system/`); who looks after it (the knowledge base agent with this skill; the owner can change it on the page); when and how it changes (the cases in "When it goes stale"); who uses it, and when (Claude Code at the start of every session, any agent that starts at the top, the owner to check it); where it is mentioned (the project README, the system README, the knowledge base agent, this skill); related knowledge (the memory notes, the project and system docs, the doc skills).
- **Details**, `CLAUDE.meta.json`, with the fields in `file-index`.
- **Example**, `CLAUDE.example.md`: the outline above.
- **Questions**, `CLAUDE.questions.md`: open questions for the owner about this file, or "None open."

## Checks

- The four parts are there, in the order the owner set.
- The reading list has exactly the six docs, in the owner's order, and each path exists.
- The stage and its work match the project vision and the newest plan; stage two parts are out of scope and named as stage two.
- Each rule from memory that holds for every session is in the rules, and no rule contradicts a newer decision.
- Every skill named in the update table exists, and every doc that a change can make stale is in the table.
- No reference numbers, decision or input codes, hashes, history or key values.
- It is within the length.
- A new session started in `agents/system/` can say, from this file alone, what the project is, its stage, what to read first and what to do after an input.
