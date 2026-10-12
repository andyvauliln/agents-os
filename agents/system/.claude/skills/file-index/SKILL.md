---
name: file-index
description: Write and keep the "How it works" of every file and folder of the Agent OS, one Markdown file each, named after the file without its extension (vision.md has vision.index.md), bottom up, so anyone can understand any part of the system in one read. Use it after every change that makes an index file stale, and to fold in the owner's edits from the File Tree page.
---

# File index: How it works, one file each

Every file and folder in the Agent OS has its own How it works file. It answers, for someone who sees the project for the first time, what the thing is, who looks after it, when it changes, who uses it and what to keep in mind. The File Tree page shows it as the first tab of every file and folder, and every agent reads a folder's index file before it works in that folder.

A How it works file is built from three things: the object's own notes (its section in the file tree notes), the knowledge that applies to it directly, and the How it works files of its children. So a folder's file sums up what is inside it, and the root's file sums up the whole system.

Paths are relative to the planning folder `/mnt/project-files/vision/` (scripts in `tools/`). In the repository the scripts are in `agents/system/.claude/skills/ide-build/scripts/`, and every index file sits next to its real file.

## Where the file goes

| Object | Its How it works file |
|---|---|
| A file `vision.md` | `vision.index.md`, next to it: the file's name without its extension. |
| A file without an extension, `.gitignore` | `.gitignore.index.md`: the name stays whole. |
| Two files whose names would share one (`run.js` and `run.py`), or a file named like its folder (`server/server.py`) | each keeps its extension: `run.js.index.md`, `server.py.index.md`. Today only `apps/project-IDE/server/server.py`. |
| A folder `configs/` | `configs/configs.index.md`, inside it |
| The root | `agent-os/agent-os.index.md` |
| A placeholder `[agent-name]/` | `[agent-name]/[agent-name].index.md`, describing the pattern |

Every file and folder also has a Details file with the same name and `.meta.json` (`vision.meta.json`, `configs/configs.meta.json`), the page's Details tab; it is empty for now and filled in later (plan `plans/file-set.md`). This skill writes only the How it works file. An index or Details file has none of its own. While we plan, a file or folder that already exists as a draft keeps its index file right next to the draft: `.claude/docs/README.index.md`, `.claude/docs/vision.index.md`, the agent's and each skill's, and the `.claude/`, `agents/` and `skills/` folders. Everything else does not exist yet, so its index file sits in a mirror of the planned tree, `tree/agent-os/...`. `tools/index_files.py` knows every path (`index_path(node)`, `meta_path(node)`; drafts are listed in `DRAFTS` and `DRAFT_DIRS`; in a name, `|` becomes `-` and `, ` becomes `+`). When a new doc gets its first draft, add it to `DRAFTS` and move its index file next to it. When the repo is built, every index file moves next to its real file: a file nobody has written yet exists only as its index file, and a placeholder folder such as `[agent-name]/` holds only its index file.

## The format

```markdown
---
about: agent-os/agents/system/docs/README.md
node: n-2.1
basis: 1a2b3c4d5e6f
written: 2026-10-05T07:31:00Z
by: knowledge-base-agent
confirmed: 2026-10-05T09:40:00Z
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

- **Front matter.** `about` is the path it describes and `node` its id on the File Tree page. `basis` is the hash of what it was written from; `build_map.py` sets it, never by hand. `written` and `by` say when and who. `confirmed` is set when someone checked it and it is still right.
- **The six fixed headings**, in this order, are the format every file and folder moves to, one by one as its doc is rebuilt (`vision.md` and `README.md` first). Until then a file has one `## Summary` instead.
- **Keep in mind** comes last, with zero to four lines.
- Nothing else goes in: no other headings, no notes for agents, no history.

## Steps

