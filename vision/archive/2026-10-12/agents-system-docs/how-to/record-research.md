# Agent OS: Record research (v0.2)

How to open, run and close a research item at any level, so results and decisions are kept and nobody repeats the work. Every level has `research/` with an `index.json` and one folder per item (D-025); the level's SI sub-agent is the main writer. Fields: see data-schemas.md. This runbook is [2.11.8] in the file tree.

## Steps
<!-- k: id=howto-record-research-steps applies=[2.11.8],path:agents/**/research/index.json,name:[research-id]-[slug],[10.9],[19.13],[21.13],[50],[2.6],[10.1.12],[19.1.12],[21.1.12] sources=D-025,in-20260929-2036,D-056 status=proposed -->
1. **Read the level's `research/index.json` first** ([10.9.1], [19.13.1], [21.13.1], [50.1]) so you do not repeat work. Research on several children of one agent usually lives at that parent's level (like [21.13]).
2. **Add an item:** `id` `r-NNNN` (unique in the level, never reused), `slug`, `topic`, `question`, `status: planned`, `requested_by`, `ran_by`, `folder`.
3. **Create its folder** `research/[research-id]-[slug]/` with a `README.md` holding the question and the method.
4. **Run it:** set `status: running` and `started`; keep every artifact (datasets, charts, run outputs, notes) in the item's folder.
5. **Close it:** write the results and decisions in `README.md`; in `index.json` fill `results_summary`, `decisions[]` (decision, by, approved_by, date, decision_ref), `links[]` and `finished`, and set `status` to `done` or `abandoned`.
6. **Link what it led to** in `related`: new agents (new versions), their `changes.md`, tests, other research. An owner decision also gets an entry in the decision log [2.6].
7. **The SI sub-agent saves a pointer, not the research,** in its memory `.claude/agent-memory/[si-name]/MEMORY.md` (e.g. [21.1.12]): the item id and the lesson in one line.

## Checks
<!-- k: id=howto-record-research-checks applies=[2.11.8],path:agents/**/research/index.json,name:[research-id]-[slug] sources=D-025 status=proposed -->
- The item has every field, a final status and `finished`; its folder has a `README.md`.
- Every path in `related` and `links` exists.
- The SI memory holds a pointer to the item, not the research itself.
- No secret value appears in any artifact.

## Changelog
- v0.2 (2026-10-07): neutral wording instead of strategies, variants and backtests (D-056, D-058).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
