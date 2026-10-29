# The generator and the release

## The generator
state.json is not written by hand. gen/make_state.py makes it. Change the generator, then make the state again.
- gen/make_state.py: the views, the functions, their tests and the state. It checks that each function has pseudo code.
- gen/style_part.py: the base styles of the page (in index-view html).
- gen/pseudo.py: the pseudo code of each function. Change it when the code changes.
- gen/docs_part.py: these docs. make_state.py writes them to docs/.
- gen/performance.json: the times of each function from the page test. The generator puts them in performance.tests of each function.
- gen/build.js: makes the next version document (commits/cNNNNNN) for a release.
Run it in the folder of the repo:
```sh
python3 gen/make_state.py
```

## The tests
```sh
node --test tests/*.test.js
```
1. tests/state-core.test.js: the library of the runtime.
2. tests/page.test.js: the page in Chromium (Playwright). It clicks through the views, runs the tests that are written in the state, and writes gen/performance.json.
3. All tests take about 7 minutes. Do not make the state again while the tests run.

## The release
1. Make the state and run the tests.
2. Commit to main and push to the agent-os branch: git push origin main:agent-os.
3. Record the run (see agent-runs.md). Commit the run file. Make the state again and commit it.
4. Make the version document:
```sh
node gen/build.js <previous commit.json> <release.json> <out dir>
```
release.json has request (the words of the owner), session (the link) and explain ([{part, before, now}], in ASD-STE100).
5. A big version also gets <out dir>/cNNNNNN.state.json. Upload it as a file of the page (Artifact publish with asset: true). Then write its id into the document:
```sh
node gen/build.js --state-file <out dir>/cNNNNNN.json <file id>
```
6. Save the document as commits/cNNNNNN in the page database.
7. When index.html, state-core.js or vendor/ change, publish the runtime files first.
8. An open page runs the new version at once.

## Start it on another server
1. Clone the repo: git clone -b agent-os https://github.com/andyvauliln/agents-os.
2. In the folder, run python3 -m http.server 8000. Open http://localhost:8000.
3. The page runs from state.json with a memory store: there is no database, no comments, no Send to Claude and no MCP. A save stays until the page reloads.
4. For the agent: open the folder with Claude Code. It reads .claude/CLAUDE.md. You need python3, node and (for the page test) Playwright with Chromium.