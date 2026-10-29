# The extension: views and functions

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
- A view keeps what cannot be in the state in os.refs['<view name>']. The refs go when the view unmounts.