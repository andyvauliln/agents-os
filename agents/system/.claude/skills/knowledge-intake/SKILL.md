---
name: knowledge-intake
description: Process one owner input or one system change into the Agent OS knowledge base - store it, extract the knowledge, place it in the right docs, ripple it to every related file doc and topic, record it, rebuild the map and refresh the How it works summaries.
---

# Knowledge intake

Use this for every owner input (project chat, a thread, the File Tree page), every change to the system's files, and whatever a session learned about the system even when no file changed. The aim: every AI that later touches a file finds all the context it needs to change it precisely. The guide to your notes is the `README.md` in the notes folder (`apps/project-IDE/data/` in the repository, `vision/docs/` while we plan); read it first if you have not this session. It is not the people README in the system's `docs/`.

Paths below are relative to the planning folder `/mnt/project-files/vision/` (notes in `docs/`, scripts in `tools/`). In the repository the records (inputs, decisions, changelog, the tree notes, the map, sources) are in `apps/project-IDE/data/`, the topic notes in `agents/system/docs/`, and the scripts in `agents/system/.claude/skills/ide-build/scripts/`. Messages and edits from the File Tree page reach you through the project IDE agent's `ide-sync`, already saved word for word.

## 1. Store the input

For an owner input:
1. Pick its id: `in-YYYYMMDD-HHMM` from its UTC time; add `-2`, `-3` if that minute is taken (check `docs/inputs/index.json`).
2. Write `docs/inputs/YYYY-MM-DD-HHMM-<topic-slug>.md`: header lines (At, Where, Source, Ref, Categories, Summary), `## Raw input` with the text word for word inside a `~~~text` fence, `## Processed into` (filled in step 6). Never edit the raw text, typos included.
3. Add a row to `docs/inputs/index.json`: `id, at, where, source, ref, file, chars, categories (1-3 from the list at the top of the file), summary (one sentence), processed_into: []`.
4. **A question and its answer are one input.** When the owner asked something and Claude answered (in chat, in a thread, on the File Tree page), store the answer in the same file under `## Answer` and set `answered: true` on the row. The answer is knowledge: it goes through steps 2 to 7 like the owner's own words.

Page inputs: read the page database collection `inputs` (status `new`); each is one input, with the page assistant's `answer` when the owner asked something. The page's `changes` records show what the page already applied; treat those edits as the owner's proposal for the text, but place the knowledge yourself (an old page draft can carry text that later decisions replaced).

For a system change with no owner words (a file edited, added, moved or deleted by an agent or a person): do not create an input file. Note the change and its source (commit, file, agent) for step 6.

## 2. Extract the knowledge

Read the input against what the knowledge base says now. Write a short working list, one line per item:

- **statement**: the knowledge in one plain sentence ("An agent's ID starts with its domain code").
- **kind**: fact · rule · format · flow · rename/move · removal · decision · question answered · new question.
- **status**: decided (the owner said it) · proposed (your reading or a gap you fill) · open.
- **scope**: the files and folders it concerns, as [n] numbers or patterns.

Separate what the owner said from what you infer. For a question, extract from the answer too: what it says about how the system works is knowledge with the status of what it rests on (decided when it restates a decision, proposed when the answer suggested something new). A question is also a signal: the place in the docs that should have answered it was missing or unclear, so fix that place. **Every question gets a home:** write the explanation of how exactly that thing works where the owner should have found it (the How it works of the file it is about, or the topic note), and when the docs already cover it, check that they answer exactly what was asked and sharpen them if not. Record that place in `processed_into`. If the input contradicts a decided rule, keep the item and flag it for the owner in step 8 instead of choosing silently.

## 3. Find where each item lives

For each item, look before you write:
- `python3 tools/build_map.py --context <node>` for each node in scope: its file doc, the knowledge that applies directly and from folders above, its children.
- `grep -rn "<key term or old value>" docs/` for every place the same fact is stated.
- `docs/index/knowledge-map.json` → `entries[*].nodes` to see what else a section applies to.

Then choose one home per item:
- about one object only → its section in `docs/file-tree.md` (and its tree comment in §1 when the one-line summary changes);
- shared by several objects, a kind of file, or a mechanism → a section in the topic doc that owns the topic (see the layers table in `docs/README.md`);
- a format → `data-schemas.md`; a rule → `conventions.md` or `safety.md`; a sequence of steps → `flows.md` or a `how-to/` runbook; a term → `glossary.md`;
- nothing fits → a new section, or a new doc (tagged, and listed in `docs/README.md` read order and layers table).

## 4. Write

- Edit knowledge where it lives. Replace outdated text; do not append a second version next to the first.
- A new section gets a tag on the line after its heading: `<!-- k: id=<prefix>-<kebab> applies=<[n], [n]/**, name:glob, path:glob> sources=<input id>,<D-0xx> status=<decided|proposed|open> -->`. Keep `applies` precise: exactly the objects whose readers must know this.
- An existing section: extend `sources` with the input id, adjust `applies` and `status` if the scope or status changed.
- New objects in the tree: next free [n] (numbers are never reused), a tree line with a comment, and an object section. Removed or moved objects keep a one-line stub section.
- Keep the owner's words for names and concepts where possible. Call them "the owner" (they/them when a pronoun is needed).

## 5. Ripple

Every other place that states the changed fact must now agree. Check, in this order:
1. The grep results from step 3 (docs, tree comments, feature-map rows, how-to steps, glossary terms, examples in index lists).
2. Every node in the changed section's `applies`: does its file doc still read true?
3. Renames: grep the old name across `docs/`, and in the planning phase `tools/enrich.py` and `tools/tabs.py` (examples and field guides shown on the page).
4. Open questions the input answers: move them to resolved (or delete them) wherever they appear.
5. Related logic: the agents, skills, scripts, index lists and How it works files that depend on each changed file (from `--context`: the knowledge that applies to it, from every folder above included, and the sections that name it). Each must still be true, or it changes in this round.

## 6. Record

- The owner decided something → a `decisions.md` entry with the next D number: date, decision in one to three sentences, why, status, sources (input ids), applies, and the objects it changed. Superseded entries get "superseded by D-0xx".
- One line in `changelog.md`.
- Every doc you changed: bump its version and add a changelog line.
- The input's `processed_into` (index.json row and the input file): D ids, docs and [n] objects.

## 7. Rebuild and summarise

1. `python3 tools/build_map.py` and fix every problem it prints about the docs you touched.
2. Run the `file-index` skill until `python3 tools/build_map.py --stale` prints nothing.
3. Planning phase: rebuild the explorer data (`tools/README.md`) and republish the File Tree page; mark processed page inputs `status: processed` with `processed_into`.

## 8. Report

Two to five plain lines to the owner: what changed and where; what you marked proposed; the questions only the owner can answer (one line each, with your recommendation). No ids except [n] numbers.

## Checks before you finish

- The raw input is stored and unchanged; its row has categories, summary and processed_into.
- No two places state different versions of the same fact (grep the key terms once more).
- `build_map.py` prints no problem for the docs you touched, and `--stale` is empty.
- No secret values anywhere; nothing committed to git unless the owner asked.
