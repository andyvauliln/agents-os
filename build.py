"""Builds index.html, the published page, from src/ and state.json.

Run after changing any of them: python3 build.py
"""
import json
import pathlib

root = pathlib.Path(__file__).parent
state = (root / "state.json").read_text().rstrip("\n")
json.loads(state)  # stop on invalid JSON

page = (root / "src/shell.html").read_text()
page = page.replace("/*__CSS__*/", (root / "src/state-view.css").read_text().rstrip("\n"))
page = page.replace("//__JS__", (root / "src/state-view.js").read_text().rstrip("\n"))
page = page.replace("__STATE__", state.replace("</", "<\\/"))
(root / "index.html").write_text(page)
print("index.html written")
