# Questions: file-tree-explorer.html

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-01: Why the new agent and skill were not in the tree

> why i don't see them in mine file tree

At that time the page showed a planned tree built from the tree notes, which still had the old agent name and no vision skill. Today the tree is exactly the files on disk, so `agents/system/.claude/agents/knowledge-base-agent.md` and `agents/system/.claude/skills/vision-doc/SKILL.md` show like every other file, with their real text on the File tab.

### 2026-10-05: Why the .index.md files are not in the tree

> i still can't see .index.md files in a the tree files, why?

They were shown only inside the How it works tab, never as rows. Today the "metadata" switch, on by default, shows each file's How it works file and Details file as rows right under it, and each folder's own first inside it; a click on one opens that tab.

### 2026-10-06: Why files show in a search but not in the tree

> when i do search file tree i can see vision.md and another vision skill, why i don't see them in a file tree without search

They are in the tree, inside folders that start closed, and a search opens every folder on the way to a match. A first click on a closed folder now opens it and selects it; a second click, or its arrow, closes it. This changed later: `vision.md` moved from `agents/system/.claude/docs/` to `agents/system/docs/`.

### 2026-10-09: Why vision/ is not in the tree

> why i can't see it in a file tree how i said we always should have real represention of file tree on a disk and on ui

The planning folder `vision/` was left out on purpose at first. Now the page shows every file git keeps, `vision/` included, and lists the two `.env` files as local-only without their text; the build checks that the page tree equals the files in git.

### 2026-10-09: Why real metadata files stay when the metadata switch is off

> why files like .claude.meta.json not hidden when checkbox metadata off

The switch first covered only the metadata rows the page added for each item, and the real metadata files found on disk came in as ordinary files. Now every metadata file follows the switch, and with the switch on each one shows once.

### 2026-10-12: Why the tree after a pull differs from the page

> fuck man why i just pull last version and i don't have same file tree as i have on current ide

The page also showed about 400 planned items that were not on disk yet. Today the page tree is exactly the files in git, plus the two local-only `.env` files, and every build checks this, so a pulled repository and the page show the same tree once the page is rebuilt. This changed later: the planned items were first hidden behind a switch, then made real files, and then all logic about planned items was removed.
