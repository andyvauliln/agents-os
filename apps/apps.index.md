---
about: agent-os/apps/
node: n-43
basis: 1e4e4b27d5d4
written: 2026-10-07T14:21:32Z
by: knowledge-base-agent
---
# apps/

## Summary

Applications and projects: our own apps, the outside apps we use and repositories cloned only to study them. Today it holds the owner's project IDE in `project-IDE/` (the File Tree page, its server and this project's knowledge) and the prediction-market domain's trading dashboard in `trading-ui/`, empty for now, and `temp/` for research clones. Every app has its own `docs/` with a vision, a README and a rebuild prompt, like the system; for an outside app these three docs are all its metadata for now. An outside app we use is forked on GitHub and gets its own folder with `docs/` and `repo/`, the fork: its `main` branch holds our changes and is what runs, and its `upstream` branch follows the source and is merged into `main` from time to time. None is brought in yet, and every app has a row in the apps list. Later, when the owner asks, a skill will turn an app fully into the system's way. Still open: whether agents may clone on their own, whether the earlier Polymarket tools come in as a forked app, and how the fork sits in the repository.

## Keep in mind

- When you clone a repository only to study it, put it in `temp/`; never commit the clone.
- When we start using an outside app, fork it first and change only our `main` branch; never change `upstream`.
- When an app is added, updated from its source or removed, update its docs and its row in the apps list in the same change.
