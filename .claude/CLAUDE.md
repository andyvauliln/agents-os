# Agent OS

The page runs from its state. `index.html` is only a runtime: it loads the newest saved version of the state, then renders `extension.views.index-view`; everything after that comes from the state. The docs in `docs/` tell how each part works (ASD-STE100); start with `docs/overview.md`.

## Where things are
- `state.json`: the state, made by `gen/make_state.py`. Never edit it by hand.
- `gen/`: the generator. `make_state.py` (views, functions, tests), `style_part.py` (base styles), `pseudo.py` (pseudo code of each function; change it when the code changes), `docs_part.py` (the docs; written to `docs/`), `performance.json` (times from the page test), `build.js` (the version document of a release).
- `index.html`, `state-core.js`: the runtime (`docs/runtime.md`). A change of them, or of `vendor/`, needs a publish of the runtime files before the next version.
- `tests/`: `node --test tests/*.test.js` (the page test needs Playwright with Chromium; about 7 minutes; do not run the generator while it runs).
- `scripts/run-log.js` and `.claude/agents/run-recorder.md`: the record of each agent run (`docs/agent-runs.md`).
- `vendor/`: CodeMirror 5.65.16 and js-beautify 1.15.1, not minified, each with its LICENSE.
- `docs/inputs.json`: the owner's inputs, cleaned and merged, with metadata. `docs/vision.md` comes from it.

## Code map (in `gen/make_state.py`)
- timeline-view `local.refresh` (about 2000 lines) holds the shared drawing helpers in `os.refs['timeline-view']` (`R`): `drawPair`, `drawChanges`, `kindView`, `drawPerformance`, `drawAgentRun`, `drawDetails`, `pairFrom`, `versionOf`, `showTip`; inside: `fileView`, `mdPane`, `jsonPane`, `codePane`, `pseudoView`, `viewPage`, `changedItems`, `changedKinds`, `touchesOf`, `runsOf`, `runDetails`.
- state-view `local.refresh` draws the bar, the tabs and the editor and calls those helpers; `local.edit` keeps the draft (`R.draft`, `R.draftFrom`), `local.save` saves it.
- The older notes of this file (before v48) are in git history (commit e57163b).

## Rules
- Do only what the owner asks. Name each new or removed state field and function, and why.
- Change the generator, not `state.json`. Then run `python3 gen/make_state.py` and the tests.
- `agents.agent-oss.files` is always the files of main (every file of the repo except `state.json`).
- All the data that a view shows is in its `ui-data`; what cannot be in the state is in `os.refs`.
- Run files and the state have no secrets, tokens or passwords, and run files have no file contents (paths and sizes only).
- Write the docs and each release `explain` in ASD-STE100.

## When a session changes files
1. Make the state and run the tests.
2. Commit to main and push (`git push origin main:agent-os`).
3. Record the run with the `run-recorder` subagent (`--from` the commit before the run, `--to` the new commit). Commit `runs/<session>-<run>.json`, make the state again, and commit.
4. Save the new version as `commits/cNNNNNN` (`docs/generator-and-release.md`): `node gen/build.js <previous commit.json> <release.json> <out dir>`; release.json has `request` (the owner's words), `session` (link) and `explain` (`[{part, before, now}]`). A big version keeps its state in a file of the page (`state_file`).
5. An open page runs the new version at once.
