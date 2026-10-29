# The state view

## Open the state view
1. Click the State button in the header.
2. The state view shows the chosen block of the timeline. When no block is chosen, it is the last agent run. The editor shows the state at the version of the block.
3. The state view is the one view for the state and its changes. It has two rows at the top.
   - The bar, from the left: the State icon with Agent or UI (the kind of the chosen block of the timeline: an agent run or a UI block; some logic of the UI is different for each), the filter, Only changes, Show empty, then Track this view, Timeline, Collapse all, Save and close (×). Put the pointer on an icon to see its name.
   - The tabs: Full State, Files, Views, Functions, Network, Environment, Performance, Improvements, Flow, Video, Docs and Agent Run.
4. Full State is the whole JSON of the state. The other tabs are parts or views of the same state:
   - Files, Views, Functions, Network and Environment: only that kind, as a tree on the left and the chosen one on the right.
   - Flow: what happens inside the chosen block (its parts and its calls; an AI run shows its notification).
   - Agent Run: the AI run notification of the chosen AI run block, or of the last AI run.
   - Docs: only the docs folder of the agent.
   - Performance, Improvements and Video are empty for now.

## Edit and save the state
1. Edit the JSON in the editor. You can write comments with // and /* */.
2. Push Cmd+S or Ctrl+S, or click the Save button.
3. If the JSON has small errors, the save repairs them first.
4. The border of the editor becomes green for a short time. This shows that the new version is saved.

## Filter the state
1. Type in the filter at the top of the state view.
2. The editor shows only the entries whose path has the text, with the first and last lines of the objects around them.
3. The other lines fold into "⋯ N lines". You can still edit the lines that show.
4. Click the Files, Views, Functions, Network or Environment tab to see only that kind, as a tree: for example, Files shows the files in their folders. Click one in the tree to see it on the right. With Changes, an updated md file in read mode shows its changes: green lines are new or changed, red lines are removed. Put the pointer on a green or red line to see why the run changed the file. Click Full State to see the editor again. This works with or without text.
5. Click Only changes to see only what the chosen block changed. After Older or Newer, it is what the version on the screen changed. On a tab that is not a part of the state (Flow, Agent Run, Docs, Performance, Improvements, Video), Only changes goes to Full State.
   For an AI run, Full State also keeps the files that the run read or ran, and its default context (.claude/CLAUDE.md for the main agent, .claude/agents/<name>.md for a sub agent). Badges after the line of a file tell who (main or sub agent) and what (read, changed, run, default context).
6. Click Show empty to hide the entries with an empty value: {}, [], "" or null. They hide with no "⋯" mark. Click it again to show them.
7. Click Track this view to add what you do in the state view and the timeline as blocks of the timeline.
8. Push Escape to clear the filter.
- Older and Newer (the arrows with the version between them) are in the bar of the timeline. The arrow keys do the same. On a touch screen, swipe the timeline: right for older, left for newer.
- The version, the path and the status are in the bar at the bottom of the state view.

## Look at older versions
1. Open the timeline. Click its Older arrow, or push the left arrow key (or swipe the timeline to the right). The state view leaves the chosen block.
2. You cannot edit an older version.
3. Click Only changes to see only the changes of that version. Green is added, yellow is updated, red is deleted.

## Long text
- Long text, and text that has more than one line, shows as "...". A text of only {} or [] (an empty json file) shows as it is, in grey, and Show empty off hides it. Put the pointer on it to see the start of the text, in the colors of its kind (md, js, html, css or json).
- Click the "..." to open the text in the viewer. You can edit it there.
- When you close the viewer, your changes go into the editor. Then save them.

## Read and edit an md file
1. Click the "..." of an md file, for example agents.agent-oss.files.docs.how-it-works.md.
2. The file shows as a document. Click a line and edit the text there.
3. Push Enter to start a new line of the same kind: a new item, the next step, or a paragraph.
4. Push Backspace at the start of a line to remove its mark. Push it again to join the line to the line before it.
5. Click the arrow next to a heading to fold its section. Click it again to open the section.
6. Click a theme button above the document to change how it looks: Reader (the default, for long reading), White, Black, Sepia, Night or Mono. The theme stays in ui-data.md_theme.

## Try a view in the viewer
1. Click the "..." of the html of a view, for example extension.views.header-view.html.
2. The html is on the left. On the right, the view runs with a copy of the state.
3. Click a button of the view. The function of the button runs in the copy. Nothing is saved.
4. Below the view, you see the ui-data of the view. The lines that the last action changed are yellow.
5. Edit the html on the left. The view on the right starts again with the new html.