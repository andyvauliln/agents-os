# in-20261009-2219: Will the project IDE work on the server like the page here?
- At: 2026-10-09T22:19:59Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbxLNAyMPm2NpbfD1PSw417sX
- Categories: question, ui
- Summary: The owner asks whether starting the project IDE now works the same as the page on claude.ai.

## Raw input
~~~text
if i start project-ide right now will it works same like current artifcat does
~~~

## Answer
~~~text
Not before this change: the server looked for apps/project-IDE/ and agents/system/, which the repository does not have yet, so it found no page and Claude Code had no folder to start in. Now the server runs from the planning folder vision/: the page from vision/explorer/, edits written into the file the page showed (a draft in vision/ or a real file), How it works edits into the item's .index.md, the real files' texts read fresh from disk, Claude Code started in vision/. Differences from claude.ai by design: the request box needs claude-agent-sdk and Claude Code signed in on the server; voice needs GROQ_API_KEY; notes are kept as files in vision/page-store/.
~~~

## Processed into
- server/server.py, server.config.json, server/README.md; tools/enrich.py (src_file); changelog 2026-10-09
