# in-20261012: After a pull, the disk does not match the page's tree
- At: 2026-10-12 · Where: thread "Interactive file tree UI" · Source: chat
- Categories: ui, structure
- Summary: The owner pulled main and the files on disk differ from the tree the page shows.

## Raw input
~~~text
fuck man why i just pull last version and i don't have same file tree as i have on current ide
~~~

## Answer
~~~text
The page also showed about 400 planned files and folders that are not on disk yet (agents/system, the prediction-market domain, apps/project-IDE and more), mixed in with the real ones; their texts were drafts kept in vision/. Now a "planned" switch, off by default, hides them, so the tree is exactly the files in git. Checked file by file: 1,509 paths on disk, 1,509 on the page, no difference. Also: files git ignores are left out of the tree, and four How it works and Details files of the keys files that .gitignore was wrongly hiding are now in git.
~~~

## Processed into
- explorer/file-tree-explorer.html (planned switch); tools/enrich.py (git-ignored files left out; the .secrets mirror notes shown); .gitignore; inputs-vision.md UI-02, UI-09; changelog
