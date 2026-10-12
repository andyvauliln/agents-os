---
name: rebuild-prompt-doc
description: Write or update rebuild-prompt.md, the prompt an AI coding agent follows to rebuild the whole Agent OS from an empty repository and end with the same working system - the complete tree, exact names and formats, every part, the build order and the checks. Use it to build the prompt the first time, and after every change to the system's design, last, after the vision and the README.
---

# Rebuild prompt doc

## What rebuild-prompt.md is

A prompt for an AI coding agent, such as Claude Code. Given only this file and an empty repository, the agent rebuilds the Agent OS and ends with the same working system: the same folders and file names, the same file formats and settings, the same scripts doing the same jobs, the same agents and helpers with the same instructions in substance, the same safety rules and the same project IDE. It is the full and exact spec of the system as it is designed today, written as instructions.

It is kept current after every change to the system's design, last of all the docs, so that at any moment the system could be rebuilt from it alone.

It is not a doc for reading through like the vision or the README, although the owner can read it to check. It holds no history, no reasons beyond a line where a reason prevents a wrong guess, no runtime data, logs or results, and never a secret value.

## Who reads it

- An AI coding agent rebuilding the system, or a part of it, from nothing.
- An agent checking whether the system still matches its spec.
- The owner, to check that nothing important is missing.

## What to read before writing

- **The tree notes:** one section per file and folder, with every name, format and rule. This is the main source; every path in the prompt comes from it.
- **The topic notes:** conventions, data schemas, safety, flows, architecture, the how-to runbooks and the common knowledge, for the exact formats and rules.
- **The decisions**, so you know what is decided, what is our proposal and what is open.
- **What exists today:** the drafts of the system's prompt, the helper agents and their skills, the build scripts, the File Tree page and its server. Where a part exists, the prompt describes it as it is.
- **The vision and the README**, already updated for this round: the prompt uses the same names and never contradicts them.

## Outline

The file always has these sections, in this order. A heading can be worded to fit, but the order and the purpose stay the same. The File Tree page shows this outline as the file's Example, so keep it in step with what the doc really looks like.

```markdown
# Rebuild the Agent OS

## Your task
Who you are (an AI coding agent in an empty repository), what you build, what "the same system" means (the checks at the end), what you never do (write a secret value, set anything live, push or publish without the owner's go), and how to work: follow the build order, run each step's check before the next, and ask the owner whenever this prompt says a point is open.

## The system in brief
What the Agent OS is and how it works, in about 300 words, in the same words as the vision: enough to make sensible choices wherever this prompt leaves room.

## Ground rules
The rules every file follows: safety (keys, test and live, approvals), formats (JSON for settings, Markdown for docs, the script languages), names, links, what git ignores, and the How it works file next to every file and folder.

## The repository tree
The complete tree as one code block: every folder and file with a one-line comment. Placeholders in [brackets] with their name format; examples marked as examples.

## Conventions
Exact names and formats, each with an example: agent names, script and data suffixes, link names, the children's link folders, the standard agent folder, the standard AI setup folder, versions and changelogs in docs.

## The parts
One section per part, in the same order as the README's parts. For each: the files to create, by exact path; what each file holds, with the exact schema or key list where one is decided, as a short JSON or Markdown example; what each script does (inputs, outputs, options, errors, what it logs); how the part connects to the others; and the check that proves the part works.

## Build order
Numbered steps from an empty repository to the finished system, each ending with its check.

## Acceptance checks
The list that proves the rebuilt system is the same: the tree matches, every settings file parses and fits its schema, every link is built and none is broken, the tests pass, nothing can act live without the owner's approval, no secret value is in git, every file and folder has its How it works file, the File Tree page builds.

## Do not build
Ideas still being weighed and questions still open, one line each, with what to leave in their place: nothing, a placeholder, or a setting switched off.
```

### At other levels

The system's prompt rebuilds the system's own parts and lists the prompts below it in build order. Every domain and every agent below it has its own prompt too, like its vision and README, and it covers only its own folder: it assumes the levels above exist, names what it takes from them, builds the rest and lists its children's prompts in build order. Until a level's parts are designed, its prompt is only its How it works file. For the levels a domain defines below itself, that domain's `docs/doc-outlines.md` says what each prompt covers and how long it is.

An app in `apps/` has its own prompt. For our own app it is the exact spec of its parts. For an outside app it gives the source, how to fork it (our `main`, an `upstream` branch that follows the source), the commit to start from, every change we made, and how to set it up, run and test it; it does not describe the outside code file by file.

## Length

