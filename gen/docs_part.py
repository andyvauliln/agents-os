# The docs folder of the agent, in ASD-STE100 Simplified Technical English. Each file is its text.
# Examples show the real code of the functions, taken from this generator, so the docs and the state agree.

FENCE = "```"
def code(text, lang="js"):
    return FENCE + lang + "\n" + text + "\n" + FENCE

DIAGRAM = """<svg viewBox="0 0 780 500" role="img" aria-label="Architecture of Agent OS">
<defs><marker id="arrow-head" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="8" markerHeight="8" orient="auto"><path class="head" d="M0,0 L8,4 L0,8 z"/></marker></defs>
<rect class="box" x="20" y="20" width="140" height="56" rx="8"/>
<text class="title" x="36" y="44">Browser</text><text class="mono" x="36" y="62">opens the artifact</text>
<rect class="key" x="230" y="20" width="220" height="56" rx="8"/>
<text class="title" x="246" y="44">index.html (runtime)</text><text class="mono" x="246" y="62">+ state-core.js</text>
<rect class="box" x="540" y="20" width="220" height="74" rx="8"/>
<text class="title" x="556" y="44">Page database</text><text class="mono" x="556" y="62">commits/c000001 ... (versions)</text><text class="mono" x="556" y="78">calls/&lt;session&gt; (call records)</text>
<rect class="group" x="20" y="150" width="740" height="190" rx="10"/>
<text class="title" x="36" y="174">Live state (JSON): the newest version</text>
<rect class="box" x="36" y="188" width="320" height="136" rx="8"/>
<text class="title" x="50" y="210">extension.views</text>
<text class="mono" x="50" y="232">index-view   html, ui-data, functions</text>
<text class="mono" x="50" y="252">header-view  html, ui-data, functions</text>
<text class="mono" x="50" y="272">docs-view    html, ui-data, functions</text>
<text class="mono" x="50" y="292">state-view   html, ui-data, functions</text>
<text class="mono" x="50" y="312">local.init, local.save, ...</text>
<rect class="box" x="372" y="188" width="180" height="136" rx="8"/>
<text class="title" x="386" y="210">extension.functions</text>
<text class="mono" x="386" y="232">render</text><text class="mono" x="386" y="252">get-state</text><text class="mono" x="386" y="272">unmount</text>
<rect class="box" x="568" y="188" width="176" height="136" rx="8"/>
<text class="title" x="582" y="210">agents.agent-oss.files</text>
<text class="mono" x="582" y="232">docs (these docs)</text><text class="mono" x="582" y="252">.claude</text>
<rect class="group" x="20" y="400" width="740" height="84" rx="10"/>
<text class="title" x="36" y="424">Page (DOM): #index-view</text>
<rect class="box" x="36" y="436" width="200" height="34" rx="6"/><text class="mono" x="50" y="458">#header-view</text>
<rect class="box" x="290" y="436" width="200" height="34" rx="6"/><text class="mono" x="304" y="458">#docs-view</text>
<rect class="box" x="544" y="436" width="200" height="34" rx="6"/><text class="mono" x="558" y="458">#state-view</text>
<path class="flow" marker-end="url(#arrow-head)" d="M160 48 H228"/>
<path class="flow" marker-end="url(#arrow-head)" d="M450 48 H538"/><text class="num" x="470" y="40">1</text>
<path class="flow" marker-end="url(#arrow-head)" d="M610 94 V148"/><text class="num" x="618" y="126">2</text>
<path class="flow" marker-end="url(#arrow-head)" d="M340 76 V110 H462 V186"/><text class="num" x="350" y="102">3</text>
<path class="flow" marker-end="url(#arrow-head)" d="M462 324 V398"/><text class="num" x="470" y="366">4</text>
<path class="flow" marker-end="url(#arrow-head)" d="M136 434 V326"/><text class="num" x="144" y="384">5</text>
<path class="flow" marker-end="url(#arrow-head)" d="M196 326 V360 H300 V340"/><text class="num" x="240" y="354">6</text>
<path class="flow" marker-end="url(#arrow-head)" d="M710 150 V96"/><text class="num" x="718" y="126">7</text>
</svg>"""


