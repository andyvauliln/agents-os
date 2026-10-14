---
about: agent-os/apps/project-IDE/data/inputs/YYYY-MM-DD-HHMM-[topic].md
node: n-2.10.1
basis: 8c11d10c098c
written: 2026-10-01T00:54:39Z
by: summary-worker
confirmed: 2026-10-05T15:38:31Z
---
# YYYY-MM-DD-HHMM-[topic].md

## Summary

One file per owner input, named by its date, time and topic. It holds a header (id, time, channel, categories, one-line summary), the owner's words unchanged, and a "Processed into" list of the decisions, docs and objects it changed. When the input is a question, the answer is stored in the same file. The knowledge agent writes it on receipt.

## Keep in mind

- When you store an input, copy the owner's words exactly and never edit them later; corrections go into the docs.
- When the input is a question, store the answer in the same file under `## Answer`: the answer is knowledge too.
