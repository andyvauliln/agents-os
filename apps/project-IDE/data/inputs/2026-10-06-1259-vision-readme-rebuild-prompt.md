# in-20261006-1259: what the vision and the README are for, and a third doc: an AI prompt to rebuild the system
- At: 2026-10-06T12:59:00Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbx4gfQS4yFAqPD4oZRycWDQ2
- Categories: docs-knowledge, vision
- Summary: After choosing "Sharpen both", the owner sets each doc's job: the vision is the top-level doc (concept, ideas, examples, business logic, what we build and how it should work); the README is the full, exact overview of every main part of the system, with no logic inside the agents and with the path to each part's own README; and a new third doc is a prompt from which AI can rebuild the same working system, with its own skill.

## Raw input
~~~text
yes README suppose to be full long docs with a overview how it works all system,  to read for deeper and exact understanding how system works good for human and for ai, it should not contain also information about any logic inside the agents, but should have just descriptional view on all main parts of the system with a provided paths to the main documentation README for specific part of the sytem, and vision yes like mostly for human but also for ai for high level view, ideas concept examples, busness logic, what we are bulding how it should works. So vision it's top level document, from where after we  go deeper to have better understanding how things works. and also let's make one more document it ll be prompt for ai, from what we can rebuild the system that at the end we have same working system. update this documents base on this, make additional skill for the 3rd document and update current if needs
~~~

## Answer
~~~text
Got it: vision on top, README as the full map of every part with paths, plus a rebuild prompt for AI. Starting with the skills.
~~~

Final reply:
~~~text
Nothing needed from you. The vision is now the top-level doc: concept, how it should work, business logic and examples. The README describes every part with the path to its own docs, and no logic inside agents. The new rebuild prompt is the full spec an AI follows to rebuild the same system, and it has its own skill; choices it made are marked as defaults you can change. The File Tree page shows all three (version 38).
~~~

## Processed into
- D-048 (decisions.md, changelog.md 2026-10-06)
- Skills: .claude/skills/vision-doc/SKILL.md and readme-doc/SKILL.md rewritten; .claude/skills/rebuild-prompt-doc/SKILL.md new [10.1.2.7]
- Docs: .claude/docs/vision.md (rewritten, ~4,000 words), README.md (rewritten, ~9,800 words), rebuild-prompt.md (new [2.22], ~15,000 words); sources in .claude/knowledge/sources/
- Agent and rules: .claude/agents/knowledge-base-agent.md (three main docs, order vision, README, rebuild prompt), .claude/CLAUDE.md (read-first order)
- Tree notes: docs/file-tree.md v1.25 ([2], [2.1], [2.2], [2.22], [10.1.2.3], [10.1.2.4], [10.1.2.7], [19.6.2], [19.6.3], [21.6.2], [21.6.3]); tools index_files.py DRAFTS and enrich.py DOC_SKILLS
- How it works files refreshed (356 fresh); File Tree page v38 (data v32)
- Memory: human-docs-style, claude-folder-docs-layout, file-tree-explorer-sync, MEMORY.md
