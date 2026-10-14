# in-20261006-1611: one file for every tab, plus metadata for every file and folder
- At: 2026-10-06T16:11:21Z · Where: thread "Interactive file tree UI" · Source: chat · Ref: thread cmsg_01Sk8xdkWKCz34CUCfVMyQbxP1hyoB8xVJjehy8MzA6ckj, message cmsg_01Sk8xdkWKCz34CUCfVMyQbxRKhLSurYPBdQ1dAHBGgrL7
- Categories: structure, docs-knowledge, ui, naming
- Summary: The owner asks why How it works files carry two .md endings and sets a new rule: every tab is a file next to its subject (vision.index.md, the file itself, vision.example.md, vision.questions.md, custom views vision.{type}.{name}.view.html, also as templates for a category), plus a metadata file with the mapping for every file and folder; asks for suggestions (maybe a changelog), to define everything and raise questions first, then do it.

## Raw input
~~~text
why for vision index file we have 2 md? vision.md.index.md. generally let's make logic like this, sow how it works every tab on a file will represent a document, so how it works it's vision.index.md, file it's a file by it self the always exist, next one could be could not, example ll be vision.example.md and questions ll be vision.questions.md, also custom views for folder or for files or specific folders or files in category like a template so for example like vision.{type}.{optional for unique views name}.view.html, also i guess we need mapping also make as file metdata for ever file folder, i don't know what else we need as metadata for files, maybe change log, suggest me, let's fist difine all information we need do like this if needs any another files or you still have question and then do
~~~

## Answer
~~~text
The two endings came from keeping the whole file name, so that `run.js` and `run.py` could never share one How it works file. There's no such pair in the tree, so it becomes `vision.index.md`.

The full set is in file-set.md. It follows your naming and adds a Details file with the mapping, a Changes file, and a format file for configs. It also says how view templates work.
~~~

Card (16:2x): "Apply this file set to every file and folder in the tree?" Go as written (recommended) / Rename first / Change it first. Waiting for the owner.

## Processed into
- in progress: vision/plans/file-set.md (definition, proposed)
