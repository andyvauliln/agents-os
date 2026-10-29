# The timeline

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
2. The ui-data of timeline-view keeps the chosen block (selected; null is the last agent run), whether the replay runs (playing), show (all, runs or ui: the AI runs and UI buttons), flows_open, and the saved flows (flows: each has a name and the names of its blocks). The ui-data of state-view keeps timeline_open (the Timeline button), track_state (Track this view), changes (Only changes) and filter_kind (the tab).