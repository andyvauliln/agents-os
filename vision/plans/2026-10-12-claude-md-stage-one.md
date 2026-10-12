# Plan: CLAUDE.md for the system, the docs at every level, stage one

- Input: in-20261012-stage1 (2026-10-12), word for word in `docs/inputs/2026-10-12-claude-md-stage-one.md`
- Status: proposed, waiting for the owner's go
- Paths are from the top of the repository (the owner's `agent-oss/`).

## What the owner wants

When the owner starts Claude Code in `agents/system/`, it knows at once what the project is, which stage it is at and what to do next. It does that from `agents/system/CLAUDE.md`. That file points to the project docs, the system docs, the plain file tree and the IDE docs. Every doc is written again from all the information we have. The README also gets an ASD-STE100 version. Every file and folder has its metadata files, and the page shows a tab only when its file really exists. The prediction-market domain is emptied to its folders for stage two.

## Defaults we picked (say if you want another)

1. **Name of the AI rebuild doc:** you wrote `reverse-prompt.md`, and today it is `rebuild-prompt.md` (D-048). We keep `rebuild-prompt.md`.
2. **The ASD-STE100 README** is `README.asd.md`, next to `README.md` in every docs folder. On the page it is a tab named "ASD-STE100" on the README.
3. **Folder names under prediction-market** stay as they are now: `prediction-market/strategy-1-agent/pm-strategy-1.momentum-v1.opus55-test/`. You wrote `strategy-1/strategy-1.v1.Claude-Opus5.5/`. We rename only if you say so.
4. **Project level docs** go in a new `docs/` folder at the top of the repository. "Project" means the whole repository: agents, apps and how we work on it. "System" means the system domain in `agents/system/`.
5. **Metadata for every file:** every file and folder outside `vision/` gets `x.index.md` (How it works) and `x.meta.json` (Details), empty when nothing is written yet. `vision/` is the planning area and is left out.
6. **The real files become the source** for these docs. Their old drafts and every other doc move into `vision/`, and the build stops copying drafts over them.

## The files

| Level | Folder | Files (each with `.index.md` and `.meta.json`) |
|---|---|---|
| Project | `docs/` | `vision.md`, `README.md`, `README.asd.md`, `rebuild-prompt.md`, `file-tree.md` (plain paths, built) |
| System | `agents/system/` | `CLAUDE.md` (moves here from `agents/system/.claude/CLAUDE.md`) |
| System | `agents/system/docs/` | `vision.md`, `README.md`, `README.asd.md`, `rebuild-prompt.md` |
| Trading (general) | `agents/trading/docs/` | `vision.md`, `README.md`, `README.asd.md`, `rebuild-prompt.md` |
| Apps | `apps/docs/` | `vision.md`, `README.md`, `README.asd.md`, `rebuild-prompt.md` |
| Project IDE | `apps/project-IDE/docs/` | `vision.md`, `README.md` (the full IDE documentation), `README.asd.md`, `rebuild-prompt.md` |

Only these main docs and the two `.env` files also get their extra metadata files: `x.example.md` (Example tab; for `.env` it is `.env.example` with key names only) and `x.questions.md` (Questions tab). Other files get these later, when they need them.

## CLAUDE.md (agents/system/CLAUDE.md)

1. What the project is, in a few lines, and where we are: **stage one**.
2. Read first, in order: project vision, project README, system vision, system README, the file tree (`docs/file-tree.md`), the IDE docs (`apps/project-IDE/docs/README.md`).
3. Stage one, the current work: finish the project IDE; go through every file and folder, write custom views, make all metadata correct, and finish every doc at the project, system, trading and apps levels. The prediction-market domain and everything below it are stage two: do not touch them.
4. Rules from memory: decided only on the owner's word, never a key value, plain docs for people, the page tree always equals the disk, plan every change, ask before merging into main, and the rest.
5. After every input or update: file it word for word, then update the docs it touches in a fixed order, then the metadata, then rebuild and check the page, then commit.
6. When and how to update each doc: a table of which change makes which doc stale, and the skill that writes it.

## Skills (in `agents/system/.claude/skills/`)

- Revise `vision-doc`, `readme-doc`, `rebuild-prompt-doc` for the four levels, and `file-index` for all metadata files (`.index.md`, `.meta.json`, `.example.md`, `.questions.md`).
- New `readme-asd-doc`: writes `README.asd.md` from `README.md` in ASD-STE100 (the rules from the inputs vision), so the two can be compared.
- New `claude-md-doc`: writes and keeps `CLAUDE.md`.
- The file tree is built by the IDE build, not written by hand.

## Steps

1. Move every other doc into `vision/`: the topic notes in `agents/system/docs/` (architecture, conventions, flows, glossary, inputs vision and the rest), the old drafts, and the planning copies. Where two versions exist, keep the better one and fold the rest in.
2. Prediction market: delete every file under `agents/trading/prediction-market/`, keep the folders (each with a `.gitkeep`), and remove them from the build's planned list so nothing is created there again.
3. Create every file in the table, plus the metadata files, empty at first.
4. Revise the four skills and write the two new ones.
5. Write `CLAUDE.md` and every doc fresh from all the information: per level, vision, then README, then README.asd, then rebuild prompt. Order of levels: project, system, apps, project IDE, trading.
6. Write the metadata for the new docs and the `.env` files.
7. Page: a tab shows only when its metadata file exists, and it shows that file. New ASD-STE100 tab. Example and Questions tabs disappear where there is no file.
8. Build the plain `docs/file-tree.md`, rebuild the page, check page and disk are the same, publish, commit, open a PR.

## Open for the owner

- The three defaults above: the doc name, the folder names, and where the project docs go.
