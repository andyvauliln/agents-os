const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const core = require('../state-core.js');

const seed = fs.readFileSync(path.join(__dirname, '..', 'state.json'), 'utf8');

test('diff finds added, updated and deleted entries', () => {
  const changes = core.diff({ a: 1, b: { c: 2, d: 3 } }, { a: 1, b: { c: 5 }, e: {} });
  assert.deepEqual(changes, [
    { type: 'updated', path: ['b', 'c'], before: 2, after: 5 },
    { type: 'deleted', path: ['b', 'd'], before: 3 },
    { type: 'added', path: ['e'], after: {} }
  ]);
  assert.deepEqual(core.summarize(changes), { added: 1, updated: 1, deleted: 1 });
});

test('diff of equal states is empty', () => {
  assert.deepEqual(core.diff(JSON.parse(seed), JSON.parse(seed)), []);
});

test('changes view keeps only what changed, with line marks', () => {
  const before = JSON.parse(seed);
  const after = JSON.parse(seed);
  after.extension.view['header-view'].notifications_button.count = 5;
  delete after.extension.view['header-view'].back_button;
  after.extension.data.note = 'hi';
  const v = core.changesView(before, after);
  const parsed = JSON.parse(v.text);
  assert.deepEqual(Object.keys(parsed), ['extension']);
  assert.deepEqual(parsed.extension.view['header-view'], { notifications_button: { count: 5 }, back_button: {} });
  assert.deepEqual(parsed.extension.data, { note: 'hi' });
  assert.deepEqual(v.marks.map(m => [m.type, m.path.join('.')]), [
    ['updated', 'extension.view.header-view.notifications_button.count'],
    ['deleted', 'extension.view.header-view.back_button'],
    ['added', 'extension.data.note']
  ]);
  const lines = v.text.split('\n');
  v.marks.forEach(m => assert.ok(lines[m.from].includes(JSON.stringify(m.path[m.path.length - 1]))));
  assert.equal(v.marks[0].before, 2);
});

test('changes view of identical states is empty', () => {
  const v = core.changesView({ a: 1 }, { a: 1 });
  assert.equal(v.empty, true);
  assert.equal(v.text, '{}');
});

test('commits chain and record what changed', () => {
  const c1 = core.makeCommit(null, seed, 't1');
  assert.equal(c1.n, 1);
  assert.equal(c1.parent, null);
  assert.equal(c1.summary.added, 2);
  const next = JSON.parse(seed);
  next.extension.view['header-view'].state_button.pressed = true;
  const c2 = core.makeCommit(c1, JSON.stringify(next, null, 2), 't2');
  assert.equal(c2.n, 2);
  assert.equal(c2.parent, 1);
  assert.deepEqual(c2.summary, { added: 0, updated: 1, deleted: 0 });
  assert.deepEqual(c2.paths, ['updated extension.view.header-view.state_button.pressed']);
  assert.equal(core.commitId(2), 'c000002');
});

test('history steps stay inside the commits and the draft', () => {
  const commits = [core.makeCommit(null, '{"a":1}', 't1')];
  commits.push(core.makeCommit(commits[0], '{"a":2}', 't2'));
  assert.equal(core.step(1, 1, commits, null), 1);
  assert.equal(core.step(1, 1, commits, '{"a":3}'), 2);
  assert.equal(core.step(0, -1, commits, null), 0);
  assert.equal(core.textAt(2, commits, '{"a":3}'), '{"a":3}');
  assert.deepEqual(core.pairAt(0, commits, null), { before: {}, after: { a: 1 } });
  assert.deepEqual(core.pairAt(2, commits, '{"a":3}'), { before: { a: 2 }, after: { a: 3 } });
});

test('tracker records name, input, output, related data and errors', async () => {
  let t = 0;
  const seen = [];
  const tr = core.createTracker({ now: () => 'now', clock: () => (t += 5), onRecord: r => seen.push(r.name) });
  const v = tr.track('save', { size: 3 }, ctx => { ctx.relate({ commit: 2 }); return 'ok'; });
  assert.equal(v, 'ok');
  assert.throws(() => tr.track('bad', null, () => { throw new Error('nope'); }), /nope/);
  await tr.track('later', null, async ctx => { ctx.relate({ pos: 1 }); return 7; });
  assert.deepEqual(tr.records.map(r => [r.id, r.name, r.ok, r.output, r.error, r.related]), [
    [1, 'save', true, 'ok', null, { commit: 2 }],
    [2, 'bad', false, null, 'nope', {}],
    [3, 'later', true, 7, null, { pos: 1 }]
  ]);
  assert.equal(tr.records[0].ms, 5);
  assert.deepEqual(seen, ['save', 'bad', 'later']);
});