DOCS = {
"overview.md": """# Agent OS: overview

## What it is
Agent OS is a web page that runs only from its state. The state is one JSON document. It holds the views, the functions, the data and the files of the agent. The page has no other content.
An agent (Claude Code) changes the page. It changes the files of the repo, makes a new state, and saves it as a new version. An open page runs the new version at once.
You see everything that happens: each call, each change of the state, each request, and each agent run. You can edit the state on the page and save it as a new version.

## The main parts
- State: the JSON document. Its parts are agents, network, environment and extension. See state.md.
- Extension: the views and the functions of the page (extension.views, extension.functions). See extension.md and functions.md.
- Runtime: index.html and state-core.js. They load the state, run the functions, record each call and save the versions. See runtime.md and render-steps.md.
- Flow: what happens, in order, when the page opens, when you click, when you save and when an agent makes a new version. See flow.md.
- State view: the main view for the state and its changes, with tabs. See state-view.md.
- Timeline: the blocks of what happened since the page opened. See timeline.md.
- Network and environment: the requests and the browser, filled from code. See network-and-environment.md.
- Agent runs: the record of each agent run (runs/). See agent-runs.md.
- Recorder and notes: the record button and the Notes view. See recorder-and-notes.md.
- Generator and release: how the agent makes the state and saves a version. See generator-and-release.md.

## The other docs
- how-it-works.md: the architecture diagram, the parts and the rules.
- vision.md: where Agent OS goes, from the inputs of the owner.
- review-report.md: the review of v48: what was removed, the bugs, the speed and the proposals.
- inputs.json: the inputs of the owner (messages and page comments), cleaned and merged, with metadata.

## Words
- State: the JSON document that the page runs from.
- Version: a saved copy of the state (a commit, commits/c000001 and up, in the page database).
- View: one part of the page, with html, ui-data and functions.
- ui-data: all the data that a view shows.
- Function: code in the state that the runtime runs and records.
- Call: one run of a function.
- Block: one item of the timeline (a call that nothing else called, or a part of the page start).
- Agent run: one request to the agent, from a message to the next message.
- Release: the agent saves a new version made from the files of main.

## Where the files are
The repo is andyvauliln/agents-os, branch agent-os. The page is a claude.ai artifact.
- index.html, state-core.js: the runtime.
- state.json: the state (made by the generator).
- gen/: the generator (make_state.py, docs_part.py, pseudo.py, style_part.py, build.js, performance.json).
- tests/: the tests (state-core.test.js, page.test.js).
- scripts/run-log.js: reads the session log of an agent run.
- runs/: the run files.
- vendor/: CodeMirror 5.65.16 and js-beautify 1.15.1.
- docs/: these docs.
- .claude/: the default files of the agent (CLAUDE.md, settings, agents/run-recorder.md).""",

"how-it-works.md": """# How Agent OS works

## Architecture
""" + FENCE + "svg" + DIAGRAM + FENCE + """
1. The runtime reads all saved versions from the page database.
2. The newest version becomes the live state.
3. The runtime calls the function render for index-view.
4. render fills the html of a view with its ui-data and puts it into the element of the view.
5. You click a button. The button calls a function of its view.
6. The function changes the state, for example the ui-data of a view. Then the views show the new state.
7. The Save button of the state view saves the state as a new version in the page database.

## The parts
- The state is one JSON document. It holds all the data, views and functions of the page.
- The runtime is the file index.html. It loads the state and starts the first view. It has no page content.
- A view is one part of the page. A view has html, ui-data and functions. The html starts with one root element. The id of this element is the name of the view.
- A function is JavaScript code in the state. The runtime runs it and records the result.
- The code of a function starts with import lines. Each line names a thing that the function uses. The imports field of the function tells where each thing comes from.
- A version is a saved copy of the state. The page keeps all versions in its database.

## Where the parts are
- On the page, from the top: the timeline (when it is open), the header, one main view (docs, state or Notes), then the footer with the record button. Only one main view is open at a time: when you open one, the one that was open closes. Each main view has a close button (×). Each view uses only the space between the header and the footer. If its content is longer, it scrolls in that space.
- Views: extension.views.
- Shared functions: extension.functions.
- Files of the agent: agents.agent-oss.files. These are the files of main, except state.json (state.json is the state).
- These docs: agents.agent-oss.files.docs (docs/ in the repo).

## Rules
- All the data that a view shows is in the ui-data of that view.
- A function changes the state. Then the view shows the new state.
- The expected-state-change of a function tells which parts of the state it can change. If the function changes nothing, it is empty.
- After each run, the runtime updates the output, performance and errors of the function.
- When a newer version is saved in a different place, an open page shows it immediately. Each view keeps its ui-data. Unsaved edits in the state view stop this.
- To change the page, change the state and save it. Do not change index.html.

## Read more
overview.md lists all the docs. Each part of the page has its own doc: state.md, extension.md, functions.md, runtime.md, render-steps.md, flow.md, state-view.md, timeline.md, network-and-environment.md, agent-runs.md, recorder-and-notes.md and generator-and-release.md.""",

"state.md": """# The state

## What the state is
The state is one JSON document. The page runs only from it. All data, views and functions of the page are in it. A part of the page that is not in the state does not exist.
The state can hold comments (// and /* */). Save repairs small JSON errors first (autofix in state-core.js).

## The parts
The state has four parts at the top.
- agents: the agents and their files. agents.agent-oss.files is the files of main: each file of the repo, except state.json. A folder is an object. A file is its text. A folder with only .gitkeep is {}. agents.agent-oss.connection is for the connection of the agent (empty now).
- network: the requests of the page, by group (html, scripts, claude.ai, api, state, file code, packages, styles, other). The runtime fills them. See network-and-environment.md.
- environment: the browser and the server. The runtime fills the browser parts. The generator writes environment.server. See network-and-environment.md.
- extension: what the page is.
  - extension.views: the views (index-view, header-view, docs-view, timeline-view, state-view, recorder-view, notes-view). See extension.md.
  - extension.functions: the shared functions (get-state, render, unmount). See functions.md.
  - extension.data, extension.common_app_storage, extension.apps: empty now. They are for the data of the extension and its apps (see vision.md).

## Example
```json
{
  "agents": { "agent-oss": { "connection": {}, "files": { ".claude": { "CLAUDE.md": "..." }, "docs": { "overview.md": "..." } } } },
  "network": { "html": { "index.html": { "url": "index.html", "used_for": "The page itself", "expected": true } } },
  "environment": { "browser": {}, "server": { "machine": {}, "runtimes": {}, "repo": {}, "agent": {} } },
  "extension": {
    "views": { "header-view": { "html": "<header id=\\"header-view\\">...", "ui-data": { "state_open": false }, "functions": { "local.init": {} } } },
    "functions": { "render": {}, "get-state": {}, "unmount": {} },
    "data": {}, "common_app_storage": {}, "apps": {}
  }
}
```

## Fields that the runtime writes
After each run of a function, the runtime writes into the state:
- output: what the function returned (nothing = {}).
- errors: a throw, and each change that expected-state-change did not allow.
- performance: last, min, max and count, in ms.
- each declared call gets the output of its last run.
- network and environment, when a call starts and when it ends.
These fields are not changes of the state for a diff: stripRuntime in state-core.js removes them first.

## Versions
1. A version is a saved copy of the state. The page database keeps each version as a document commits/c000001, commits/c000002 and so on.
2. A version has n, parent, at, state, summary (added, updated, deleted) and paths (what changed). A release also has source (git, branch, message, request, session, explain).
3. A database document holds at most 256 KB. A bigger version keeps its state in a file of the page: state_file is the id of the file (served at /_blob/<id>). Without files (not an editor), the page saves stateGz: the state gzipped, in base64.
4. When the page opens, it runs the newest version. With no versions, it saves state.json as version 1.
5. Each page load also writes calls/<session>: the record of each call.

## Rules
- All the data that a view shows is in the ui-data of the view.
- What cannot be in the state (an editor, a recording, unsaved text) is in os.refs, never in the state.
- A function changes the state. Then the views show the new state.
- The state on the page and state.json in the repo are the same after a release.
- Change the generator (gen/), not state.json. See generator-and-release.md.""",

"extension.md": """# The extension: views and functions

## What the extension is
extension is the part of the state that is the page: the views and the functions. The runtime renders index-view first. index-view then renders the other views.

## Views
A view is one part of the page. It has three fields.
- html: a template. It starts with one root element. The id of this element is the name of the view (for example <header id="header-view">). ${...} sees the ui-data of the view as d. e() escapes text.
- ui-data: all the data that the view shows.
- functions: the local functions of the view (local.init, local.refresh, local.close and more).
render (in extension.functions) fills the html with the ui-data. It puts the root element in place of the empty element with the same id in the html of the parent view. Then it calls local.init of the view.

## The views now
- index-view: the page. Its html has the styles of all views and the empty elements of the other views. local.init renders header-view and recorder-view (the footer). header-view local.init renders the main view that is open.
- header-view: the header. Buttons: Device, Docs, State, and the timer of a recording.
- docs-view: the docs (agents.agent-oss.files.docs). A main view.
- state-view: the state and its changes. A main view. See state-view.md.
- timeline-view: the timeline above the header. state-view renders it. See timeline.md.
- recorder-view: the footer with the record button. See recorder-and-notes.md.
- notes-view: the notes. A main view. See recorder-and-notes.md.

## Buttons
A button calls a function of its view with data-call="local.x". data-input gives the input as JSON. os.bind(root, view) connects the buttons under root (not root itself). A view that draws itself again must bind again.
```html
<button class="btn" id="state-button" data-call="local.open.state-view">
<button role="menuitemradio" data-call="local.set-device" data-input='{"device":"mobile"}'>
```

## A view that watches
A view can watch the state: os.watch(view, 'local.refresh'). After each top-level call, the runtime runs local.refresh of each mounted view that watches. state-view, timeline-view, recorder-view and notes-view watch.

## Main views and layout
1. The page from the top: the timeline (when it is open), the header, one main view, then the footer with the record button.
2. The main views are docs-view, state-view and notes-view (MAIN_VIEWS). Only one is open at a time. When you open one, the one that was open closes. header-view ui-data docs_open and state_open follow this.
3. Each main view has a close button (×): #docs-close, #sv-close, #notes-close.
4. A view uses only the space between the header and the footer. Longer content scrolls in that space.

## Device
1. Click the Device button in the header (at the left of the Docs button). Its menu shows Mobile (390 px), Tablet (820 px) and Desktop (the full page). The device that shows now is blue.
2. Click a device. All the views show at its width, in the middle of the page. The views use the layout of that width, as on a phone or a tablet.
3. Desktop shows the views on the full page again. A click out of the menu, or Escape, closes the menu.
4. The ui-data of header-view keeps device (mobile, tablet or desktop) and device_open (the menu is open).
5. How it works: header-view local.init sets data-device on #index-view. Then #index-view is a container of that width. The generator adds an @container copy of each @media (max-width) rule, so the views use the layout of that width.

## Functions
A function is code in the state, with the data about it. Its fields are input, output, imports, tests, expected-state-change, docs, pseudo, performance, code and calls. See functions.md for each field, an example, the imports and the tests.
- Shared functions are in extension.functions: get-state (returns a part of the state), render (draws a view), unmount (removes a view).
- Local functions are in the functions of a view. Their names start with local. A button or ctx.call('local.x') calls them in their view.

## Rules
- A view gets all its data from its ui-data. A function that changes what a view shows changes its ui-data.
- expected-state-change tells which parts of the state a function can change. A function that changes nothing has {}.
- A view keeps what cannot be in the state in os.refs['<view name>']. The refs go when the view unmounts.""",

"functions.md": """# Functions

## The fields of a function
- input: the parameters of the function, with example values. For render, the parameter is view_path.
- output: the value that the function returned in its last run. If the function returns nothing, output is empty.
- imports: where each import line of the code comes from. "index.html" is the runtime. A URL loads a script. Source code is a module. A path in the state points to source code or URLs that the state keeps one time.
- tests: the checks for the function.
- expected-state-change: the parts of the state that the function can change, and how.
- docs: a short text that tells what the function does.
- pseudo: what the code does, step by step, in short lines with keywords (SET, READ, IF, ELSE, FOR EACH, CALL, DRAW, WATCH, WAIT, RETURN, THROW). A line inside a step starts with 2 more spaces. When you change the code, change the pseudo code too.
- performance: the time of the last run, the shortest and longest time, and the number of runs. The unit is milliseconds.
- code: the function as JavaScript, with its name and its parameters.
- calls: the functions that this function calls, with their input and their last output.
- errors: the problems of the last run. The runtime writes this field.

## Example: get-state with all its fields
""" + code("""{
  "input": { "path": "extension.views.header-view" },
  "output": { "html": "...", "ui-data": { "docs_open": false, "state_open": false }, "functions": { ... } },
  "imports": { "os": "index.html" },
  "tests": {
    "reads header-view": { "input": { "path": "extension.views.header-view" }, "expect": { "output-has": ["html", "ui-data", "functions"] } }
  },
  "expected-state-change": {},
  "docs": "Returns the JSON state: all of it, or the part at path (for example extension.views.header-view).",
  "pseudo": "READ the state at path (all the state when there is no path)\\nIF nothing is at path\\n  THROW \\"Nothing at <path>\\"\\nRETURN a copy of the value",
  "performance": { "last": 0.1, "min": 0.1, "max": 0.4, "count": 3 },
  "code": "import os from 'os';\\n\\nasync function getState({ path }) { ... }",
  "calls": {},
  "errors": []
}""", "json") + """
## How a function runs
1. A button, a key or a different function calls the function. A shared function has a path, for example extension.functions.render. A function of a view has a local name, for example local.save.
2. The runtime loads the imports. It gives each name of an import line its value.
3. The runtime runs the code with the input.
4. The runtime compares the state before and after the run.
5. The runtime checks the change against expected-state-change. A change that a called function made is not a change of the caller.
6. The runtime writes output, performance and errors.

## Imports
The code can use only what its import lines name. Each name must be in the imports field.
""" + code("""import os from 'os';
import ctx from 'ctx';
import core from 'state-core';
import CodeMirror from 'codemirror';""") + """
""" + code("""{
  "os": "index.html",
  "ctx": "index.html",
  "state-core": "extension.views.state-view.functions.local.init.imports.state-core",
  "codemirror": "extension.views.state-view.functions.local.init.imports.codemirror"
}""", "json") + """
- os comes from index.html. It is the live state and the page:
- os.get(path): the live state at a path. Without a path, all of the state.
- os.call(name, input, view): calls a function.
- os.template(html, data): fills an html template with data.
- os.bind(element, view): connects the buttons that have data-call.
- os.watch(view, name): runs the function name after each call.
- os.refs: data that the state cannot keep, for example the editor.
- os.history: the saved versions. os.preview: a page that runs one view with a copy of the state.
- ctx comes from index.html. It is this call:
- ctx.call(name, input): calls a different function and records the call.
- ctx.root: the element of the view of the function.
- state-core is a module. Its source is in the state one time, in local.init of state-view. The other functions point to it.
- codemirror is the editor. Its scripts are files of the repo (vendor/codemirror/5.65.16/, not minified), and the page loads them from its own files. The name CodeMirror is the editor that the scripts give.

## The rules of expected-state-change
- "changes": the value must change.
- "toggles": the value must change from true to false, or from false to true.
- "input.name": the value must become the input parameter with that name.
- "may change": the value can change.
- Other values: after the run, the value must be equal to this value.
- "*": all changes are permitted.

## Tests
- before: the calls that prepare the page for the test.
- input: the input for the function.
- expect: what must be true after the run. You can check output, output-has, dom, dom-absent, state and state-changed.
- The runtime also checks the errors of the run. A test with errors fails.
- The result of each test goes into the result field of the test.

## Example: a test of local.toggle-changes
""" + code("""{
  "turns the changes view on": {
    "before": {
      "extension.functions.render": { "view_path": "extension.views.state-view" },
      "local.filter-kind": { "kind": "all" }
    },
    "input": {},
    "expect": {
      "state": { "extension.views.state-view.ui-data.changes": true },
      "dom": ["#changes[aria-pressed=\\"true\\"]", "#tl-detail:not([hidden]) .st-legend, #tl-detail:not([hidden]) .tl-text"]
    }
  }
}""", "json") + """
1. before renders the state view and pushes All. Then ui-data.changes is false.
2. The runtime runs local.toggle-changes with the input {}.
3. The runtime checks that ui-data.changes is true, that the Changes button is pressed, and that the pane shows the changes.""",

"runtime.md": """# The runtime

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
- A change of index.html or state-core.js needs a new publish of the runtime before the next version.""",

"render-steps.md": """# How the page renders from the state

## When the page opens
1. The browser opens index.html.
2. index.html loads the library state-core.js.
3. The runtime connects to the database of the page.
4. The runtime reads all saved versions from the commits collection.
5. If there is no version, the runtime saves state.json as version 1.
6. The runtime reads the newest version. This is the live state.
7. The runtime calls extension.functions.render with view_path extension.views.index-view.
8. render reads the view from the live state.
9. render finds the element that has the name of the view as its id. For index-view, this is the empty element index-view in index.html.
10. render fills the html of the view with its ui-data. In the html, d is the ui-data and e() makes text safe.
11. The result starts with one root element that has the same id. This element replaces the empty element. Then render connects each button that has data-call to its function.
12. render calls the local.init function of the view.
13. local.init of index-view calls get-state for header-view. Then it calls render for header-view.
14. render does steps 8 to 12 again for header-view. The html of index-view has an empty element header-view. The root element of header-view replaces it. The header shows the Docs button and the State button.
15. local.init of header-view reads its ui-data. If docs_open or state_open is true, it renders that view.
16. After each call, the runtime writes the output, performance and errors of the function into the state.
17. The runtime keeps a record of all calls of this page load in the calls collection.

## Example 1: the runtime starts index-view (step 7)
The runtime makes this call. The input has one parameter, view_path.
""" + code("call('extension.functions.render', { view_path: 'extension.views.index-view' });") + """
## Example 2: render (steps 8 to 12)
This is the code of extension.functions.render. The import lines at the start name what it uses: os and ctx. Its imports field is { "os": "index.html", "ctx": "index.html" }, because the runtime index.html gives them. render returns nothing, so its output is {}.
""" + code(RENDER) + """
## Example 3: html and ui-data become the page (step 10)
1. The html of header-view starts with its root element. It has this button:
""" + code('<header id="header-view">\n  <button class="btn" id="state-button"\n          data-call="local.open.state-view"\n          aria-pressed="${d.state_open}" aria-label="State view" title="State view">', "html") + """
2. The ui-data of header-view is:
""" + code('{ "docs_open": false, "state_open": false, "device": "desktop", "device_open": false }', "json") + """
3. render replaces ${d.state_open} with the value from ui-data. The page gets this button:
""" + code('<header id="header-view">\n  <button class="btn" id="state-button"\n          data-call="local.open.state-view"\n          aria-pressed="false" aria-label="State view" title="State view">', "html") + """
## Example 4: local.init of index-view (step 13)
""" + code(INDEX_INIT) + """
The call to get-state returns the header-view part of the state. Its output is that JSON. This is the code of get-state:
""" + code(GET_STATE) + """
## Example 5: local.init of header-view (step 15)
""" + code(HEADER_INIT) + """
## When you click a button
1. The button calls the function in its data-call, with the input in its data-input.
2. The function changes the state. For example, local.open.state-view changes ui-data.state_open of header-view.
3. The function renders the views that must change.
4. The runtime compares the state before and after the call. It checks the change against expected-state-change.
5. The state view watches the state. After each call, its local.refresh function shows the new state.

## Example 6: you click the State button
1. The button has data-call="local.open.state-view". It has no data-input, so the input is {}.
2. The runtime runs local.open.state-view of header-view:
""" + code(open_view("state-view", "state_open")) + """
3. Before the run, ui-data.state_open of header-view is false. After the run, it is true.
4. The expected-state-change of the function permits this change:
""" + code('{ "extension.views.header-view.ui-data.state_open": "may change" }', "json") + """
5. render and local.init of state-view also change the state. These changes are their changes, not changes of local.open.state-view.
6. The runtime writes the result into the function: output is {} because the function returns nothing, performance gets the time of the run, errors is [].
7. render draws header-view again. Now the button has aria-pressed="true".

## Example 7: a button with input
The left arrow button of the state view has data-input. The input goes to the parameter delta.
""" + code("""<button class="btn" id="older"
        data-call="local.step" data-input='{"delta":-1}'>""", "html") + """
""" + code(STEP) + """
The expected-state-change of local.step is { "extension.views.state-view.ui-data.position": "may change" }. After the run, local.refresh shows the version at the new position.""",

"flow.md": """# The flows

## 1. The page opens
1. The browser downloads index.html. It downloads state-core.js and the scripts of claude.ai.
2. The runtime script runs (block "Run index.html"). It notes the start time and makes a session id.
3. loadState: the runtime downloads state.json, connects to the database and reads the versions. It parses the newest version.
4. The runtime calls render for index-view (via: start).
5. render fills the html of index-view and calls its local.init. local.init renders header-view and recorder-view.
6. header-view local.init renders the main view that its ui-data says is open (docs-view or state-view).
7. state-view local.init renders timeline-view, the editor and the tabs. Then the views that watch start to watch.
See render-steps.md for each step with the code.

## 2. You click a button
1. The button has data-call="local.x". os.bind connected it when the view drew.
2. The runtime calls local.x of the view, with data-input as the input (via: click).
3. local.x changes the state, for example the ui-data of its view, and draws what it must draw.
4. The runtime records the call: its changes, errors and time.
5. Then each view that watches runs local.refresh. The state view, the timeline, the footer and the notes show the new state.
6. The timeline adds a block for the call (the calls of the state view and the timeline only with Track this view).

## 3. You save the state
1. You edit the JSON in the state view. local.edit keeps the text as a draft.
2. You push Cmd+S or Ctrl+S, or click Save. local.save repairs small JSON errors.
3. local.save saves the text as a new version (commit n + 1) in the database.
4. The live state becomes the new state. The editor border is green for a short time.
5. If a newer version came during the draft, local.save does not save. The bar tells you to copy your edit and reload.

## 4. An agent makes a new version
1. You write a request (a message, a page comment or a note).
2. The agent (Claude Code) changes the generator, the runtime, the docs or the tests in the repo.
3. It runs python3 gen/make_state.py. This makes state.json and writes docs/.
4. It runs the tests: node --test tests/*.test.js.
5. It commits and pushes to the agent-os branch.
6. It records the run (runs/<session>-<run>.json), commits it, and makes state.json again.
7. It saves the new version in the page database: gen/build.js makes commits/cNNNNNN with source (git, request, session, explain).
8. An open page gets the new version at once (loadNewerVersion). The timeline adds a New version block and an AI run notification block.
See generator-and-release.md for the commands.

## 5. You look at what happened
1. Open the state view (the State button). Click the Timeline button.
2. Click a block. The state view goes to the version of the block.
3. Click Only changes to see only what the block changed. Each tab shows only its changes.
4. The Flow tab shows the calls inside the block, in order. The Agent Run tab shows the chosen agent run.

## Saved flows
The timeline keeps saved flows in timeline-view ui-data.flows: each has a name and the names of its blocks. The Flows button lists them. A click on the play button replays only those blocks. First enter is the page opening (its first 4 blocks).""",

"state-view.md": """# The state view

## Open the state view
1. Click the State button in the header.
2. The state view shows the chosen block of the timeline. When no block is chosen, it is the last agent run. The editor shows the state at the version of the block.
3. The state view is the one view for the state and its changes. It has two rows at the top.
   - The bar, from the left: the State icon with Agent or UI (the kind of the chosen block of the timeline: an agent run or a UI block; some logic of the UI is different for each), the filter, Only changes, Show empty, then Track this view, Timeline, Collapse all, Save and close (×). Put the pointer on an icon to see its name.
   - The tabs: Full State, Files, Views, Functions, Network, Environment, Performance, Improvements, Flow, Video, Docs and Agent Run.
4. Full State is the whole JSON of the state. The other tabs are parts or views of the same state:
   - Files, Views, Functions, Network and Environment: only that kind, as a tree on the left and the chosen one on the right.
   - Environment has two tabs: Browser (what the page finds in the browser) and Server (the machine where the agent works and makes the state: environment.server).
   - Flow: what happens inside the chosen block (its parts and its calls; an AI run shows its notification).
   - Agent Run: the AI run notification of the chosen AI run block, or of the last AI run.
   - Docs: only the docs folder of the agent. With Only changes: only the docs that the block changed.
   - Performance: the time of each function. The page test measures each version in a browser. The generator puts the times in performance.tests of each function (count, avg and max, in ms). The table shows the version on the screen, the version before it, the change (red is slower, green is faster) and the times of this page. Under it: the AI runs, with their time, steps and tokens.
   - Improvements and Video are empty for now.

## Edit and save the state
1. Edit the JSON in the editor. You can write comments with // and /* */.
2. Push Cmd+S or Ctrl+S, or click the Save button.
3. If the JSON has small errors, the save repairs them first.
4. The border of the editor becomes green for a short time. This shows that the new version is saved.

## Filter the state
1. Type in the filter at the top of the state view.
2. The editor shows only the entries whose path has the text, with the first and last lines of the objects around them.
3. The other lines fold into "⋯ N lines". You can still edit the lines that show.
4. Click the Files, Views, Functions, Network or Environment tab to see only that kind, as a tree: for example, Files shows the files in their folders. Click one in the tree to see it on the right. With Changes, an updated md file in read mode shows its changes: green lines are new or changed, red lines are removed. Put the pointer on a green or red line to see why the run changed the file. Click Full State to see the editor again. This works with or without text.
5. Click Only changes to see only what the chosen block changed. After Older or Newer, it is what the version on the screen changed. On a tab that is not a part of the state (Flow, Agent Run, Performance, Improvements, Video), Only changes goes to Full State. Each tab shows only its changes, and a tab with no changes hides.
   For an AI run, Full State also keeps the files that the run read or ran, and its default context (.claude/CLAUDE.md for the main agent, .claude/agents/<name>.md for a sub agent). Badges after the line of a file tell who (main or sub agent) and what (read, changed, run, default context).
6. Click Show empty to hide the entries with an empty value: {}, [], "" or null. They hide with no "⋯" mark. Click it again to show them.
7. Click Track this view to add what you do in the state view and the timeline as blocks of the timeline.
8. Push Escape to clear the filter.
- Older and Newer (the arrows with the version between them) are in the bar of the timeline. The arrow keys do the same. On a touch screen, swipe the timeline: right for older, left for newer.
- The version, the path and the status are in the bar at the bottom of the state view.

## Look at older versions
1. Open the timeline. Click its Older arrow, or push the left arrow key (or swipe the timeline to the right). The state view leaves the chosen block.
2. You cannot edit an older version.
3. Click Only changes to see only the changes of that version. Green is added, yellow is updated, red is deleted.

## Long text
- Long text, and text that has more than one line, shows as "...". A text of only {} or [] (an empty json file) shows as it is, in grey, and Show empty off hides it. Put the pointer on it to see the start of the text, in the colors of its kind (md, js, html, css or json).
- Click the "..." to open the text in the viewer. You can edit it there.
- When you close the viewer, your changes go into the editor. Then save them.

## Read and edit an md file
1. Click the "..." of an md file, for example agents.agent-oss.files.docs.how-it-works.md.
2. The file shows as a document. Click a line and edit the text there.
3. Push Enter to start a new line of the same kind: a new item, the next step, or a paragraph.
4. Push Backspace at the start of a line to remove its mark. Push it again to join the line to the line before it.
5. Click the arrow next to a heading to fold its section. Click it again to open the section.
6. Click a theme button above the document to change how it looks: Reader (the default, for long reading), White, Black, Sepia, Night or Mono. The theme stays in ui-data.md_theme.

## Try a view in the viewer
1. Click the "..." of the html of a view, for example extension.views.header-view.html.
2. The html is on the left. On the right, the view runs with a copy of the state.
3. Click a button of the view. The function of the button runs in the copy. Nothing is saved.
4. Below the view, you see the ui-data of the view. The lines that the last action changed are yellow.
5. Edit the html on the left. The view on the right starts again with the new html.""",

"timeline.md": """# The timeline

## The blocks
1. Open the state view (the State button in the header). Click the Timeline button at the left of its bar. The timeline shows at the top of the page, above the header. Click the button again to hide it.
2. It shows what happened since the page opened, as blocks in a row from left to right. The first block is the last AI run notification: the last agent run (if the state has one). Then: Network (every request and the environment), index.html runs, the runtime loads the state, the page starts.
3. Each next block is one call that nothing else called, for example a click on a button.
4. Each block shows its number, the time since the page opened, the function, its time in ms and how many state changes it made.
5. What you do in the state view and in the timeline (clicks on blocks, the replay, the buttons) is not a block. Turn on Track this view (in the bar of the state view) to add it as blocks too.
6. When the row of blocks scrolls, the last agent run stays at the left and the newest block stays at the right. These two pinned blocks are bigger than the others (wider and taller), with a thicker border.
7. Each AI run block is purple (its border and a light purple color). Each other block (a UI block: the page, the network, a click) is blue.
8. On a narrow screen (a phone), the blocks are smaller and show only their number and name, so that you can see at least 4 blocks.

## A block
1. Click a block. The state view shows it, and its bottom bar names it (for example "Block 3: Run index.html"). When no block is chosen, the state view shows the last agent run.
   The state view goes to the version of the block: the version that an agent run made, or that a New version brought. For the other blocks, it is the newest version.
2. Only changes (the button in the bar of the state view): the state cut down to what this block changed: green is added, yellow is updated (with the old value), red is deleted. Under it, a table says which function changed what.
   A long text, or a text of more than one line, shows as "...", as in the state view. Put the pointer on it to see its start. An updated text (and its "was "..."") shows its changes: red lines are removed, green lines are added. Click it to open the whole text in the viewer. Press Escape or × to close the viewer.
   Type in Filter paths (the filter of the state view) to see only the paths that have the text. The table shows only the paths that the filter shows.
   The tabs Full State, Files, Views, Functions, Network and Environment choose what shows. Full State shows the changes as above. Each other button shows only that kind, in its own view:
   - On the left: a tree of only what the block changed (for example the changed files, in their folders). A changed one has a dot and the color of its change: green added, yellow updated, red deleted. A folder that holds a change is yellow. For an AI run, the tree also has the files that the run read or ran, and tags after each one: who (main or sub agent) and what (read, changed, run, default context).
   - A tab with no changes in the block hides. The tab that is open stays.
   - On the right: the one that you click, in tabs. The first tab is its content: File (the text of the file), Page (a view as the page shows it), Function (its code and its other fields), Request (a request of network) or Value (a part of environment).
   - A view has the tabs Page, Source (its html, ui-data and functions) and Changes. Page shows the view with the style of the page. Its buttons do nothing: it is a picture. When the block changed the view, Page shows it before and after the block, side by side. index-view is the page: it shows with the views that are on the page now.
   - A function also has the Pseudo code tab: its docs, then what its code does, step by step. Each line has a number. The keywords have colors: IF, ELSE and FOR EACH (the flow) are purple, CALL is blue, SET, READ, DRAW and the other actions are green, RETURN and THROW are red. A line inside a step is indented, with a guide line.
   - When the block changed it, the Changes tab shows the change. A text (a file, html, code) shows side by side: red lines are only before, green lines are only after. An object shows cut down to what changed.
   - The filter text keeps only the items whose path has it.
   - A file shows in the file viewer for its kind. The head has the size and the tokens (about). The name and the kind are in the path above the viewer. The buttons are icons: put the pointer on one to see its name (Read, Source, Tree, Contents, Functions, Copy, Wrap, Open all, Close all, Full screen).
     - Contents (md) and Functions (code) are hidden at first. Click the button with the side panel icon to show them on the left, and again to hide them.
     - Full screen: the file viewer covers the page. Click Exit full screen or push Escape to go back.
     - md: reads as a page, with the look and the theme of the md viewer of the state view. Each theme has its own colors for the changes, so that you can read them in a light and in a dark theme. Contents lists the headings: click one to go to it. The Style select chooses the theme: Reader, White, Black, Sepia, Night or Mono. The theme stays in state-view ui-data.md_theme, so the md viewer of the state view uses it too. Source shows the text.
     - json: a tree. Click an object or a list to open or close it. The first two levels are open. Find opens the parts that have the text and marks them. Open all, Close all. Source shows the text.
     - Code (js, html, css, python and more): Functions lists the functions, classes and constants (ids, scripts and styles in html; selectors in css), each with its line. Click one to go to the line. Find marks every match: Enter goes to the next one, Shift+Enter to the one before. Wrap wraps long lines.
   - A click on "..." opens the text in the same file viewer.
3. Flow (a tab of the state view): what happens inside the block. The function, then each function it called, in the order they started, with their input and time.
   Each function says what it does (its docs), why it ran (a click, a watch, or the function that called it) and what it changed in the state. Click its name to see its code.
   The first blocks happen before any function runs, so they show their parts instead:
   - Run index.html: the runtime script runs. What it did, with times, the start time (os.started), the session id of the call log, the call tracker, and the functions in os.
   - Load the state: state.json downloads, the page connects to the database, reads the saved versions and parses the newest one. A version that is too big for one database document (256 KB) keeps its state in a file of the page (state_file), and the page downloads that file.
   Each part says what happens and why it is needed. Click a part to open it: it shows the lines of index.html that do it (with their line numbers), then what it made:
   - Run the runtime script shows what the runtime did, with times, and the code of the runtime script.
   - Note the start time shows the browser's timings. Make a session id shows the first record of the call log. Create the call tracker counts the calls by name. Build os lists what is in os: click one to see what it is for, which functions use it, how often they ran, and its code.
   - Download state.json shows state.json. Connect to the database shows where the versions and the call log are. Read the saved versions lists the versions. Parse the newest version shows the parts of the state and their sizes.

## The buttons
The buttons are above the blocks.
1. The arrow buttons show the block before and the next block.
2. The Replay button shows the next block every 1.6 seconds. From the last block, it starts again at the first. It goes on to the newest block. With Track this view on, each move adds a block, so it stops at the block that was the newest when it started. It also stops when you click it again, or when you click a block.
3. Older and Newer (with the version between them) go through the versions of the state view, as the arrow keys do. On a touch screen, swipe the timeline: right for older, left for newer.
4. AI runs shows only the AI run blocks. UI shows only the other blocks. Click the pressed button again to show all the blocks.
5. The Restart button reloads the page, so the history starts again. The timeline opens again on the last AI run notification. If the state has unsaved changes, it does not reload: save them first.
6. The Flows button opens the list of saved flows. Click the play button of a flow to replay only its blocks. First enter is the page opening: its first 4 blocks (index.html, runtime, loadState, the render of index-view).
7. The close button (×, at the right) closes the timeline. The Timeline button of the state view opens it again.
8. The timeline is part of the state view: when you close the state view, the timeline hides too.

## A new version
1. A Claude Code session changes the files of main. It commits the change, pushes it and saves a new version of the state.
2. An open page gets the new version and runs it immediately. You do not reload the page.
3. Each view keeps its ui-data. The views that were open stay open.
4. The timeline adds a New version block.
5. Only changes: the differences between the version that ran before and the new version. Long texts are cut.
6. Flow: where the version came from (the git commit, the request and the session), how each part worked before and how it works now, side by side, and each changed file side by side. Red lines are only in the old version. Green lines are only in the new version.

## Where it comes from
1. The timeline comes from the call log of the runtime (os.calls), not from the state. If the state kept the timeline, each call would change the state again.
2. The ui-data of timeline-view keeps the chosen block (selected; null is the last agent run), whether the replay runs (playing), show (all, runs or ui: the AI runs and UI buttons), flows_open, and the saved flows (flows: each has a name and the names of its blocks). The ui-data of state-view keeps timeline_open (the Timeline button), track_state (Track this view), changes (Only changes) and filter_kind (the tab).""",

"network-and-environment.md": """# Network and environment

## The browser
1. The state has two parts that the runtime fills: network and environment.
2. network has a group for each kind of request: html, scripts (our scripts), claude.ai (the scripts of the claude.ai artifact page, such as its database), api (the database calls), state, file code (code that the timeline downloads as text), packages, styles. Other requests go in other.
3. Each request has url, start (ms after the page opened), ms (download time), size (bytes), count, and parallel (what downloaded at the same time).
4. The state lists the requests that the page expects. Each has used_for (what the page uses it for) and expected: true. A request that is not in the list gets expected: false.
5. A request that this page load did not ask for (yet) has no values: count is 0.
6. environment has browser (name, version, system, screen, processor cores, memory, graphics card, connection and more), browser data (the storages and how much they use, also the claude.ai database: its versions and the call log of this page), browser api, document (title, elements, focus, fonts and more), window (sizes, scroll, origin and more), event listeners, timers, observers, connections, devices, permissions, subscriptions, background services and other.
   - event listeners: each element (or window, document) that has listeners, each event, how many, and who added them: the call that was running, or the page.
   - timers: the timeouts that wait, the intervals and the animation frames, with who added them.
   - observers: MutationObserver, ResizeObserver, IntersectionObserver and PerformanceObserver, with what they watch and who added them.
   - connections: the open WebSocket, EventSource and BroadcastChannel connections.
   - devices: how many cameras, microphones and speakers, the battery, gamepads, and which device APIs the browser has.
   - permissions: the state of each permission (granted, denied or prompt).
   The runtime finds listeners, timers, observers and connections because it wraps the browser functions that add them, before other code of the page runs. Code that ran before the runtime (the scripts of claude.ai) is not in these lists.
7. Each call writes network and environment into the state when it starts and when it ends. So the Changes of a block show what the block loaded and what changed around the page. expected-state-change does not check network and environment.
8. Block 1, Network, shows every request in its group: the url, the size, the time (in the version that this page loaded, now, and the difference), what downloaded in parallel, expected and used for. Click a request to see its code. A file on another address (cdnjs, Google Fonts) runs on the page, but the browser can stop the page from downloading it as text. Then the request shows why, and a link that opens the file. Environment is next to it. A yellow value is not the same as in the version that this page loaded.
9. When you save a version, it keeps network and environment as they are. The next page load shows the difference.

## The server
1. environment.server is the machine where the agent works and makes the state. The generator (gen/make_state.py) writes it each time it makes the state.
2. It has machine (os, arch, cpu_cores, memory_gb), runtimes (python, node, git), repo (the branch, and where it is pushed) and agent (its name, where it works, and the command that makes the state).
3. It has no secrets: no addresses, no keys and no paths of the user.
4. The Environment tab of the state view has two tabs: Browser (what the page finds in the browser) and Server (environment.server).
5. The network of the server, the agent and MCP is not in the state yet (see vision.md).""",

"agent-runs.md": """# Agent runs

## What an agent run is
1. An agent run is one request to an agent (Claude Code): from a message (of a person, the coordinator or a notification) to the next message.
2. After each run that changes the files of main, the agent records the run in runs/<session>-<run>.json:
   - scripts/run-log.js reads the session log (the .jsonl file of Claude Code). It makes the raw data: the requests, the context sizes, each tool use and the files.
   - The run-recorder subagent (.claude/agents/run-recorder.md) reads the raw data. It groups the tool uses into steps and writes why for each step, use and file. It does not copy secrets or the content of files.
   - The release puts the files of main into the state, so the run is in agents.agent-oss.files.runs.
3. The timeline shows the last run of the state as block 1, before the page start. Its name is Last AI run notification, its time is the time ago, and it shows the first 3 characters of the session. The newest block at the right also starts with Last (for example Last click). A new version that comes with new runs gets an AI run notification block after the New version block, for each new run. Then the newest AI run notification has the name Last AI run notification, and the state view shows it when no block is chosen: so the files of the new version show without a click.
4. Click an AI run notification block, then the Flow tab or the Agent Run tab of the state view. It has three tabs:
   - Index: the title and the summary of the run (summary in the run file; an older run without it shows the request and the counts), then Actions for you (actions in the run file) or No action needed. Then the chips: the agent, the session, the run, the start and end time, the version that the run made, the context at the start and at the end, the cached part of the context, and whether the session was compacted. Then what started the session, the run, the workflow, the subagents and the skills; MCP use, Skill use, Subagents and Workflow, each with how many times and why; then the context sizes.
   - Details: the state as the run touched it, in one tree. The files are under Files/, in their folders, with the color of what the run did: green added, yellow updated, red deleted, blue read. Then the other items in groups (MCP calls, Commands and scripts, Searches, Skills, Subagents): an MCP call that sent or wrote something is yellow, the others are blue. The counts of each color are above the tree. The buttons show only what one source did: All, Main agent, Subagents, MCP, Skills or Workflows. Each source has its color, and each item has a chip for its source. On the right, the item that you click, in tabs: File (the file viewer, with the text from the version that the run made), Changes (side by side: the version before the run and the version that the run made) and Why (what, by who, in which steps, why, the size in tokens). A file that is not in the state (it is not a file of the repo) has only Why. When a step is chosen (in Steps), Details shows only that step; Whole run shows all of it again.
   - Steps: the agent timeline, then the steps one by one. The timeline: the start card, then each step from left to right, in the lane of the agent that did it. The first lane is the main agent. A subagent is a helper agent with its own context, which the main agent started (for example run-recorder, which writes the record of the run). A subagent lane starts with a dashed line that tells what the subagent is and which steps are its own; its steps are short cards. Under it, each step has its number on a line, its title, who did it (with the MCP, skill, subagent or workflow chips), its start, its time, its context and why. Click a step (a card or a row) to open it: what it did (each item with its kind), and the files that it changed and read. Click it again to close it. See it in Details shows the step in Details.
5. Changes of an AI run notification: the differences between the version before the run and the version that the run made, if this page has both versions.

## How a run is recorded
1. scripts/run-log.js reads the session log of Claude Code (~/.claude/projects/<folder>/<session>.jsonl):
```sh
node scripts/run-log.js <session>.jsonl --repo . --run 72 --from <commit before> --to <new commit>
```
2. It prints the raw data of the run: started_by, context (tokens: input + cache read + cache write), uses (MCP, skills, subagents, workflows), events (each tool use) and files (read, created, updated, deleted; git wins).
3. The run-recorder subagent (.claude/agents/run-recorder.md) turns it into the run file. It removes events and adds title, summary, actions (what the owner must do), steps ({title, lane, from, to, items, why, context_tokens, cached_tokens, files}) and why for each use and file.
4. A run file has no secrets, no tokens, no passwords and no file contents: only paths and sizes.
5. The agent commits runs/<session>-<run>.json. The next state has it in agents.agent-oss.files.runs.

## Where the timeline gets it
runsOf, runStep and runDetails (in timeline-view local.refresh) read the run files of the loaded state. The last run is block 1. A New version block that brings new runs gets an AI run notification block for each new run.""",

"recorder-and-notes.md": """# Recorder and notes

## Record
The footer at the bottom of the page is recorder-view. The red button at its right records.
1. Click it one time to record audio (the microphone). Click it two times to open its menu: 1 Record audio, 2 Record video (a screen, a window or a tab that you choose, with its sound and the microphone), 3 Notes. A click on the button or out of the menu, or Escape, closes the menu.
2. Or use the keys (not while you type in a field or an editor): push Arrow Up two times to record audio. Push Arrow Up and Arrow Down at the same time to record video.
3. While it records, the button is a stop button, and the header shows the kind and the time (for example "Audio 00:12").
4. While it records, you are in select mode. The element under the pointer has a red frame. Click an element to select it: the page does not get the click. A timeline block or a view part has a purple frame, and its path shows above it: the view in the state, then the elements down to it, and the block (for example "extension.views.timeline-view › #tl-strip > button.tl-step:nth-of-type(3) (block 3: Run index.html)").
5. To stop, click the button, push the same keys again, or stop the sharing of the browser.
6. The card above the button plays the recording and lists the elements that you selected, with their time. Save file saves it (webm). On claude.ai, you confirm the download. The close button forgets the recording. The recording is in the memory of the page only, not in the state.
7. The browser asks you to let the page use the microphone or the screen. If it does not let the page record, a red note above the button tells why.
8. The ui-data of recorder-view keeps: recording ("", audio or video), started_at, selected (the last path), selections (each {at, path}), result (kind, time, size, type), error and menu_open. The calls of the record button are timeline blocks only when Track state is on.
9. Hold the button for 4 seconds to open the Notes page (notes-view), or click Notes in the menu. It shows between the header and the footer, as the other views do. Click × to close it. When you release the button after the 4 seconds, it does not record.

## Notes
1. Each recording is a note when it stops. You can also write a note: type it in "Write a note" and click Add note.
2. A note shows its text (a note that you wrote, or a recording after Transcribe) in a box where you can change it. A recording without text shows its player.
3. The buttons of a note:
   - Transcribe (a recording): puts the text that the browser heard while it recorded into the note. If there is no text, a message tells why.
   - Send now: the note goes to Claude in this Claude session, as a comment of the page that is sent to Claude. Only editors of the page can send. It works on claude.ai.
   - Send now new session: the note starts a new Claude Code session, through the task in settings.new_session_task and the Claude Code Remote connector.
   - Delete: the note goes, with its recording.
4. Under the text: the box, the view path of the note and Show state. The view path is the view of the first element that you selected while it recorded, or the view that was open (state view, docs view, else the header). Show state shows the ui-data of that view under the note. Click Hide state to hide it.
5. Check the boxes of notes, then click Send selected (at the bottom) to send them together to Claude in this session.
6. Settings (the gear button): Transcription is Browser (the default) or Off. With Browser, the browser turns what the microphone hears into text while you record (Chrome sends the sound to its speech service). Language is the language to hear (for example en-US); empty is the language of the browser. New session task is the id of the scheduled task (trig_...) that Send now new session starts: a task that starts a new session at each run.
7. On claude.ai, the frame of the page cannot use the microphone or the screen, so it cannot record or transcribe there. Text notes and sending work there. Recording and transcription work when you open the page from the repo on your computer.
8. The ui-data of notes-view keeps notes (each {id, kind, at, time, text, view_path, selections, file}), settings ({transcribe, lang, new_session_task}), settings_open and message. The recordings and the heard texts are in the memory of the page (os.refs.notes); on claude.ai a recording is also a file of the page (file, served at /_blob/<file>). The notes stay when you save the state.

## The microphone on claude.ai
1. On claude.ai, the page runs in a frame of the artifact. The frame does not have the permission to use the microphone or the screen.
2. So the browser does not ask you. The record button shows "The browser did not let the page record the microphone: Permission denied" at once.
3. The capabilities of an artifact have no microphone. The page cannot change this.
4. Recording and transcription work when you open the page from the repo on your computer (python3 -m http.server in the folder of the repo).
5. On claude.ai you can still dictate with the dictation of your system (for example Fn Fn on a Mac, Win+H on Windows) into "Write a note".
6. A choice is open: what the page does when the microphone is blocked (see vision.md).""",

"generator-and-release.md": """# The generator and the release

## The generator
state.json is not written by hand. gen/make_state.py makes it. Change the generator, then make the state again.
- gen/make_state.py: the views, the functions, their tests and the state. It checks that each function has pseudo code.
- gen/style_part.py: the base styles of the page (in index-view html).
- gen/pseudo.py: the pseudo code of each function. Change it when the code changes.
- gen/docs_part.py: these docs. make_state.py writes them to docs/.
- gen/performance.json: the times of each function from the page test. The generator puts them in performance.tests of each function.
- gen/build.js: makes the next version document (commits/cNNNNNN) for a release.
Run it in the folder of the repo:
```sh
python3 gen/make_state.py
```

## The tests
```sh
node --test tests/*.test.js
```
1. tests/state-core.test.js: the library of the runtime.
2. tests/page.test.js: the page in Chromium (Playwright). It clicks through the views, runs the tests that are written in the state, and writes gen/performance.json.
3. All tests take about 7 minutes. Do not make the state again while the tests run.

## The release
1. Make the state and run the tests.
2. Commit to main and push to the agent-os branch: git push origin main:agent-os.
3. Record the run (see agent-runs.md). Commit the run file. Make the state again and commit it.
4. Make the version document:
```sh
node gen/build.js <previous commit.json> <release.json> <out dir>
```
release.json has request (the words of the owner), session (the link) and explain ([{part, before, now}], in ASD-STE100).
5. A big version also gets <out dir>/cNNNNNN.state.json. Upload it as a file of the page (Artifact publish with asset: true). Then write its id into the document:
```sh
node gen/build.js --state-file <out dir>/cNNNNNN.json <file id>
```
6. Save the document as commits/cNNNNNN in the page database.
7. When index.html, state-core.js or vendor/ change, publish the runtime files first.
8. An open page runs the new version at once.

## Start it on another server
1. Clone the repo: git clone -b agent-os https://github.com/andyvauliln/agents-os.
2. In the folder, run python3 -m http.server 8000. Open http://localhost:8000.
3. The page runs from state.json with a memory store: there is no database, no comments, no Send to Claude and no MCP. A save stays until the page reloads.
4. For the agent: open the folder with Claude Code. It reads .claude/CLAUDE.md. You need python3, node and (for the page test) Playwright with Chromium.""",

"vision.md": """# Vision

This vision comes only from the inputs of the owner (inputs.json). Each part names the inputs it comes from.

## The goal
Agent OS is a page and an agent that work on one state. The agent builds the page. The page shows everything that the agent and the page do, so that the owner can see, understand and direct each change. (m00, m04, m40)
The first state (m00) names the product Slide: an extension with profiles and apps (for example an Instagram Slide app), a connection to the agent, MCP from the agent to the extension, and shared storage. Agent OS is the base for it.

## Principles
1. Everything is state. The views, the functions, the files of the agent, the network, the environment and the metadata of each file and folder are in one JSON state. The page renders only from it. (m00, m06, m45, c06, c50)
2. Every call is visible and tested. Each function has its input, output, imports, tests, expected changes, docs, pseudo code and performance. After each run, the state shows what happened. (m04, c06, c10, c14, c17)
3. Each change has a version and a reason. Each save is a version. Each agent change comes with the request, the session and an explanation of how each part worked before and how it works now. (m04, m40)
4. One state view, many representations. Full State is the whole state. Each other tab is a filter or a view of the same state. With Only changes, each tab shows only what one block changed or touched. (m48, m69, c37, c48)
5. Readable for a person. Icons, time ago, "..." for long text with a preview, formatted and colored code, md as a page with themes, a viewer for each kind of file. (m21, m23, m49, m50, c03, c43)
6. Do only what the owner asks. Name each new field and tell why. (m02, m07)

## What works now (v48)
- The state, the versions, the runtime and the tracked calls.
- The state view with 12 tabs, Only changes, tags of agent runs, and the timeline.
- Agent runs as AI run notifications, with Index, Details and Steps.
- Network and environment from code (Browser and Server).
- The recorder (outside claude.ai), notes, Send to Claude.
- The device sizes, one main view at a time, the docs.

## Next
These come from inputs that are not done yet (status open or partly in inputs.json).
1. Improvements tab: what an agent run can do better, from the analysis of the runs and the collected inputs. It shows only those changes in the state view. (m69)
2. Performance: also memory and cost, for each function, flow, agent and skill. (m69, c50)
3. Network: the requests of the server, the agent and MCP, next to those of the browser. (m69)
4. Functions tab: a tree split into agent and extension, each function marked local or public. (m69)
5. Views tab: the rendered view with the tabs html, data, functions, state and requests. A Page that you can click, with a copy of the state, as the viewer does. (m20, m69)
6. Metadata and views for each file, kind of file and folder, in the state. (c50)
7. Video tab. (m69)
8. The microphone on claude.ai: the owner must choose what the page does when it is blocked (a dictation box, a clear message, or as it is). (m72, m73)
9. The Slide extension: the header with brand, connections (apps, agent, MCP, storage), model chip, notifications, apps and theme; extension.data, common_app_storage and apps. (m00)
10. Run on another server with saves: a local store for the versions, so that saves stay after a reload. (m76)

## How the work goes
1. The owner writes a request: a message, a page comment, or a note from the page (Send to Claude).
2. The agent does only that request. It changes the generator, tests the page, records the run and saves a new version.
3. The page shows the new version at once, with the run and the changes. The owner reads it in the state view and comments on the page.""",

"review-report.md": """# Review report (v48)

This report tells what the review of v48 found: what was removed, the bugs, the speed, and how the architecture can change. The changes that the owner must approve are proposals only.

## Summary
- Removed: 35 lines of style rules that no element uses, 1 variable that no code uses, and the old long notes in .claude/CLAUDE.md (the docs hold them now).
- Fixed: 4 bugs (a save could undo a new version, the test times mixed whole tests with functions, the docs view showed ### and indented items as plain text, and a save error said "Invalid JSON").
- Found, not fixed: 4 problems (3 of speed, and a new version that waits after a draft).
- Proposals: 6 changes of the architecture. The biggest gain is a smaller state.

## What was removed
1. Style rules of old versions (gen/make_state.py and gen/style_part.py). No element has these classes now:
   - .st-bar, .st-title, .st-close, .st-filter, #st-filter, #st-filter-input (the old bar of the state view).
   - .sv-check, .sv-checks, .sv-switch, .sv-switches, .sv-track (the old check boxes and switches; v46 made them buttons and tabs).
   - .tl-check, .tl-tabs, .tl-tab, .tl-detail-head (the old timeline details; the tabs of the state view do this now).
   - .fv-badge-js, -ts, -html, -css, -json, -md, -py, -sh and the others (the file badge went in v47; .fv-badge stays for the pseudo code badge).
   - .ar-files, .legend, .lg-add, .lg-upd, .lg-del.
2. The variable coreFile in timeline-view local.refresh (defined, never used).
3. The old notes in .claude/CLAUDE.md (24 KB, a part was out of date: the Details field, the kind buttons). The file is now short: where things are, a code map, the rules and the release steps. The details are in docs/. The old text is in git history (commit e57163b).
4. how-it-works.md was one doc of 4900 words. It is now split: each part has its own doc (see overview.md).
Nothing in the state shape was removed: no field and no function.

## Bugs that were fixed
1. A save could undo a new version. While you edit the state (a draft), the page does not run a new version that comes. Save then took the newest version as the parent, but saved your text, which has the old state. So the changes of the new version went away without a message.
   Now: local.edit keeps the version that the draft starts from (os.refs['state-view'].draftFrom). local.save does not save when a newer version came. The bar says: "vN came while you edited vM. Copy your edit, reload the page, then edit again." A page test checks this.
2. The test times mixed two kinds of records. gen/performance.json counted the records of each test run (runTest, the whole test) under the short name of the function (for example local.init). So 32 entries had wrong names and wrong times, and the Performance tab could not find them. Now the page test counts only the calls of functions.
3. The docs view showed "### A block" as a paragraph, and an indented "- " item as plain text. Now ### is a heading and an indented item is an item. A .json file in docs shows as code.
4. Save with an error that is not a JSON error showed "Invalid JSON: ...". Now local.edit adds "Invalid JSON:" to its own message, and the bar shows each error as it is.

## Problems that were found, not fixed
Problems 1 to 3 need a change of the runtime (index.html), so a new publish of the runtime. They are proposals B and C below. Problem 4 is in the state view and in state-core.js.
1. Each call copies the whole state two times (before and after) and compares the copies. With a state of 2.5 MB this takes about 150 ms for each call, also for a call that does almost nothing (recorder-view local.refresh: 19 calls, 3 s in total in one test).
2. After each top-level call, each view that watches runs local.refresh, also when nothing that it shows changed. A click is 4 calls: the click, then state-view, timeline-view and recorder-view refresh. A tab click takes about 1 s.
3. A new version that comes during a draft stays in the history, but the page does not run it after the draft ends. You must reload. (The fix above stops the data loss. It does not load the version.)
4. When the state view shows the newest version, each refresh writes the live state into the editor text again (patchText), and then parses that text and compares it with the state, to check it. With a state of 2.7 MB this takes about 0.9 s to 1.5 s for each refresh. The last AI run of v48 made v48, so the state view opens on the newest version, and this cost is in each click. The page test now waits longer for the replay (20 s) and notes the green border of a save with a watcher. To fix it: patchText can keep the tokens of the last text, or the refresh can patch only the paths that the call changed (proposal B).

## Unused, but kept
- state-core.js exports esc, historyLength, kindOf and stripComments. No code outside state-core.js uses them. state-core.js uses them itself. To remove them from the exports needs a new publish of the runtime and gives nothing.
- .claude/commands, hooks, output-styles and skills hold only .gitkeep. They are the default folders of the agent (inputs m00, m01).
- extension.data, common_app_storage and apps are empty. They come from the first state (m00) and are part of the vision.
- The Improvements and Video tabs are empty. They are in the plan of the owner (m69).

## Speed (measured in this container, headless Chromium)
- The page opens (to ready): 3.6 s.
- Open the state view: 0.5 s.
- Open the timeline: 4.3 s.
- Click a tab of the state view: 1.0 to 1.4 s.
- Only changes on: 1.5 s.
- state-view local.refresh: 0.4 s for each run (max 1.1 s) on an older version; 1.4 s (max 6 s) on the newest version (problem 4).
- A call that does almost nothing: about 0.15 s.
The state is 2.5 MB: agents.agent-oss.files is 2.1 MB of it. vendor/ is 926 KB (37 %), runs/ 484 KB (19 %), gen/ 413 KB, tests/ 111 KB. The views and functions are 406 KB.

## Architecture: what works well
- One state, one runtime: the page has no hidden parts. The runtime does not know the views.
- Each call is recorded with its changes, errors and time, and each function has tests in the state.
- Versions with the source, the request and explain make each change easy to follow.
- The generator makes the state, the docs and the tests from one place, and checks that each function has pseudo code.

## Architecture: proposals
A. A smaller state. vendor/ (926 KB) is a copy of the library files, which the page loads as files of the artifact and lists under network packages. Keep vendor files in agents.agent-oss.files as metadata (path, size, version, license) and not as text. The state goes from 2.5 MB to about 1.6 MB. Each call, each version file and each draw of the editor gets faster. This changes the rule "the files are every file of main", so the owner must approve it.
B. Cheaper calls. The runtime can record only the paths that a function sets, or copy only the parts that change, in place of two full copies and a full diff for each call. A change of the runtime.
C. Fewer refreshes. A view that watches can tell which paths it shows. The runtime runs its local.refresh only when one of them changed. A change of the runtime.
D. Smaller functions. timeline-view local.refresh is one function of about 2000 lines. The other views use its helpers through os.refs['timeline-view']. Move the helpers (file view, kind view, changes view, run view, performance) into their own functions in the state. Then each has its own tests, docs, pseudo code and performance, as the principles ask. This adds functions to extension.functions, so the owner must approve it.
E. Code in code files. gen/make_state.py is 4700 lines, and the code of each function is a text in Python. Put the code of each function in its own .js file (for example gen/views/state-view/local.save.js). The generator reads them. Then a code editor can check and color them.
F. One md parser. The docs view has its own md parser in its html template. state-core.js already has mdParse, which the file viewer uses. The docs view can use mdParse too.

## The order that this report proposes
1. A (smaller state): the biggest gain, one rule changes.
2. C and B (runtime): faster clicks.
3. D and E (code): easier to read and to test.
4. F (docs view).""",
}
