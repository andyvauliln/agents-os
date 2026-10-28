# The pseudo code of each function: what its code does, step by step, in ASD-STE100 words.
# Keywords: SET, READ, IF / ELSE IF / ELSE, FOR EACH, CALL, DRAW, WATCH, WAIT, RETURN, THROW, END.
# make_state.py puts it into the function as "pseudo". When the code of a function changes, change its pseudo code too.
PSEUDO = {
"get-state": """\
READ the state at path (all the state when there is no path)
IF nothing is at path
  THROW "Nothing at <path>"
RETURN a copy of the value""",

"render": """\
READ the view at view_path
IF there is no view: THROW "No view"
SET id = the last part of view_path
FIND the empty element with that id on the page
IF there is none: THROW "No element #id"
FILL the html template of the view with its ui-data (d) and e() for escape
IF the first element of the html does not have the same id: THROW
REPLACE the empty element with the new element
BIND the buttons of the element (data-call, data-input) to the functions of the view
MARK the view as mounted
IF the view has local.init
  CALL local.init of the view""",

"unmount": """\
FIND the element of the view (its id is the last part of view_path)
EMPTY it and hide it
MARK the view as not mounted""",

"index-view/local.init": """\
CALL get-state for extension.views.header-view
IF there is no header-view: THROW
CALL render for header-view
CALL render for recorder-view (the record button)""",

"recorder-view/local.init": """\
IF an older init has listeners: REMOVE them
SET os.refs.recorder-view = a new memory
WHEN you hold the record button 4 s: CALL local.open-notes (the click after it does nothing)
WHEN you click the record button
  IF it records: CALL local.stop
  ELSE IF a second click comes in 300 ms: CALL local.toggle-menu with open = true
  ELSE IF the menu is open: CALL local.toggle-menu with open = false
  ELSE: CALL local.start with audio
WHEN you click out of the menu, or push Escape, while it is open: CALL local.toggle-menu with open = false
WHEN you push Arrow Up two times in 400 ms (not in a field or an editor)
  IF it records: CALL local.stop
  ELSE: CALL local.start with audio
WHEN Arrow Up and Arrow Down are down at the same time
  IF it records: CALL local.stop
  ELSE: CALL local.start with video
WHEN it records (select mode)
  the element under the pointer: DRAW a red frame
  a click on an element: the page does not get it
    CALL local.select with the path of the element (its view, the elements down to it, its block)
WATCH recorder-view: after each call, CALL local.refresh
CALL local.refresh""",

"recorder-view/local.refresh": """\
DRAW the button again from ui-data: record, or stop while it records
DRAW the error and the card of the last recording
IF there is a recording in memory: SHOW its player in the card
SET select mode = recording
IF an element is selected: DRAW a purple frame on it and its path above it
DRAW the timer in the header""",

"recorder-view/local.start": """\
IF mode is not audio or video: THROW
IF it records: THROW
SET menu_open = false
IF the browser cannot record: SET error and RETURN
TRY
  IF audio: READ the microphone
  ELSE
    READ a screen, a window or a tab that you choose (with its sound)
    READ the microphone, IF the browser gives it
    PUT the sounds into one track
    WHEN you stop sharing: CALL local.stop
IF it fails: SET error = why, and RETURN
IF transcription (Settings of Notes) is not off and the browser can hear words
  START speech recognition in the language of the settings (or of the browser)
  WHEN it hears words: ADD them to the heard text in memory
  WHEN it stops after a silence: START it again
START the recorder
SET recording = mode, started_at = now, selected = "", selections = [], result = null
START the timer of the header""",

"recorder-view/local.stop": """\
IF it does not record: RETURN
STOP the recorder and WAIT for its last data
STOP the microphone and the screen
STOP the speech recognition
STOP the timer
SET the file = the data, in the memory of the page
SET result = { kind, time, size, type }
ADD a note to the top of notes-view notes: { id, kind, at, time, text: "", view_path, selections, file }
  view_path = the view of the first selected element, or the open view (state-view, docs-view, header-view)
  the file and the heard text stay in the memory of the page (os.refs.notes: it stays when Notes closes)
  IF the assets capability is there: UPLOAD the file and SET file = its id
SET recording = """"",

"recorder-view/local.select": """\
SET selected = path
ADD { at: the time in the recording, path } to selections""",

"recorder-view/local.save": """\
IF there is no recording: THROW
SET name = agent-os-<kind>-<date and time>.webm (or .mp4)
IF the downloads capability of claude.ai is there
  CALL save with the name and the file (you confirm it)
ELSE
  the browser downloads the file
RETURN { saved: name }""",

"recorder-view/local.toggle-menu": """\
SET menu_open = open, or NOT menu_open when there is no open
(the menu: 1 Record audio, 2 Record video, 3 Notes)""",

"recorder-view/local.open-notes": """\
SET menu_open = false
IF notes-view is not mounted: CALL render notes-view (the Notes page)""",

"notes-view/local.init": """\
KEEP os.refs.notes-view (the checked and the shown notes); the recordings and the heard texts are in os.refs.notes
WHEN you type a new note: REMEMBER the draft
WHEN you type in the text of a note: after 400 ms, CALL local.edit
WHEN you change Transcription, Language or New session task: CALL local.set-settings
WHEN you click Add note and the new note has text: CALL local.add-text
WATCH notes-view: after each call, CALL local.refresh
CALL local.refresh""",

"notes-view/local.refresh": """\
IF after = local.edit: RETURN (the text box keeps its place)
FORGET checked and shown notes that are gone
DRAW the page from ui-data, with the checked and the shown notes
PUT the draft back into the new note
FOR EACH recording without text: SHOW its player (from memory, or /_blob/<file>), or say it is gone
FOR EACH shown note: SHOW the ui-data of its view as JSON""",

"notes-view/local.toggle-settings": """\
SET settings_open = NOT settings_open""",

"notes-view/local.set-settings": """\
IF transcribe is given
  IF it is not browser or off: THROW
  SET settings.transcribe = transcribe
IF lang is given: SET settings.lang = lang
IF new_session_task is given: SET settings.new_session_task = new_session_task
RETURN settings""",

"notes-view/local.add-text": """\
IF text is empty: THROW
ADD a note to the top of notes: { id, kind: text, at: now, text, view_path: the open view, selections: [] }
SET message = "", FORGET the draft
RETURN { id }""",

"notes-view/local.edit": """\
FIND the note with id, or THROW
SET its text = text""",

"notes-view/local.transcribe": """\
FIND the recording with id, or THROW
IF the browser heard words in it: SET its text = the heard text and RETURN it
SET message = why there is no text (transcription off, no speech service, no permission, a reload, no words)""",

"notes-view/local.send": """\
FIND the notes with ids, or THROW
SET text = each note: its kind and time, its text, its view, the elements selected in it (at most 4 KB)
IF new_session
  IF there is no mcp capability or no settings.new_session_task: SET message and RETURN
  CALL fire_trigger of Claude Code Remote with the task and the text (a new Claude Code session starts)
ELSE
  IF there is no comments capability, or Claude cannot get it now: SET message and RETURN
  CALL sendToClaude: a comment at the first note, sent to Claude (this Claude session gets it)
SET message = sent, or "Not sent: " and why""",

"notes-view/local.delete": """\
FIND the note with id, or THROW
REMOVE it from notes
FORGET its recording and its heard text in memory
IF it has a file of the page: DELETE the file""",

"notes-view/local.pick": """\
CHECK or UNCHECK the note in os.refs.notes-view.picked (for Send selected)""",

"notes-view/local.show-state": """\
SHOW or HIDE the ui-data of the note's view (os.refs.notes-view.shown)""",

"notes-view/local.close": """\
CALL unmount notes-view""",

"recorder-view/local.clear": """\
FORGET the recording in memory
SET result = null, selections = [], selected = "", error = """"",

"header-view/local.init": """\
READ ui-data of header-view
IF the page reloads from the Reload button of the timeline
  SET state_open = true, and timeline_open of state-view = true
IF docs_open and docs-view is not mounted: CALL render docs-view
IF state_open and state-view is not mounted: CALL render state-view""",

"header-view/local.open.docs-view": """\
SET docs_open = NOT (docs-view is mounted)
IF docs_open
  CALL render docs-view
ELSE
  CALL unmount docs-view
CALL render header-view (the button shows pressed or not)""",

"header-view/local.open.state-view": """\
SET state_open = NOT (state-view is mounted)
IF state_open
  CALL render state-view
ELSE
  CALL unmount state-view
CALL render header-view""",

"docs-view/local.init": """\
READ the docs folder of the agent (agents.agent-oss.files.docs)
SET docs = the names of the files in it
IF selected is not one of them: SET selected = the first doc
SET content = the text of the selected doc
DRAW the view again from its html and ui-data
BIND its buttons""",

"docs-view/local.open-doc": """\
IF name is not in the docs folder: THROW "No doc"
SET selected = name
SET content = the text of the doc
DRAW the view again from its html and ui-data
BIND its buttons""",

"timeline-view/local.init": """\
IF an older timeline has a replay timer: STOP it
SET os.refs.timeline-view = a new empty memory (steps, parts, files)
WATCH timeline-view: after each call, CALL local.refresh
CALL local.refresh
IF the page reloads from the Reload button
  CALL local.select the first block (the last agent run)
  CALL local.play""",

"timeline-view/local.refresh": """\
SHOW the timeline IF state-view is mounted and its timeline_open is true, ELSE HIDE it
DRAW the bar again from ui-data (buttons, flows list)
READ the call log of this page load (os.calls)
FOR EACH call
  IF another call made it: PUT it inside that call
  ELSE IF it is a call of the timeline, the state view or the record button, and Track state is off: SKIP it
  ELSE: it is a block
SET blocks =
  the last agent run of the state (runs/*.json), if there is one
  Network (requests and environment)
  Run index.html
  each top call (Load the state, Start the page, clicks, new versions)
  after a New version: an Agent run block for each new run
FOR EACH block: count its state changes
SET the chosen block = selected, or the newest agent run block when nothing is chosen (the newest block when there is no run)
DRAW the row of blocks (number, time, name, changes); the chosen block is on
  the agent run block: its time ago and the first 3 characters of its session
  the newest agent run block stays at the left, and the newest block at the right, when the row scrolls; their names start with Last
DRAW the position and the progress line
GIVE the state view what it needs:
  current = the chosen block, number = its place
  versionOf(block) = the version the block made or brought (the newest version for the other blocks)
  showTip(element, text, path, old text) = the preview of a long text: its first lines in the colors of its kind;
    with the old text, its changes (red lines out, green lines in), from a little before the first change
  pairFrom(before, after) = two states and the rows of what changed
  drawPair(box, kind, pair) = the changes of two states (all, or one kind as a tree)
  kindView(box, kind, state) = one kind of the state as a tree
  drawChanges(box, kind) = the state changes of the block
    ALL: the state cut down to the changes, long texts as "...", a table of who changed what
    ONE KIND (files, views, functions, network, environment):
      a tree of all of them on the left
      tabs on the right: the content (File / View / Function / Request / Value), Pseudo code, Changes
      a file shows in the file viewer (md page, json tree, code): its kind, size and tokens, icon buttons, one Style select for md
        Contents (md) and Functions (code) hidden until their button shows them (os.refs.timeline-view.fileSide)
      an updated md file in read mode: new lines green, removed lines red; the pointer on them shows why the run changed the file
  drawDetails(box) = what happens inside the block
    Network: the requests by group and the environment
    Agent run: the steps in lanes, the uses, what started it, the files as a tree
    a call: its parts, then each call inside it with what, why and its changes
IF playing and no timer: START a timer that CALLs local.next every 1.6 s
IF not playing and a timer runs: STOP it""",

"timeline-view/local.select": """\
SET playing = false, and leave the flow
SET selected = id (null: no block, the state view shows the last agent run)""",

"timeline-view/local.next": """\
IF a flow is not playing: leave the flow
SET ids = the blocks of the flow, or all the blocks
SET to = the place of the chosen block (or the block that shows) + delta (not past the first or the last)
SET selected = ids[to]
IF to is the last block, or the end of the replay: SET playing = false""",

"timeline-view/local.reload": """\
IF the state has unsaved changes: THROW "Save them first"
REMEMBER "replay after the reload" (sessionStorage, or the address)
RELOAD the page""",

"timeline-view/local.toggle-blocks": """\
SET show_blocks = NOT show_blocks""",

"timeline-view/local.toggle-flows": """\
SET flows_open = NOT flows_open""",

"timeline-view/local.play-flow": """\
FIND the flow with this name in ui-data.flows
IF there is none: THROW "No flow"
SET ids = []
FOR EACH block name of the flow
  FIND the first block with that name after the block found before
  IF found: ADD it to ids
IF ids is empty: THROW
SET the flow = { name, ids }, and the end of the replay = the last of ids
SET flows_open = false
SET selected = the first of ids
SET playing = true IF the flow has more than one block
RETURN { blocks: the number of ids }""",

"timeline-view/local.play": """\
IF the flow ended: leave the flow
SET ids = the blocks of the flow, or all the blocks
SET playing = NOT playing
IF playing and the chosen block is the last (or none): SET selected = the first block
IF playing
  SET the end = the newest block now IF Track state is on, ELSE no end (it goes on to the newest)""",

"state-view/local.init": """\
READ the saved versions (os.history)
SET the memory of the view: the editor, the draft, the base text (the newest version)
SET ui-data: the version, the position, no changes, no unsaved draft
CREATE the editor (CodeMirror) with folds, colors for keys and matching brackets
WHEN you type: WAIT a moment, then CALL local.edit
WHEN you press the arrow keys (not in the editor): CALL local.step with -1 or 1
WHEN you press Cmd+S or Ctrl+S anywhere: CALL local.save
WHEN you type in Filter paths: CALL local.filter; Escape empties it
IF timeline-view is not mounted: CALL render timeline-view (hidden until the Timeline button; it keeps the blocks)
WATCH state-view: after each call, CALL local.refresh
CALL local.refresh""",

"state-view/local.refresh": """\
IF you type and local.edit did not run yet: RETURN (leave the editor alone)
IF the timeline has a newly chosen block
  the view is on the block: SET position = the version of the block (IF there is no draft)
SET the text =
  IF there is a draft and it is the newest position: the draft
  ELSE IF it is the newest version: the live state (keep the comments and the layout; change only the values)
  ELSE: the older version at position
IF the text is not the text in the editor
  SET the text in the editor, and fold again the objects that were folded
SET the editor to read only IF it shows an older version
MARK a bad line IF the JSON has an error
SHOW each long text as "..." (a text of only {} or [] shows as it is; the pointer shows its start in the colors of its kind, a click CALLs local.open-viewer)
HIDE the lines that the filter text does not show ("... N lines")
IF show_empty is false: HIDE the entries with an empty value ({}, [], "" or null), with no mark
DRAW the buttons, the kind buttons, Show empty, Track state and the bottom bar again from ui-data
OPEN or CLOSE the viewer as viewer_path says
SET the md theme of the viewer
DRAW the chosen block in the bottom bar (IF the view is on it)
IF details, changes or a kind (not all)
  HIDE the editor and SHOW the pane
  IF details: the text of the block, then CALL drawDetails of the timeline
  ELSE IF changes and the view is on the block: CALL drawChanges of the timeline with the kind
  ELSE IF changes: CALL drawPair with the version before and the version on screen (or the draft)
  ELSE: CALL kindView with the state on screen (a tree of the kind)
  KEEP the scroll IF it shows the same thing
ELSE
  SHOW the editor and HIDE the pane""",

"state-view/local.edit": """\
READ the text of the editor
SET draft = the text, or null IF it is the same as the saved text
IF there is a draft: the view leaves the chosen block
SET unsaved = there is a draft
SET position = the newest (the draft is after the last version)
SET error = "", fixable = false
TRY to parse the text (JSON with comments)
IF it fails
  SET error = the message
  IF autofix repairs it: SET fixable = true""",

"state-view/local.step": """\
SET last = the last position (the draft counts when there is one)
SET position = position + delta, not past the first or the last
the view leaves the chosen block (Changes shows the changes of the version)""",

"state-view/local.toggle-changes": """\
IF details is on: SET changes = true
ELSE: SET changes = NOT changes
SET details = false""",

"state-view/local.toggle-details": """\
SET details = NOT details""",

"state-view/local.toggle-timeline": """\
SET timeline_open = NOT timeline_open
IF timeline-view is not mounted: CALL render timeline-view""",

"state-view/local.toggle-tracking": """\
SET track_state = NOT track_state""",

"state-view/local.collapse-all": """\
FOR EACH line of the editor, from the last to the first
  IF an object starts on the line: FOLD it""",

"state-view/local.open-viewer": """\
READ the value at path, as it is on the screen (an older version shows its own)
SET viewer_path = path
SET the memory of the viewer: the keys, the first value, can you edit it
CREATE the editor of the viewer once
SET its mode by the kind: html, code, json, md or text
IF html
  RUN the view in the frame next to the code, with a copy of the state that has this html
  AFTER each action in the frame: SHOW the ui-data of the view and what changed
  WHEN you type: WAIT 400 ms, then RUN it again
IF md
  SHOW the text as a page that you edit in place, in the md theme
  FOR EACH line: a heading, an item, a step or a paragraph
  A heading folds its section; Enter adds a block; Backspace joins blocks
  EACH edit goes back into the text of the viewer
SHOW the viewer""",

"state-view/local.filter": """\
SET filter = text (empty text shows all)""",

"state-view/local.filter-kind": """\
IF kind is not all, files, views, functions, network or environment: THROW
SET filter_kind = kind
SET details = false""",

"state-view/local.toggle-empty": """\
SET show_empty = NOT show_empty""",

"state-view/local.set-md-theme": """\
IF theme is not reader, white, black, sepia, night or mono: THROW
SET md_theme = theme""",

"state-view/local.close-viewer": """\
IF you can edit the viewer and its text changed
  PUT the new text into the editor, in place of the old value
SET viewer_path = ""
STOP the timer of the viewer and forget it
EMPTY the frame and hide the viewer
IF the text went into the editor: CALL local.edit""",

"state-view/local.save": """\
READ the text of the editor
IF it is the same as the saved text: THROW "Nothing to save"
TRY to parse the text
IF it fails: SET the text = autofix(text), parse it again, SET fixed = true
SET the ui-data of state-view in the text to the new version (version, position, no draft)
WAIT for the database to save the new version (commit n + 1)
SET the live state = the new state
SET the base text = the text; there is no draft; the view leaves the chosen block
SET the editor text IF it is not the same
SHOW a green border for 2 seconds
CALL render header-view
RETURN { version, changes (the first 50 paths), fixed }""",
}
