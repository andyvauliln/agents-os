# Questions: rebuild-prompt.md

## Open questions for the owner

- **Does a rebuild start from the existing page file, or must the prompt alone write the page from nothing?** The page has approximately 230 KB of code. This prompt gives its behaviour, not its source. Today the prompt tells the rebuild to start from the existing page file when it exists. The answer decides how long and how exact this prompt must be.
- **When the sources move, can we change `repo` to `../../..` and set the final paths?** The copy of `server.config.json` in `apps/project-IDE/server/` still points to `vision/`. It sets `repo` to `../..`, which from there is `apps/`. If you start the server from there today, it looks in the wrong folder.

## The owner's questions

None recorded yet.
