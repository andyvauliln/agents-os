#!/usr/bin/env python3
"""Rebuild the page data for a start of the project IDE, without a needless new version.

    python3 rebuild.py

Runs materialize.py, builds the data into a scratch folder with the current data version, and
compares it with the data next to the page (without the "generated" time). Only when something
differs is the data built again in place with the next data version, so a restart with no change
leaves git clean. Then it reports the How it works check and the tree check. It does not write How
it works files and never publishes; a stale How it works file is reported, not fixed.
Exit code 0 when the data is in place and the tree check passes, 1 otherwise.
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get("REPO_DIR") or subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=HERE,
                                                     capture_output=True, text=True, check=True).stdout.strip()
UI = os.path.join(REPO, "apps/project-IDE/current-ui")
DATA = os.path.join(UI, "file-tree.data.json")


def run(script, *args, env=None, quiet=False):
    p = subprocess.run([sys.executable, "-W", "ignore::DeprecationWarning", os.path.join(HERE, script), *args], cwd=REPO, capture_output=True, text=True,
                       env={**os.environ, "REPO_DIR": REPO, **(env or {})})
    out = (p.stdout + p.stderr).strip()
    if out and not quiet:
        print("\n".join("  " + line for line in out.splitlines()[-6:]))
    return p.returncode, out


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def same(a, b):
    if a is None or b is None:
        return False
    strip = lambda d: {k: v for k, v in d.items() if k != "generated"}
    return strip(a) == strip(b)


def main():
    print("materialize: metadata files for new items, docs/file-tree.md")
    if run("materialize.py")[0]:
        return 1

    current = load(DATA)
    version = int((current or {}).get("data_version", 0))
    with tempfile.TemporaryDirectory() as tmp:
        code, out = run("enrich.py", os.path.join(tmp, "file-tree.data.json"), env={"DATA_VERSION": str(version)}, quiet=True)
        if code:
            print(out)
            return 1
        fresh = load(os.path.join(tmp, "file-tree.data.json"))
        with open(os.path.join(tmp, "real-files.json"), "rb") as f:
            texts_fresh = f.read()
    try:
        with open(os.path.join(UI, "real-files.json"), "rb") as f:
            texts_same = f.read() == texts_fresh
    except OSError:
        texts_same = False

    if same(current, fresh) and texts_same:
        print(f"page data: no change, kept at version {version}")
    else:
        print(f"page data: changed, built as version {version + 1}")
        if run("enrich.py", env={"DATA_VERSION": str(version + 1)})[0]:
            return 1

    print("how it works files:")
    run("build_map.py")
    print("tree check:")
    code, out = run("check_tree.py")
    return 0 if code == 0 and "tree ok" in out else 1


if __name__ == "__main__":
    sys.exit(main())
