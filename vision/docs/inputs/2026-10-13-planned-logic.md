# Input 2026-10-13: what logic we have around planned and not planned files

- From: the owner, in the thread "Interactive file tree UI"
- Date: 2026-10-13

## Words
~~~text
what logic we currently have around planed not planed files, don't watch vision folder, check all another
~~~

## Answer
~~~text
Planned = an item in the tree block of vision/docs/file-tree.md (259 outside vision/: 170 folders, 89 files). Every one is on disk (materialize.py): 33 files carry their draft text, 20 are empty, the rest are the docs and configs written in place. Found = on disk and in git but not in the plan: 206 trading research studies, HANDOFF.md, the two .env.example files, and 24 folders that the plan names only inside a longer name (skills/vision-doc/SKILL.md makes vision-doc/ a found folder). Found items get empty metadata files and no How it works of their own. The "planned" switch hides nothing now, since every planned item is on disk.
Fixed: 30 items were listed twice on the page (planned "vision-doc/SKILL.md" plus the found SKILL.md inside the found folder). enrich.py now moves such a planned item into the found folder under its own name (_adopt). Page v65, data v60.
Proposed: add the found items to the plan (the 24 folders as their own lines, the research folder, HANDOFF.md, .env.example) and drop the "planned" switch.
~~~

## Processed into
- vision/tools/enrich.py (_adopt)
