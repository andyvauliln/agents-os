---
about: agent-os/apps/project-IDE/data/sources/prediction-market/metadata/
basis: 981c7ce4dc3d
written: 2026-10-14T20:00:00Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# metadata/

## What it is

Copies of the earlier How it works (`.index.md`) and Details (`.meta.json`) files of the prediction-market domain, in the folders its old files had: `.claude/`, `configs/`, `data/`, `docs/`, `logs/`, `research/`, `scripts/`, `strategy-1-agent/`, `tests/` and the top files such as `start`, `init` and `requirements`. They are plain data, kept for stage two.

## Who looks after it

Nobody writes it now.

## When and how it changes

It does not change until the owner starts stage two.

## Who uses it, and when

Nobody reads it now. The build lists every file in it as a plain file with its text: nothing inside gets metadata files of its own, and none of its files is an orphan.

## Where it is mentioned

It is described in its folder's How it works file `apps/project-IDE/data/sources/prediction-market/prediction-market.index.md`, in `docs/metadata.md` (section 3) and in `agents/system/.claude/skills/ide-build/scripts/README.md`.

## Related knowledge

The build treats it as data through the constant `KEPT` in `agents/system/.claude/skills/ide-build/scripts/index_files.py`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules") and `docs/metadata.md`.

## Keep in mind

- When you move or rename this folder, change `KEPT` in `index_files.py` in the same change, or the build makes metadata files for every copy inside.
