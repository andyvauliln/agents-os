# in-20261009-1459: The page tree always matches the files on disk
- At: 2026-10-09T14:59:30Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbxUpGo999gnv8GqrM5PiHDLe
- Categories: ui, structure
- Summary: The owner restates the rule: the File Tree page must always show the real file tree on disk, so vision/ must be on it.

## Raw input
~~~text
why i can't see it in a file tree how i said we always should have real represention of file tree on a disk and on ui
~~~

## Answer
~~~text
Fixed. The page now shows every real file in the repository, vision/ included (1,479 files); only git's own files and the secrets folder are left out. A file's text loads when it is opened. Page v52, PR #3.
~~~

## Processed into
- D-061 (updated); tools/enrich.py (scan of every folder); page v52; PR #3
