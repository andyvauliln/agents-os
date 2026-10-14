# The Agent OS project: vision

## In short

The Agent OS is the owner's personal system for running AI agents of any kind: agents that trade, that work on social media or that help with management. It runs many small agents side by side, each with one clear job, tries every idea safely first and keeps what works, like a wheel that keeps turning. Trading on prediction markets is its first area of work. This project is how the Agent OS gets built: the owner says what they want in plain words, and AI writes the plans, the docs and later the code, while the owner follows, understands and steers everything through their own window on the project, the project IDE. Nothing of the system runs yet. The project is in its first stage: finishing that window and writing down the whole design, clearly and completely, before the first trading agents are built in the second stage.

## Why we are building it

There is far more useful work for AI agents than one person can set up and watch by hand, and in every area most first ideas do not work. The Agent OS makes trying ideas cheap: many variations of an idea run side by side in a safe test mode, the results show which ones work, and only those are kept. Agents of every kind need the same base (information, running on time, safe testing, getting better, being visible to the owner), so that base is built once and each area adds only what is its own.

Building such a system by vibecoding is fast, but it has a cost. When AI writes most of the plans, docs and code, it soon becomes hard to see what exists, why it exists and what depends on what. A person who cannot see the whole picture cannot steer it, and an AI that cannot see it makes changes that break something somewhere else. So the project is built around two things that keep the picture whole: plain docs at every level, and an IDE that shows every file and folder with an explanation a person can read.

The goals of the project:

- a working Agent OS, built step by step, whose first area is trading on prediction markets;
- an owner who always understands what exists, why, and what is happening, without reading code;
- docs that are exact enough for any AI to act on, so that the next session starts knowing everything the last one learned;
- a project that could be rebuilt by an AI from its docs alone;
- every owner word kept, and every owner question answered where it belongs in the docs.

Success means that the owner can open any part of the project, understand it in one read, ask for a change in plain words, and see that change land everywhere it should, with nothing lost and nothing surprising.

## The concept

The project has two halves that grow together: the system being built, and the way it is built.

**The system.** The Agent OS is made of many small agents, each with one job, grouped by area of work into domains. The system agent looks after the whole system and everything every agent shares. Each domain arranges its agents in the levels its work needs, and every agent has a parent above it. Trading is a group of domains of its own, and its first domain is prediction markets, where agents trade on the outcome of events such as elections or sports. Apps sit beside the agents: tools the project builds for itself, outside tools it uses, and code it only studies.

**The levels of the docs.** The project is described at several levels, from the whole down to its parts. The project level, described here, covers the whole repository and the way of working. Below it come the system level, the level of trading as a whole, the level of all apps, and the level of each app, the project IDE first. Each level has the same set of docs: a vision on top, saying what and why; a README that describes every part of that level exactly and where its own docs are; the same README again in Simplified Technical English (the ASD-STE100 standard), so the two can be compared; and a rebuild prompt, the exact instructions an AI follows to build that level again. A lower level never repeats what a higher level says; it sums it up in a sentence and adds only what is its own.

**Metadata next to everything.** Every file and folder has small companion files beside it: a "How it works" note in plain words, a Details file with the facts about it (who writes it, who reads it, when it changes, what must change with it), and, for the main docs, an outline of their structure and the open questions about them. The project IDE shows each of these as a tab, and shows a tab only when its file really exists.

**The way of working.** The owner vibecodes: they say what they want, in any words and any mix of languages. Every input is kept word for word. Every change gets a written plan first, which the owner sees before anything is built. Then the AI does the work, brings every related doc and note in line, rebuilds the IDE, checks it, and hands the result to the owner, who decides what is merged.

**The project IDE.** The owner's window on the project is the File Tree page: a clickable map of every folder and file in the repository, with its text, its How it works and its other tabs, a box to ask the AI a question or for a change, and a button that carries everything the owner left on the page into the files. The same page runs on claude.ai and on the owner's own server, where Claude Code works behind its request box. The IDE serves every AI too: before it changes a file, an AI sees what the file is for, how it works, what depends on it and which rules reach it from the levels above.

**One source for every text.** Every file is its own only source and is edited where it lives. The records of the work, every input word for word, the decisions, the changelog and the plans, are kept with the IDE, and the IDE is built from the files on disk and their metadata alone.

## How it should work

A round of work, from the owner's words to a merged change, goes like this.

1. **The owner says what they want**, in a chat, on the File Tree page, by voice or as an edit to a file. They do not need to know where it belongs.
2. **The input is kept word for word**, with a short summary, its categories and the answer the AI gave. A question and its answer are kept together, because the answer is knowledge too.
3. **A plan comes first** for anything that changes the system, its structure, its code or its docs. The plan says what the owner asked, what will change, which defaults the AI picked and what is still open. The owner reads it and says go, or changes it.
4. **The docs are brought in line, in a fixed order.** At each level touched, the vision first, then the README, then its Simplified Technical English version, then the rebuild prompt last. When a lower level changes, the levels above it are checked too. Decisions and the changelog get their entries.
5. **The metadata follows.** Every How it works note and Details file that the change made stale is rewritten, children before their folders, so a folder always sums up what is inside it.
6. **The IDE is rebuilt and checked.** The page is built again from the repository, tested on a desktop and a phone, and checked so that the tree it shows is exactly the files on disk. A plain list of every path in the repository is written again too.
7. **The work is committed and proposed.** The change goes into the repository with a message that says what changed and why, and into a pull request. It is merged only on the owner's word.

