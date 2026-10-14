# Questions: file-tree.md

## Open questions for the owner

None open.

## The owner's questions

### 2026-09-29: Why the file tree was not in the docs list

> why you not added  a file tree file in a list of docs?

The first layout put the file tree under `agents/docs`, so it was moved into the top-level docs. Today `docs/file-tree.md` is one of the project docs: a plain list of every path in the repository, one per line, written by the IDE build every round and never by hand. This changed later: the old annotated tree with its notes became the tree notes in the planning area, `vision/docs/file-tree.md`, and `docs/file-tree.md` became the plain list.

### 2026-10-12: Are all planned items real files now?

> i mean all what was planned should be already real files,  what i saw before on a file tree should be already real file tree, is it right now?

Yes. There is no separate plan of files: the tree on the page is exactly the files on disk, and a file with nothing written in it yet is an empty file, marked "empty" on the page. To add a file or folder, an agent creates it. This changed later: the same day a build step made every planned item a real file; the next day all logic about planned items was removed, and the build creates nothing from a plan.
