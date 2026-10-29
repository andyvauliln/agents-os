# Agent OS: overview

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
- .claude/: the default files of the agent (CLAUDE.md, settings, agents/run-recorder.md).