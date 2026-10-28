# How Agent OS works

## Architecture
```svg<svg viewBox="0 0 780 500" role="img" aria-label="Architecture of Agent OS">
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
</svg>```
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
   - A file shows in the file viewer for its kind. The head has a badge for the kind (JS, HTML, CSS, JSON, MD, PY), the size and the tokens (about). The name is in the path above the viewer. The buttons are icons: put the pointer on one to see its name (Read, Source, Tree, Contents, Functions, Copy, Wrap, Open all, Close all, Full screen).
     - Contents (md) and Functions (code) are hidden at first. Click the button with the side panel icon to show them on the left, and again to hide them.
     - Full screen: the file viewer covers the page. Click Exit full screen or push Escape to go back.
     - md: reads as a page, with the look and the theme of the md viewer of the state view. Contents lists the headings: click one to go to it. The Style select chooses the theme: Reader, White, Black, Sepia, Night or Mono. The theme stays in state-view ui-data.md_theme, so the md viewer of the state view uses it too. Source shows the text.
     - json: a tree. Click an object or a list to open or close it. The first two levels are open. Find opens the parts that have the text and marks them. Open all, Close all. Source shows the text.
     - Code (js, html, css, python and more): Functions lists the functions, classes and constants (ids, scripts and styles in html; selectors in css), each with its line. Click one to go to the line. Find marks every match: Enter goes to the next one, Shift+Enter to the one before. Wrap wraps long lines.
   - A click on "..." opens the text in the same file viewer.
3. Details (the button after Changes): what happens inside the block. The function, then each function it called, in the order they started, with their input and time.
   Each function says what it does (its docs), why it ran (a click, a watch, or the function that called it) and what it changed in the state. Click its name to see its code.
   The first blocks happen before any function runs, so they show their parts instead:
   - Run index.html: the runtime script runs. What it did, with times, the start time (os.started), the session id of the call log, the call tracker, and the functions in os.
   - Load the state: state.json downloads, the page connects to the database, reads the saved versions and parses the newest one. A version that is too big for one database document (256 KB) keeps its state in a file of the page (state_file), and the page downloads that file.
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
3. The timeline shows the last run of the state as block 1, before the page start. Its name is Last agent run, its time is the time ago, and it shows the first 3 characters of the session. The newest block at the right also starts with Last (for example Last click). A new version that comes with new runs gets an Agent run block after the New version block, for each new run. Then the newest Agent run block has the name Last agent run, and the state view shows it when no block is chosen: so the files of the new version show without a click.
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
1. Click it one time to record audio (the microphone). Click it two times to open its menu: 1 Record audio, 2 Record video (a screen, a window or a tab that you choose, with its sound and the microphone), 3 Notes. A click on the button or out of the menu, or Escape, closes the menu.
2. Or use the keys (not while you type in a field or an editor): push Arrow Up two times to record audio. Push Arrow Up and Arrow Down at the same time to record video.
3. While it records, the button is a stop button, and the header shows the kind and the time (for example "Audio 00:12").
4. While it records, you are in select mode. The element under the pointer has a red frame. Click an element to select it: the page does not get the click. A timeline block or a view part has a purple frame, and its path shows above it: the view in the state, then the elements down to it, and the block (for example "extension.views.timeline-view › #tl-strip > button.tl-step:nth-of-type(3) (block 3: Run index.html)").
5. To stop, click the button, push the same keys again, or stop the sharing of the browser.
6. The card above the button plays the recording and lists the elements that you selected, with their time. Save file saves it (webm). On claude.ai, you confirm the download. The close button forgets the recording. The recording is in the memory of the page only, not in the state.
7. The browser asks you to let the page use the microphone or the screen. If it does not let the page record, a red note above the button tells why.
8. The ui-data of recorder-view keeps: recording ("", audio or video), started_at, selected (the last path), selections (each {at, path}), result (kind, time, size, type), error and menu_open. The calls of the record button are timeline blocks only when Track state is on.
9. Hold the button for 4 seconds to open the Notes page (notes-view), or click Notes in the menu. It covers the page. Click × to close it. When you release the button after the 4 seconds, it does not record.

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
- To change the page, change the state and save it. Do not change index.html.