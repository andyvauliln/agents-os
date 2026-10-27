# Functions

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
```json
{
  "input": { "path": "extension.views.header-view" },
  "output": { "html": "...", "ui-data": { "docs_open": false, "state_open": false }, "functions": { ... } },
  "imports": { "os": "index.html" },
  "tests": {
    "reads header-view": { "input": { "path": "extension.views.header-view" }, "expect": { "output-has": ["html", "ui-data", "functions"] } }
  },
  "expected-state-change": {},
  "docs": "Returns the JSON state: all of it, or the part at path (for example extension.views.header-view).",
  "pseudo": "READ the state at path (all the state when there is no path)\nIF nothing is at path\n  THROW \"Nothing at <path>\"\nRETURN a copy of the value",
  "performance": { "last": 0.1, "min": 0.1, "max": 0.4, "count": 3 },
  "code": "import os from 'os';\n\nasync function getState({ path }) { ... }",
  "calls": {},
  "errors": []
}
```
## How a function runs
1. A button, a key or a different function calls the function. A shared function has a path, for example extension.functions.render. A function of a view has a local name, for example local.save.
2. The runtime loads the imports. It gives each name of an import line its value.
3. The runtime runs the code with the input.
4. The runtime compares the state before and after the run.
5. The runtime checks the change against expected-state-change. A change that a called function made is not a change of the caller.
6. The runtime writes output, performance and errors.

## Imports
The code can use only what its import lines name. Each name must be in the imports field.
```js
import os from 'os';
import ctx from 'ctx';
import core from 'state-core';
import CodeMirror from 'codemirror';
```
```json
{
  "os": "index.html",
  "ctx": "index.html",
  "state-core": "extension.views.state-view.functions.local.init.imports.state-core",
  "codemirror": "extension.views.state-view.functions.local.init.imports.codemirror"
}
```
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
```json
{
  "turns the changes view on": {
    "before": { "extension.functions.render": { "view_path": "extension.views.state-view" } },
    "input": {},
    "expect": {
      "state": { "extension.views.state-view.ui-data.changes": true },
      "dom": ["#changes[aria-pressed=\"true\"]"]
    }
  }
}
```
1. before renders the state view. Then ui-data.changes is false.
2. The runtime runs local.toggle-changes with the input {}.
3. The runtime checks that ui-data.changes is true and that the Changes button is pressed.