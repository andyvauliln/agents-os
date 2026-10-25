// Drives index.html in Chromium with Playwright, against a fake db, and checks each tracked call.
// Run: node --test tests/  (set CM_DIR to a local codemirror@5.65.16 package to work offline)
const test = require('node:test');
const assert = require('node:assert/strict');
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');

const root = path.join(__dirname, '..');

function serve() {
  const server = http.createServer((req, res) => {
    const file = path.join(root, decodeURIComponent(req.url.split('?')[0]).replace(/^\/$/, '/index.html'));
    if (!file.startsWith(root) || !fs.existsSync(file)) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'content-type': file.endsWith('.js') ? 'application/javascript' : file.endsWith('.json') ? 'application/json' : 'text/html' });
    fs.createReadStream(file).pipe(res);
  });
  return new Promise(r => server.listen(0, () => r(server)));
}

// A small stand-in for the page's db capability: commits/<id> and calls/<id> documents in memory.
function fakeDb() {
  window.__docs = {};
  const snap = (id, d) => ({ id, exists: !!d, data: () => d && JSON.parse(JSON.stringify(d)), metadata: {} });
  const doc = p => ({ id: p.split('/').pop(), path: p,
    get: async () => snap(p.split('/').pop(), window.__docs[p]),
    set: async d => { window.__docs[p] = JSON.parse(JSON.stringify(d)); } });
  const collection = c => {
    let order = null;
    const q = {
      orderBy(f) { order = f; return q; },
      async get() {
        const docs = Object.keys(window.__docs).filter(k => k.startsWith(c + '/')).map(k => window.__docs[k]);
        if (order) docs.sort((a, b) => a[order] - b[order]);
        return { docs: docs.map(d => snap('', d)), size: docs.length, empty: !docs.length };
      },
      doc: id => doc(c + '/' + id)
    };
    return q;
  };
  window.claude = { use: async name => (name === 'db' ? { doc, collection } : null) };
}

test('page: load, open, edit, save, changes, history and call log', async () => {
  const server = await serve();
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    if (process.env.CM_DIR) {
      await page.route('https://cdnjs.cloudflare.com/**', route => {
        const f = route.request().url().split('5.65.16/')[1];
        const local = f === 'codemirror.min.js' ? 'lib/codemirror.js' : f.replace('.min.js', '.js');
        route.fulfill({ body: fs.readFileSync(path.join(process.env.CM_DIR, local)), contentType: 'application/javascript' });
      });
      await page.route('https://fonts.googleapis.com/**', route => route.fulfill({ body: '' }));
    }
    await page.addInitScript(fakeDb);
    await page.goto(`http://localhost:${server.address().port}/`);

    // load: header from state, state view closed (state_button.pressed is false), first commit created
    await page.waitForSelector('#state-button');
    assert.equal(await page.isHidden('#state-view'), true);
    const load = await page.evaluate(() => window.agentOS.calls[0]);
    assert.equal(load.name, 'loadState');
    assert.deepEqual(load.related, { created: 1, store: 'db', commits: 1, head: 1 });
    assert.ok(await page.evaluate(() => !!window.__docs['commits/c000001']));

    // open the state view
    await page.click('#state-button');
    assert.equal(await page.isVisible('#state-view'), true);
    assert.match(await page.textContent('#pos'), /Version 1 of 1/);

    // edit like an editor, then save as version 2
    await page.evaluate(() => {
      const cm = window.agentOS.editor;
      const line = cm.getValue().split('\n').findIndex(l => l.includes('"Slide"'));
      const ch = cm.getLine(line).indexOf('"Slide"') + 6;
      cm.replaceRange('s', { line, ch });
    });
    assert.match(await page.textContent('#status'), /Unsaved changes/);
    await page.click('#save');
    await page.waitForFunction(() => window.agentOS.state.commits.length === 2);
    const commit = await page.evaluate(() => window.__docs['commits/c000002']);
    assert.deepEqual(commit.summary, { added: 0, updated: 1, deleted: 0 });
    assert.deepEqual(commit.paths, ['updated extension.view.header-view.brand.name']);
    const save = await page.evaluate(() => window.agentOS.calls.find(c => c.name === 'saveCommit'));
    assert.equal(save.ok, true);
    assert.equal(save.related.commit, 2);

    // changes: only the changed entry, marked as updated, with the old value
    await page.click('#changes');
    const text = await page.evaluate(() => window.agentOS.editor.getValue());
    assert.deepEqual(JSON.parse(text), { extension: { view: { 'header-view': { brand: { name: 'Slides' } } } } });
    assert.equal(await page.locator('.chg-updated').count(), 1);
    assert.equal(await page.textContent('.was'), 'was "Slide"');

    // arrow left steps back to version 1, where everything is new
    await page.focus('#changes');
    await page.keyboard.press('ArrowLeft');
    assert.match(await page.textContent('#pos'), /Version 1 of 2/);
    assert.ok(await page.locator('.chg-added').count() > 0);
    await page.keyboard.press('ArrowRight');
    assert.match(await page.textContent('#pos'), /Version 2 of 2/);

    // collapse all folds nested objects
    await page.click('#changes');
    await page.click('#collapse');
    assert.ok(await page.locator('.CodeMirror-foldmarker').count() >= 2);

    // every call is in the stored call log
    await page.waitForFunction(() => Object.keys(window.__docs).some(k => k.startsWith('calls/') && window.__docs[k].count >= 8), null, { timeout: 5000 });
    const log = await page.evaluate(() => Object.entries(window.__docs).find(([k]) => k.startsWith('calls/'))[1]);
    assert.deepEqual([...new Set(log.items.map(i => i.name))].sort(),
      ['collapseAll', 'editDraft', 'loadState', 'saveCommit', 'stepHistory', 'toggleChanges', 'toggleStateView']);
    assert.ok(log.items.every(i => i.ok && i.at && typeof i.ms === 'number'));
    assert.deepEqual(errors, []);
  } finally {
    await browser.close();
    server.close();
  }
});