| Level | Length |
|---|---|
| System | about 8,000 to 15,000 words |
| Domain | 2,000 to 4,000 words |
| Levels below a domain | as that domain's `doc-outlines.md` says |
| App | 300 to 3,000 words |

Every word must help the agent build the right thing. Long is fine; vague is not.

## How to write it

This doc is written for AI, so the rules for docs for people bend here; the knowledge base agent's other rules still hold.

- **Instructions, in the second person and the imperative:** "Create `agents/system/configs/system.config.json` with these keys."
- **Exact everywhere.** Real paths, file names, keys, formats and name patterns, the same as in the tree notes, character for character. When the tree notes give a format, give it here with a short example.
- **Complete.** Every part in the tree is covered. If the agent would have to guess, the prompt is not finished: give the detail, or say that the point is open and what to leave in its place.
- **Status is explicit.** Build what is decided. Build our proposals as they stand, since they are part of the system today, and mark them "default, the owner may change it". Never build an idea still being weighed or an open question: list them under "Do not build".
- **No references from the notes.** No `[n]` numbers, decision or input codes, hashes or hidden tags: they mean nothing outside our notes. Name things by their paths.
- **No history.** Only the system as it is designed now.
- **Never a secret value.** Key names only, and where each key's value is loaded from.
- **Checks you can run.** Each check is a command or an observation with a clear pass: "the `check-links` script reports no broken link."
- **Same words** as the vision, the README and the glossary.

Too loose:

> Set up the configs for each agent.

Right:

> In every agent folder create `configs/[name].config.json` (the agent's settings), `configs/[name].workers.json` (every job the agent runs, one entry each with `enabled`, `id`, `purpose`, `type`, `schedule` and, for a script, `run`, for an AI run, `platform`, `model` and `prompt`) and `configs/[name].links.json` (every shared file the agent uses). `[name]` is `system` for the system agent, the domain's folder name for a domain, and the agent's name otherwise. Check: every file parses as JSON and the `check-links` script reports no broken link.

## Steps

### First build, or a full rebuild

1. Read the sources above.
2. In your notes (never in the doc), list every part and every file the prompt must cover, with its status (decided, proposed, open) and where it came from.
3. Write the doc section by section from that list. Take every path and format from the tree notes, never from memory.
4. Run the checks below.
5. Save the list with its sources in `sources/rebuild-prompt.md` in the notes, so the next update knows which sections a change touches.
6. Refresh the How it works panel of `rebuild-prompt.md` on the File Tree page (see "Its page on the File Tree").

### After every change

This runs every round that changes the system's design, last of all the docs.

1. Find the sections the change touches, using `sources/rebuild-prompt.md` in the notes. Always check the tree, the build order, the acceptance checks and "Do not build".
2. Rewrite those passages so the prompt still describes one system, as it is designed now. Remove what is no longer true.
3. A point the owner decided leaves "Do not build" and goes into its part, the tree and the build order.
4. Run the checks and update `sources/rebuild-prompt.md` in the notes.
5. If the outline or the way the doc is kept changed, refresh the How it works panel too.

## Its page on the File Tree

Every file shows the same tabs on the File Tree page. For `rebuild-prompt.md`:

- **Example** shows the outline above: the sections of the file and what goes in each.
- **How it works** shows short, plain answers under fixed headings, for someone who sees the project for the first time. They live in `rebuild-prompt.index.md` next to the doc. Write them with the `file-index` skill after every change to the outline or to the way the doc is kept:
  - **What it is:** one or two sentences.
  - **Who looks after it:** the knowledge base agent with this skill; the owner can also change it on the page.
  - **When and how it changes:** after every change to the system's design, last of all the docs, and the steps the agent takes.
  - **Who uses it, and when:** an AI agent rebuilding the system or checking it against its spec; the owner, to check it.
  - **Where it is mentioned:** the knowledge base agent's instructions and this skill, the vision and README skills' last steps, the file tree.
  - **Related knowledge:** the docs and notes it must agree with and what each adds.
  - **Keep in mind:** up to four lines, "When you ..., ...".
- **Questions** and **File** work as for every other file.

## Checks

- An AI agent that has never seen the project could build the system from this file alone without guessing. Read it once as that agent, step by step.
- Every path and name matches the tree notes; every format matches the topic notes.
- Every part in the tree is covered, and every build step has a check.
- Nothing still weighed or open is told to be built; every proposal is marked as a default.
- No `[n]` numbers, decision or input codes, hashes, hidden tags or history.
- No secret value anywhere.
- It agrees with the vision and the README.
- It is within the length for its level.
