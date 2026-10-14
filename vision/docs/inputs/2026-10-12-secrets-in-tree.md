# in-20261012-secrets: Show the keys folder and its metadata; only the real .env stays out of git
- At: 2026-10-12 · Where: thread "Interactive file tree UI" · Source: chat
- Categories: security, structure, ui
- Summary: The owner wants to see .secrets and its metadata files in the tree and in git; only the real .env files are not committed.

## Raw input
~~~text
how we can make that i can see secretes and it metadata files, metadata we can commit, i think only real .env we not commit
~~~

## Answer
~~~text
Done (D-063). .gitignore no longer ignores .secrets/; every .env file stays ignored. The keys folder, test/ and live/ (each with a .gitkeep), secrets.index.json (key names only) and the How it works and Details files are in git and in the tree. The .env files show in the tree as local-only: the page never reads, shows or edits what is in them.
~~~

## Processed into
- .gitignore; tools/materialize.py; tools/enrich.py; explorer page; CLAUDE.md; inputs-vision.md SEC-02; decisions D-063; changelog
