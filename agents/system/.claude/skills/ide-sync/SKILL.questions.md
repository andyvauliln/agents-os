# Questions: SKILL.md

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-05: How page notes and comments become agent work

> also not clear how we now hanlding agentic works from the ui comments and notes on files and folders?

Everything left on the page is saved at once in the page's store and marked "changed". When the owner presses Apply changes or says "sync the file tree", this skill files each message as an owner input word for word, writes edits into their files, applies notes meant as changes and turns other open notes into open questions, runs the requests, cleans up deletions, hands the inputs to the knowledge base agent and rebuilds the page with `ide-build`. On the owner's server, edits go into the files at once and a request runs Claude Code straight away.
