# in-20261006-2206: apps have their own docs; research clones in a temp folder; apps we use are forked
- At: 2026-10-06T22:06:57Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbxX561U7ADZ5yN8gboBWnsnh
- Categories: structure, docs-knowledge, process
- Summary: Every app in apps/ has its own docs. A repo cloned from GitHub for research goes to a temp folder first, and on request it can get docs (vision, README, rebuild prompt). An app we use is forked, with our own main branch; from time to time updates from the source are merged in and then into our main. For now an app's metadata is only these three docs; later, on request, a skill (which must be kept up like any other) turns an app fully into the system's way: metadata for every file, one job per file, the other docs.

## Raw input
~~~text
also related input apps folder also will contains apps and inside them docs, when we cloned a repo to the app from the github from another project first just clone in a temp if it's for research but still also we can  add under request for it in docs folder related files vision our README and reverse prompt if it's not cloned for research purpose we can store such project then in a temp folder the apps we use should be forked and made new main branch where we ll once in a time merge udpate from the source and then merge them in our main fork. so the app metadata for now only nessasary for this 3 files, we supposely should have some skill that will completly turn the app in a same way like current system has for example add all metadata to files, split to individual files and another docs etc, but for now let's just do this 3 files and under request later a skill that can handle it but this skill we need support as well
~~~

## Answer
~~~text
Done for the rules. Every app now has its own docs folder with a vision, a README and a rebuild prompt, and for an outside app those three are all its metadata for now. A research clone goes to apps/temp/<name>/, is never committed, and gets docs only when you ask. An app we use is forked: our changes go on its main branch, and an upstream branch follows the source and is merged into main from time to time. The skill that turns an app fully into the system's way waits for your request.

I read your message as research clones in temp and the apps we use as forks; tell me if I got that wrong.

The project IDE's own three docs are in the tree, and I'll write them with the docs at every level so they are written once. The other defaults (the fork as a submodule, forks in your GitHub account, updates when we ask) are in the plan.
~~~

## Processed into
- D-055; `plans/2026-10-06-2206-apps-docs-clones-forks.md` (new) and its row in `plans/index.json`; conventions v0.3 (Apps and outside code); architecture ([43] row and line); file-tree v1.29 ([43], [53], new [53.4] to [53.4.3], new [55], [48], [2.18.5]); the vision, README and rebuild prompt skills (an app's outline and length); README (layout, apps paragraph, open question); rebuild prompt (tree, .gitignore, Apps and outside code, part 18, do not build); How it works of apps/, the IDE and its docs, apps/temp/, .gitignore, the apps list, the top folder and the index folder; page v43 (data v37).
