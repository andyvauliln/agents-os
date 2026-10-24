"""Writes index.html: template.html with state.json put in."""
import json, pathlib
here = pathlib.Path(__file__).parent
text = (here / "state.json").read_text().rstrip("\n")
json.loads(text)
page = (here / "template.html").read_text().replace("__STATE__", text.replace("</", "<\\/"))
(here / "index.html").write_text(page)
