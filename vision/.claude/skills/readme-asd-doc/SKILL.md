---
name: readme-asd-doc
description: Write or update README.asd.md, the ASD-STE100 (Simplified Technical English) version of a README.md, at any of the five doc levels (project, system, trading, apps, one app), so the owner can compare the full overview of how a level works with the same content in controlled, simple language. Use it right after every change to a README.md, and when a README.asd.md is missing or does not match its README.md.
---

# README in ASD-STE100

## What README.asd.md is

`README.asd.md` is the README of a level again, in ASD-STE100. ASD-STE100 is Simplified Technical English: a controlled language from the aerospace industry. It uses short sentences, one topic in each sentence, simple approved words and one meaning for each word. Text in this language is easy to read and to translate, also for a reader whose first language is not English, and for AI.

It has the same content and the same sections, in the same order, as the `README.md` next to it. It adds nothing, removes nothing and does not change a fact. `README.md` is always the source: when the two disagree, `README.md` is right and `README.asd.md` is written again.

The owner reads the two side by side, to compare the full overview in plain prose with the same overview in controlled language. On the File Tree page `README.asd.md` shows as the ASD-STE100 tab of the README, and as a file of its own.

## The five doc levels

Every level has its own `docs/` folder with the same four docs: `vision.md`, `README.md`, `README.asd.md` and `rebuild-prompt.md`.

| Level | File |
|---|---|
| Project | `docs/README.asd.md` |
| System | `agents/system/docs/README.asd.md` |
| Trading | `agents/trading/docs/README.asd.md` |
| Apps | `apps/docs/README.asd.md` |
| One app | `apps/<app>/docs/README.asd.md`, such as `apps/project-IDE/docs/README.asd.md` |

The domains and the levels below them, starting with the prediction-market domain, are stage two. They get a `README.asd.md` when their `README.md` is written.

## Who reads it

- The owner, to compare it with `README.md`.
- Readers who want short, exact sentences: a reader whose first language is not English, a reader who looks for one fact fast.
- Agents, as a second form of the same facts.

## The four docs of a level, in order

Inside a level the docs are always written in this order: `vision.md` (`vision-doc`), `README.md` (`readme-doc`), then `README.asd.md` with this skill, right after the README, then `rebuild-prompt.md` (`rebuild-prompt-doc`), last.

## What to read before writing

- **The `README.md` of the level**, already updated for this round. It is the only source of content.
- **The current `README.asd.md`**, to keep the sentences that are still correct.
- **The terms**, so that each name is the same in both files: the README itself, and the glossary in the notes (`vision/docs/glossary.md` while we plan).
- **A model of the style:** `vision/archive/2026-10-12/claude-docs/inputs-vision.md`, which gives every owner requirement in ASD-STE100.

## The writing rules

These rules come from the ASD-STE100 standard and from the style of the inputs vision.

### Sentences

1. Write one topic in each sentence. Write one instruction in each sentence.
2. Write a descriptive sentence with a maximum of 25 words.
3. Write a procedural sentence (an instruction) with a maximum of 20 words.
4. Write a paragraph with a maximum of 6 sentences. Give each paragraph one topic. Start the paragraph with its topic sentence.
5. Use the active voice. Write "The build copies the file", not "The file is copied by the build".
6. Use the present tense in descriptions. Use the imperative in instructions: "Run the build."
7. Start an instruction with a verb.
8. Keep the articles "a", "an" and "the". Do not leave them out to make a sentence short.
9. Do not write a noun cluster of more than three words. Write "the file of the page data", not "the page data file build output".
10. Do not use contractions ("does not", not "doesn't").
11. Use "it", "this" and "they" only when the word they refer to is in the same sentence or in the sentence before. If not, write the name again.

### Words

12. Use simple, approved words: "use", not "utilize"; "make", not "generate"; "start", not "initiate"; "show", not "display"; "about", not "approximately"; "to", not "in order to".
13. Give one word one meaning, and one meaning one word. Use the same word for the same thing in all of the document. Do not use a synonym to make the text more interesting.
14. Use the names in `README.md` exactly: the names of parts, files, folders, settings, agents and skills. A name in backticks, such as `agents/system/`, does not change.
15. Use technical names and technical verbs only for a thing or an action that has no simple word. Explain a new term in the first sentence that uses it.
16. Do not use idioms, slang or figures of speech. Write "the owner sees all of the project on one page", not "the page gives the owner the big picture".
17. Do not use a verb with a particle when a single verb is possible: "make", not "set up"; "find", not "find out"; "remove", not "take out".
18. Do not use the "-ing" form of a verb as a noun or as an adjective. Write "When the build starts", not "On starting the build".
19. For a rule, use "must", "can" or "do not". Do not use "should", "may" or "might". If a point is not decided, say so in a sentence of its own: "This is a proposal. The owner did not decide it."

### Procedures and lists

20. Write a procedure as numbered steps. Give one action in each step. Give the steps in the order the reader does them.
21. Put a warning or a caution before the step it is about. Start it with a command: "Do not write a key value in a file."
22. Use a list for three or more items of the same type. Introduce the list with a sentence that ends with a colon.
23. Keep the tables and the pictures of `README.md`. Write the text in a table cell with the same rules. Do not change a picture of a tree or a path.

