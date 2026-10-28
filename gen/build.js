// Makes the next version's commit document from state.json.
// node gen/build.js <previous commit.json> <release.json> <out dir>
// release.json: {request, session, explain: [{part, before, now}]} (see .claude/CLAUDE.md, Releases).
// The previous commit: read it from the page database (ArtifactData commits/cNNNNNN).
// Writes <out dir>/cNNNNNN.json: save it as commits/cNNNNNN.
const fs = require('fs'), path = require('path'), zlib = require('zlib'), cp = require('child_process');
const REPO = path.dirname(__dirname), core = require(REPO + '/state-core.js');
const [prevFile, releaseFile, out] = process.argv.slice(2);
const prev = JSON.parse(fs.readFileSync(prevFile, 'utf8'));
if (prev.stateGz) { prev.state = zlib.gunzipSync(Buffer.from(prev.stateGz, 'base64')).toString(); delete prev.stateGz; }
const release = JSON.parse(fs.readFileSync(releaseFile, 'utf8'));
const n = prev.n + 1;
const st = JSON.parse(fs.readFileSync(REPO + '/state.json', 'utf8'));
const u = st.extension.views['state-view']['ui-data'];
u.current_state_version = n; u.position = n - 1; u.version = 'v' + n;
const c = core.makeCommit(prev, JSON.stringify(st, null, 2), new Date().toISOString());
const git = cmd => cp.execSync('git -C ' + JSON.stringify(REPO) + ' ' + cmd).toString().trim();
c.source = { git: git('log -1 --format=%H'), branch: git('rev-parse --abbrev-ref HEAD'), message: git('log -1 --format=%s'), request: release.request, session: release.session, explain: release.explain };
// A database document holds at most 256 KB: a big state goes gzipped in base64.
if (JSON.stringify(c).length > 200000) { c.stateGz = zlib.gzipSync(Buffer.from(c.state)).toString('base64'); delete c.state; }
const id = 'c' + String(n).padStart(6, '0');
fs.writeFileSync(path.join(out, id + '.json'), JSON.stringify(c));
console.log(id, 'parent', c.parent, c.summary, c.paths.length + ' paths', JSON.stringify(c).length + ' bytes');
