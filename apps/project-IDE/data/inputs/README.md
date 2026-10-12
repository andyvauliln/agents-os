# Owner inputs archive
Every owner input (project chat, a thread, or an edit on the File Tree page) is stored here word for word, one file per input, before the knowledge agent extracts its knowledge (see ../README.md). The raw text is never edited, not even typos; corrections go in the summary or "Processed into".

- Files: `YYYY-MM-DD-HHMM-<topic-slug>.md` (UTC, slug of 2-4 words; id `in-YYYYMMDD-HHMM`, `-2` when two share a minute). Each has a header (time, where, source, ref, categories, summary), `## Raw input` in a `~~~text` fence, and `## Processed into` (D-0xx ids, docs with versions, [n] objects, or "answered in chat").
- **Questions and answers are knowledge too** (owner, in-20260930-1841): when the owner asks and Claude answers, the answer is stored in the same file under `## Answer` (word for word, or the page's answer record) and its knowledge is filed like any other input. `index.json` marks these rows `answered: true`.
- `index.json` is the list the knowledge map reads (`tools/build_map.py`): one row per input, in time order, with `file`, `categories`, `summary` and `processed_into`. No knowledge tags in this folder; docs cite input ids in `sources`.

Categories (1-3 per input):
- `setup`: project, repo and tool setup.
- `vision`: goals and the owner's picture of the system.
- `structure`: folders, files and where things live.
- `agents`: agent levels, sub-agents, roles and behaviour.
- `configs`: config files, their sections and fields.
- `links`: symlinks, `.link` rules, links files, relink.
- `workers-jobs`: workers, jobs, schedules, the scheduler.
- `docs-knowledge`: docs, the knowledge base, maps and summaries.
- `secrets-safety`: secrets, `.env`, `.gitignore`, safety rules.
- `tests-research`: tests, runners and research folders.
- `naming`: names and IDs of agents, files and folders.
- `ui`: the File Tree page and the trading UI.
- `process`: how we work: syncs, updates, ripples, flows.
- `question`: the owner asked something; the answer is stored under `## Answer` and filed as knowledge.
