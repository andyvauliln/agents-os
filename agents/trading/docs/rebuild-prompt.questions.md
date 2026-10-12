# rebuild-prompt.md: open questions

- **Should the research studies be rebuilt by re-running their pipeline, or only restored from git?** Today the prompt restores them as they are, because a re-run would not give the same text.
- **When the prediction-market domain is written again in stage two, does its rebuild prompt take over its empty folders, or does this prompt keep creating them?** Today this prompt creates them, and the domain's prompt is listed for stage two.
- **Does the rebuild need the How it works and Details files written next to every item on disk, or only in the planning mirror `vision/tree/agent-os/`?** Today the mirror is the source while we plan and the build copies them next to each item.
