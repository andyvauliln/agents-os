# in-20261006-2047: what the IDE and the docs are for: full context for the owner and for every AI
- At: 2026-10-06T20:47:52Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbxY95s5dpj1RfT4cCAkKA38i
- Categories: docs-knowledge, process, vision
- Summary: The owner states the purpose of the custom IDE and file tree: to manage, analyse and view the system easily, and for AI to always have all related context to make changes precisely; docs perfect for developers and AI; on any change the AI knows which related files, agents, skills, docs, indexes and logic to update and how; a file deep in the hierarchy gets the top-level knowledge that applies to it; new knowledge from sessions and inputs is distributed well; every owner question finds its place in the docs with an explanation of how that exact thing works.

## Raw input
~~~text
make notes of where if need for this mine input. So the idea of all of this thing related to custome ide and file treee, that i can easly mange, analayse, view the system with and this interface, and ai always know all related and needed context to more precisely make all changes, so all documentation should be perfect for developer and the ai, and ai knows everything about the system make decisions base on that, he knows if changed one file when he analysing changes what related files, agents, skills, docs, indexes, and logic he should update and how, also if he dealing with some file dow to hierahy for example some subagent skill, he should know top level knowledges that applies to the skill, all system should very good destribute new knowledges from the sesssion and mine inputs, every mine question should have find place in documentation with explanation how this exact things works
~~~

## Answer
~~~text
Filed. The purpose is now written where every AI reads it: the vision, the README, the rebuild prompt, both helper agents, the intake skill and the system's CLAUDE.md. The rules it adds:

- Before changing a file, an AI reads its whole context, including what applies from the levels above.
- After a change, everything related (files, agents, skills, docs, lists) is brought in line in the same round.
- What a session learns is filed even when no file changed.
- Every question you ask gets its answer written into the docs where you should have found it.

The file-set plan now has two more Details fields: what must change with the file and how, and what it inherits from above. The File Tree page is version 39. The card on the file set is still waiting for your pick.
~~~

## Processed into
- D-049 (decisions.md v1.6, changelog.md 2026-10-06)
- Docs: .claude/docs/vision.md (What the owner sees and does; principle "Every AI works with the whole picture"), README.md (The knowledge base and the docs; The project IDE), rebuild-prompt.md (part 17 "Whole context for every change"; the agent body; Do not build: the file set); sources in .claude/knowledge/sources/
- Agents and rules: .claude/agents/knowledge-base-agent.md (job, when it runs, step 2, a question gets a home), .claude/agents/project-ide-agent.md (job), .claude/skills/knowledge-intake/SKILL.md (scope, every question gets a home, ripple step 5), .claude/CLAUDE.md (what the project is for, --context before a change, rules)
- Plan: plans/file-set.md (What it is for; Details fields update_with and inherits)
- Tree notes: docs/file-tree.md v1.26 ([10.1.1.2], [10.1.2.1], [10.1.5], [53])
- How it works: n-0, n-53, n-10.1.5, n-10.1.2.1, n-10.1.1.2, n-10.1.1.3 rewritten; parents confirmed; File Tree page v39 (data v33)
- Memory: full-context-for-ai (new), file-family-plan, file-tree-explorer-sync, MEMORY.md
