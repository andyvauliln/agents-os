---
about: agent-os/apps/docs/
basis: b1db8f6523a0
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T19:42:37Z
---
# docs/

## What it is

The docs for all apps together: why the system has apps (`vision.md`), every app exactly with the path to its own docs and the list of apps (`README.md`), the same README in ASD-STE100 (`README.asd.md`), and how an AI builds `apps/` again (`rebuild-prompt.md`). Each doc also has its How it works, Details, Example and Questions files.

## Who looks after it

The knowledge base agent, with the `vision-doc`, `readme-doc` and `rebuild-prompt-doc` skills and the `file-index` skill for the metadata. The owner can change any of them on the File Tree page.

## When and how it changes

When an app is added, changed, updated from its source or removed, or when the rules for outside code change. The docs are rewritten in order: vision, README, README in ASD-STE100, rebuild prompt, then their metadata.

## Who uses it, and when

The owner and anyone new, to see what apps exist and why; every agent before working in `apps/`; an AI rebuilding the repository, through the rebuild prompt.

## Where it is mentioned

The project and system docs point here for apps; the system rebuild prompt calls the apps rebuild prompt; `docs/file-tree.md` lists the folder.

## Related knowledge

It sits between the project docs above and each app's own docs below, such as the project IDE's in `apps/project-IDE/docs/`. It sums up the apps and leaves each app's detail to its own docs.

## Keep in mind

- When you change one of the four docs, bring the others in line in the order vision, README, README.asd.md, rebuild prompt.
- When you write here, sum up an app in a few lines and point to its own docs.
