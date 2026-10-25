# Agent OS

The page runs from its state. `index.html` is only a runtime: it loads the newest saved version of the state, then renders `extension.views.index-view`, and everything after that comes from the state.

- `state.json`: the starting state (version 1 when the page has no history yet).
- Views (`extension.views.*`): `mount` (CSS selector), `html` (a template: `${...}` sees the view's `ui-data` as `d`, `e()` escapes text), `css`, `ui-data`, `functions`.
- Functions (`extension.functions.*` and a view's `local.*`): `input`, `output`, `imports` (script URLs loaded first), `tests`, `expected-state-change`, `docs`, `performance` (`last`/`min`/`max`/`count` in ms), `code`, `calls`. With `code`, the code runs as an async body with `ctx`, `input` and `os`; with no code, the declared `calls` run in order. `output`, `performance`, each call's `output` and each test's `result` are filled in while the page runs.
- Buttons in a view's html call functions with `data-call="local.x"` (and `data-input` as JSON).
- Tests: `{ "before": {call: input}, "input": ..., "expect": { "output": {...}, "output-has": [...], "dom": [...], "dom-absent": [...] } }`.
- `state-core.js`: paths, templates, diffs, the changes view, commits, history steps, test checks and the call tracker.
- `tests/`: `node --test tests/*.test.js` (set `CM_DIR` to a local codemirror@5.65.16 package to run the page test offline).
- On claude.ai the page stores `commits/c000001`… (`n`, `parent`, `at`, `state`, `summary`, `paths`) and `calls/<session>` (each call: `name`, `input`, `output`, `ok`, `error`, `ms`, `related` with `fn`, `parent`, `stateChanges`, `performance`).
