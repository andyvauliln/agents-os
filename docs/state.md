# The state

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
    "views": { "header-view": { "html": "<header id=\"header-view\">...", "ui-data": { "state_open": false }, "functions": { "local.init": {} } } },
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
- Change the generator (gen/), not state.json. See generator-and-release.md.