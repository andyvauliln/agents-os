// Makes the next version's commit document from state.json.
// node gen/build.js <previous commit.json> <release.json> <out dir>
// release.json: {request, session, explain: [{part, before, now}]} (see .claude/CLAUDE.md, Releases).
// The previous commit: read it from the page database (ArtifactData commits/cNNNNNN); a commit with state_file needs
// its state next to it as <previous commit>.state.json.
// Writes <out dir>/cNNNNNN.json, and <out dir>/cNNNNNN.state.json when the version is too big for one database
// document (256 KB). Then upload cNNNNNN.state.json as an asset of the page and run
// node gen/build.js --state-file <out dir>/cNNNNNN.json <asset id>: the document gets state_file and loses state.
// Save the document as commits/cNNNNNN.
const fs = require('fs'), path = require('path'), zlib = require('zlib'), cp = require('child_process');
const REPO = path.dirname(__dirname), core = require(REPO + '/state-core.js');
if (process.argv[2] === '--state-file') {
  const [file, id] = process.argv.slice(3), c = JSON.parse(fs.readFileSync(file, 'utf8'));
  delete c.state; delete c.stateGz; c.state_file = id;
  fs.writeFileSync(file, JSON.stringify(c));
  console.log(path.basename(file), 'state_file', id, JSON.stringify(c).length + ' bytes');
  process.exit(0);
}
const [prevFile, releaseFile, out] = process.argv.slice(2);
const prev = JSON.parse(fs.readFileSync(prevFile, 'utf8'));
if (prev.state_file) prev.state = fs.readFileSync(prevFile.replace(/\.json$/, '.state.json'), 'utf8');
if (prev.stateGz) { prev.state = zlib.gunzipSync(Buffer.from(prev.stateGz, 'base64')).toString(); delete prev.stateGz; }
const release = JSON.parse(fs.readFileSync(releaseFile, 'utf8'));
const n = prev.n + 1;
const st = JSON.parse(fs.readFileSync(REPO + '/state.json', 'utf8'));
const u = st.extension.views['state-view']['ui-data'];
u.current_state_version = n; u.position = n - 1; u.version = 'v' + n;
const c = core.makeCommit(prev, JSON.stringify(st, null, 2), new Date().toISOString());
const git = cmd => cp.execSync('git -C ' + JSON.stringify(REPO) + ' ' + cmd).toString().trim();
c.source = { git: git('log -1 --format=%H'), branch: git('rev-parse --abbrev-ref HEAD'), message: git('log -1 --format=%s'), request: release.request, session: release.session, explain: release.explain };
const id = 'c' + String(n).padStart(6, '0');
// A database document holds at most 256 KB: a big state goes gzipped in base64, or (too big for that) into a file.
const text = c.state;
if (JSON.stringify(c).length > 200000) { c.stateGz = zlib.gzipSync(Buffer.from(text)).toString('base64'); delete c.state; }
if (JSON.stringify(c).length > 240000) {
  delete c.stateGz;
  fs.writeFileSync(path.join(out, id + '.state.json'), text);
  c.state_file = 'UPLOAD ' + id + '.state.json';
}
fs.writeFileSync(path.join(out, id + '.json'), JSON.stringify(c));
console.log(id, 'parent', c.parent, c.summary, c.paths.length + ' paths', JSON.stringify(c).length + ' bytes' + (c.state_file ? ', state in ' + id + '.state.json: upload it, then --state-file' : ''));
