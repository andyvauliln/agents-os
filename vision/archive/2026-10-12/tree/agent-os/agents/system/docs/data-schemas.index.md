---
about: agent-os/agents/system/docs/data-schemas.md
node: n-2.14
basis: e7edd42a4f1c
written: 2026-10-07T19:01:11Z
by: knowledge-base-agent
---
# data-schemas.md

## Summary

The shape of every JSON and Markdown file, so workers, agents, scripts and the UI read and write the same format. General rules come first (plain files, no database for now; encoding, UTC times, units, ids, `schema_version`), then each file type's fields: outputs, configs, jobs and links files, routing, logs, index tables, tests configs, the research index and Markdown templates. The prediction-market domain's files are in its `trading-data-schemas.md`. Many details are proposed.

## Keep in mind

- When you add a file type or change its fields, update its section here and add a line to `changelog.md` in the same change.
- When you rename, remove or change the meaning of a field, bump `schema_version`; a new optional field needs no bump (proposed rule).
