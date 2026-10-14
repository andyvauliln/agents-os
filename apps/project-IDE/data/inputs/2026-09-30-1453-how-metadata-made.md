# in-20260930-1453: How is file and folder metadata made?
- At: 2026-09-30T14:53:01Z · Where: thread: Interactive file tree UI · Source: chat · Ref: cmsg_01Sk8xdkWKCz34CUCfVMyQbxGgpp5sfZPYtrwjvRTHDF2o
- Categories: question, docs-knowledge, process
- Summary: The owner asked how metadata for files and folders is currently produced from their inputs.

## Raw input
~~~text
describe how we currently make metadata to the files and folders after mine inputs
~~~

## Answer (given in chat)
~~~text
Right now each file's details go through three steps.

1. **Your input becomes text in file-tree.md.** I give the item a number [n] and a one-line comment in the tree. It also gets a section with Purpose, details, Writers / readers, when it is updated and open questions. Your decisions go into the decision log as D-0xx, and my own ideas are marked "proposed". Then I bring vision.md and feature-map.md in line.
2. **A build turns that text into the page's data.** It reads the tree and the sections, then adds:
   - **Status:** decided if the item cites your request or a D-number, proposed if marked so, planned otherwise; `[name]` items become placeholders, and the example agent's items become examples.
   - **Shared rules:** matched by keywords.
   - **Notes, rules and examples:** set per file type.
   - **Field guides and editable tables:** Jobs, Links, Capabilities and Variables.
   - **Exists:** set for anything already in the repo.
3. **Your edits on the page save straight away** to the page's own database, one record per item. Claude then fixes related items and writes the "How it works" text. These edits reach file-tree.md only when you say "sync the file tree".

The weak spot is the field guides, examples and table rows. I write them by hand in the build scripts, not in file-tree.md, so they can fall out of step with the doc. I can move them into file-tree.md so it holds everything.
~~~

## Processed into
- answered in chat
