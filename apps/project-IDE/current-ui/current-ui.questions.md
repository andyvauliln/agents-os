# Questions: current-ui/

## Open questions for the owner

None open.

## The owner's questions

### 2026-10-05: Why the page files look empty, and are they the page?

> why projec ide current ui html and file-tree data is empty files? current artifact ui that i se suppose to be representation of this files?

Yes, the page is these two files: `file-tree-explorer.html`, the page itself, and `file-tree.data.json`, the data it loads. While we plan, the build writes the working data in the planning area (`vision/explorer/`), so `file-tree.data.json` here is still an empty placeholder until the build writes there; that is part of the plan to leave `vision/`. On the page, the File tab of the page shows its own source, and the data file shows itself as the page loaded it, read only.