### Facts and status

24. Keep every fact of `README.md`, and keep its status: decided, proposed, open or stage two. Do not make a proposal into a decision.
25. Do not add a fact, an example or an explanation that is not in `README.md`.
26. Do not write reference numbers, decision codes, input codes or history, the same as in `README.md`. Call the owner "the owner".

Not correct:

> The page's tree is always in sync with what's on disk, since the build regenerates everything from the repo each time it's kicked off.

Correct:

> The tree on the page is the same as the files on the disk. Each time the build starts, it makes the page again from the repository.

## Outline

The file has the same sections as the `README.md` of its level, in the same order, with the same headings. Before the first section it has one line that says what the file is. Write `README.asd.example.md` next to the doc from this outline, adapted to the level: it is the file's Example tab on the File Tree page. The page build also reads the block below.

```markdown
# [The title of README.md] (ASD-STE100)

This document is the ASD-STE100 version of README.md. README.md is the source. If the two documents are different, README.md is correct.

## In short
The same content as "In short" in README.md, in ASD-STE100.

## At a glance
The same parts, table and picture as in README.md, in ASD-STE100.

## How it is laid out
The same tree as in README.md. The explanations in ASD-STE100.

## The parts
The same parts, in the same order, with the same headings. Each part ends with the same "Its docs" line.

### [Part]

## Where each part's docs are
The same table as in README.md, with the text in ASD-STE100.

## Still open in the design
The same open points as in README.md, one sentence or two for each point.
```

If `README.md` at a level uses other headings, use those headings and that order. The section list above is the one that `readme-doc` gives.

## Length

About the same number of words as the `README.md` of the level: often between 80 and 120 percent. Short sentences make more sentences, and simple words make some phrases longer. If the file is much shorter than `README.md`, a fact is missing. If it is much longer, the text explains more than `README.md` does.

## When it goes stale

`README.asd.md` is stale each time its `README.md` changes. Write it again right after the README, in the same round, before the rebuild prompt of the level. It is also stale when a rule in this skill changes, or when the glossary changes a name that it uses.

## Steps

### First build, or a full rebuild

1. Read the `README.md` of the level from start to end.
2. Make a list of the names in `README.md` (parts, files, folders, agents, skills, settings). Use each name in the same form in all of the new file.
3. Write the first line. Then write each section of `README.md` again, in the same order, with the rules above.
4. Do the checks below.
5. Write or refresh the metadata of `README.asd.md` with `file-index`: `README.asd.index.md`, `README.asd.meta.json`, `README.asd.example.md` and `README.asd.questions.md`.

### After a change to README.md

1. Find the sections of `README.md` that changed (`git diff` on `README.md`).
2. Write the same sections again in `README.asd.md`. Remove a sentence that is not correct now.
3. If a heading moved, was added or was removed in `README.md`, do the same change in `README.asd.md`.
4. Do the checks below.
5. Refresh the metadata of `README.asd.md` with `file-index` if the outline or the way the file is kept changed.

## Its page on the File Tree

The File Tree page shows a tab only when its file exists.

- On `README.md`, the **ASD-STE100** tab shows `README.asd.md`.
- `README.asd.md` is also a file in the tree, with its own tabs:
  - **How it works**, `README.asd.index.md`, under the fixed headings of `file-index`: what it is (the README of the level in ASD-STE100); who looks after it (the knowledge base agent with this skill); when and how it changes (right after every change to `README.md`); who uses it and when (the owner, to compare); where it is mentioned (`README.md`, the knowledge base agent, this skill and `readme-doc`); related knowledge (`README.md` is its only source).
  - **Details**, `README.asd.meta.json`, with the fields in `file-index`. Its `related` names `README.md` as "built from".
  - **Example**, `README.asd.example.md`: the outline above, adapted to the level.
  - **Questions**, `README.asd.questions.md`: open questions for the owner about this file, or "None open."

## Checks

1. Make sure that the first line says that the file is the ASD-STE100 version of `README.md` and that `README.md` is the source.
2. Make sure that the sections and the headings are the same as in `README.md`, in the same order.
3. Make sure that each fact of `README.md` is in the file, and that no new fact is in it.
4. Make sure that each status is the same: decided, proposed, open or stage two.
5. Count the words of each sentence. A descriptive sentence has a maximum of 25 words. An instruction has a maximum of 20 words.
6. Make sure that each paragraph has a maximum of 6 sentences and one topic.
7. Make sure that each instruction starts with a verb and that each procedure has numbered steps.
8. Look for the passive voice, the "-ing" forms, "should", "may", "might", contractions, idioms and verbs with a particle. Write these sentences again.
9. Make sure that each name, path and file name is the same as in `README.md`.
10. Make sure that the file has no reference numbers, decision codes, input codes, history or key values.
11. Make sure that the length is between about 80 and 120 percent of `README.md`.

A short script can do check 5. It splits the text into sentences and shows each sentence with more than 25 words:

```bash
python3 -c "import re,sys; t=open(sys.argv[1]).read(); [print(len(s.split()), s.strip()[:100]) for s in re.split(r'(?<=[.!?])\s+', re.sub(r'\x60\x60\x60.*?\x60\x60\x60', '', t, flags=re.S)) if len(s.split())>25]" README.asd.md
```
