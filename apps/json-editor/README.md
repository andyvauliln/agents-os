# JSON editor

An otherwise empty page that holds the owner's JSON (`state.json`) in an editor. The page is published on claude.ai at https://claude.ai/artifact/1YzMjLVfh9gp54PTXtPGoG, and Save there keeps the edit as a new version of the page.

- `state.json`: the JSON, as the owner gave it on 2026-10-24.
- `template.html`: the page, with `__STATE__` where the JSON goes.
- `build.py`: writes `index.html` from the two. Run `python3 apps/json-editor/build.py` after changing either.

Edits saved on claude.ai stay in the published page; copy them back into `state.json` to keep the repository in step.
