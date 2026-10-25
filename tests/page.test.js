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

test('page: boots from state, renders the header, runs state tests, saves and steps history', async () => {
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
    await page.evaluate(() => window.agentOS.ready);

    // boot: version 1 from state.json, index-view rendered, which rendered header-view with all its data
    assert.ok(await page.evaluate(() => !!window.__docs['commits/c000001']));
    assert.equal(await page.textContent('.hv-brand'), 'Slide');
    assert.equal(await page.locator('.hv-conn').count(), 4);
    assert.equal(await page.textContent('.hv-conn[data-key=mcp] em'), 'off');
    assert.equal(await page.isHidden('#state-view'), true);
    const boot = await page.evaluate(() => window.agentOS.calls.map(c => [c.name, c.related.parent]));
    assert.deepEqual(boot.map(b => b[0]).sort(), ['extension.functions.get-state', 'extension.functions.render', 'extension.functions.render', 'loadState', 'local.init', 'local.init']);

    // outputs and performance are filled in on the functions that ran
    const init = await page.evaluate(() => window.agentOS.state.extension.views['index-view'].functions['local.init']);
    assert.equal(init.performance.count, 1);
    assert.ok(init.calls['extension.functions.render'].output.view, 'render output filled');

    // the tests written in the state pass
    const results = await page.evaluate(() => window.agentOS.os.runTests());
    assert.ok(results.length >= 5);
    assert.deepEqual(results.filter(r => !r.ok), []);

    // open the state view from the header and edit the brand name
    await page.click('#state-button');
    await page.waitForSelector('#state-view .CodeMirror');
    await page.evaluate(() => {
      const cm = document.querySelector('.CodeMirror').CodeMirror;
      const line = cm.getValue().split('\n').findIndex(l => l.includes('"name": "Slide"'));
      const ch = cm.getLine(line).indexOf('"Slide"') + 6;
      cm.replaceRange('s', { line, ch });
    });
    assert.match(await page.textContent('#status'), /Unsaved changes/);
    await page.click('#save');
    await page.waitForFunction(() => window.agentOS.history.commits.length === 2);
    assert.equal(await page.textContent('.hv-brand'), 'Slides');
    const commit = await page.evaluate(() => window.__docs['commits/c000002']);
    assert.deepEqual(commit.paths, ['updated extension.views.header-view.ui-data.brand.name']);

    // changes view and history steps
    await page.click('#changes');
    assert.equal(await page.locator('.chg-updated').count(), 1);
    assert.equal(await page.textContent('.was'), 'was "Slide"');
    await page.focus('#changes');
    await page.keyboard.press('ArrowLeft');
    assert.match(await page.textContent('#pos'), /Version 1 of 2/);
    await page.keyboard.press('ArrowRight');
    assert.match(await page.textContent('#pos'), /Version 2 of 2/);

    // every call, with its parent, is in the stored call log
    await page.waitForFunction(() => Object.keys(window.__docs).some(k => k.startsWith('calls/') && window.__docs[k].items.some(i => i.name === 'local.step')), null, { timeout: 5000 });
    const log = await page.evaluate(() => Object.entries(window.__docs).find(([k]) => k.startsWith('calls/'))[1]);
    const names = new Set(log.items.map(i => i.name));
    for (const n of ['loadState', 'extension.functions.render', 'local.open.state-view', 'local.save', 'local.toggle-changes', 'local.step', 'runTest']) assert.ok(names.has(n), n);
    assert.ok(log.items.every(i => i.ok && i.at && typeof i.ms === 'number'));
    assert.deepEqual(errors, []);
  } finally {
    await browser.close();
    server.close();
  }
});