1. `python3 tools/build_map.py --stale` lists the index files that are missing or stale, children before parents. One is stale when its object's notes, the knowledge applying to it, or a child's How it works changed since it was written.
2. Take them in that order. For each one, run `python3 tools/build_map.py --context <node>`, read all of it, and read the index file itself.
3. **Still true and complete:** collect its id for `python3 tools/build_map.py --confirm <id> <id> ...`. That stops the ripple: its parent does not go stale because of it.
4. **Needs a change:** edit the index file. Keep the front matter, set `written` to now and `by` to your name, change the body, then run `--confirm <id>` so the basis matches. For many files at once, write a JSON file `{"<node id>": {"text": "...", "sections": [{"title": "What it is", "text": "..."}, ...], "keep": ["When you ..., ..."]}}` (no `sections` means a `## Summary` file) and run `BY=<your name> python3 tools/build_map.py --set <file.json>`, which writes the index files from it.
5. Run `--stale` again: parents of changed files are now stale. Repeat until it prints nothing.

For many files, split the work by subtree: one worker per subtree writes it bottom up, leaving out the subtree's ancestors; then one pass writes the ancestors up to the root.

## The owner's edits on the page

The How it works tab on the File Tree page has an Edit button, like the File tab. The owner's edit is saved on the page at once and waits there for the next sync.

1. At the sync, write the edited text into the index file as it is. Keep the front matter, set `written` to now and `by` to `owner`, then run `--confirm <id>`.
2. Treat the edit as an owner input (`knowledge-intake`): if it states a new fact or rule, place it where it lives in the notes, so the next rewrite keeps it.
3. Never drop the owner's words at a later rewrite. When the knowledge changes, edit around them and say so in your report.

## How to write it

The reader is the owner, or anyone new to the project, and any agent that needs to understand this part fast. It says how the thing works now.

- **Start with what it is and what it is for**, in one sentence, in plain words.
- **Then how it works:** what it holds or does, who writes it and who reads it, when it changes, what it connects to.
- **Folders sum up their children.** Group the children by what they do instead of listing every one; name the two to four that matter most. Never contradict a child's How it works: if they disagree, the children and the notes win, and the conflict goes in your report.
- **Say what is not settled.** When the object or a key detail is an idea or an open question, say so in plain words ("The format is still a proposal." / "Still open: who may retire an agent."). Never present an idea as decided.
- **Knowledge from folders above** only when it changes how this object behaves ("Like every links file, it is only changed through relink.").
- **Placeholders** describe the pattern: "One folder per agent, named after it."
- **Links** say what they point at and why the agent needs it.
- The owner is "the owner" ("they" when a pronoun is needed).
- No decision or input codes and no hashes. In the six-heading format, no reference numbers either; in a `## Summary` file, numbers like [2.1] only where they help the reader jump (the page makes them clickable). File and folder names in backticks. No em-dashes.

**What goes under each heading** (the doc's own skill adds specifics in its "Its page on the File Tree" section):

| Heading | What it says |
|---|---|
| What it is | What it is and what it is for, in one or two sentences. |
| Who looks after it | The agent and the skill responsible for it; the owner when they change it on the page. |
| When and how it changes | The kinds of input or event that change it, and the steps in a few words. |
| Who uses it, and when | The people and agents that read or update it, and at what moment. |
| Where it is mentioned | The files that point to it or build on it. |
| Related knowledge | What else must agree with it, and what each adds. |

Each heading gets one to four sentences or a short list, for a reader who is not technical.

**Keep in mind:** zero to four lines, each "When you <deal with this in a certain way>, <do this>." Only rules that apply here and that someone working on it would get wrong otherwise, taken from the knowledge that applies (safety and conventions first), never invented. Folders keep only rules for the folder as a whole; the root keeps the short system-wide list. No list is better than an obvious one.

**Length:**

| Object | Length |
|---|---|
| File, link, placeholder (`## Summary`) | 1 to 4 sentences, at most 80 words |
| Folder (`## Summary`) | 2 to 6 sentences, at most 130 words |
| Agent level folders, `agents/`, the root | at most 200 words; may end with a short list of the main parts |
| Six-heading format | each heading 1 to 4 sentences or a short list |

## Checks

- `--stale` prints nothing, and `python3 tools/build_map.py` reports no missing files.
- No orphans: `python3 tools/build_map.py --orphans` lists index files whose object is gone. Move them to `archive/<date>/tree/`.
- Spot-check three files against their `--context`: every claim is backed by the notes, an applying entry or a child's How it works; nothing decided is called an idea, or the other way round.
- The root and the level folders still read as one clear picture of the whole after the change.
- Every owner edit from the page is in its index file, word for word.
