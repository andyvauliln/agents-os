# rebuild-prompt.md: open questions for the owner

- The page is about 230 KB of code; this prompt gives its behaviour, not its source. Should a rebuild start from the existing page file when it exists (as the prompt says now), or must the prompt alone be enough to write the page from nothing? It decides how long and how exact this prompt must be.
- The copy of `server.config.json` in `apps/project-IDE/server/` still points at `vision/` and resolves `repo` as `../..`, which from there is `apps/`. May we fix it to `../../..` and the final paths when the sources move? Started from there today, the server would look in the wrong folder.
