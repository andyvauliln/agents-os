# Agent OS: Process an input (v0.2)

What happens to every owner input (project chat, a thread, the File Tree page) and every change to the system, so the knowledge base stays true (D-033). The knowledge agent `sys-knowledge-agent` [10.1.1.2] (was `sys-docs-agent`) does it with two skills: `knowledge-intake` and `file-index`. This is the short version; the full flow is in docs/README.md ("The flow for every input or change") and in the two skills.

## Steps
<!-- k: id=howto-process-an-input-steps applies=[2.11.10],[2.10]/**,[10.1.1.2],[2]/** sources=D-033,in-20260930-1533,in-20260930-0839,in-20260930-1841,in-20260930-1603 status=decided -->
1. **Hand it to the knowledge agent.** Every owner input and every system change goes to `sys-knowledge-agent` [10.1.1.2], which runs `knowledge-intake`. Nothing that says how the system should be is "just chat".
2. **Store the input** word for word in `docs/inputs/` [2.10] (one file per input, like [2.10.1]) and add it to `inputs/index.json` with its id `in-YYYYMMDD-HHMM` and its categories. When the owner asked a question, store the answer in the same file under `## Answer`: the answer is knowledge too. A system change with no owner words gets no input file; note its source instead.
3. **Extract the knowledge:** new facts, rules, formats, renames, removals, questions answered and new questions, each marked decided (the owner said it), proposed or open. For a question, extract from the answer as well, and make the place that should have answered it clearer.
4. **Place each piece** using the knowledge map `index/knowledge-map.json`: update the entry or the file doc in file-tree.md [2.13] that already holds it, or add a tagged section to the right topic doc, or create a new doc when nothing fits (and list it in docs/README.md [2.1]).
5. **Ripple:** bring every other entry and file doc that states the same thing in line, so one fact lives in one place.
6. **Record:** an entry in decisions.md [2.6] when the owner decided something, a line in changelog.md [2.9], and `processed_into` on the input.
7. **Rebuild the map** (`python3 tools/build_map.py`), then run `file-index` on every stale node, children first, up to the root (`python3 tools/build_map.py --stale` lists them). Each summary can carry up to four "Always keep in mind" lines.
8. **Republish** the explorer data and page, and report two to five plain lines to the owner: what changed, what is proposed, what only the owner can answer.

## Checks
<!-- k: id=howto-process-an-input-checks applies=[2.11.10],[2.10]/**,[10.1.1.2],[2]/** sources=D-033,in-20260930-1533 status=proposed -->
- The input file and its `inputs/index.json` row exist, and `processed_into` is filled.
- `python3 tools/build_map.py` reports no problem in the docs that were touched.
- `python3 tools/build_map.py --stale` prints nothing.
- No two docs state different versions of the same fact, and every status is honest: nothing the owner did not decide is marked decided.
- Every owner decision has its decisions.md entry.

## Changelog
- v0.2 (2026-09-30): answers to questions are stored and filed; keep-in-mind lines (in-20260930-1841, in-20260930-1603).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
