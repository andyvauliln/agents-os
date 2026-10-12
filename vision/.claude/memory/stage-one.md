---
name: stage-one
description: Project is at stage one (D-064, 2026-10-12): CLAUDE.md in agents/system, docs at five levels, prediction-market is folders only until stage two
metadata:
  type: project
  modified: 2026-10-12T15:45:29.532Z
---
Owner 2026-10-12: the project is at **stage one**: finish the project IDE, make every file's metadata correct (custom views per file kind), finish the docs at the project (`docs/`), system, trading, apps and project-IDE levels. Prediction-market is **stage two**: only its folders exist (files in vision/archive/2026-10-12/prediction-market/); materialize.py makes nothing there (STAGE_TWO).

- `agents/system/CLAUDE.md` is the entry point (reading order, rules, round, doc-update table); kept with skill claude-md-doc.
- Each docs folder: vision.md, README.md, README.asd.md (ASD-STE100 twin, skill readme-asd-doc), rebuild-prompt.md, plus .example.md/.questions.md; these docs are real-file sources (edit in place), their metadata source is the mirror vision/tree/agent-os/.
- Page shows Example/Questions/ASD-STE100 tabs only when the file exists.
- Defaults built without the owner's answer yet: keep rebuild-prompt.md (owner wrote reverse-prompt.md), keep current pm folder names, project docs in top `docs/`.
- Auto mode blocks deletions: "delete" is done as git mv into vision/archive/<date>/.

**Why:** the owner wants Claude Code started in agents/system/ to know the project and its stage.
**How to apply:** don't touch prediction-market until the owner starts stage two; after any change follow CLAUDE.md's round. Related: [[planned-items-are-real-files]], [[file-tree-explorer-sync]].
