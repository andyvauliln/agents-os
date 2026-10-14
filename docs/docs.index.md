---
about: agent-os/docs/
node: n-57
basis: 7dfcaaae5eec
written: 2026-10-14T08:00:17Z
by: knowledge-base-agent
confirmed: 2026-10-14T10:21:35Z
---
# docs/

## What it is

The project docs: the folder that describes the whole repository and the way the Agent OS is built, read first by people and by every AI session. It holds the project vision, the project README, the README again in ASD-STE100, the rebuild prompt for the top level, a plain list of every path in the repository, and `metadata.md`, the full logic of the metadata files in ASD-STE100.

## Who looks after it

The knowledge base agent writes the four docs with its skills `vision-doc`, `readme-doc`, `readme-asd-doc` and `rebuild-prompt-doc`, and their metadata with `file-index`. The project IDE agent's `ide-build` writes `file-tree.md`. The owner can change any of them on the File Tree page.

## When and how it changes

The docs change when an input changes the project as a whole: its levels, its top folders, its way of working, its stage or its rules. They are written in a fixed order: vision, README, README.asd, rebuild prompt. `file-tree.md` is written again every round.

## Who uses it, and when

The owner reads it first, to see the whole project. Claude Code started in the system folder reads the vision and the README right after its entry file. An AI rebuilding the repository starts from the rebuild prompt.

## Where it is mentioned

`agents/system/CLAUDE.md` (the reading list), the front page, the system's vision and README, which sum up the project level, and the doc skills.

## Related knowledge

The docs of the levels below must agree with it: the system (`agents/system/docs/`), trading (`agents/trading/docs/`), the apps (`apps/docs/`) and the project IDE (`apps/project-IDE/docs/`). The records behind it are the owner's inputs and the decisions in `vision/docs/`.

## Keep in mind

- When a lower level changes something the project docs say, bring these docs in line in the same round.
- When you write the vision or the README here, keep to plain prose with no ids, codes or history.
- When you need `file-tree.md` changed, change the build, never the file.
- When a metadata rule changes, change `metadata.md` and the `file-index` skill together.
