# in-20261006-1129: why vision.md and the vision skill show only in search
- At: 2026-10-06T11:29:40Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbxLri9Fo3YiZpiCgZwBnkSow
- Categories: ui, question
- Summary: The owner sees vision.md and the vision skill when searching the File Tree page, but not in the tree without a search, and asks why.

## Raw input
~~~text
when i do search file tree i can see vision.md and another vision skill, why i don't see them in a file tree without search
~~~

## Answer
~~~text
They're in the tree, but inside folders that start closed:

- `vision.md` is in agents → system → .claude → docs.
- The vision skill is in agents → system → .claude → skills, as `vision-doc/SKILL.md`.

A search opens every folder on the way to a match, which is why they show up there.

Until now, your first click on a folder only selected it, so it looked empty. The File Tree page is updated (version 36): a first click on a closed folder now opens it too. A second click, or its arrow, closes it.
~~~

## Processed into
- file-tree.md v1.23: [53.1.1] opening folders (a first click on a closed folder opens it)
- the page v36
- changelog
