# in-20261012-metadisk: Is file metadata in the disk tree?
- At: 2026-10-12 · Where: thread "Interactive file tree UI" · Source: chat
- Categories: structure, ui
- Summary: The owner asked whether each file's metadata files are in the real tree on disk.

## Raw input
~~~text
is file metatdata in a disk tree or what?
~~~

## Answer
~~~text
It was not: every How it works (.index.md) and Details (.meta.json) file lived only in the mirror folder vision/tree/agent-os/. Now the build copies each one next to its item (inside a folder, beside a file), 784 files, so the disk tree is the same as the page with the metadata switch on. The copy in vision/ stays the source while we plan; the owner's server writes a How it works edit into both. Checked: page and git list the same 2,719 paths, plus the two local-only .env files.
~~~

## Processed into
- tools/materialize.py; server/server.py; changelog
