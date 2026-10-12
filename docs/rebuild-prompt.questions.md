# Open questions: docs/rebuild-prompt.md

- **Should a rebuilt repository include `vision/` at all, or only the system as designed?** Today the prompt copies the planning area as the owner hands it over; once the real files are the only source, it could be left out.
- **Is the order of the lower prompts right: system, apps (then the project IDE), trading?** It follows the order in which the docs are written; the IDE's build scripts live in the system's folder, so the system must come first.
- **Should `HANDOFF.md` be rebuilt?** It is a planning-time note; the prompt copies it only when the owner hands it over.
