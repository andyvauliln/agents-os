# in-20261005-1421: the page's own two files show as empty
- At: 2026-10-05T14:21:09Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxF9k4PQiD28Wpah8mjR2F6M
- Categories: ui, question
- Summary: The owner sees project-IDE/current-ui/file-tree-explorer.html and file-tree.data.json as empty files on the page, and asks whether the page they see is supposed to be those two files.

## Raw input
~~~text
why projec ide current ui html and file-tree data is empty files? current artifact ui that i se suppose to be representation of this files?
~~~

## Answer
~~~text
Yes: the page you see is exactly those two files, the page source and the data it loads. They looked empty because the build only put into the page the text of files listed as drafts, and these two were never listed; the data file also cannot hold a copy of itself. Now the page's File tab shows the page source as published, and the data file exactly as the page loaded it, read-only because it is rebuilt every round. Long files show 3,000 lines at a time with a button for more.
~~~

## Processed into
- docs/file-tree.md v1.18.2: [53.1.1] and [53.1.2] File tab lines; changelog v1.18.2
- tools/enrich.py: the page source is shown for [53.1.1] (VISION_FILES); [53.1.2] is marked content_self and readonly
- File Tree page version 30: the data file shows itself, read-only; long files show in steps of 3,000 lines with the size
- ide-build skill: the finished page goes in explorer/ before the data is built
- changelog.md: 2026-10-05 line
