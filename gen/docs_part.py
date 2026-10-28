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

## The timeline
1. Open the state view (the State button in the header). Click the Timeline button at the left of its bar. The timeline shows at the top of the page, above the header. Click the button again to hide it.
2. It shows what happened since the page opened, as blocks in a row from left to right. The first block is the last agent run (if the state has one). Then: Network (every request and the environment), index.html runs, the runtime loads the state, the page starts.
3. Each next block is one call that nothing else called, for example a click on a button.
4. Each block shows its number, the time since the page opened, the function, its time in ms and how many state changes it made.
5. What you do in the state view and in the timeline (clicks on blocks, the replay, the buttons) is not a block. Turn on Track state (in the bar of the state view) to add it as blocks too.
6. When the row of blocks scrolls, the last agent run stays at the left and the newest block stays at the right.

### A block
1. Click a block. The state view shows it, and its bottom bar names it (for example "Block 3: Run index.html"). When no block is chosen, the state view shows the last agent run.
   The state view goes to the version of the block: the version that an agent run made, or that a New version brought. For the other blocks, it is the newest version.
2. Changes (the button in the bar of the state view): the state cut down to what this block changed: green is added, yellow is updated (with the old value), red is deleted. Under it, a table says which function changed what.
   A long text, or a text of more than one line, shows as "...", as in the state view. Put the pointer on it to see its start. An updated text (and its "was "..."") shows its changes: red lines are removed, green lines are added. Click it to open the whole text in the viewer. Press Escape or × to close the viewer.
   Type in Filter paths (the filter of the state view) to see only the paths that have the text. The table shows only the paths that the filter shows.
   The buttons All, Files, Views, Functions, Network and Environment choose what shows. All shows the changes as above. Each other button shows only that kind, in its own view:
   - On the left: a tree of all of them in the state after the block (for example all the files, in their folders). A changed one has the color of its change: green added, yellow updated, red deleted. A folder that holds a change is yellow.
   - On the right: the one that you click, in tabs. The first tab is its content: File (the text of the file), View (its html and ui-data), Function (its code and its other fields), Request (a request of network) or Value (a part of environment).
   - A function also has the Pseudo code tab: its docs, then what its code does, step by step. Each line has a number. The keywords have colors: IF, ELSE and FOR EACH (the flow) are purple, CALL is blue, SET, READ, DRAW and the other actions are green, RETURN and THROW are red. A line inside a step is indented, with a guide line.
   - When the block changed it, the Changes tab shows the change. A text (a file, html, code) shows side by side: red lines are only before, green lines are only after. An object shows cut down to what changed.
   - The filter text keeps only the items whose path has it.
   - A file shows in the file viewer for its kind. The head has a badge for the kind (JS, HTML, CSS, JSON, MD, PY), the name, the language, the lines, the size, the tokens (about), Copy and Full screen.
     - Full screen: the file viewer covers the page. Click Exit full screen or push Escape to go back.
     - md: reads as a page, with the look and the theme of the md viewer of the state view. Contents on the left lists the headings: click one to go to it. The "Aa" buttons choose the theme: Reader, White, Black, Sepia, Night or Mono. The theme stays in state-view ui-data.md_theme, so the md viewer of the state view uses it too. Source shows the text.
     - json: a tree. Click an object or a list to open or close it. The first two levels are open. Find opens the parts that have the text and marks them. Open all, Close all. Source shows the text.
     - Code (js, html, css, python and more): the outline on the left (functions, classes and constants; ids, scripts and styles; selectors), each with its line. Click one to go to the line. Find marks every match: Enter goes to the next one, Shift+Enter to the one before. Wrap wraps long lines.
   - A click on "..." opens the text in the same file viewer.
3. Details (the button after Changes): what happens inside the block. The function, then each function it called, in the order they started, with their input and time.
   Each function says what it does (its docs), why it ran (a click, a watch, or the function that called it) and what it changed in the state. Click its name to see its code.
   The first blocks happen before any function runs, so they show their parts instead:
   - Run index.html: the runtime script runs. What it did, with times, the start time (os.started), the session id of the call log, the call tracker, and the functions in os.
   - Load the state: state.json downloads, the page connects to the database, reads the saved versions and parses the newest one.
   Each part says what happens and why it is needed. Click a part to open it: it shows the lines of index.html that do it (with their line numbers), then what it made:
   - Run the runtime script shows what the runtime did, with times, and the code of the runtime script.
   - Note the start time shows the browser's timings. Make a session id shows the first record of the call log. Create the call tracker counts the calls by name. Build os lists what is in os: click one to see what it is for, which functions use it, how often they ran, and its code.
   - Download state.json shows state.json. Connect to the database shows where the versions and the call log are. Read the saved versions lists the versions. Parse the newest version shows the parts of the state and their sizes.
