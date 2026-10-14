# Agent OS: Knowledge base (v0.2)

This folder is the planning copy of the knowledge base. It holds everything we know about the system, split into layers so that one agent, the knowledge base agent [10.1.1.2] (D-033, D-034), can keep it right after every owner input or system change. In the repository (D-041) this guide and the records (`inputs/`, `decisions.md`, `changelog.md`, `file-tree.md`, the knowledge map) go to `apps/project-IDE/data/` [53.2], and the topic notes to `agents/system/docs/` [2]; the docs for people are in `agents/system/docs/` [2] too (D-047; they were in `.claude/docs/` [10.1.14]): the vision [2.2] first, then the README [2.1], and the rebuild prompt for AI [2.22] (D-048).

## Read order
<!-- k: id=readme-read-order applies=[2.1],[10.1.1.2] sources=D-033,in-20260930-1533 status=decided -->

1. `overview.md`: the whole system on one page.
2. `vision.md`: what the owner wants and why.
3. `architecture.md`: how the parts fit together.
4. `flows.md`: data flows and user flows, step by step.
5. `file-tree.md`: every folder and file, numbered [n], one section each.
6. `conventions.md`, `safety.md`, `data-schemas.md`, `glossary.md`.
7. `how-to/`, `common/`, `metrics.md`, `roadmap.md`.
8. History: `inputs/`, `decisions.md`, `changelog.md`. Indexes: `index/`.

## Layers
<!-- k: id=readme-layers applies=[2.1],[2],[10.1.1.2] sources=D-033,in-20260930-1533,in-20260930-1603 status=proposed -->

| Layer | Where | What it holds | Who writes it |
|---|---|---|---|
| Inputs | `inputs/` | Every owner input, word for word, with its categories and what it changed | knowledge agent, on receipt |
| File docs | `file-tree.md` §2 | One section per file or folder: purpose, contents, writers and readers, open questions | knowledge agent |
| Topic docs | `overview.md`, `vision.md`, `architecture.md`, `flows.md`, `data-schemas.md`, `conventions.md`, `safety.md`, `glossary.md`, `metrics.md`, `roadmap.md`, `how-to/`, `common/` | Knowledge that is about more than one file: concepts, rules, formats, flows | knowledge agent |
| History | `decisions.md`, `changelog.md`, `inputs/index.json` | What was decided and changed, when, and from which input | knowledge agent |
| Map | `index/knowledge-map.json` | Which knowledge applies to which file or folder (many to many), built by `tools/build_map.py` | the script |
| How it works files | `[name].index.md`, one per file and folder, named without the file's extension, with an empty `[name].meta.json` beside it (a mirror in `vision/tree/` while we plan) | "How it works" for every file and folder, written bottom up from the layers above, plus a "Keep in mind" list (when dealing with this, do that) | knowledge agent, `file-index` skill |

One fact lives in one place. A file doc says what the file is and points to the topic doc for the shared rule; the topic doc says which files the rule applies to. Decisions are history, not a separate kind of knowledge: the rule a decision made lives in a topic doc, and the decision entry records when and why.

## Knowledge tags
<!-- k: id=readme-tags applies=[2.1],[2.18.8],[10.1.2.1],[14.1] sources=D-033 status=proposed -->

Every section of a topic doc that holds knowledge starts with a tag on the line after its heading:

```markdown
## Links file per agent
<!-- k: id=links-file applies=name:*.links.json,[14.1],[10.6] sources=in-20260930-1112,D-031 status=decided -->
```

- `id`: kebab-case, unique across the whole knowledge base.
- `applies`: comma-separated, no spaces. Each item is one of:
  - `[n]`: the object numbered n in `file-tree.md`.
  - `[n]/**`: the folder [n] as a whole. The knowledge is shown on [n] directly and on everything inside it as "from the folder above".
  - `path:<glob>`: every node whose path (without `agent-os/`) matches, e.g. `path:agents/**/configs/*.links.json`. `*` matches within one name, `**` across folders.
  - `name:<glob>`: every node whose name matches, e.g. `name:init.sh`, `name:*.workers.json`.
  - `none`: background knowledge that belongs to no single file (still shown on the root).
- `sources`: input ids (`in-YYYYMMDD-HHMM`), decision ids (`D-0xx`), or `derived` for our own synthesis.
- `status`: `decided` (owner said so), `proposed` (our idea, waiting for the owner), `open` (a question), `retired` (kept for history).

The section runs until the next heading of the same or a higher level, or the next tagged heading. Untagged headings (intros, changelogs) are not knowledge entries. `file-tree.md` object sections (`### [n] ...`) need no tag: each one is the file doc of the objects in its heading.

## Map and summaries
<!-- k: id=readme-map-summaries applies=[2.1],[2.18.8],[10.1.2.2],[14.1] sources=D-033,in-20260930-1533 status=proposed -->

`python3 tools/build_map.py` reads every doc here plus `file-tree.data.json` and writes `index/knowledge-map.json`:
- `entries`: every knowledge entry with its doc, heading, status, sources, hash and the nodes it resolves to.
- `nodes`: for every file and folder, its file doc, the entries that apply directly, the ones inherited from folders above, its children, and the `basis` hash its summary must match.
- `inputs`: every archived input and what it was processed into.
- `problems`: tags that do not resolve, duplicate ids, nodes with no knowledge at all.

Every file and folder has its How it works in its own Markdown file (D-039): `vision.index.md` next to `vision.md` (the file's name without its extension, D-057), `f/f.index.md` inside a folder `f/` (while we plan, in the mirror `vision/tree/agent-os/...`, through `tools/index_files.py`). The front matter carries `basis`, a hash of the node's file doc, the entries that apply to it directly and its children's How it works texts. When the basis in the map differs from the one stored in the file, the file is stale and gets rewritten, children first. A child that comes out unchanged stops the ripple there. `index/summaries.json` (D-033) is retired.

## The flow for every input or change
<!-- k: id=readme-flow applies=[2.1],[2.10],[10.1.1.2],[10.1.2.1] sources=D-033,in-20260930-1533,in-20260930-1841 status=decided -->

Every owner input (project chat, a thread, the File Tree page) and every change to the system goes through the `knowledge-intake` skill:

1. Store the input word for word in `inputs/` and add it to `inputs/index.json` with its categories. When the input is a question, store the answer with it: an answer is knowledge too.
2. Extract the knowledge in it: new facts, rules, formats, changes, questions answered, questions raised. For a question, extract from the answer as well; a question also shows where the docs were unclear, so the place that should have answered it gets clearer.
3. Place each piece: find the entries and file docs it touches through the map; update them in place, or add a tagged section to the right topic doc, or create a new doc when nothing fits (and add it to this README).
4. Ripple: every other entry and file doc that states the same thing is brought in line, so there are no two versions of one fact.
5. Record: a `decisions.md` entry when the owner decided something, a `changelog.md` line, and `processed_into` on the input.
6. Rebuild the map, then run `file-index` on every stale node, bottom up, up to the root.
7. Rebuild the explorer data and republish the page.

## Changelog
- v0.2 (2026-09-30): answers to the owner's questions are inputs too; every summary can carry an "Always keep in mind" list (in-20260930-1603, in-20260930-1841).
- v0.1 (2026-09-30): knowledge base created from `vision.md`, `overview.md`, `feature-map.md`, `file-tree.md` and the 41 owner inputs so far (D-033).
