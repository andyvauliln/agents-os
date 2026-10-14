---
about: agent-os/.secrets/secrets.index.json
basis: 0b926e7a68a1
written: 2026-09-30T20:11:26Z
by: knowledge-agent
confirmed: 2026-10-14T15:07:13Z
---
# secrets.index.json

## Summary

Metadata about every key in the two `.env` files: kind, test or live, who uses it, when it was created and when to rotate it. It never holds a value. It changes in the same change as the `.env` files whenever a key is added, renamed or removed, and the owner wants that to happen automatically; a proposed `check-secrets-index` script would catch drift. What triggers the sync is still open.

## Keep in mind

- When a key is added, renamed or removed in an `.env` file, update its entry here in the same change, with no value.
