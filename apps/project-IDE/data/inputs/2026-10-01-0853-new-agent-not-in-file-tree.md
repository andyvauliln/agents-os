# in-20261001-0853: Why the new agent and skill were not on the File Tree page
- At: 2026-10-01T08:53:27Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxR5HmtfdWKwkFSMsQCbgNU3
- Categories: question, ui
- Summary: The owner asked why the new knowledge base agent and vision skill did not show on their File Tree page; the page was rebuilt so they do.

## Raw input
~~~text
why i don't see them in mine file tree
~~~

## Answer
The page shows the planned repo tree, built from file-tree.md, and that still had the old agent name and no vision skill, because the file tree was planned for the last round. Fixed now: under agents/system/.claude/, agents/ shows knowledge-base-agent.md and skills/ shows vision-doc/SKILL.md, and the File tab of each (and of the two older skills) shows the real text from the project folder. The docs/ folder inside .claude/ is added at the file tree step, when the docs exist.

## Processed into
- file-tree.md: [10.1.1.2] renamed to knowledge-base-agent.md; [10.1.2.3] vision-doc/SKILL.md added.
- tools/enrich.py: CLAUDE_DRAFTS shows the real .claude drafts on the page; data v12; page v17.
- Plain summaries for the agent, the skills, .claude/agents, .claude/skills, .claude and docs.
