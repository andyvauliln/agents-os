# The runtime

## What the runtime is
The runtime is two files: index.html and state-core.js. They are the only code that is not in the state. Do not change them for a change of the page: change the state.
- index.html: a title, a small base style, an empty <div id="index-view"> and 2 scripts. The second script is the runtime.
- state-core.js: the library of the runtime (window.StateCore). It has no access to the page.

## What index.html does
1. It wraps the browser functions that add event listeners, timers, observers and connections. It does this before other code of the page runs, so environment can show each one and who added it.
2. It downloads state.json and connects to the page database (window.claude.use('db')). Without a database it uses a memory store: saves stay only until the page reloads.
3. It reads the saved versions. With no versions, it saves state.json as version 1. The newest version becomes the live state.
4. It calls extension.functions.render for index-view. All the rest of the page comes from the state.
5. It follows the database: a newer version that is saved somewhere else runs at once (loadNewerVersion). Each view keeps its ui-data. A draft in the state view stops this.

## os: what each function gets
- os.get(path), os.set(path, value), os.replace(state): read and write the live state.
- os.call(name, input, viewPath): run a function. ctx.call(name, input) runs one in the same view.
- os.template(html, data): fill a template. os.bind(root, viewPath): connect the data-call buttons under root.
- os.mounted(path), os.setMounted(path, on): which views are on the page.
- os.watch(viewPath, fnName): run that function after each top-level call.
- os.refs: what a view keeps that cannot be in the state.
- os.calls: the record of each call of this page load. os.started: when the runtime started.
- os.history: the versions (commits), and put to save a new one.
- os.preview(frame, state, viewPath, id): run one view in a frame with a copy of the state. Nothing is saved.
- os.runTests(): run the tests that are written in the state.
ctx is the call itself: ctx.root (the root element of the view), ctx.call, ctx.input, ctx.id.

## A call
1. The runtime finds the function (a local function in its view first, then by its path).
2. It writes network and environment into the state, and takes a copy of the state (before).
3. It loads the imports of the function (see functions.md), then runs the code with the input.
4. It takes a copy of the state again (after). It compares before and after with expected-state-change.
5. It writes output, errors and performance into the function. It records the call in os.calls: name, input, output, ok, error, ms, related (fn, parent, stateChanges).
6. After a top-level call (a call that nothing else called), it runs the functions that the views watch.
7. It writes the call records to calls/<session> in the database, 1.2 seconds after the last call.

## state-core.js
- Paths: getPath, setPath, walk, clone, stripRuntime.
- JSON: parseJsonc (JSON with comments), autofix, patchText (changes a text and keeps its comments and layout).
- Templates: template, brief, ago, emptyText.
- Diffs: diff, summarize, changesView, pairAt.
- Versions: makeCommit, commitId.
- The editor: spans, filterLines, keyOverlay, mdParse, mdText, mdLine.
- Tests: checkExpect, checkStateChange.
- The call tracker: createTracker.

## Storage
- On claude.ai: the page database (db capability). commits/<id> for the versions, calls/<session> for the call records. A version bigger than 256 KB keeps its state in a file of the page (assets capability).
- Not on claude.ai: a memory store. The page works, but a save stays only until the page reloads.
- The capabilities of the artifact: db, downloads, assets, comments, mcp (Claude Code Remote, fire_trigger).

## Rules
- The runtime has no page content. It does not know the views.
- A change of index.html or state-core.js needs a new publish of the runtime before the next version.