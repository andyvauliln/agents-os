# Apps: vision

## In short

Apps are the programs that sit next to the agents of the Agent OS and help people and agents work with it. Some are our own, such as the owner's project IDE, the interactive map of the whole project. Others come from outside: code someone else wrote, which we either study for a while or adopt and keep as our own copy. Every app, whatever its origin, explains itself in the same way as the rest of the system, so the owner and every AI can see what it is for, how it is built and how to build it again.

## What apps are for, and who uses them

Apps are the tools around the agents' work: screens where the owner watches and steers the project, and outside programs the project relies on.

- **The owner** uses apps to see the project, change it and approve what only they can approve.
- **Every AI** that works on the project uses the same apps to find the context it needs before it changes anything.
- **Agents** may later use outside apps as tools.

## Why the system has apps

Outside code reaches a project in two very different ways, and each needs a clear home. Without a rule, copies of other people's code pile up in the project, changes we make to someone else's program are lost the next time it is updated, and no AI knows what a program is for.

So the system knows three kinds of app:

1. **Our own apps.** Programs we write for the project. The first is the project IDE: the owner's window on the whole project, and the place where every AI gets the full context of any file. A second, a dashboard for the prediction-market domain, is planned but empty, and may never be needed if the IDE does its job.
2. **Research copies.** When we want to learn from a program someone else published, we copy it into a temporary place, study it and then delete it. What we learn is kept by the agent that studied it; the copy itself is never kept in the project.
3. **Apps we use.** When we decide to rely on someone else's program, we make our own copy of it on GitHub, called a fork. Our changes go only into our own main line of that copy, which is what we run. A second line follows the original author's work and is never changed by us. From time to time the original author's updates come into that second line and are then merged into ours, so we stay up to date without losing our own changes.

## How apps should work for us

- **Every app explains itself.** Each one has its own vision, README and rebuild prompt, written like the system's own docs, and a README in Simplified Technical English next to the README so the two can be compared. For an app from outside, these docs are all the explanation it gets for now: we do not describe someone else's code file by file.
- **Research copies stay out of the project.** They are never saved with it, and they get their own docs only when the owner asks.
- **Apps we use stay ours and current.** We change only our own line of the fork, we take in the original author's updates on purpose, test the app after each update and note the update in its docs.
- **Every app is listed** with what kind it is, where it comes from, which version we use and who uses it.
- **Apps follow the system's safety rules.** An app never holds or shows a key's value, and nothing an app does can touch real money or act live without the owner's approval.

## The apps today

- **The project IDE** is our own and the most important app. It shows the whole project as a clickable tree where every file and folder explains itself, lets the owner edit, comment, ask questions and delete items, and carries those changes back into the files. It runs as a published page and on the owner's server, with Claude Code behind its request box.
- **The prediction-market dashboard** is a place kept for that domain's own screen, where the owner would watch its trading agents and approve their live actions. It is empty, belongs to the second stage of the project, and may never be built.
- **Research copies:** none yet. **Apps we use from outside:** none yet.

## Where we stand and what comes next

The rules for apps are decided, and the project IDE is built and in daily use. The project is in its first stage: finishing the IDE, making every file's explanations and details correct, writing custom views for the different kinds of files, and finishing the docs at the project, system, trading and apps levels. Next, the first outside program the project relies on comes in as a fork; earlier tools for working with Polymarket are the likely first. Later, when the owner asks, a helper skill will turn an app fully into the system's way, with an explanation and details for every one of its files.

## Ideas we are still weighing

- **Keeping the fork as a linked copy.** Problem: the project must record exactly which version of an outside app it uses. The idea: keep the fork inside the project as a linked copy pinned to one version, which makes the version visible and reproducible.
- **Updating outside apps on a schedule.** Problem: updates from the original author are easy to forget. The idea: a job that checks for new versions and tells the owner. For now updates happen only when we ask.
- **Adopting an app fully.** Problem: an outside app explains itself only through three docs. The idea: a helper skill that gives it the full treatment every part of the system gets. It is written only on the owner's request.

## Open questions

- May agents copy an outside program for research on their own, or only when the owner asks? It decides how freely agents can learn from other people's work.
- Do the earlier Polymarket tools come in as an app we use? It decides the first fork and the prediction-market domain's tools.
- Where do our forks live on GitHub: in the owner's own account or in an organization? It decides who owns and can change them.
- Is the prediction-market dashboard needed at all, or does the project IDE take its place? It decides whether a second app of our own is ever built.

## Going deeper

The README describes every app exactly: where each one lives, how the apps folder is laid out, how outside apps are copied, forked and updated, and where each app's own docs are. It is at `apps/docs/README.md`.
