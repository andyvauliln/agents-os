# The state view

## Open the state view
1. Click the State button in the header.
2. The editor shows the live state of the newest version.

## Edit and save the state
1. Edit the JSON in the editor. You can write comments with // and /* */.
2. Push Cmd+S or Ctrl+S, or click the Save button.
3. If the JSON has small errors, the save repairs them first.
4. The border of the editor becomes green for a short time. This shows that the new version is saved.

## Filter the state
1. Type in the filter at the top of the state view.
2. The editor shows only the entries whose path has the text, with the first and last lines of the objects around them.
3. The other lines fold into "⋯ N lines". You can still edit the lines that show.
4. Turn a switch off to hide a kind: Files, Views or Functions. This works with or without text.
5. Push Escape to clear the filter.
- The version, the path and the status are in the bar at the bottom of the state view.

## Look at older versions
1. Click the left arrow button, or push the left arrow key.
2. You cannot edit an older version.
3. Click the Changes button to see only the changes of that version. Green is added, yellow is updated, red is deleted.

## Long text
- Long text, and text that has more than one line, shows as "...". Put the pointer on it to see the start of the text.
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