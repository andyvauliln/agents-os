# in-20261005-1041: repo layout: trading-ui, agents as the tree, project IDE logic in system .claude
- At: 2026-10-05T10:41:10Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxFEWkt3wNCiQ4W7s8V4cYUE
- Categories: structure, process, ui, docs-knowledge
- Summary: The owner proposes the GitHub repo layout: trading-ui; agents representing the current file tree as it is now (all of it confirmed); the project IDE logic (sub-agent, skills: building and updating the IDE, updating files, metadata and views from the IDE, handling user notes, running requests) in agents/system/.claude.

## Raw input
~~~text
i think we should have something like this what do you think?
trading-os (github-project)

* trading-ui
* agents (represent current file tree how it’s right now we see it all should be already all confirmed from what files exist in a tree right now)
   * system
      * .claude
project-ide logic ( subagent, skills, whatever agent things that responsible for building and updating ide project and how from ide we update files, or metadata, views, handling user notes, or running requests)
~~~

## Answer
We agreed it is better than a separate planning/ folder: the repo itself becomes the tree. Proposed: root CLAUDE.md, README.md, trading-ui/ (the File Tree page as the dashboard's first screen), researches/, agents/ exactly as the tree is now; agents/system/.claude/ holds agents (knowledge-base-agent, project-ide-agent), skills (knowledge-intake, file-index, vision-doc, readme-doc, ide-build, ide-sync), docs (people) and knowledge (agent notes). Every file and folder is created with its .index.md; a file not written yet exists only as its .index.md; placeholders become folders holding only their .index.md. A second agent, project-ide-agent, builds the page from the repo, turns page notes and edits into file changes and runs requests from the page; build scripts in agents/system/scripts/ide/. "All confirmed" read as: the tree as it is now is the agreed structure, so the 19 proposed items become decided; open questions inside files stay open. Waiting for the owner's go to build, push to the thread branch and open a PR.

## Processed into
- plans/github-sync.md (owner's layout, proposed, waits for go); memory github-sync-plan
- Then (in-20261005-1254): D-041; file-tree.md v1.18; project-ide-agent, ide-build, ide-sync; CLAUDE.md; plans/github-sync.md; data v22.
