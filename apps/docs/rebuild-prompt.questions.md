# Questions: rebuild-prompt.md

## Open questions for the owner

- The project IDE's own rebuild prompt is not written yet, so this prompt falls back to the system rebuild prompt's IDE parts. Is that fallback right until the IDE's prompt exists? It decides how the IDE is rebuilt meanwhile.
- Should this prompt add the `apps/temp/*/repo/` line to `.gitignore` itself, or should the system rebuild prompt, which owns `.gitignore`, do it? It decides which prompt owns the ignore rule.

## The owner's questions

None recorded yet.
