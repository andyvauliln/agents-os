---
about: agent-os/.secrets/test/
basis: 981c7ce4dc3d
written: 2026-10-14T15:17:50Z
by: knowledge-base-agent
confirmed: 2026-10-15T07:11:37Z
---
# test/

## What it is

The test side of the keys store. It holds `.env`, git-ignored, meant for every test key; `.env.example`, its key names with no values; and the metadata files of the keys file. Agents may read and update the test keys because they are safe test credentials.

## Who looks after it

It is written by the owner.

## When and how it changes

It changes when a file is added to or removed from the test side of the keys store.

## Who uses it, and when

It is read by the owner; and load-secret (the proposed shared loader, not written yet).

## Where it is mentioned

It is described in `agents/system/docs/README.md` and its folder's How it works file `.secrets/.secrets.index.md`.

## Related knowledge

It has the same format as `.secrets/live/`. The rules that apply to it come from `agents/system/CLAUDE.md` (section "Rules"), `docs/metadata.md`, `docs/README.md` (section "Keys and secrets") and `agents/system/docs/README.md` (section "Keys and secrets").

## Keep in mind


