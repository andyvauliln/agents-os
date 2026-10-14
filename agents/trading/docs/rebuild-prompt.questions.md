# Questions: rebuild-prompt.md

## Open questions for the owner

- **Do we rebuild the research studies with their pipeline, or only restore them from git?** Today the prompt restores them as they are. A new run of the pipeline does not give the same text.
- **In stage two, does the rebuild prompt of the prediction-market domain make its empty folders?** The alternative is that this prompt continues to make them. Today this prompt makes them. The prompt of the domain is planned for stage two.
- **Does the rebuild write the How it works and Details files next to each item on disk?** The alternative is only in the planning mirror `vision/tree/agent-os/`. Today the mirror is the source while we plan. The build copies the files next to each item.

## The owner's questions

### 2026-10-07: Why did the agents have no rebuild prompt?

> why agents didn't got a rebuild-prompt?

At the time of the first rebuild prompt, the lower levels were to get their prompts after the design of their parts. Thus only the system had one.

Today the docs folder of each level has a rebuild prompt:

1. The project.
2. The system.
3. Trading.
4. The apps.
5. The project IDE.

The prediction-market domain and its agents get their prompts in stage two.

Docs improved: none, the answer was already in docs/README.md (every level's docs folder holds the same four docs).
