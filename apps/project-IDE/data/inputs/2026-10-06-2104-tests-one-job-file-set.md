# in-20261006-2104: a Tests file and view per code file, skill and agent; one job per code file; what file-set.md is
- At: 2026-10-06T21:04:05Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbxGrhXSDPLjmd7xcW8sw9njJ
- Categories: structure, tests-research, question
- Summary: The owner adds a tests metadata file (Tests tab with its own view that runs tests) for every code file, skill, agent and subagent; sets the rule that every code file holds one runnable thing with one purpose (parameters allowed, no mixed common files; related things in a folder, each with its own metadata) and asks to write it where it belongs; asks whether file-set.md is implemented or only documentation, where such knowledge lives, and whether mechanism detail gets its own files or goes into the README and vision.

## Raw input
~~~text
also i think we need add to file test metadata file that will goes also in a tabs, not all will have for now all code files, skills agent and subagent should have also, and test tabs should also have they own view, where i can run a test, also every code file should have only one function, endpoint or whatever runable one, could with different params, but have one purpose let's not make a common files with different things, better have folder and one things for the file with own metadata, it's pretty common rule so make sure we put it in a right places for documentation and further works. also tell me about file-set.md, so it's already implemented and part just of documentation? and if it's part of documentation where in another knowledges and which way we store it there, because it looks like there a lot of knowledge of how it works and i am not sure should we in such cases have separate files for some logic or add it in a README and vision and such files and reference there, or just have short view on it there, so don't know what we gonna do
~~~

## Answer
~~~text
file-set.md is a plan, not built. Nothing is renamed and the page still works the old way. It sits with the other plans in the planning notes, and the docs only mention it as a proposal. Once you say go, its content moves into the knowledge like everything else, one fact in one place, and the plan is archived:

- The whole mechanism becomes its own note for agents (I'd call it file-family.md), since every file follows it.
- The short rules go into the conventions, and the steps into the skills that do the work.
- The README gets a short paragraph with the path to that note, and the vision gets one sentence.
- The rebuild prompt gets the exact formats.

That's the general answer too: detail lives in its own note or skill, the README gives a short view with the path, and the vision keeps only the idea.

Also done:
- The one-job rule is now in the conventions, the prompt every agent reads, the self-improvement template, the system's CLAUDE.md, the vision, the README and the rebuild prompt. Our own build scripts and the server break it today; splitting them is a step in the plan.
- The plan has a Tests file for every code file, skill, agent and subagent, and a Tests view with Run buttons. On your server Run starts the test; on claude.ai it sends the run to Claude.

The File Tree page is version 41. The card on the file set still waits for your pick.
~~~

## Processed into
- D-050 (decisions.md v1.7, changelog.md 2026-10-06)
- One job per code file: docs/conventions.md v0.2 (One job per code file), docs/common/common-prompt.md v0.2, docs/common/self-improvement-templates.md (base template), .claude/CLAUDE.md (rules), .claude/docs/vision.md (principle "One file, one job"), README.md (How the project is laid out), rebuild-prompt.md (Ground rules: Code; Do not build)
- Tests file and view: plans/file-set.md (Tests section, steps 6 and 7)
- The question (what file-set.md is; where detail goes): plans/file-set.md "Where this goes once it is built"; .claude/agents/knowledge-base-agent.md "Where detail goes"
- Tree notes: docs/file-tree.md v1.27 ([14], [30], [10.1.2.5]); How it works: keep lines on code folders and the multi-job scripts, the rest confirmed; File Tree page v41 (data v35)
