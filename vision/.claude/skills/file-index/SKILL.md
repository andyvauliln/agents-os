---
name: file-index
description: Write and keep every metadata file of the Agent OS - the How it works file (x.index.md) and the Details file (x.meta.json) that every file and folder outside vision/ has, and the extra tab files that some items have (x.example.md, x.questions.md, README.asd.md next to a README, .env.example next to a .env) - named after the item without its extension, bottom up, so anyone can understand any part of the project in one read and the File Tree page shows a tab only for a file that exists. Use it after every change that makes a metadata file stale, and to fold in the owner's edits from the File Tree page.
---

# File index: the metadata files of every item

Every file and folder in the project has metadata files: small files next to it that describe it. Each one is a tab on the File Tree page. The page shows a tab only when its file exists, and it shows that file as it is.

| Tab | File, for `vision.md` | Who has it |
|---|---|---|
| How it works | `vision.index.md` | every file and folder outside `vision/` |
| Details | `vision.meta.json` | every file and folder outside `vision/` |
| Example | `vision.example.md` | for now only the main docs and the two `.env` files (for `.env` it is `.env.example`) |
| Questions | `vision.questions.md` | the main docs and the two `.env` files, and any item with a question: an open one for the owner, or one the owner asked |
| ASD-STE100 | `README.asd.md`, next to `README.md` | every `README.md` of the five doc levels |
| File | the item itself | every file |

The main docs are the four docs of each of the five doc levels: `vision.md`, `README.md`, `README.asd.md` and `rebuild-prompt.md` in `docs/`, `agents/system/docs/`, `agents/trading/docs/`, `apps/docs/` and `apps/project-IDE/docs/`, and `agents/system/CLAUDE.md`. Other items get an Example or Questions file later, when they need one; until then they have no such tab. A How it works or Details file may be empty until it is written: the item still has it.

`README.asd.md` is a main doc in its own right, with its own How it works, Details, Example and Questions files (family `README.asd`), and the page also shows it as the ASD-STE100 tab of the README next to it. It is written with `readme-asd-doc`, not with this skill.

The prediction-market domain and everything below it are stage two: only their folders exist, and no metadata file is made inside `agents/trading/prediction-market/`, except in its `docs/`, which holds the trading notes; every file and folder there has its metadata files like any item. The full metadata logic, in ASD-STE100, is in `docs/metadata.md`; keep it true when this skill changes. The planning area `vision/` is left out too: its drafts keep the metadata files listed below, but no other item there needs them.

## Names

A metadata file is named after its item without the item's last extension, and sits next to it. A folder's metadata files sit inside the folder and use the folder's name.

| Item | Its metadata files |
|---|---|
| A file `vision.md` | `vision.index.md`, `vision.meta.json`, and where they exist `vision.example.md`, `vision.questions.md` |
| A file without an extension, `.gitignore`, `.env` | the name stays whole: `.gitignore.index.md`; `.env.index.md`, `.env.meta.json`, `.env.questions.md`, and `.env.example` for its Example |
| `README.asd.md` | family `README.asd`: `README.asd.index.md`, `README.asd.meta.json`, `README.asd.example.md`, `README.asd.questions.md` |
| Two files whose names would share one (`run.js` and `run.py`), or a file named like its folder (`server/server.py`) | each keeps its extension: `run.js.index.md`, `server.py.index.md` |
| A folder `configs/` | `configs/configs.index.md`, `configs/configs.meta.json` |
| The top of the repository | `agent-os.index.md`, `agent-os.meta.json` |
| A placeholder `[agent-name]/` | `[agent-name]/[agent-name].index.md`, describing the pattern |

In a name, `|` becomes `-` and `, ` becomes `+`. The endings `.index.md`, `.meta.json`, `.example.md`, `.questions.md` and `.asd.md` are reserved for metadata. A metadata file has no metadata files of its own, except `README.asd.md`, which is a main doc.

## Where the source is, while we plan

- **How it works and Details.** The source is in `vision/`. For an item whose draft lives in `vision/` (the helper agents and skills in `vision/.claude/`), the two files sit next to the draft. For every other item they sit in the mirror of the tree, `vision/tree/agent-os/<path of the item>/...`. The build step `vision/tools/materialize.py` copies each one next to its item in the repository, inside a folder or beside a file, and makes an empty pair for any item outside `vision/` that has none. Always edit the source in `vision/`: a copy next to the item is written over at the next build. The owner's server writes a How it works edit from the page into both. `vision/tools/index_files.py` knows every path (`index_path(node)`, `meta_path(node)`; the drafts are listed in `DRAFTS` and `DRAFT_DIRS`).
- **Example, Questions and `.env.example`.** These sit only next to the item, in the repository. There is no copy in the mirror.
- When the repository becomes the source, the mirror is retired and every metadata file is edited where it sits. In the repository the build tools are in `agents/system/.claude/skills/ide-build/scripts/`.

