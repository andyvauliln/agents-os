# Agent OS

The project's state is in `state.json`. `index.html` shows it: a start page with one card per section, and a state view (the **State view** button) where you can fold and unfold objects, edit values and keys, add and remove entries, switch to raw JSON, and save.

- `state.json`: the state.
- `index.html`: the page, built by `python3 build.py` from `src/` and `state.json`.
- `src/`: the page shell, and the state view's styles and script.
- `.claude/`: Claude Code settings, instructions (`CLAUDE.md`), an agent, a command, a skill, a hook that rebuilds the page, and an output style.

The page is published on claude.ai at https://claude.ai/artifact/NaGjuUJ6hCkCZchVa8uPB6, where Save keeps your edits in the published page. Copy them back into `state.json` to keep the repository in step.
