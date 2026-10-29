# The flows

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
The timeline keeps saved flows in timeline-view ui-data.flows: each has a name and the names of its blocks. The Flows button lists them. A click on the play button replays only those blocks. First enter is the page opening (its first 4 blocks).