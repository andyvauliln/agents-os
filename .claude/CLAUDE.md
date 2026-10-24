# Agent OS

This repository is the Agent OS project. Its state lives in one file, `state.json`, and the page `index.html` shows it.

## Files

- `state.json`: the project state. It is the source of truth; edit it, then rebuild.
- `index.html`: the published page. It is generated: never edit it by hand.
- `src/shell.html`, `src/state-view.css`, `src/state-view.js`: the page's parts. The state view is the collapsible, editable tree of `state.json`.
- `build.py`: puts `src/` and `state.json` together into `index.html`. Run `python3 build.py` after any change.
- `.claude/`: this file, settings, and the project's agents, commands, skills, hooks and output styles.

## Rules

- Keep `state.json` valid JSON with two-space indents, and keep key order: the page shows keys in file order.
- After changing `state.json` or `src/`, run `python3 build.py` and commit `index.html` with the change.
- The page is also published on claude.ai, and Save there changes only the published copy. When the owner says they saved edits on the page, copy that JSON back into `state.json`.
- Never put keys, tokens or passwords in `state.json`: the page shows everything in it.
