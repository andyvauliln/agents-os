# Project IDE: records

This folder holds the records of the project: what the owner said, what was decided, what changed and what was planned. The knowledge base agent writes them; the docs for people are built from them and live in the `docs/` folders at each level.

## What is here

| Where | What it holds |
|---|---|
| `inputs/` | Every owner input, word for word, one file each, with a row in `inputs/index.json` (its categories and what it changed). When the input is a question, the answer is stored with it. |
| `decisions.md` | Every decision the owner made, numbered, with the input it came from. |
| `changelog.md` | Every change to the project, newest first. |
| `plans/` | Every change plan, one file each, with a row in `plans/index.json` (its status, inputs and decisions). |
| `archive/` | Records that are kept but no longer used, one folder per date. |
| `sources/` | Earlier knowledge notes, kept but not referenced by any doc, skill or agent, and the earlier prediction-market metadata files kept as plain data (`sources/prediction-market/metadata/`). |
| `overrides.json` | The owner's kept edits of the extra tables on the File Tree page. |
| `page-store/` | On the owner's server only: the notes, edits and messages left on the page, one file each, until the next sync. |

## How they change

Every owner input goes through the `knowledge-intake` skill: it is stored word for word in `inputs/`, its knowledge goes into the docs and the metadata files it touches, a decision gets an entry in `decisions.md`, and the change gets a line in `changelog.md`. A change that alters the system is planned first with the `change-plan` skill, in `plans/`.

The records are history. Never change the owner's words in a stored input, and never rewrite an old decision or changelog entry: add a new one.
