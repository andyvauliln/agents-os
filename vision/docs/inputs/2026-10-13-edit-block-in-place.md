# Input 2026-10-13: edit a block in place, not as Markdown

- From: the owner, in the thread "Interactive file tree UI"
- Date: 2026-10-13

## Words
~~~text
can we when we edit file block in ide  not change format to md again for editing, just same box but just edit there
~~~

## Answer
~~~text
Done: a double-click in the Read view now makes the block itself editable, looking as it reads (paragraphs, headings, lists, tables, code blocks, quotes). Save turns it back into Markdown and writes only those lines. A Markdown button still opens the source lines; the front matter always opens as source. Page v63, data v58.
~~~

## Processed into
- vision/explorer/file-tree-explorer.html (editBlock, wysMarkdown)
- apps/project-IDE/docs/README.md and README.asd.md (Edit in place)

## Follow-up (2026-10-13)
~~~text
after edit if i click ouside the block close it
~~~

## Answer
~~~text
Done: a click outside the block saves it (only if something changed) and closes it, in both the rich edit and the Markdown edit. Esc still closes without saving.
~~~