### The buttons of the timeline
1. The arrow buttons show the block before and the next block.
2. The Replay button shows the next block every 1.6 seconds. From the last block, it starts again at the first. It goes on to the newest block. With Track state on, each move adds a block, so it stops at the block that was the newest when it started. It also stops when you click it again, or when you click a block.
3. The Reload button reloads the page, so the history starts again at block 1. The timeline opens again and replays the blocks from the first one: the last agent run, then the page start. If the state has unsaved changes, it does not reload: save them first.
4. The blocks button hides or shows the row of blocks.
5. The Flows button opens the list of saved flows. Click the play button of a flow to replay only its blocks. First enter is the page opening: its first 4 blocks (index.html, runtime, loadState, the render of index-view).
6. The timeline is part of the state view: when you close the state view, the timeline hides too.

### A new version
1. A Claude Code session changes the files of main. It commits the change, pushes it and saves a new version of the state.
2. An open page gets the new version and runs it immediately. You do not reload the page.
3. Each view keeps its ui-data. The views that were open stay open.
4. The timeline adds a New version block.
5. Changes: the differences between the version that ran before and the new version. Long texts are cut.
6. Details: where the version came from (the git commit, the request and the session), how each part worked before and how it works now, side by side, and each changed file side by side. Red lines are only in the old version. Green lines are only in the new version.

### Agent runs
1. An agent run is one request to an agent (Claude Code): from a message (of a person, the coordinator or a notification) to the next message.
2. After each run that changes the files of main, the agent records the run in runs/<session>-<run>.json:
   - scripts/run-log.js reads the session log (the .jsonl file of Claude Code). It makes the raw data: the requests, the context sizes, each tool use and the files.
   - The run-recorder subagent (.claude/agents/run-recorder.md) reads the raw data. It groups the tool uses into steps and writes why for each step, use and file. It does not copy secrets or the content of files.
   - The release puts the files of main into the state, so the run is in agents.agent-oss.files.runs.
3. The timeline shows the last run of the state as block 1, before the page start. A new version that comes with new runs gets an Agent run block after the New version block, for each new run.
4. Click an Agent run block, then Details:
   - The chips: the agent, the session, the run, the start and end time, the version that the run made, the context at the start and at the end, the cached part of the context, and whether the session was compacted.
   - Timeline (Agent run): the start card, then each step from left to right. Each step is in the lane of the agent that did it. The first lane is the main agent. A subagent is a helper agent with its own context, which the main agent started (for example run-recorder, which writes the record of the run). A subagent lane starts with a dashed line that tells what the subagent is and which steps are its own; its steps are short cards. A main agent step shows what it did (for example "read index.html", "create scripts/run-log.js"), why, its time and the context at its end. An MCP, skill, subagent or workflow use in a step is bold, with a color.
   - Click a step. Under the timeline, you see only this step: its lane, its time, its context, what it did (each item with its kind), and why. Click the step again to see the whole run.
   - Under it, two tabs. Changes: the files that the agent created, updated or deleted, and the MCP calls that sent or wrote something. Reads: what came into the context of the agent: the files that it read, the output of commands, tests and searches, and the data of MCP calls, skills and subagents.
   - The buttons show only what one source did: All, Main agent, Subagents, MCP, Skills or Workflows. Each source has its color, and each item in the tree has a chip for its source.
   - On the left, the tree: the files under Files/, in their folders, with the color of their change (green created, yellow updated, red deleted), then the other items in groups (MCP calls, Commands and tests, Searches, Subagents). On the right, the item that you click, in tabs: File (the file viewer, with the text from the version that the run made), Changes (side by side: the version before the run and the version that the run made) and Why (what, by who, in which steps, why, the size in tokens). A file that is not in the state (it is not a file of the repo) has only Why.
   - Details: what started the session, the run, the workflow, the subagents and the skills; MCP use, Skill use, Subagents and Workflow, each with how many times and why; then the context sizes.
5. Changes of an Agent run: the differences between the version before the run and the version that the run made, if this page has both versions.

