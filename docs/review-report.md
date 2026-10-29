# Review report (v48)

This report tells what the review of v48 found: what was removed, the bugs, the speed, and how the architecture can change. The changes that the owner must approve are proposals only.

## Summary
- Removed: 35 lines of style rules that no element uses, 1 variable that no code uses, and the old long notes in .claude/CLAUDE.md (the docs hold them now).
- Fixed: 4 bugs (a save could undo a new version, the test times mixed whole tests with functions, the docs view showed ### and indented items as plain text, and a save error said "Invalid JSON").
- Found, not fixed: 3 problems of the runtime (speed, and a new version that waits after a draft).
- Proposals: 6 changes of the architecture. The biggest gain is a smaller state.

## What was removed
1. Style rules of old versions (gen/make_state.py and gen/style_part.py). No element has these classes now:
   - .st-bar, .st-title, .st-close, .st-filter, #st-filter, #st-filter-input (the old bar of the state view).
   - .sv-check, .sv-checks, .sv-switch, .sv-switches, .sv-track (the old check boxes and switches; v46 made them buttons and tabs).
   - .tl-check, .tl-tabs, .tl-tab, .tl-detail-head (the old timeline details; the tabs of the state view do this now).
   - .fv-badge-js, -ts, -html, -css, -json, -md, -py, -sh and the others (the file badge went in v47; .fv-badge stays for the pseudo code badge).
   - .ar-files, .legend, .lg-add, .lg-upd, .lg-del.
2. The variable coreFile in timeline-view local.refresh (defined, never used).
3. The old notes in .claude/CLAUDE.md (24 KB, a part was out of date: the Details field, the kind buttons). The file is now short: where things are, a code map, the rules and the release steps. The details are in docs/. The old text is in git history (commit e57163b).
4. how-it-works.md was one doc of 4900 words. It is now split: each part has its own doc (see overview.md).
Nothing in the state shape was removed: no field and no function.

## Bugs that were fixed
1. A save could undo a new version. While you edit the state (a draft), the page does not run a new version that comes. Save then took the newest version as the parent, but saved your text, which has the old state. So the changes of the new version went away without a message.
   Now: local.edit keeps the version that the draft starts from (os.refs['state-view'].draftFrom). local.save does not save when a newer version came. The bar says: "vN came while you edited vM. Copy your edit, reload the page, then edit again." A page test checks this.
2. The test times mixed two kinds of records. gen/performance.json counted the records of each test run (runTest, the whole test) under the short name of the function (for example local.init). So 32 entries had wrong names and wrong times, and the Performance tab could not find them. Now the page test counts only the calls of functions.
3. The docs view showed "### A block" as a paragraph, and an indented "- " item as plain text. Now ### is a heading and an indented item is an item. A .json file in docs shows as code.
4. Save with an error that is not a JSON error showed "Invalid JSON: ...". Now local.edit adds "Invalid JSON:" to its own message, and the bar shows each error as it is.

## Problems that were found, not fixed
These need a change of the runtime (index.html), so a new publish of the runtime. They are proposals B and C below.
1. Each call copies the whole state two times (before and after) and compares the copies. With a state of 2.5 MB this takes about 150 ms for each call, also for a call that does almost nothing (recorder-view local.refresh: 19 calls, 3 s in total in one test).
2. After each top-level call, each view that watches runs local.refresh, also when nothing that it shows changed. A click is 4 calls: the click, then state-view, timeline-view and recorder-view refresh. A tab click takes about 1 s.
3. A new version that comes during a draft stays in the history, but the page does not run it after the draft ends. You must reload. (The fix above stops the data loss. It does not load the version.)

## Unused, but kept
- state-core.js exports esc, historyLength, kindOf and stripComments. No code outside state-core.js uses them. state-core.js uses them itself. To remove them from the exports needs a new publish of the runtime and gives nothing.
- .claude/commands, hooks, output-styles and skills hold only .gitkeep. They are the default folders of the agent (inputs m00, m01).
- extension.data, common_app_storage and apps are empty. They come from the first state (m00) and are part of the vision.
- The Improvements and Video tabs are empty. They are in the plan of the owner (m69).

## Speed (measured in this container, headless Chromium)
- The page opens (to ready): 3.6 s.
- Open the state view: 0.5 s.
- Open the timeline: 4.3 s.
- Click a tab of the state view: 1.0 to 1.4 s.
- Only changes on: 1.5 s.
- state-view local.refresh: 0.4 s for each run (max 1.1 s).
- A call that does almost nothing: about 0.15 s.
The state is 2.5 MB: agents.agent-oss.files is 2.1 MB of it. vendor/ is 926 KB (37 %), runs/ 484 KB (19 %), gen/ 413 KB, tests/ 111 KB. The views and functions are 406 KB.

## Architecture: what works well
- One state, one runtime: the page has no hidden parts. The runtime does not know the views.
- Each call is recorded with its changes, errors and time, and each function has tests in the state.
- Versions with the source, the request and explain make each change easy to follow.
- The generator makes the state, the docs and the tests from one place, and checks that each function has pseudo code.

## Architecture: proposals
A. A smaller state. vendor/ (926 KB) is a copy of the library files, which the page loads as files of the artifact and lists under network packages. Keep vendor files in agents.agent-oss.files as metadata (path, size, version, license) and not as text. The state goes from 2.5 MB to about 1.6 MB. Each call, each version file and each draw of the editor gets faster. This changes the rule "the files are every file of main", so the owner must approve it.
B. Cheaper calls. The runtime can record only the paths that a function sets, or copy only the parts that change, in place of two full copies and a full diff for each call. A change of the runtime.
C. Fewer refreshes. A view that watches can tell which paths it shows. The runtime runs its local.refresh only when one of them changed. A change of the runtime.
D. Smaller functions. timeline-view local.refresh is one function of about 2000 lines. The other views use its helpers through os.refs['timeline-view']. Move the helpers (file view, kind view, changes view, run view, performance) into their own functions in the state. Then each has its own tests, docs, pseudo code and performance, as the principles ask. This adds functions to extension.functions, so the owner must approve it.
E. Code in code files. gen/make_state.py is 4700 lines, and the code of each function is a text in Python. Put the code of each function in its own .js file (for example gen/views/state-view/local.save.js). The generator reads them. Then a code editor can check and color them.
F. One md parser. The docs view has its own md parser in its html template. state-core.js already has mdParse, which the file viewer uses. The docs view can use mdParse too.

## The order that this report proposes
1. A (smaller state): the biggest gain, one rule changes.
2. C and B (runtime): faster clicks.
3. D and E (code): easier to read and to test.
4. F (docs view).