# Questions: file-tree.md

## Open questions for the owner

None open.

## The owner's questions

### 2026-09-29: Why was the file tree not in the list of docs?

> why you not added  a file tree file in a list of docs?

The first layout put the file tree in `agents/docs`. Thus the agent moved it into the top-level docs.

Today `docs/file-tree.md` is one of the project docs. It is a plain list of all paths in the repository, one path on each line. The IDE build writes it each round. Nobody writes it by hand.

This changed later: the old tree with its notes became the tree notes in the planning area, `vision/docs/file-tree.md`. `docs/file-tree.md` became the plain list.

Docs improved: none, the answer was already in docs/file-tree.index.md.

### 2026-10-12: Are all planned items real files now?

> i mean all what was planned should be already real files,  what i saw before on a file tree should be already real file tree, is it right now?

Yes. There is no separate plan of files. The tree on the page is exactly the files on disk. A file that has no text yet is an empty file. The page marks it "empty". To add a file or a folder, an agent makes it.

This changed later: on the same day, a build step made each planned item a real file. On the next day, all logic about planned items was removed. The build makes nothing from a plan.

Docs improved: apps/project-IDE/current-ui/file-tree-explorer.index.md.
