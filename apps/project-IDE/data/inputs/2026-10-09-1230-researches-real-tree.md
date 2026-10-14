# in-20261009-1230: Move researches/ to trading/researches/; the tree shows the real files
- At: 2026-10-09T12:30:57Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbxHAnP7x6aib4EPEQxuFko43
- Categories: structure, page-sync
- Summary: The owner asks to pull the latest repository, move its researches/ folder to trading/researches/, and make the File Tree page show the project's real file tree.

## Raw input
~~~text
get last version from github there will be researches folder move it to trading/researches folder, and make sync that current file tree represent real file tree in a project
~~~

## Answer
~~~text
Done. The repository's researches/ now sits at agents/trading/researches/ with all three studies (the prediction-market research, self-improving agents and trading-agent architectures). The File Tree page reads the repository at every build: it marks what exists and lists every real file under it (214 today), each with its text on the File tab. The planning copy vision/ is left out of the tree. Page v51.
~~~

## Processed into
- D-061; the repository (git mv); file-tree.md v1.34 ([56], [56.2], [54]-[54.3]); tools/enrich.py and build_map.py (real file scan); mirror tree; page v51
