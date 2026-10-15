# in-20260929-2025: Standard .claude folder at every level
- At: 2026-09-29T20:25:19Z · Where: project chat · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbx8vtPrNyddH36FMwtrnu2Hm
- Categories: structure, agents
- Summary: The owner asked to fill every .claude folder with the full standard Claude Code layout, keep CLAUDE.md inside .claude, and leave concrete logic such as specific skills for later.

## Raw input
~~~text
populate .claude folder with a current full strutcture ── .claude/
    ├── CLAUDE.md              # alternative location for project instructions
    ├── settings.json          # permissions, hooks, env, model, statusLine, outputStyle (committed)
    ├── settings.local.json    # personal overrides (gitignored)
    ├── rules/                 # topic-scoped instructions
    │   ├── testing.md         #   `paths:` frontmatter = loads only when matching files are read
    │   └── frontend/react.md  #   subfolders work too
    ├── skills/                # reusable prompts, invoked via /name or auto-invoked
    │   └── security-review/
    │       ├── SKILL.md       #   entrypoint (frontmatter + instructions)
    │       └── checklist.md   #   any supporting files, scripts, templates
    ├── commands/              # single-file prompts, /name (same mechanism as skills)
    │   └── fix-issue.md
    ├── agents/                # subagents with their own context window and tools
    │   └── code-reviewer.md
    ├── workflows/             # dynamic workflow scripts (*.js), each becomes a /<name> command
    ├── output-styles/         # project-shared output styles (*.md)
    ├── agent-memory/          # persistent memory for subagents with `memory: project`
    │   └── <agent-name>/MEMORY.md
    └── agent-memory-local/    # same, but for `memory: local` (keep out of git). and let's keep CLAUDE.md inside this folder not in a root. don't include concreate logic related things like  security-review/, we ll fill it later
~~~

## Processed into
- D-024; vision.md v0.15; file-tree.md v1.8 ([2.7.2], [10.1.5]-[10.1.13], [19.1.5]-[19.1.13], [21.1.5]-[21.1.13], [24.5]-[24.13]; [37] moved into .claude); feature-map.md v1.6
