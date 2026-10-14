# Questions: current-ui/

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-05: Why are the page files empty, and are they the page?

> why projec ide current ui html and file-tree data is empty files? current artifact ui that i se suppose to be representation of this files?

Yes. The page is these two files:

1. `file-tree-explorer.html` is the page.
2. `file-tree.data.json` is the data that the page loads.

While we plan, the build writes the working data in the planning area (`vision/explorer/`). Thus `file-tree.data.json` here is an empty placeholder until the build writes to it. This is part of the plan to leave `vision/`.

On the page, the File tab of the page shows its own source. The data file shows the data as the page loaded it. It is read-only.

Docs improved: apps/project-IDE/current-ui/current-ui.index.md.
