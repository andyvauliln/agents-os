# Input 2026-10-15: one panel for AI notes and runs, with run details

- From: the owner, in the Claude Code chat on the owner's server
- Date: 2026-10-15

## Raw input
~~~text
So for AI notes, it's right now only working on every folder details or file details. Now I just want that it when I make send.  it sends, but I want to see a job after in a header for all notifications. there will be notification messages about runs and another we add them later, and there I wanna see the row about this ai note. I can cancel them, delete, I can send them, I can edit them after triscribe. it has statuses, transcribing, sending, working, done, So also I need the button at the bottom of this section send all, notification section should be hidable make toggle button in a header. When i send all or selected it combine in one and tracking it all in one run. Show also from which version it sends and it which was fixed,  Also I want to see details about this note. If I press it, i want context that we send from ui for now it'f from whee was note recorded or sent or additional context later we need,  make recording input textarea with a size of the message, in a notes and in a page bottom, on list view of notification i also want to see path from where the notes with a checkbox to not send it, also button "send after transcript",  there should be also shown runs from terminal claude put current there, in details pages for this run i want to see all details about this run step by step what agent did with a collapsable steps, i want what files it reads, what skills, he use what subagents runs, mcp, tools, plugins, workflows, etc what files changed,  his context on every steps, output input from tools subagents etc, at start out input and output, git status and data like workspace branch, test data, plan if exist, asd style run summary, make pr make pr and merge,  mark also runs with a tags, like question, i don't know some meaningfull short info, also on a file or folder pages if i select text and press record it goes also as a context, add last 3 runs already there including this one
~~~

## Answer
~~~text
This is a change to the page and the server, so it gets a plan first: apps/project-IDE/data/plans/2026-10-15-0925-notes-and-runs-panel.md. Nothing is built until the owner says go.
~~~

The owner answered the plan's questions and said go without pull requests (D-074). Built and tested on the owner's server on 2026-10-15: a Notes and runs panel in the header of the server page lists every note (typed, recorded, or about selected text) and every Claude Code run in the repository, terminal runs too, 10 at a time with Show more, those that need the owner first; notes can be edited, sent, cancelled, deleted and sent together as one run, with the send options (local, auto merge, related tests, bug check, report); each run from the page works on its own branch in .worktrees/ and the server merges it into main locally; each run has its own page with every step, what it used, git, checks, plan, and a summary in ASD-STE100 with tags by Claude Haiku. Make PR and Make PR and merge are shown but off: pull requests wait for a later step.

## Processed into
- D-074 (decisions.md)
- apps/project-IDE/data/plans/2026-10-15-0925-notes-and-runs-panel.md (distributed; pull requests wait)
- apps/project-IDE/data/changelog.md (2026-10-15)
- apps/project-IDE/server/: runs.py, worktrees.py, notes.py, run_summary.py (new, with How it works and Details); server.py, claude_bridge.py, server.config.json (changed, with metadata); README.md and README.questions.md
- apps/project-IDE/current-ui/file-tree-explorer.html (and its metadata)
- .gitignore (and its metadata)
- apps/project-IDE/docs/vision.md, README.md (parts "Notes and runs", "The page of a run"), README.asd.md, rebuild-prompt.md
- agents/system/.claude/skills/ide-sync/SKILL.md (notes on the server)
- agents/system/CLAUDE.md (section "The File Tree page")
- apps/docs/README.md, apps/docs/README.asd.md, apps/docs/rebuild-prompt.md, docs/README.md, docs/README.asd.md, docs/rebuild-prompt.md
