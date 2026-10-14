# Plan: apps with their own docs, research clones and forks

Status: building (steps 1 to 4 done; 5 to 7 wait) · Request: in-20261006-2206 · Updated: 2026-10-06

## The request

You said that every app in `apps/` has its own docs; that a repository cloned from GitHub for research goes into a temp folder first, and can still get its vision, README and rebuild prompt when asked; that an app we use is forked, with "new main branch where we ll once in a time merge udpate from the source and then merge them in our main fork"; that "the app metadata for now only nessasary for this 3 files"; and that later, on request, a skill turns an app fully into the system's way (Details for every file, one job per file, the other docs), a skill "we need support as well".

We read it as two kinds of outside code: a research clone (temp, not kept) and an app we use (forked, kept up to date). Tell us if we read it wrong.

## What it is for

Outside code comes into the project in two ways, and each needs a clear home. Without a rule, clones pile up in the repository, changes we make to someone else's code are lost at the next update, and no AI knows what an app is for. After this change, every app explains itself in the same three docs as the system, research clones never weigh on the repository, and the apps we use stay ours and up to date.

## What exists today

- `apps/` holds our own apps: the project IDE (`project-IDE/`) and the trading dashboard (`trading-ui/`, empty). A cloned repository was to get "its own folder when one is needed"; the open questions were pinned versions, whether agents may clone on their own, and whether the earlier Polymarket tools come in as a clone.
- `index/apps.md` was planned as "every cloned repo in apps/, version, used by".
- The project IDE explains itself through its How it works file and the READMEs of its server and data folders; it has no vision, README or rebuild prompt of its own.

## The change

**Every app has its own docs.** Each folder in `apps/` has a `docs/` folder with three files, written like the system's: `vision.md` (what the app is for and why), `README.md` (its parts and where they are) and `rebuild-prompt.md` (how to build it again exactly). For an app we use from GitHub, the rebuild prompt says where it comes from (the source, our fork, the branch and commit) and what we changed. For now these three files are all the knowledge an outside app gets: no How it works or Details for each of its files.

**A research clone** goes into `apps/temp/<name>/`: the clone itself in `repo/`, which is never committed, and, only when you ask, our three docs in `docs/`, which are kept. What the research finds is written, as always, in the research folder of the agent that studies it. When the research is done, the clone is deleted.

**An app we use** is forked on GitHub, and lives in `apps/<name>/`: our docs in `docs/` and our fork in `repo/`. In the fork:

- `main` is our branch: everything we change goes there, and it is what we run.
- `upstream` follows the source's main branch and is never changed by us.
- From time to time we update `upstream` from the source, merge it into `main`, run the app's tests, and note the update in the app's docs and in `index/apps.md`.

**A skill for later.** On your request, a skill (name proposed: `adopt-app`) turns an app fully into the system's way: a How it works and Details file for every file, one job per file, features and the other docs. Like every skill it is kept up and tested. It is not written now.

**The list of apps.** `index/apps.md` lists every app: its kind (ours, a fork, a research clone), the source, our fork and its branches, the commit we use, when it was last updated from the source, and who uses it.

## Choices for you

1. **Where the fork sits in our repository:** as a submodule (recommended), so our repository records exactly which commit of the fork it uses and a clone with submodules gets everything; or as a plain clone that git ignores, with the fork's address and commit only in the docs.
2. **Where forks live on GitHub:** in your own account, next to this repository (recommended), or in an organization.
3. **How often to update from the source:** when we ask (recommended for now); a job that checks for new commits in the source is proposed for later.
4. **When the project IDE gets its three docs:** with the docs at every level from the general-system plan (recommended), so they are written once inside the new hierarchy; or now, ahead of it.

The build follows the recommended defaults unless you say otherwise.

## Steps

1. ✓ Save your message and write this plan.
2. ✓ Record the rules: the decision, the conventions note, the architecture note, the tree notes for `apps/`, `apps/temp/`, the project IDE's `docs/`, the ignore file and the list of apps. Check: the File Tree page shows the new folders.
3. ✓ Give the three doc skills an outline and a length for an app. Check: each skill has an "App" line and a row in its length table.
4. ✓ Bring the system's README and rebuild prompt in line. Check: both describe the two kinds of outside code; the vision needs no change.
5. Write the project IDE's three docs, with the docs at every level (choice 4).
6. Bring the first outside app in (the earlier Polymarket tools are the likely first), following these rules. Check: its folder has `docs/` and `repo/`, and it has a row in the list of apps.
7. On your request: write the `adopt-app` skill, with its tests.

## What it touches

The decision log, the conventions, architecture and tree notes, the ignore file, the list of apps, the three doc skills, the system's README and rebuild prompt, the How it works of `apps/` and the project IDE, and the File Tree page.

## Where the knowledge goes once built

- **The rules for apps:** the conventions note (where things go); the tree notes of `apps/` and `apps/temp/`; the README's layout in short; the rebuild prompt in full.
- **The app outline:** the three doc skills.
- **The fork workflow:** the tree notes of `apps/` now; later a how-to note "add or update an app" once the first app comes in.

## Log

- 2026-10-06 22:06: request received.
- 2026-10-06 22:10: plan written; your message is the go for the rules and the three docs per app, so steps 2 to 4 are built now.
- 2026-10-06 22:17: steps 2 to 4 done: decision D-055, the conventions, architecture and tree notes (v1.29), the ignore file, the list of apps, the three doc skills, the README and the rebuild prompt; File Tree page v43. Step 5 waits for the docs at every level, step 6 for the first outside app, step 7 for your request.
