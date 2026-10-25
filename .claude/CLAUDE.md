# Agent OS

- `state.json`: the starting state. The page loads it once to make version 1.
- `index.html`: the page. It renders its header from the state (`extension.view.header-view`); the state view shows the state in an editor with history (←/→), a Changes view and Save, which commits a new version.
- `state-core.js`: the page's logic with no page code: diffs, the changes view, commits, history steps and the call log.
- `tests/`: `node --test tests/*.test.js` (set `CM_DIR` to a local codemirror@5.65.16 package to run the page test offline).
- On claude.ai the page keeps its data in the artifact's database: `commits/c000001`… (one per saved version: `n`, `parent`, `at`, `state`, `summary`, `paths`) and `calls/<session>` (every tracked call of one page load: `name`, `input`, `output`, `ok`, `error`, `ms`, `related`).