```text
  the owner's words ──► kept word for word ──► plan ──► the owner's go
                                                           │
   merge on the owner's word ◄── commit, pull request ◄── docs, metadata, IDE rebuilt and checked
```

## The business logic

These are the rules the project follows, whatever is being built.

- **Decided means the owner decided.** Anything the AI suggests is a proposal until the owner agrees, and the docs say which is which.
- **Every input is kept.** The owner's words are never changed, never lost and never shortened in the record.
- **Every change has a plan.** Small fixes, such as a typo or a rebuild, need none; everything else is planned and shown first.
- **The docs describe the project as it is now.** No history in the docs for people, no reference numbers and no codes; the history lives in the records.
- **What is learned is written down before the round ends.** Every answer to an owner question is placed in the docs where the owner should have found it.
- **The IDE always shows the real repository.** The tree on the page and the files on disk are the same, every round.
- **Keys never leave the owner's machine.** Only the names of keys are written anywhere; the files that hold their values never go into the repository, and the page never shows them.
- **Nothing hard to undo happens without the owner.** Deleting, rewriting history, merging and anything that acts in the outside world wait for the owner's word.
- **Work is done in stages.** What belongs to a later stage is left as a folder with no files until its stage comes.

The system itself has its own business logic (test first, versions that compete, the owner's approval before anything acts for real), described in the system's vision.

## Examples

**Example: a request from the File Tree page.** The owner opens the How it works of a folder, finds it unclear and writes in the request box: "explain what the jobs file is for, in plain words". The AI answers on the page, keeps the question and the answer as an input, writes the answer into the docs where it belongs, refreshes that How it works note and its folder's, rebuilds the page and commits. The next time anyone opens that folder, the answer is already there.

**Example: a change that touches several levels.** The owner asks that every main doc get a second version of its README in Simplified Technical English. The AI keeps the input, writes a plan with its defaults (the file name, how the page shows it) and waits. After the owner's go, it adds the new skill that writes such a version, writes the new files level by level in the fixed order, adds their How it works and Details files, rebuilds the page so a new tab appears where the file exists, checks that the page tree equals the disk, commits and opens a pull request. The owner reads the result and says merge.

**Example: a session that starts cold.** The owner starts Claude Code on their server in the system's folder. It reads its entry file first, which tells it what the project is, which stage it is in, what to read and in which order, the rules and what to do after every input. Within minutes it knows as much as the session before it, and works by the same rules.

## What the owner sees and does

- They give inputs in plain words: in a chat, by voice, as a note or an edit on the File Tree page.
- They read each plan and say go, or change it.
- They open any file or folder on the page and read what it is, how it works, its details, its outline and its open questions.
- They edit files and How it works notes on the page, add or delete items, and press one button to carry everything into the files.
- They ask questions in the request box and get answers, which are kept.
- They decide what is merged, and answer the open questions when they are ready.

## Where we are and what comes next

The project is in its first stage. The repository already has the shape of the whole system: every planned file and folder exists, written or still empty, each with its metadata files beside it. The File Tree page works on claude.ai and on the owner's server, shows exactly the files on disk, and lets the owner edit, ask, delete and apply changes. The helpers that keep the knowledge and the page, and the skills that write the docs and the metadata, are written. Research on ways to make money on prediction markets, on agents that improve themselves and on how trading agents are built is in the repository. None of the system's agents is built yet.

Stage one, now:

1. Finish the project IDE, with its own full documentation.
2. Go through every file and folder, write the custom views each kind of item needs, and make all metadata correct.
3. Finish the docs at the project level, the system level, the level of trading as a whole and the level of the apps.

Stage two: the prediction-market domain, its strategies and their trading agents. Until then that domain is its folders and earlier notes kept in its docs.

Later: building the system's machinery, starting the first strategy chosen by the owner in test mode, more trading domains copied from the first, and agents of other kinds.

## Principles

**The owner understands everything.** If a doc or a note cannot be understood in one read by someone who is not technical, it is not finished.

**One place for each fact.** Each fact lives in the doc that owns it; other docs sum it up, so nothing disagrees.

**Top down, then bottom up.** The vision leads and the other docs follow it; metadata is written from the children up, so a folder always tells the truth about its contents.

**Plain files.** Everything is a file the owner can open; the IDE is built from the files and never holds anything the files do not.

**Plan, then build, then file.** Every change starts as a plan the owner sees, and ends with what it taught placed in the docs.

**Every AI starts with the whole picture.** The docs and the IDE give any session the full context, so changes land everywhere they should.

**Stages keep the work small.** Only the current stage's work is done; later work waits as empty folders, not half-written files.

## Ideas we are still weighing

**A plain file tree that grows.** The plain list of every path is kept without metadata for now. The idea: add a little information to each line later, such as what the item is for. What it would change: a fast overview for people and for AI, at the cost of a longer file to keep current.

## Open questions

- **What should the rebuild doc be called?** It is called the rebuild prompt today; the owner has also called it a reverse prompt. The name appears at every level.
- **Should the repository and its top folder be renamed** to match the name Agent OS? The name appears in links and in every How it works note.
- **What should the front page say?** It is the first thing anyone sees on GitHub, and it is still empty.
- **When does stage two start?** It decides when the first agents are built and when the prediction-market domain gets its files again.

## Going deeper

The README describes every part of the repository exactly: what each part holds, how the parts connect, how a round of work goes, and where each part's own docs are. It is at `docs/README.md`.
