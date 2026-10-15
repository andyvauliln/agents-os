# Agent OS: Add an account or secret (v0.2)

How to add the key of an outside account, a platform key or any other secret, and give it only to the agent or job that needs it. The store is [47] `.secrets/` at the repo root (D-023, D-027); the rules are in safety.md. A domain may add its own account steps: for example, the prediction-market domain's `how-to/add-trading-account.md`. This runbook is [2.11.6] in the file tree.

## Steps
<!-- k: id=howto-add-account-or-secret-steps applies=[2.11.6],[47],[47.1.1],[47.2.1],[47.3],[11.11],[27.2],[27.4],[14.1],[48] sources=D-023,D-027,in-20260930-0804,in-20260930-0812-2,D-056 status=proposed -->
1. **The owner creates the key** at the platform or provider.
2. **Test key:** add a `KEY=value` line to [47.1.1] `.secrets/test/.env`, with a prefix per provider and account, e.g. `[PROVIDER]_[ACCOUNT]_[WHAT]`. Agents may read and update this file (D-027). The owner can also edit keys in the local UI; values never leave the machine.
3. **Live key:** only the owner adds it, under the same key name, to [47.2.1] `.secrets/live/.env` (file `chmod 600`, folder `chmod 700`). This is a later phase.
4. **Metadata:** add the key to [47.3] `secrets.index.json`: kind, env, used by, created, `rotate_by`; never the value. The owner wants this to happen automatically whenever a variable is added (in-20260930-0812-2); until a script or agent does it, do it by hand.
5. **Reference it:** a platform key goes into [11.11] `platforms`. The system knows any other outside account only by its key names and the owner's approval for live; a domain may keep more about its accounts in its own config. A live entry needs owner approval.
6. **Give it to the agent:** add the key names to its config's `secret_keys` (like [27.2]) or to the job's `secret_keys` in its workers file (like [27.4]; `local` jobs only).
7. **Test run with the test key:** `load-secret [PROVIDER]_[ACCOUNT]_* -- python3 scripts/[worker-name].worker.py`. The loader [14.1] exports only the declared keys into that one process and logs only key names, mode and result.
8. **Check links:** `node scripts/relink.system.link.js --check` (it runs the `check-links` rules), which fails on any link or copy into `.secrets/`.
9. **Rotation:** write the new value under the same key name, update `rotate_by` in [47.3], then revoke the old key at the provider. The notifier warns before `rotate_by`.

## Checks
<!-- k: id=howto-add-account-or-secret-checks applies=[2.11.6],[47.1.1],[47.2.1],[47.3],[48],[14.1],name:settings.json sources=D-023,D-027,D-028,D-056 status=proposed -->
- The key line is in the right `.env`; file and folder permissions are 600 and 700; `.secrets/` is git-ignored [48].
- [47.3] has the entry with `rotate_by` and no value.
- No value appears in any config, doc, data file, log, prompt or link; configs hold key names or refs only.
- A test run gets exactly the declared keys, and a missing key fails fast with its name.
- `load-secret` refuses live keys unless the agent is live-allowed and the run is owner-approved, and every level's `settings.json` still denies `.secrets/live/**`.

## Changelog
- v0.2 (2026-10-07): trading parts moved to the prediction-market domain's `how-to/add-trading-account.md` (D-056, D-058).
- v0.1 (2026-09-30): created from file-tree.md v1.15, vision.md v0.19 and the owner inputs (D-033).
