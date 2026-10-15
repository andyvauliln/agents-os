---
about: agent-os/.secrets/live/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-15T07:11:37Z
---
# live/

## What it is

The live side of the keys store, for a later phase. It holds `.env`, git-ignored and empty for now, which only the owner will fill with live values and no agent reads; `.env.example`, the same key names with no values; and the metadata files of the keys file.

## Who looks after it

It is written by the owner.

## When and how it changes

It changes when a file is added to or removed from the live side of the keys store.

## Who uses it, and when

It is read by the owner; and load-secret (the proposed shared loader, not written yet), only for owner-approved live runs.

## Where it is mentioned

It is described in `agents/system/docs/README.md` and its folder's How it works file `.secrets/.secrets.index.md`.

## Related knowledge

It has the same format as `.secrets/test/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `docs/README.md` (section "Keys and secrets") and `agents/system/docs/README.md` (section "Keys and secrets").

## Keep in mind


