# in-20261006-2143: tests for agents; a plan for every change; features; docs at every level; a general system
- At: 2026-10-06T21:43:51Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbxHhVysVp7TgBHtkR5Zsb51Q
- Categories: process, structure, vision
- Summary: The owner asks where agent and subagent tests live and how they are named; sets a rule that every change request gets a stored plan, with its logic distributed after the build, and planning as the main development skill; asks for features as their own knowledge files mapped both ways to files, small features inside bigger ones; wants the vision, README and rebuild prompt as a hierarchy across levels with updates climbing to the top; and says the system is no longer a trading OS: the top level is general and agents can be any kind (trading, social media, management), each kind with its own levels and a parent.

## Raw input
~~~text
and where do we store tests for agents and subagent and how we name them?,  ok let's right now maybe even the rule that for every change request we should make plans and store them somewhere after plan is build we should deicde what kind of logic from there we need to put where, let's add this to the plan, plan also should be a skill that we need define support and develope as main things in development, after we build plan and update related files with a knowledges and if we continue build and make changes after that we need update logic and knowledg in a related files. and yes i think some feature need have separate file for the knowledgs i think we can split them in a features and have map there to related files and to which files it relates also shoul have this mapping, we can make additional folder in a doc for agents, or the whole system for that, so the small features should relates to bigger one and we should include them in bigger, and maping the features should have scope of the logic that hard to put in overview like knoledges, view, README, reverse promt etc , also i think vision readme and reverse prompt should have hierarchy so one comes from anothers and it should have all the domain or strategy agents and system in general,  and if last has updates we can consider all documents to the top, also i want to mention that , also i think it's a big chages but, now it shouldn't be called trading oss and all logic top level any how know about trading i mean system or general knoledge, now all agents it's could be absolutly different things, trading, social media, managment etc... and every can have same and different parts of the system, that can be also have different lavlels dows but still can have parent in case of trading category of domains it's strategy and running agent but iya some of the agent can have different things
~~~

## Answer
~~~text
Tests for an agent, a helper or a skill live in the tests/agents/ folder of the level that holds them, one file per test, named by number: t-agents-001.test.md. A number says nothing about what is tested, so I propose naming each test after what it tests and checks, like pm-self-improvement-agent.never-touches-live.test.md.

The planning rule is in force now. The change-plan skill is drafted, the system's instructions tell every AI to plan each change before building it, and your message is the first plan written with it. The vision, the README and the rebuild prompt say so too.

Features, docs at every level and the general system are planned in the same file and wait for you. Until you name the system, the docs say "the system"; the vision already says the docs are being rewritten for agents of any kind. The File Tree page shows the new skill and the plans folder.

One choice is on the card below. Tell me the system's name whenever you have one.
~~~

## Processed into
- D-051 to D-054; `.claude/skills/change-plan/SKILL.md` (new); `plans/2026-10-06-2143-general-system.md` (new); `plans/index.json` (new); `.claude/CLAUDE.md` (every round: plan every change); conventions v0.2 (tests line); file-tree v1.28 ([10.1.2.8], [53.2.5]); vision (principle on plans and docs, next step 1), README (knowledge base: plans), rebuild prompt (tree, skills, CLAUDE.md); How it works of the top folder, CLAUDE.md, the skills, the plans folder, the docs and the tests file; page v42 (data v36). Features (D-052), the docs hierarchy (D-053) and the general system (D-054) are planned and wait for the owner.
