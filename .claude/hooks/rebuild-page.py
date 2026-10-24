"""PostToolUse hook: rebuilds index.html when state.json or src/ was edited."""
import json
import pathlib
import subprocess
import sys

event = json.load(sys.stdin)
path = event.get("tool_input", {}).get("file_path", "")
root = pathlib.Path(__file__).resolve().parents[2]
if path.endswith("state.json") or "/src/" in path:
    result = subprocess.run([sys.executable, str(root / "build.py")], capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(2)