## How it works: `x.index.md`

It answers, for someone who sees the project for the first time, what the item is, who looks after it, when it changes, who uses it and what to keep in mind. Every agent reads a folder's How it works before it works in that folder.

It is built from three things: the item's own notes (its section in the tree notes `vision/docs/file-tree.md`), the knowledge that applies to it, and the How it works files of its children. So a folder's file sums up what is inside it, and the top's file sums up the whole project.

```markdown
---
about: agent-os/agents/system/docs/README.md
node: n-2.1
written: 2026-10-12T00:00:00Z
by: knowledge-base-agent
basis: 1a2b3c4d5e6f
confirmed: 2026-10-12T09:40:00Z
---
# README.md

## What it is

One or two sentences.

## Who looks after it
## When and how it changes
## Who uses it, and when
## Where it is mentioned
## Related knowledge

## Keep in mind

- When you ..., ...
```

- **Front matter.** `about` is the item's path from the top, starting with `agent-os/`; `node` is its id on the File Tree page; `written` and `by` say when and who. You write these four. `basis` (the hash of what it was written from) and `confirmed` (when someone checked it and it is still right) are set by `build_map.py`, never by hand.
- **The six fixed headings**, in this order, then **Keep in mind** last with zero to four lines. Files not yet moved to this format have one `## Summary` instead; move each one when its item is next worked on.
- Nothing else goes in: no other headings, no notes for agents, no history.

