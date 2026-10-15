# in-20261005-1043: repo layout corrected: project-IDE folder with current-ui and data
- At: 2026-10-05T10:43:14Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxL2ZYjgrbU4URUjJCQoZ2ej
- Categories: structure, process, ui, docs-knowledge
- Summary: Corrects in-20261005-1041: the repo also has a top-level project-IDE/ with current-ui/ (the current page artifact) and data/ (the data the page needs and this planning project's knowledge). The IDE logic (agent, skills) stays in agents/system/.claude.

## Raw input
~~~text
sorry i mean like this > i think we should have something like this what do you think?
trading-os (github-project)

* trading-ui
* project-IDE
   * current-ui (current ui artificat)
   * data(your current data you need for the ui and knowledges for this planing project)
* agents (represent current file tree how it’s right now we see it all should be already all confirmed from what files exist in a tree right now)
   * system
      * .claude
project-ide logic ( subagent, skills, whatever agent things that responsible for building and updating ide project and how from ide we update files, or metadata, views, handling user notes, or running requests)
~~~

## Answer
Agreed: project-IDE/ holds current-ui/ (the File Tree page) and data/ (page data plus this project's knowledge: inputs, decisions, changelog, sources, the map); trading-ui/ stays the later trading dashboard; agents/ is the tree as it is now, all agreed, with a .index.md next to every file; agents/system/.claude/ holds the agents (knowledge-base-agent, project-ide-agent), skills (knowledge-intake, file-index, doc skills, ide-build, ide-sync) and the people docs. Ours: the build scripts live inside the ide-build skill. Waiting for the owner's go.

## Processed into
- plans/github-sync.md (owner's layout with project-IDE/, proposed, waits for go); memory github-sync-plan
- Then (in-20261005-1254): D-041; file-tree.md v1.18; project-ide-agent, ide-build, ide-sync; CLAUDE.md; plans/github-sync.md; data v22.
