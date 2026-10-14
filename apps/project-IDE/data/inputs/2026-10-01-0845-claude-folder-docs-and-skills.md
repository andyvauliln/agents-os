# in-20261001-0845: A .claude folder with the agent, the docs and one skill per doc
- At: 2026-10-01T08:45:05Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbx3LRPXD4wvUxEohuSfLgUDV
- Categories: docs-knowledge, process, structure
- Summary: The owner set the new layout and order of work: a `.claude` folder with `agents/knowledge-base-agent.md` and `docs/` (README regenerated after every update with everything we know, file-tree, vision, architecture, glossary and more, plus subagents links), one skill per doc starting with vision; first the agent and the vision skill for the owner to read and check, then vision.md, then the other docs one by one with the file tree and mapping last, improving the agent and skills every round.

## Raw input
~~~text
let's do like this .claude

* agents
   * [knowledge-base-agent.md](http://knowledge-base-agent.md)

* docs
* [README.m](http://READ.me)d - All information about this project to have general overview how all of this works here, regenerated after every update (by knowledge base agent). For now should contain all information we know from all mine inputs, updates and available data to make it.
* [file-tree.md](http://file-tree.md). Another very important document on which right now working which have even ui for that, where i can attach or understand knowledges on a levels of folders and files
* [vison.md](http://vison.md) what we are building as the project what we have know and what planing in a feature, goals, main logic
* [architecture.md](http://architecture.md)
* [glossary.md](http://glossary.md)
* …
* subagents.links

1. Then we need create or update agent and give me read it and check him. Also for every file i think we need a skill and write there how to build every docs let’s start with vision[-skill.md](http://file-tree-skill.md) etc and give me read.
2. Then we update with the agent and skill [vision.md](http://vision.md)
3. Then one by one all another docs. From all available information for the all system the last one ll be file tree and maping
4. All of this iteration we updates skill and knowledge base agent that it works how we decide
~~~

## Processed into
- D-034 (layout `.claude/agents`, `.claude/docs`, `.claude/skills`, agent notes in `.claude/knowledge/` proposed; order of work).
- New: `vision/.claude/agents/knowledge-base-agent.md` (replaces sys-knowledge-agent, archived in archive/2026-10-01/), `vision/.claude/skills/vision-doc/SKILL.md`; knowledge-intake and knowledge-summarise moved to `vision/.claude/skills/`.
- Pending: owner check of the agent and the vision skill; then vision.md.
