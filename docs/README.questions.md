# Open questions: docs/README.md

- **Should the records (inputs, decisions, changelog, tree notes, plans) move from `vision/docs/` into `apps/project-IDE/data/`?** The README describes both places; it decides which one is the source.
- **Should `docs/file-tree.md` list the metadata files too, or only the items?** Listing every `.index.md` and `.meta.json` roughly doubles the file; leaving them out makes it a cleaner map.
- **Should the logs and data of agents be ignored by git again?** The current `.gitignore` no longer has the rules that keep runtime `logs/` and `data/` and research clones in `apps/temp/` out of git, which the owner asked for earlier.
- **Is `HANDOFF.md` still needed once `agents/system/CLAUDE.md` is the entry point?** Both tell a new session where to start, and two starting points can disagree.
