# How the page renders from the state

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
```js
call('extension.functions.render', { view_path: 'extension.views.index-view' });
```
## Example 2: render (steps 8 to 12)
This is the code of extension.functions.render. The import lines at the start name what it uses: os and ctx. Its imports field is { "os": "index.html", "ctx": "index.html" }, because the runtime index.html gives them. render returns nothing, so its output is {}.
```js
import os from 'os';
import ctx from 'ctx';

async function render({ view_path }) {
  const view = os.get(view_path);
  if (!view) throw new Error('No view at ' + view_path);
  // A view renders into the element whose id is its name.
  const id = view_path.split('.').pop();
  const root = document.getElementById(id);
  if (!root) throw new Error('No element #' + id);
  // Its html has one root element with the same id. That element takes the place of the empty one.
  const t = document.createElement('template');
  t.innerHTML = os.template(view.html || '', view['ui-data'] || {});
  const el = t.content.firstElementChild;
  if (!el || el.id !== id) throw new Error('The html of ' + id + ' must start with one element with id="' + id + '"');
  root.replaceWith(el);
  os.bind(el, view_path);
  os.setMounted(view_path, true);
  if (view.functions && view.functions['local.init']) await os.call('local.init', {}, view_path, ctx.id);
}
```
## Example 3: html and ui-data become the page (step 10)
1. The html of header-view starts with its root element. It has this button:
```html
<header id="header-view">
  <button class="btn" id="state-button"
          data-call="local.open.state-view"
          aria-pressed="${d.state_open}" aria-label="State view" title="State view">
```
2. The ui-data of header-view is:
```json
{ "docs_open": false, "state_open": false, "device": "desktop", "device_open": false }
```
3. render replaces ${d.state_open} with the value from ui-data. The page gets this button:
```html
<header id="header-view">
  <button class="btn" id="state-button"
          data-call="local.open.state-view"
          aria-pressed="false" aria-label="State view" title="State view">
```
## Example 4: local.init of index-view (step 13)
```js
import ctx from 'ctx';

async function init() {
  const view = await ctx.call('extension.functions.get-state', { path: 'extension.views.header-view' });
  if (!view) throw new Error('No header-view in the state');
  await ctx.call('extension.functions.render', { view_path: 'extension.views.header-view' });
  await ctx.call('extension.functions.render', { view_path: 'extension.views.recorder-view' });
}
```
The call to get-state returns the header-view part of the state. Its output is that JSON. This is the code of get-state:
```js
import os from 'os';

async function getState({ path }) {
  // The JSON state: all of it, or the part at path.
  const value = path ? os.get(path) : os.get();
  if (value === undefined) throw new Error('Nothing at ' + path);
  return os.clone(value);
}
```
## Example 5: local.init of header-view (step 15)
```js
import os from 'os';
import ctx from 'ctx';

async function init() {
  // Views that ui-data says are open are opened again.
  const d = os.get('extension.views.header-view.ui-data');
  // All the views show at the width of the device in ui-data: Mobile 390 px, Tablet 820 px, Desktop the full page.
  const root = document.getElementById('index-view');
  if (d.device && d.device !== 'desktop') root.dataset.device = d.device;
  else delete root.dataset.device;
  // While the device menu is open, a click out of it or Escape closes it. A new init takes the place of the old listeners.
  const old = os.refs['header-view'];
  if (old && old.off) old.off();
  const close = () => os.call('local.toggle-device-menu', { open: false }, 'extension.views.header-view').catch(console.error);
  const onDown = e => { if (d.device_open && !e.target.closest('.dev-pick')) close(); };
  const onKey = e => { if (d.device_open && e.key === 'Escape') close(); };
  document.addEventListener('pointerdown', onDown, true);
  document.addEventListener('keydown', onKey);
  os.refs['header-view'] = { off: () => { document.removeEventListener('pointerdown', onDown, true); document.removeEventListener('keydown', onKey); } };
  // After the Reload button of the timeline, the state view opens again with the timeline.
  let replay = location.hash === '#timeline-replay';
  try { replay = replay || sessionStorage.getItem('agent-os.timeline-replay') === '1'; } catch (e) {}
  if (replay) { d.state_open = true; os.get('extension.views.state-view.ui-data').timeline_open = true; }
  // (one main view at a time: the state view, when both say open)
  if (d.docs_open && d.state_open) d.docs_open = false;
  if (d.docs_open && !os.mounted('extension.views.docs-view')) await ctx.call('extension.functions.render', { view_path: 'extension.views.docs-view' });
  if (d.state_open && !os.mounted('extension.views.state-view')) await ctx.call('extension.functions.render', { view_path: 'extension.views.state-view' });
}
```
## When you click a button
1. The button calls the function in its data-call, with the input in its data-input.
2. The function changes the state. For example, local.open.state-view changes ui-data.state_open of header-view.
3. The function renders the views that must change.
4. The runtime compares the state before and after the call. It checks the change against expected-state-change.
5. The state view watches the state. After each call, its local.refresh function shows the new state.

## Example 6: you click the State button
1. The button has data-call="local.open.state-view". It has no data-input, so the input is {}.
2. The runtime runs local.open.state-view of header-view:
```js
import os from 'os';
import ctx from 'ctx';

async function openStateView() {
  const d = os.get('extension.views.header-view.ui-data');
  d.state_open = !os.mounted('extension.views.state-view');
  // One main view at a time: the one that is open closes.
  if (d.state_open) for (const o of ["docs-view", "notes-view"])
    if (os.mounted('extension.views.' + o)) await ctx.call('extension.functions.unmount', { view_path: 'extension.views.' + o });
  d.docs_open = d.state_open ? false : d.docs_open;
  d.state_open = d.state_open ? true : d.state_open;
  if (d.state_open) await ctx.call('extension.functions.render', { view_path: 'extension.views.state-view' });
  else await ctx.call('extension.functions.unmount', { view_path: 'extension.views.state-view' });
  await ctx.call('extension.functions.render', { view_path: 'extension.views.header-view' });
}
```
3. Before the run, ui-data.state_open of header-view is false. After the run, it is true.
4. The expected-state-change of the function permits this change:
```json
{ "extension.views.header-view.ui-data.state_open": "may change" }
```
5. render and local.init of state-view also change the state. These changes are their changes, not changes of local.open.state-view.
6. The runtime writes the result into the function: output is {} because the function returns nothing, performance gets the time of the run, errors is [].
7. render draws header-view again. Now the button has aria-pressed="true".

## Example 7: a button with input
The left arrow button of the state view has data-input. The input goes to the parameter delta.
```html
<button class="btn" id="older"
        data-call="local.step" data-input='{"delta":-1}'>
```
```js
import os from 'os';

async function step({ delta }) {
  // Older and Newer go through the versions: the view leaves the chosen block.
  const d = os.get('extension.views.state-view.ui-data'), R = os.refs['state-view'], H = os.history.commits;
  const last = H.length - (R.draft === null ? 1 : 0);
  d.position = Math.max(0, Math.min(last, d.position + (+delta || 0)));
  R.onBlock = false;
}
```
The expected-state-change of local.step is { "extension.views.state-view.ui-data.position": "may change" }. After the run, local.refresh shows the version at the new position.