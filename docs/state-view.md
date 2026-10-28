# The state view

## Open the state view
1. Click the State button in the header.
2. The state view shows the chosen block of the timeline. When no block is chosen, it is the last agent run. The editor shows the state at the version of the block.
3. The state view is the one view for the state and its changes. Its bar has, from the left: the Timeline button, the kind buttons, Changes and Details, the filter with Show empty and Track state, then Collapse all, Save, Older and Newer.

## Edit and save the state
1. Edit the JSON in the editor. You can write comments with // and /* */.
2. Push Cmd+S or Ctrl+S, or click the Save button.
3. If the JSON has small errors, the save repairs them first.
4. The border of the editor becomes green for a short time. This shows that the new version is saved.

## Filter the state
1. Type in the filter at the top of the state view.
2. The editor shows only the entries whose path has the text, with the first and last lines of the objects around them.
3. The other lines fold into "⋯ N lines". You can still edit the lines that show.
4. Click Files, Views, Functions, Network or Environment to see only that kind, as a tree: for example, Files shows the files in their folders. Click one in the tree to see it on the right. With Changes, an updated md file in read mode shows its changes: green lines are new or changed, red lines are removed. Put the pointer on a green or red line to see why the run changed the file. Click All to see the editor again. This works with or without text.
5. Click Changes to see only what the chosen block changed. After Older or Newer, it is what the version on the screen changed. Click Details to see what happens inside the block.
6. Clear Show empty to hide the entries with an empty value: {}, [], "" or null. They hide with no "⋯" mark.
7. Turn on Track state to add what you do in the state view and the timeline as blocks of the timeline.
8. Push Escape to clear the filter.
- Older and newer (the arrows) are at the right end of the bar.
- The version, the path and the status are in the bar at the bottom of the state view.

## Look at older versions
1. Click the left arrow button, or push the left arrow key. The state view leaves the chosen block.
2. You cannot edit an older version.
3. Click the Changes button to see only the changes of that version. Green is added, yellow is updated, red is deleted.

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