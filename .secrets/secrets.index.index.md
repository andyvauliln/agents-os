---
about: agent-os/.secrets/secrets.index.json
basis: 0b926e7a68a1
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-14T15:07:13Z
---
# secrets.index.json

## What it is

Metadata about every key in the two `.env` files: kind, test or live, who uses it, when it was created and when to rotate it. It never holds a value. It changes in the same change as the `.env` files whenever a key is added, renamed or removed, and the owner wants that to happen automatically; a proposed `check-secrets-index` script would catch drift. What triggers the sync is still open.

## Who looks after it

It is written by the owner and knowledge-base-agent (meant to update it whenever a key changes).

## When and how it changes

It changes when a key is added, renamed or removed in a .env file, in the same change. It is empty for now.

## Who uses it, and when

It is read by the owner, file-index (writes each .env.example from it) and every agent that needs to know which keys exist.

## Where it is mentioned

It is described in `docs/rebuild-prompt.md` and its folder's How it works file `.secrets/.secrets.index.md`.

## Related knowledge

It has the same format as `.secrets/test/.env`. It is read by `.secrets/test/.env.example`, `.secrets/live/.env.example` and `agents/system/.claude/skills/file-index/SKILL.md`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `docs/README.md` (section "Keys and secrets") and `agents/system/docs/README.md` (section "Keys and secrets").

## Keep in mind

- When a key is added, renamed or removed in an `.env` file, update its entry here in the same change, with no value.
