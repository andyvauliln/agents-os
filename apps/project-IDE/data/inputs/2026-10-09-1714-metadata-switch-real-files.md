# in-20261009-1714: The metadata switch also hides metadata files found on disk
- At: 2026-10-09T17:14:45Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbxPGCtozZt3LZS1MLo4qYDLT
- Categories: ui, question
- Summary: The owner asks why real .meta.json files stay in the tree when the metadata switch is off.

## Raw input
~~~text
why files like .claude.meta.json not hidden when checkbox metadata off
~~~

## Answer
~~~text
The switch covered only the metadata rows the page adds for each item; real metadata files scanned from disk came in as ordinary files. Now they follow the switch, and with the switch on each shows once. Page v53, PR #3.
~~~

## Processed into
- explorer/file-tree-explorer.html; page v53; changelog 2026-10-09
