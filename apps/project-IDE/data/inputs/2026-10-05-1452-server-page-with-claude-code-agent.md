# in-20261005-1452: the page on the owner's server, with an agent that sends requests to Claude Code
- At: 2026-10-05T14:52:24Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxTjSgV9XDnEeZ7vVVkxSMfp
- Categories: ui, sync, agents, process
- Summary: Answering the 14:33 offer, the owner wants the page on their own server too, with the ability to run an AI agent from it that sends requests to Claude Code connected to the Trading OS project.

## Raw input
~~~text
i mean yes i would love to have on a server also ability to run ai agent that can send request to claude code connected to this trading os project
~~~

## Answer
~~~text
Recorded as a decision: the page also runs on your server, and its request box sends requests to Claude Code working in the repository. The design is a proposal for you to check. It uses one page file for both places. A small service in project-IDE/server/ serves the page from the repository, saves your notes and edits straight into the files, and runs each request as a Claude Code session through the Claude Agent SDK, showing its progress, cost and time. The service can only be reached from the machine or a private network. Pushing, deleting and anything outside the repository wait for your click. It is built after the GitHub sync, because the server works from a clone of the repository.
~~~

## Processed into
- D-042 (the wish decided; the design proposed)
- docs/file-tree.md v1.19: new proposed [53.3] project-IDE/server/ with README.md, server.py, claude_bridge.py, server.config.json; [53], [53.1.1], [53.2.5], [10.1.1.3] updated
- plans/server-ide.md (new); plans/github-sync.md (points to it)
- .claude/docs/README.md: one sentence on the page on the server
- changelog.md; the page data
