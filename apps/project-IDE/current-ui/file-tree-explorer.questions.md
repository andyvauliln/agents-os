# Questions: file-tree-explorer.html

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-01: Why were the new agent and skill not in the tree?

> why i don't see them in mine file tree

At that time, the page showed a planned tree. The build made that tree from the tree notes. The tree notes had the old agent name and no vision skill.

Today the tree is exactly the files on disk. Thus `agents/system/.claude/agents/knowledge-base-agent.md` and `agents/system/.claude/skills/vision-doc/SKILL.md` show as all other files do. The File tab shows their real text.

Docs improved: apps/project-IDE/current-ui/file-tree-explorer.index.md.

### 2026-10-05: Why are the .index.md files not in the tree?

> i still can't see .index.md files in a the tree files, why?

At that time, the page showed them only in the How it works tab, not as rows.

Today the "metadata" switch is on by default. It shows the How it works file and the Details file of each file as rows immediately below that file. The metadata files of a folder show first, in that folder. When you click one of these rows, the page opens that tab.

Docs improved: none, the answer was already in apps/project-IDE/docs/README.md (the metadata switch).

### 2026-10-06: Why do files show in a search but not in the tree?

> when i do search file tree i can see vision.md and another vision skill, why i don't see them in a file tree without search

They are in the tree, in folders that are closed at the start. A search opens each folder on the path to a match.

Now the first click on a closed folder opens it and selects it. The second click, or a click on its arrow, closes it.

This changed later: `vision.md` moved from `agents/system/.claude/docs/` to `agents/system/docs/`.

Docs improved: none, the answer was already in apps/project-IDE/current-ui/file-tree-explorer.index.md.

### 2026-10-09: Why is vision/ not in the tree?

> why i can't see it in a file tree how i said we always should have real represention of file tree on a disk and on ui

At first, the page did not show the planning folder `vision/`. This was intentional.

Now the page shows each file that git keeps, `vision/` also. It shows the two `.env` files as local-only, without their text. The build checks that the page tree is equal to the files in git.

This changed later: on 2026-10-14 `vision/` was removed from the repository. Thus the page does not show it.

Docs improved: apps/project-IDE/current-ui/file-tree-explorer.index.md.

### 2026-10-09: Why do real metadata files stay when the metadata switch is off?

> why files like .claude.meta.json not hidden when checkbox metadata off

At first, the switch controlled only the metadata rows that the page added for each item. The real metadata files on disk showed as usual files.

Now each metadata file obeys the switch. When the switch is on, each metadata file shows one time.

Docs improved: none, the answer was already in apps/project-IDE/docs/README.md (the metadata switch).

### 2026-10-12: Why is the tree after a pull different from the page?

> fuck man why i just pull last version and i don't have same file tree as i have on current ide

The page also showed approximately 400 planned items that were not on disk yet.

Today the page tree is exactly the files in git, plus the two local-only `.env` files. Each build checks this. Thus, after the next page build, a pulled repository and the page show the same tree.

This changed later: first, a switch hid the planned items. Then the build made them real files. Then the owner had all logic about planned items removed.

Docs improved: apps/project-IDE/current-ui/file-tree-explorer.index.md.
