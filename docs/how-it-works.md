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
overview.md lists all the docs. Each part of the page has its own doc: state.md, extension.md, functions.md, runtime.md, render-steps.md, flow.md, state-view.md, timeline.md, network-and-environment.md, agent-runs.md, recorder-and-notes.md and generator-and-release.md.