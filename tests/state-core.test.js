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
  const fixture = { agents: {}, extension: { views: { 'header-view': { 'ui-data': { notifications_button: { pressed: false, count: 2 }, back_button: {} } } }, data: {} } };
  const before = JSON.parse(JSON.stringify(fixture));
  const after = JSON.parse(JSON.stringify(fixture));
  after.extension.views['header-view']['ui-data'].notifications_button.count = 5;
  delete after.extension.views['header-view']['ui-data'].back_button;
  after.extension.data.note = 'hi';
  const v = core.changesView(before, after);
  const parsed = JSON.parse(v.text);
  assert.deepEqual(Object.keys(parsed), ['extension']);
  assert.deepEqual(parsed.extension.views['header-view']['ui-data'], { notifications_button: { count: 5 }, back_button: {} });
  assert.deepEqual(parsed.extension.data, { note: 'hi' });
  assert.deepEqual(v.marks.map(m => [m.type, m.path.join('.')]), [
    ['updated', 'extension.views.header-view.ui-data.notifications_button.count'],
    ['deleted', 'extension.views.header-view.ui-data.back_button'],
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
  next.extension.views['header-view']['ui-data'].state_button = { pressed: true };
  const c2 = core.makeCommit(c1, JSON.stringify(next, null, 2), 't2');
  assert.equal(c2.n, 2);
  assert.equal(c2.parent, 1);
  assert.deepEqual(c2.summary, { added: 1, updated: 0, deleted: 0 });
  assert.deepEqual(c2.paths, ['added extension.views.header-view.ui-data.state_button']);
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

test('paths read keys that hold dots', () => {
  const s = { extension: { views: { 'header-view': { functions: { 'local.open.state-view': { code: 'x' } } } } }, files: { 'CLAUDE.md': 1 } };
  assert.equal(core.getPath(s, 'extension.views.header-view.functions.local.open.state-view.code'), 'x');
  assert.equal(core.getPath(s, 'files.CLAUDE.md'), 1);
  assert.equal(core.getPath(s, 'extension.nothing'), undefined);
  core.setPath(s, 'files.CLAUDE.md', 2);
  assert.equal(s.files['CLAUDE.md'], 2);
});

test('runtime fields are left out of comparisons', () => {
  const s = { v: { functions: { 'local.init': { code: '', output: { a: 1 }, performance: { last: 2 }, calls: { f: { input: 'x', output: 3 } }, tests: { t: { input: 1, result: { ok: true } } } } } } };
  assert.deepEqual(core.stripRuntime(s), { v: { functions: { 'local.init': { code: '', calls: { f: { input: 'x' } }, tests: { t: { input: 1 } } } } } });
  assert.equal(s.v.functions['local.init'].output.a, 1);
});

test('templates fill ui-data and escape text', () => {
  assert.equal(core.template('<b>${e(d.name)}</b>${d.n ? `<i>${d.n}</i>` : ""}', { name: '<Slide>', n: 2 }), '<b>&lt;Slide&gt;</b><i>2</i>');
});

test('test expectations report each failure', () => {
  const has = sel => sel === '#a';
  assert.deepEqual(core.checkExpect({ output: { open: true }, 'output-has': ['x'], dom: ['#a'], 'dom-absent': ['#b'] }, { open: true, x: 1 }, has), []);
  assert.deepEqual(core.checkExpect({ output: { open: true }, dom: ['#b'] }, { open: false }, has), ['output.open is false, expected true', 'no element #b']);
});

test('brief keeps logs small', () => {
  assert.deepEqual(core.brief({ a: 1 }), { a: 1 });
  assert.deepEqual(core.brief('x'.repeat(300)), { type: 'text', length: 300 });
  assert.equal(core.brief(undefined), null);
});

test('state.json runs from index-view and every function is complete', () => {
  const s = JSON.parse(seed);
  const views = s.extension.views;
  assert.deepEqual(Object.keys(views), ['index-view', 'header-view', 'state-view']);
  core.walk(s, [], (v, p) => {
    if (p[p.length - 2] !== 'functions') return;
    for (const k of ['input', 'output', 'imports', 'tests', 'expected-state-change', 'docs', 'performance', 'code', 'calls']) assert.ok(k in v, `${p.join('.')} has ${k}`);
    assert.ok(v.docs.length > 10, `${p.join('.')} has docs`);
    for (const name of Object.keys(v.calls)) assert.ok(name.startsWith('local.') || core.getPath(s, name), `${name} exists`);
  });
  Object.values(views).forEach(v => assert.doesNotThrow(() => core.template(v.html, v['ui-data'])));
});

test('comments are allowed and kept out of the data', () => {
  const text = '{\n  // the header\n  "a": 1, /* inline */ "b": "x // not a comment"\n}';
  assert.deepEqual(core.parseJsonc(text), { a: 1, b: 'x // not a comment' });
  const c = core.makeCommit(null, text, 't');
  assert.equal(c.state, text);
});

test('autofix repairs the owner draft and keeps its comment', () => {
  const draft = fs.readFileSync(path.join(__dirname, 'fixtures', 'owner-draft.jsonc'), 'utf8');
  assert.throws(() => core.parseJsonc(draft));
  const fixed = core.autofix(draft);
  const s = core.parseJsonc(fixed);
  assert.ok(fixed.includes('// last minimum and maximum'));
  assert.deepEqual(Object.keys(s.extension), ['views', 'functions', 'data', 'common_app_storage', 'apps']);
  assert.deepEqual(Object.keys(s.extension.views), ['index-view', 'header-view', 'state-view']);
  assert.equal(s.extension.views['header-view'].functions['local.init'].code, '');
});

test('autofix handles other common slips', () => {
  assert.deepEqual(core.parseJsonc(core.autofix("{a: 'x', b: [1 2,], c: True,}")), { a: 'x', b: [1, 2], c: true });
  assert.deepEqual(core.parseJsonc(core.autofix('{"a": {"b": 1')), { a: { b: 1 } });
  assert.equal(core.autofix('{"a": 1}'), '{"a": 1}');
});
