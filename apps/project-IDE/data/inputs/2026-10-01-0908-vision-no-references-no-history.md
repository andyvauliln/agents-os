# in-20261001-0908: No references and no "the owner said" in the docs
- At: 2026-10-01T09:08:00Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxEjaAJK7EcZuJvDhGcMKnKa
- Categories: docs-knowledge
- Summary: Looking at the first-version vision, the owner said the docs must have no references to other docs or sections; include a summary, or the concrete details if needed, right there. And no attribution or history such as "the owner later said": just the facts as they are now.

## Raw input
~~~text
about vision "i
- The owner later said workers are just scripts, described in config (D-007). How that is built now: architecture.md `arch-jobs`." i down want any referencess there, you can link something down the file you should just include summary or if need concreate things there. Also i don't need this types of The owner later said and something like this just fact on this moments without ataching to how say what and when
~~~

## Processed into
- `.claude/agents/knowledge-base-agent.md`, "How every doc is written": new rules "No references" (no pointers to other docs; summarise or give the concrete detail here) and "Facts as they are now" (no who said what, when or what it was before); the owner named only as the user of the system; lower levels sum up what they share instead of pointing up.
- `.claude/skills/vision-doc/SKILL.md`: no pointer to the Architecture doc, principles are the system's rules, facts stated as of today, a second too-technical example, a new check.
- First people doc written with these rules: `.claude/docs/vision.md`; sources in `.claude/knowledge/sources/vision.md`.