### Network and environment
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

### Where it comes from
1. The timeline comes from the call log of the runtime (os.calls), not from the state. If the state kept the timeline, each call would change the state again.
2. The ui-data of timeline-view keeps the chosen block (selected; null is the last agent run), whether the replay runs (playing), show_blocks, flows_open, and the saved flows (flows: each has a name and the names of its blocks). The ui-data of state-view keeps timeline_open (the Timeline button), track_state (Track state), changes and details.

## Record
The red button at the bottom right of the page records (recorder-view).
1. Click it one time to record audio (the microphone). Click it two times to record video (a screen, a window or a tab that you choose, with its sound and the microphone).
2. Or use the keys (not while you type in a field or an editor): push Arrow Up two times to record audio. Push Arrow Up and Arrow Down at the same time to record video.
3. While it records, the button is a stop button, and the header shows the kind and the time (for example "Audio 00:12").
4. While it records, you are in select mode. The element under the pointer has a red frame. Click an element to select it: the page does not get the click. A timeline block or a view part has a purple frame, and its path shows above it: the view in the state, then the elements down to it, and the block (for example "extension.views.timeline-view › #tl-strip > button.tl-step:nth-of-type(3) (block 3: Run index.html)").
5. To stop, click the button, push the same keys again, or stop the sharing of the browser.
6. The card above the button plays the recording and lists the elements that you selected, with their time. Save file saves it (webm). On claude.ai, you confirm the download. The close button forgets the recording. The recording is in the memory of the page only, not in the state.
7. The browser asks you to let the page use the microphone or the screen. If it does not let the page record, a red note above the button tells why.
8. The ui-data of recorder-view keeps: recording ("", audio or video), started_at, selected (the last path), selections (each {at, path}), result (kind, time, size, type) and error. The calls of the record button are timeline blocks only when Track state is on.
9. Hold the button for 4 seconds to open the Notes page (notes-view). It covers the page. It is empty for now. Click × to close it. When you release the button after the 4 seconds, it does not record.

## Where the parts are
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
- To change the page, change the state and save it. Do not change index.html.""",

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
""" + code('{ "docs_open": false, "state_open": false }', "json") + """
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
- codemirror is the editor. Its scripts load from cdnjs. The name CodeMirror is the editor that the scripts give.

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

"state-view.md": """# The state view

## Open the state view
1. Click the State button in the header.
2. The state view shows the chosen block of the timeline. When no block is chosen, it is the last agent run. The editor shows the state at the version of the block.
3. The state view is the one view for the state and its changes. Its bar has, from the left: the Timeline button, the kind buttons, Changes and Details, the filter with Show empty and Track state, then Collapse all, Save, Older and Newer.

## Edit and save the state
1. Edit the JSON in the editor. You can write comments with // and /* */.
2. Push Cmd+S or Ctrl+S, or click the Save button.
3. If the JSON has small errors, the save repairs them first.
4. The border of the editor becomes green for a short time. This shows that the new version is saved.

## Filter the state
1. Type in the filter at the top of the state view.
2. The editor shows only the entries whose path has the text, with the first and last lines of the objects around them.
3. The other lines fold into "⋯ N lines". You can still edit the lines that show.
4. Click Files, Views, Functions, Network or Environment to see only that kind, as a tree: for example, Files shows the files in their folders. Click one in the tree to see it on the right. Click All to see the editor again. This works with or without text.
5. Click Changes to see only what the chosen block changed. After Older or Newer, it is what the version on the screen changed. Click Details to see what happens inside the block.
6. Clear Show empty to hide the entries with an empty value: {}, [], "" or null. They hide with no "⋯" mark.
7. Turn on Track state to add what you do in the state view and the timeline as blocks of the timeline.
8. Push Escape to clear the filter.
- Older and newer (the arrows) are at the right end of the bar.
- The version, the path and the status are in the bar at the bottom of the state view.

## Look at older versions
1. Click the left arrow button, or push the left arrow key. The state view leaves the chosen block.
2. You cannot edit an older version.
3. Click the Changes button to see only the changes of that version. Green is added, yellow is updated, red is deleted.

## Long text
- Long text, and text that has more than one line, shows as "...". Put the pointer on it to see the start of the text, in the colors of its kind (md, js, html, css or json).
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
5. Edit the html on the left. The view on the right starts again with the new html."""
}
