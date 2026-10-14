# in-20261005-1517: project IDE into apps/, show the server code, run Claude Code from the system
- At: 2026-10-05T15:17:53Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxABNN6ywoT1kYBGHBSGjvHW
- Categories: structure, ui, agents, sync
- Summary: Move project-IDE into apps/; the owner sees no code in the server files in the tree; and agrees Claude Code on the server must start from the system folder.

## Raw input
~~~text
let's put project ide in a apps and i don't see any files with a code in a tree file, and yes we ll need to run from the system
~~~

## Answer
~~~text
Done: the project IDE is now apps/project-IDE/, in the tree, the docs and the How it works files. The server is written: server.py (the page, its notes and edits kept as files in the repository, edits written straight into their files), claude_bridge.py (each request runs as a Claude Code session started in agents/system/, with every step checked first) and server.config.json, plus a README on how to start it and reach it through an SSH tunnel. The code shows on each file's File tab. I tested it on a copy of the repository: the page found the server, an edit landed in its file, and a real request listed the system's two agents and six skills. A push asked for the owner's click and was refused when Refuse was pressed. It goes live after the GitHub sync.
~~~

## Processed into
- D-043
- docs/file-tree.md v1.20: [53] under [43] `apps/`; [43] purpose; [53.3] and [53.3.1]–[53.3.4] decided with drafts; new [53.2.7] `page-store/`
- vision/server/: server.py, claude_bridge.py, server.config.json, README.md (new)
- the page: server mode; enrich.py shows the server files
- the project IDE agent, ide-sync, ide-build, knowledge-intake, the knowledge base agent; CLAUDE.md, .claude/docs/README.md, plans/github-sync.md, plans/server-ide.md, tools/README.md, docs/README.md
- the How it works files moved under tree/trading-os/apps/; changelog