**What goes under each heading** (a doc's own skill adds specifics in its "Its page on the File Tree" section):

| Heading | What it says |
|---|---|
| What it is | What it is and what it is for, in one or two sentences. |
| Who looks after it | The agent and the skill responsible for it; the owner when they change it on the page. |
| When and how it changes | The kinds of input or event that change it, and the steps in a few words. |
| Who uses it, and when | The people and agents that read or update it, and at what moment. |
| Where it is mentioned | The files that point to it or build on it. |
| Related knowledge | What else must agree with it, and what each adds. |

Each heading gets one to four sentences or a short list, for a reader who is not technical.

**Keep in mind:** zero to four lines, each "When you <deal with this in a certain way>, <do this>." Only rules that apply here and that someone working on it would get wrong otherwise, taken from the knowledge that applies (safety and conventions first), never invented. Folders keep only rules for the folder as a whole; the top keeps the short project-wide list. No list is better than an obvious one.

**Length:**

| Item | Length |
|---|---|
| File, link, placeholder (`## Summary`) | 1 to 4 sentences, at most 80 words |
| Folder (`## Summary`) | 2 to 6 sentences, at most 130 words |
| Level folders, `agents/`, `apps/`, the top | at most 200 words; may end with a short list of the main parts |
| Six-heading format | each heading 1 to 4 sentences or a short list |

## Details: `x.meta.json`

Everything about the item that is neither its content nor its explanation. It is for agents and for the page: the Details tab shows it in plain words, with the related files as links and the decisions by their titles. An empty file (`{}`, or every field empty) is allowed until it is written. Keep every field of the schema, in this order:

| Field | Type | What it holds |
|---|---|---|
| `schema_version` | number | The version of this schema. Today `1`. |
| `about` | text | What the item is for, in one line. The page shows it under the title. |
| `kind` | text | `file`, `folder`, `file link` or `folder link`. For a link, `related` says where it points. |
| `state` | text | `written`, `empty` (exists, nothing in it yet), `stage two` (a folder kept empty for stage two) or `name pattern` (a placeholder such as `[agent-name]/`). |
| `status` | text | `decided` (the owner decided it), `proposed` (our idea, waiting for the owner) or `idea` (still being weighed). |
| `git` | text | `tracked`, or `ignored` (kept only on the machine, such as a `.env` file or `settings.local.json`). |
| `secret` | true, false or null | `true` when the item holds key values: they are never read, shown or written anywhere. `null` until filled. |
| `generated_by` | text or null | The script that builds the item, such as `vision/tools/materialize.py` for `docs/file-tree.md`. Nobody edits a generated item by hand. `null` when people or agents write it. |
| `writers` | list of text | The people, agents and scripts that write or change it. |
| `readers` | list of text | The people, agents and scripts that read it. |
| `changes_when` | text | What makes it change. |
| `related` | list of `{"path", "how"}` | The related items and how each relates: `reads`, `read by`, `writes`, `written by`, `links to`, `same format as`, `built from`, `documented in`, `checked by`, `tested by`, `summed up in`. |
| `sources` | `{"decisions", "inputs", "notes"}`, each a list | Where its knowledge comes from: decision codes (`D-064`), input ids (`in-20261012-stage1`) and note names or paths. Codes are fine here; they never go into a doc for people. |
| `update_with` | list of `{"path", "how"}` | What must change with it: for each related item, what to update and how when this item changes. An AI walks this list before it finishes any change. |
| `inherits` | list of text | The knowledge from every level above that holds for it, by note id. Built by the build script; do not fill it by hand. |
| `features` | list of text | The features it serves, by name. |
| `views` | list of text | The custom views that apply to it, its own and the shared ones. |
| `how_it_works` | object | The check of its How it works: `basis`, `written`, `by`, `confirmed`. Left `{}` until the build moves these here from the How it works front matter. |
| `tree_number` | text | Its number in the tree notes, such as `"2.1"`, for agents only; `""` when it has none. |

Example, for `agents/system/docs/README.md`:

```json
{
  "schema_version": 1,
  "about": "Every part of the system domain exactly, how the parts connect, and the path to each part's own docs.",
  "kind": "file",
  "state": "written",
  "status": "decided",
  "git": "tracked",
  "secret": false,
  "generated_by": null,
  "writers": ["knowledge-base-agent with readme-doc", "the owner, on the page"],
  "readers": ["the owner", "every agent", "Claude Code started in agents/system/"],
  "changes_when": "a part of the system domain is added, changed, moved or removed, after the system vision",
  "related": [
    {"path": "agents/system/docs/vision.md", "how": "built from"},
    {"path": "agents/system/docs/README.asd.md", "how": "summed up in"},
    {"path": "agents/system/CLAUDE.md", "how": "read by"}
  ],
  "sources": {"decisions": ["D-048", "D-064"], "inputs": ["in-20261012-stage1"], "notes": ["vision/docs/file-tree.md"]},
  "update_with": [
    {"path": "agents/system/docs/README.asd.md", "how": "written again from it with readme-asd-doc"},
    {"path": "agents/system/docs/rebuild-prompt.md", "how": "every changed path, name or format"}
  ],
  "inherits": [],
  "features": [],
  "views": [],
  "how_it_works": {},
  "tree_number": "2.1"
}
```

## Example: `x.example.md`

The structure of the item and what goes in each part. For a doc, it is the doc's outline from its skill (the "## Outline" block), adapted to the level: the headings in order, each with one line on what goes under it. For a settings file, every field with an example value and what it means. A folder has no Example.

For a `.env` file the Example is `.env.example` next to it: the key names only, grouped in the same sections as the real file, each with a one-line comment on what the key is for and every value left empty. Write it from `secrets.index.json` and the notes, never from the `.env` file: never open, read or copy a `.env` file, and never write a key value anywhere.

## Questions: `x.questions.md`

Two parts, always in this order (the full logic is in `docs/metadata.md`, Questions):

1. **Open questions for the owner**: questions an agent has for the owner, made by a plan (`change-plan`), by `make-questions`, or while a doc is written.
2. **The owner's questions**: every question the owner asked about the item, word for word, with its answer (written by `knowledge-intake`).


An open question is a short question with one sentence on why it matters, and where it came from when a plan made it. When there are none, that part says "None open." When the owner answers, the answer goes into the notes and the docs where it belongs (`knowledge-intake`), and the question leaves the open part.

An owner's question stays in the file for good, newest last, with its answer kept true: when a later change makes the answer untrue, update it and add "This changed later: ...". No decision codes or input ids in this file; dates are fine.

```markdown
# Questions: README.md

## Open questions for the owner

- Should the project IDE part list every tab of the page, or only the main ones? It decides how long this part is. From the plan: IDE manual.

## The owner's questions

### 2026-10-14: Terminal or page?

> what is a differnce if exist when we ll run agent from terminal claude code and when we make notes on ui?

The same Claude Code works on the same files. On the page every note is tied to one item and saved word for word at once; in the terminal you name the item yourself.
```

## Steps

1. `python3 vision/tools/build_map.py --stale` lists the How it works files that are missing or stale, children before parents. One is stale when its item's notes, the knowledge applying to it, or a child's How it works changed since it was written.
2. Take them in that order. For each one, run `python3 vision/tools/build_map.py --context <node>`, read all of it, and read the How it works file itself.
3. **Still true and complete:** collect its id for `python3 vision/tools/build_map.py --confirm <id> <id> ...`. That stops the ripple: its parent does not go stale because of it.
4. **Needs a change:** edit the source file. Keep the front matter, set `written` to now and `by` to your name, change the body, then run `--confirm <id>`. For many files at once, write a JSON file `{"<node id>": {"text": "...", "sections": [{"title": "What it is", "text": "..."}, ...], "keep": ["When you ..., ..."]}}` (no `sections` means a `## Summary` file) and run `BY=<your name> python3 vision/tools/build_map.py --set <file.json>`.
5. In the same pass, bring the item's Details file in line: every field true for the item as it is now, `related` and `update_with` complete.
6. For a main doc or a `.env` file, check its Example and Questions files: the Example still matches the outline or the key names, and every open question is still open.
7. Run `--stale` again: parents of changed files are now stale. Repeat until it prints nothing.
8. Run the build (`ide-build`), so `materialize.py` copies the files next to their items and the page shows the right tabs.

For many files, split the work by subtree: one worker per subtree writes it bottom up, leaving out the subtree's ancestors; then one pass writes the ancestors up to the top.

## When a metadata file goes stale

- **How it works:** its item's notes changed, the knowledge that applies to it changed, a child's How it works changed, or the owner edited it on the page.
- **Details:** the item was moved, renamed, made or emptied; who writes or reads it changed; a related item or a rule above it changed; a decision or input changed it.
- **Example:** the doc's outline in its skill changed, or the item's structure changed (for `.env.example`, a key was added, renamed or removed in `secrets.index.json`).
- **Questions:** a question was answered or a new one came up.
- **`README.asd.md`:** whenever its `README.md` changes, right after it (`readme-asd-doc`).

## The owner's edits on the page

The How it works tab on the File Tree page has an Edit button, like the File tab. The owner's edit is saved on the page at once and waits there for the next sync; on the owner's server it is written into the file at once.

1. At the sync, write the edited text into the source file as it is. Keep the front matter, set `written` to now and `by` to `owner`, then run `--confirm <id>`.
2. Treat the edit as an owner input (`knowledge-intake`): if it states a new fact or rule, place it where it lives in the notes, so the next rewrite keeps it.
3. Never drop the owner's words at a later rewrite. When the knowledge changes, edit around them and say so in your report.

## How to write it

The reader is the owner, or anyone new to the project, and any agent that needs to understand this part fast. It says how the thing works now.

- **Start with what it is and what it is for**, in one sentence, in plain words.
- **Then how it works:** what it holds or does, who writes it and who reads it, when it changes, what it connects to.
- **Folders sum up their children.** Group the children by what they do instead of listing every one; name the two to four that matter most. Never contradict a child's How it works: if they disagree, the children and the notes win, and the conflict goes in your report.
- **Say what is not settled.** When the item or a key detail is an idea or an open question, say so in plain words ("The format is still a proposal." / "Still open: who may retire an agent."). Never present an idea as decided. Say plainly when an item is stage two.
- **Knowledge from folders above** only when it changes how this item behaves ("Like every links file, it is only changed through relink.").
- **Placeholders** describe the pattern: "One folder per agent, named after it."
- **Links** say what they point at and why the agent needs it.
- The owner is "the owner" ("they" when a pronoun is needed).
- No decision or input codes and no hashes in How it works, Example or Questions. In the six-heading format, no reference numbers either; in a `## Summary` file, numbers like [2.1] only where they help the reader jump (the page makes them clickable). File and folder names in backticks. No em-dashes.

## Checks

- Every file and folder outside `vision/` and outside `agents/trading/prediction-market/` has its `.index.md` and `.meta.json`, and so does everything in `agents/trading/prediction-market/docs/`; nothing else inside the prediction-market domain has any.
- Every main doc and both `.env` files have their Example and Questions files; other items have a Questions file only when it holds a question, and no metadata file has metadata of its own (except `README.asd.md`).
- `--stale` prints nothing, and `python3 vision/tools/build_map.py` reports no missing files.
- No orphans: `python3 vision/tools/build_map.py --orphans` lists metadata files whose item is gone. Move them to `vision/archive/<date>/tree/`.
- Every `.meta.json` parses as JSON and has every field of the schema, or is empty.
- No `.env.example` holds a value, and no `.env` file was opened.
- Spot-check three How it works files against their `--context`: every claim is backed by the notes, an applying entry or a child's How it works; nothing decided is called an idea, or the other way round.
- The top and the level folders still read as one clear picture of the whole after the change.
- Every owner edit from the page is in its How it works file, word for word.
- On the page, each item shows exactly the tabs whose files exist.
