// Drives index.html in Chromium with Playwright, against a fake db, and checks each tracked call.
// Run: node --test tests/  (the libraries load from vendor/ of the repo; the fonts are left out)
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
      doc: id => doc(c + '/' + id),
      onSnapshot(next) { (window.__listeners = window.__listeners || []).push(() => q.get().then(next)); return () => {}; }
    };
    return q;
  };
  // and the assets capability: a file of the page is served at /_blob/<id>
  window.__blobs = {};
  const assets = { upload: async blob => { const id = 'a' + Object.keys(window.__blobs).length; window.__blobs[id] = await blob.text(); return { id, url: '/_blob/' + id, sizeBytes: blob.size, contentType: blob.type }; },
    delete: async id => { delete window.__blobs[id]; } };
  const fetch0 = window.fetch;
  window.fetch = (u, o) => { const m = /^\/_blob\/(\w+)$/.exec(String(u)); return m ? Promise.resolve(window.__blobs[m[1]] === undefined ? new Response('', { status: 404 }) : new Response(window.__blobs[m[1]])) : fetch0(u, o); };
  // comments (Send now: a comment sent to Claude) and mcp (Send now new session) keep what was sent in window.__sent
  window.__sent = [];
  const comments = { canSendToClaude: async () => 'available', anchorFor: async () => ({ path: 'main', x: 0, y: 0 }),
    sendToClaude: async t => { window.__sent.push({ to: 'claude', text: t.text }); return { threadId: 't1', commentId: 'c1' }; } };
  const mcp = { callTool: async (server, tool, input) => { window.__sent.push({ to: server, tool, input }); return { payload: {} }; } };
  window.claude = { use: async name => ({ db: { doc, collection }, assets, comments, mcp })[name] || null };
}

// Fake media for the record button: a tone for the microphone, a canvas that changes color for the screen.
function fakeMedia() {
  const tone = () => { const ac = new AudioContext(), o = ac.createOscillator(), d = ac.createMediaStreamDestination(); o.connect(d); o.start(); return d.stream; };
  navigator.mediaDevices.getUserMedia = async () => tone();
  navigator.mediaDevices.getDisplayMedia = async () => {
    const c = document.createElement('canvas'), g = c.getContext('2d');
    c.width = 160; c.height = 100;
    let i = 0;
    setInterval(() => { g.fillStyle = 'hsl(' + (i++ * 20 % 360) + ',70%,50%)'; g.fillRect(0, 0, 160, 100); }, 50);
    return c.captureStream(20);
  };
  // the speech service of the browser: it hears "move the save button"
  window.SpeechRecognition = class {
    start() { this.t = setTimeout(() => this.onresult && this.onresult({ resultIndex: 0, results: [Object.assign([{ transcript: 'move the save button' }], { isFinal: true })] }), 200); }
    stop() { clearTimeout(this.t); setTimeout(() => this.onend && this.onend(), 10); }
  };
}

test('page: boots from state, renders the header, runs state tests, saves and steps history', async () => {
  const server = await serve();
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    // the libraries load from vendor/ of the repo; the fonts come from Google, not here
    await page.route('https://fonts.googleapis.com/**', route => route.fulfill({ body: '' }));
    await page.addInitScript(fakeDb);
    await page.addInitScript(fakeMedia);
    await page.goto(`http://localhost:${server.address().port}/`);
    await page.evaluate(() => window.agentOS.ready);

    // a saved version as the page reads it: a big state is kept in a file of the page (state_file), or gzipped (stateGz)
    const commitDoc = id => page.evaluate(async id => {
      const c = window.__docs['commits/' + id];
      if (!c || typeof c.state === 'string') return c;
      if (c.state_file) return Object.assign({}, c, { state: window.__blobs[c.state_file] });
      const bin = atob(c.stateGz), u = Uint8Array.from(bin, ch => ch.charCodeAt(0));
      const state = await new Response(new Blob([u]).stream().pipeThrough(new DecompressionStream('gzip'))).text();
      return Object.assign({}, c, { state, stateGz: undefined });
    }, id);

    // boot: version 1 from state.json, index-view rendered (page html and styles from the state), then header-view: only the State view button
    assert.ok(await page.evaluate(() => !!window.__docs['commits/c000001']));
    // (the state is bigger than a database document can hold: it is saved as a file of the page, and reads back the same)
    assert.equal(typeof (await page.evaluate(() => window.__docs['commits/c000001'].state_file)), 'string');
    assert.equal(await page.evaluate(() => window.__docs['commits/c000001'].state), undefined);
    assert.equal((await commitDoc('c000001')).state, await page.evaluate(() => window.agentOS.history.commits[0].state));
    // (the Timeline button is in the bar of the state view)
    assert.equal(await page.locator('#header-view button').count(), 3);
    assert.ok(await page.isVisible('#device-button[aria-label="Device: desktop"] svg'));
    assert.ok(await page.isVisible('#docs-button[aria-label="Docs"] svg'));
    assert.ok(await page.isVisible('#state-button[aria-label="State view"] svg'));
    assert.equal(await page.isHidden('#state-view'), true);
    // every rule of the page styles in index-view html is read by the browser (a broken rule drops the rest)
    assert.ok(await page.evaluate(() => document.querySelector('#index-view style').sheet.cssRules.length) > 150);
    const boot = await page.evaluate(() => window.agentOS.calls.map(c => c.name));
    // (index-view renders header-view and recorder-view; recorder-view draws itself in its init, and after the start)
    assert.deepEqual(boot.sort(), ['extension.functions.get-state', 'extension.functions.render', 'extension.functions.render', 'extension.functions.render', 'loadState', 'local.init', 'local.init', 'local.init', 'local.refresh', 'local.refresh']);

    // outputs and performance are filled in on the functions that ran
    const init = await page.evaluate(() => window.agentOS.state.extension.views['index-view'].functions['local.init']);
    assert.equal(init.performance.count, 1);
    assert.deepEqual(init.errors, []);
    // output is what a function returned: get-state returns the JSON state, render returns nothing
    assert.deepEqual(Object.keys(init.calls['extension.functions.get-state'].output).sort(), ['functions', 'html', 'ui-data']);
    assert.deepEqual(init.calls['extension.functions.render'].output, {});
    assert.match(init.code, /^import ctx from 'ctx';\n\nasync function init\(\) \{/);
    assert.deepEqual(init.imports, { ctx: 'index.html' });

    // the tests written in the state pass, each checked against the state after it ran
    const results = await page.evaluate(() => window.agentOS.os.runTests());
    assert.ok(results.length >= 12, results.length);
    assert.deepEqual(results.filter(r => !r.ok), []);
    // (the tests chose blocks and changed the state view: no block, the filter empty, All, no Changes, no Details,
    // no Track state, the timeline hidden)
    await page.evaluate(async () => {
      const os = window.agentOS.os, sv = 'extension.views.state-view', d = os.get(sv + '.ui-data');
      await os.call('extension.views.timeline-view.functions.local.select', { id: null });
      await os.call(sv + '.functions.local.filter', { text: '' });
      await os.call(sv + '.functions.local.filter-kind', { kind: 'all' });
      if (d.changes) await os.call(sv + '.functions.local.toggle-changes', {});
      if (d.track_state) await os.call(sv + '.functions.local.toggle-tracking', {});
      if (d.timeline_open) await os.call(sv + '.functions.local.toggle-timeline', {});
    });
    for (const v of ['state-view', 'docs-view', 'timeline-view', 'notes-view'])
      await page.evaluate(v => window.agentOS.os.call('extension.functions.unmount', { view_path: 'extension.views.' + v }), v);

    // the Device button: Mobile, Tablet, Desktop. All the views show at that width, with the layout of that width.
    assert.equal(await page.evaluate(() => document.getElementById('index-view').dataset.device), undefined);
    await page.click('#device-button');
    assert.deepEqual(await page.$$eval('#device-menu button', b => b.map(x => x.firstChild.textContent + ':' + x.getAttribute('aria-checked'))),
      ['Mobile:false', 'Tablet:false', 'Desktop:true']);
    await page.click('#device-menu button:has-text("Mobile")');
    assert.equal(await page.isVisible('#device-menu'), false);
    const box = async s => page.locator(s).boundingBox();
    const vpw = page.viewportSize().width;
    assert.equal(Math.round((await box('#index-view')).width), 390);
    assert.equal(Math.round((await box('#header-view')).width), 390);
    // (the record button stays in the phone: its bottom right corner)
    const ivb = await box('#index-view'), rbm = await box('#rec-button');
    assert.ok(rbm.x + rbm.width <= ivb.x + ivb.width && rbm.x + rbm.width > ivb.x + ivb.width - 40, 'record button in the phone');
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data'].device), 'mobile');
    // (a narrow layout rule works at the width of the phone: the docs list is above the doc, not at its left)
    await page.click('#docs-button');
    await page.waitForSelector('#docs-view .docs');
    assert.equal(await page.evaluate(() => getComputedStyle(document.querySelector('#docs-view .docs')).gridTemplateColumns.split(' ').length), 1);
    await page.click('#docs-button');
    await page.click('#device-button');
    await page.click('#device-menu button:has-text("Tablet")');
    assert.equal(Math.round((await box('#index-view')).width), Math.min(820, vpw));
    // (a click out of the menu closes it)
    await page.click('#device-button');
    await page.mouse.click(5, 300);
    await page.waitForSelector('#device-menu', { state: 'detached' });
    await page.click('#device-button');
    await page.click('#device-menu button:has-text("Desktop")');
    assert.equal(await page.evaluate(() => document.getElementById('index-view').dataset.device), undefined);
    assert.equal(Math.round((await box('#index-view')).width), vpw);

    // the record button, at the bottom right: one click records audio, two clicks record video
    const rec = () => page.evaluate(() => window.agentOS.state.extension.views['recorder-view']['ui-data']);
    const recording = mode => page.waitForFunction(m => window.agentOS.state.extension.views['recorder-view']['ui-data'].recording === m, mode);
    await page.waitForSelector('#recorder-view #rec-button[aria-label="Record"]');
    const rb = await page.locator('#rec-button').boundingBox(), vp = page.viewportSize();
    assert.ok(rb.x + rb.width > vp.width - 40 && rb.y + rb.height > vp.height - 40, 'bottom right');
    await page.click('#rec-button');
    await recording('audio');
    assert.equal(await page.getAttribute('#rec-button', 'aria-label'), 'Stop recording');
    // the timer is in the header
    await page.waitForFunction(() => { const t = document.querySelector('#header-view #rec-timer'); return !t.hidden && /^Audio \d\d:\d\d$/.test(t.textContent); });
    // select mode: a click selects the element (the page does not get it) and its path shows above it
    await page.click('#docs-button');
    await page.waitForFunction(() => window.agentOS.state.extension.views['recorder-view']['ui-data'].selected === 'extension.views.header-view › #docs-button');
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data'].docs_open), false);
    await page.waitForSelector('.rec-label:not([hidden])');
    assert.equal(await page.textContent('.rec-label'), 'extension.views.header-view › #docs-button');
    // a click on the button stops it: the card plays it and lists what was selected
    await page.click('#rec-button');
    await page.waitForSelector('#rec-card audio');
    assert.match(await page.textContent('#rec-card .rec-sel'), /^\d\d:\d\dextension\.views\.header-view › #docs-button$/);
    assert.equal((await rec()).result.kind, 'audio');
    assert.ok(await page.evaluate(() => document.querySelector('#rec-timer').hidden));
    assert.ok(await page.evaluate(() => document.querySelector('.rec-label').hidden));
    // the keys: Arrow Up two times records audio; Arrow Up and Arrow Down together stop it, and again record video
    await page.keyboard.press('ArrowUp');
    await page.keyboard.press('ArrowUp');
    await recording('audio');
    const upDown = async () => { await page.keyboard.down('ArrowUp'); await page.keyboard.down('ArrowDown'); await page.keyboard.up('ArrowDown'); await page.keyboard.up('ArrowUp'); };
    await upDown();
    await recording('');
    await upDown();
    await recording('video');
    await upDown();
    await recording('');
    await page.waitForSelector('#rec-card video');
    // two clicks: the menu (1 Record audio, 2 Record video, 3 Notes); a click out of it closes it
    await page.dblclick('#rec-button');
    await page.waitForSelector('#rec-menu');
    assert.deepEqual(await page.$$eval('#rec-menu button', els => els.map(x => x.textContent)), ['1Record audio', '2Record video', '3Notes']);
    assert.equal((await rec()).recording, '');
    await page.mouse.click(200, 300);
    await page.waitForSelector('#rec-menu', { state: 'detached' });
    await page.dblclick('#rec-button');
    await page.click('#rec-menu button:has-text("Record video")');
    await recording('video');
    assert.equal((await rec()).menu_open, false);
    await page.waitForFunction(() => /^Video /.test(document.querySelector('#rec-timer').textContent));
    await page.click('#rec-button');
    await recording('');
    // the close button forgets the recording
    await page.click('#rec-close');
    await page.waitForSelector('#rec-card', { state: 'detached' });
    assert.equal((await rec()).result, null);
    // hold the button 4 s: the Notes page opens (empty for now); the click when you let go does not record
    await page.hover('#rec-button');
    await page.mouse.down();
    await page.waitForTimeout(3000);
    assert.equal(await page.isHidden('#notes-view'), true);
    await page.waitForSelector('#notes-view .notes-bar', { timeout: 3000 });
    await page.mouse.up();
    await page.waitForTimeout(450);
    assert.equal((await rec()).recording, '');
    assert.deepEqual(await page.$eval('#notes-view', e => { const r = e.getBoundingClientRect(); return [r.left, r.top, r.width, r.height]; }), await page.evaluate(() => [0, 0, innerWidth, innerHeight]));
    await page.click('#notes-close');
    await page.waitForFunction(() => document.querySelector('#notes-view').hidden);
    // Notes: each recording is a note (the newest first); Notes in the menu opens the page
    const nv = () => page.evaluate(() => window.agentOS.state.extension.views['notes-view']['ui-data']);
    assert.deepEqual((await nv()).notes.map(n => n.kind), ['video', 'video', 'audio', 'audio']);
    assert.equal((await nv()).notes[3].view_path, 'extension.views.header-view');
    assert.deepEqual((await nv()).notes[3].selections.map(x => x.path), ['extension.views.header-view › #docs-button']);
    await page.dblclick('#rec-button');
    await page.click('#rec-menu button:has-text("Notes")');
    await page.waitForSelector('#notes-view .note');
    assert.equal(await page.locator('#notes-view .note').count(), 4);
    assert.equal(await page.locator('#notes-view .note >> nth=3').locator('.note-media audio').count(), 1);
    assert.deepEqual(await page.locator('#notes-view .note >> nth=3').locator('.note-actions button').allTextContents(), ['Transcribe', 'Send now', 'Send now new session', 'Delete']);
    assert.equal(await page.textContent('#notes-view .note >> nth=3 >> .note-view code'), 'extension/views/header-view');
    // Transcribe: the text that the browser heard goes into the note, where you can change it
    await page.locator('#notes-view .note >> nth=3').locator('button:has-text("Transcribe")').click();
    await page.waitForSelector('#notes-view .note >> nth=3 >> .note-text');
    assert.equal(await page.inputValue('#notes-view .note >> nth=3 >> .note-text'), 'move the save button');
    await page.fill('#notes-view .note >> nth=3 >> .note-text', 'Move the Save button');
    await page.waitForFunction(() => window.agentOS.state.extension.views['notes-view']['ui-data'].notes[3].text === 'Move the Save button');
    // a note that you write: it has no Transcribe
    await page.fill('#notes-new', 'The docs need a search');
    await page.click('#notes-add');
    await page.waitForFunction(() => document.querySelectorAll('#notes-view .note').length === 5);
    assert.equal(await page.inputValue('#notes-view .note >> nth=0 >> .note-text'), 'The docs need a search');
    assert.equal(await page.locator('#notes-view .note >> nth=0').locator('button:has-text("Transcribe")').count(), 0);
    assert.equal(await page.inputValue('#notes-new'), '');
    // Show state: the ui-data of the note's view
    await page.locator('#notes-view .note >> nth=0').locator('button:has-text("Show state")').click();
    await page.waitForSelector('#notes-view .note-state');
    assert.deepEqual(JSON.parse(await page.textContent('#notes-view .note-state')), await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data']));
    await page.locator('#notes-view .note >> nth=0').locator('button:has-text("Hide state")').click();
    await page.waitForSelector('#notes-view .note-state', { state: 'detached' });
    // Send now: a comment sent to Claude; Send selected: the checked notes together
    await page.locator('#notes-view .note >> nth=0').locator('button:has-text("Send now")').first().click();
    await page.waitForFunction(() => window.__sent.length === 1);
    assert.match(await page.evaluate(() => window.__sent[0].text), /^A note from the Notes page of Agent OS:\n\nNote, .*\nThe docs need a search\nView: extension\.views\.header-view$/);
    assert.equal(await page.textContent('#notes-msg'), 'The note went to Claude.');
    assert.equal(await page.isDisabled('#notes-send-selected'), true);
    await page.locator('#notes-view .note >> nth=0').locator('.note-pick').check();
    // (the note that you wrote is the first one now: the recording with its text is the fifth)
    await page.locator('#notes-view .note >> nth=4').locator('.note-pick').check();
    await page.click('#notes-send-selected');
    await page.waitForFunction(() => window.__sent.length === 2);
    assert.match(await page.evaluate(() => window.__sent[1].text), /^2 notes .*The docs need a search.*Move the Save button\nView: extension\.views\.header-view\nSelected at \d\d:\d\d: extension\.views\.header-view › #docs-button$/s);
    // Send now new session: the task of the settings, through Claude Code Remote
    await page.locator('#notes-view .note >> nth=0').locator('button:has-text("Send now new session")').click();
    await page.waitForFunction(() => /No task for new sessions/.test(document.querySelector('#notes-msg').textContent));
    await page.click('#notes-settings-button');
    await page.fill('#notes-task', 'trig_test');
    await page.press('#notes-task', 'Tab');
    await page.waitForFunction(() => window.agentOS.state.extension.views['notes-view']['ui-data'].settings.new_session_task === 'trig_test');
    await page.click('#notes-settings-button');
    await page.locator('#notes-view .note >> nth=0').locator('button:has-text("Send now new session")').click();
    await page.waitForFunction(() => window.__sent.length === 3);
    assert.deepEqual(await page.evaluate(() => [window.__sent[2].to, window.__sent[2].tool, window.__sent[2].input.trigger_id]), ['Claude Code Remote', 'fire_trigger', 'trig_test']);
    // Settings: Transcription is Browser by default; Off and the language go to the state
    await page.click('#notes-settings-button');
    await page.waitForSelector('#notes-settings');
    assert.equal(await page.inputValue('#notes-transcribe'), 'browser');
    await page.selectOption('#notes-transcribe', 'off');
    await page.waitForFunction(() => window.agentOS.state.extension.views['notes-view']['ui-data'].settings.transcribe === 'off');
    await page.fill('#notes-lang', 'ru-RU');
    await page.press('#notes-lang', 'Tab');
    await page.waitForFunction(() => window.agentOS.state.extension.views['notes-view']['ui-data'].settings.lang === 'ru-RU');
    await page.selectOption('#notes-transcribe', 'browser');
    await page.fill('#notes-lang', '');
    await page.press('#notes-lang', 'Tab');
    await page.click('#notes-settings-button');
    // Delete: all the notes go
    while (await page.locator('#notes-view .note').count()) {
      const n = await page.locator('#notes-view .note').count();
      await page.locator('#notes-view .note >> nth=0').locator('button:has-text("Delete")').click();
      await page.waitForFunction(n => document.querySelectorAll('#notes-view .note').length === n - 1, n);
    }
    await page.evaluate(() => { window.agentOS.state.extension.views['notes-view']['ui-data'].message = ''; });
    await page.evaluate(() => window.agentOS.os.call('extension.views.notes-view.functions.local.set-settings', { new_session_task: '' }));
    await page.waitForSelector('#notes-view .notes-empty');
    await page.click('#notes-close');
    await page.waitForFunction(() => document.querySelector('#notes-view').hidden);
    // a short press is still a click: audio
    await page.click('#rec-button');
    await recording('audio');
    await page.click('#rec-button');
    await recording('');
    await page.click('#rec-close');
    await page.waitForSelector('#rec-card', { state: 'detached' });

    // the docs button lists the docs folder of the agent; a click shows a doc
    await page.click('#docs-button');
    assert.equal(await page.locator('#docs-view .doc-link').count(), 4);
    await page.click('#docs-view .doc-link:has-text("render-steps.md")');
    assert.equal(await page.textContent('#docs-view .doc h2'), 'How the page renders from the state');
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['docs-view']['ui-data'].selected), 'render-steps.md');
    assert.ok(await page.locator('#docs-view .doc pre.code').count() >= 5);
    assert.match(await page.textContent('#docs-view .doc pre.code >> nth=1'), /^import os from 'os';\nimport ctx from 'ctx';\n\nasync function render\(\{ view_path \}\) \{/);
    await page.click('#docs-view .doc-link:has-text("how-it-works.md")');
    assert.ok(await page.isVisible('#docs-view .doc .diagram svg'));
    assert.equal(await page.locator('#docs-view .doc .diagram svg text.num').count(), 7);
    await page.click('#docs-button');
    assert.equal(await page.isHidden('#docs-view'), true);

    // the state view: the one view for the state and its changes; the Timeline button is at the left of its bar
    const tl = () => page.evaluate(() => window.agentOS.state.extension.views['timeline-view']['ui-data']);
    const svd = () => page.evaluate(() => window.agentOS.state.extension.views['state-view']['ui-data']);
    const blockNames = () => page.$$eval('#tl-strip .tl-step .tl-step-name', els => els.map(x => x.textContent));
    const shownBlock = () => page.textContent('#sv-block');
    await page.click('#state-button');
    await page.waitForSelector('#state-view .CodeMirror');
    assert.equal(await page.getAttribute('#state-button', 'aria-pressed'), 'true');
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data'].state_open), true);
    assert.equal(await page.textContent('#path'), 'extension/views/state-view');
    assert.match(await page.textContent('#pos'), /^v1 (just now|\d+ min ago)$/);
    // the bar: the Timeline button, the kind buttons, Changes and Details; the filter with Show empty and Track state;
    // then icon buttons, older and newer at the end
    assert.equal(await page.locator('#state-view .sv-bar #sv-switches > #timeline-button:first-child svg').count(), 1);
    assert.deepEqual(await page.$$eval('#state-view .sv-bar #sv-switches .st-kind', els => els.map(b => b.textContent.trim())), ['All', 'Files', 'Views', 'Functions', 'Network', 'Environment', 'Changes', 'Details']);
    assert.deepEqual(await page.$$eval('#state-view .sv-bar #sv-checks label', els => els.map(b => b.textContent.trim())), ['Show empty', 'Track state']);
    assert.deepEqual(await page.$$eval('#state-view .sv-bar #sv-right button', els => els.map(b => b.id)), ['collapse', 'save', 'older', 'newer']);
    assert.equal(await page.evaluate(() => [...document.querySelectorAll('#state-view .sv-bar #sv-right button')].filter(b => b.textContent.trim()).length), 0);
    assert.equal(await page.locator('#state-view .sv-foot #pos').count(), 1);
    assert.equal(await page.locator('#state-view .sv-bar #path').count(), 0);
    assert.equal(await page.isChecked('#sv-track'), false);
    // no block chosen: the state view shows the last agent run (block 1)
    await page.waitForFunction(() => /^Block 1: AI run notification session /.test(document.querySelector('#sv-block').textContent));

    // the timeline: hidden until its button; then its blocks at the top of the page, above the header
    assert.equal(await page.isHidden('#timeline-view'), true);
    await page.click('#timeline-button');
    await page.waitForSelector('#tl-strip .tl-step');
    assert.equal((await svd()).timeline_open, true);
    assert.equal(await page.getAttribute('#timeline-button', 'aria-pressed'), 'true');
    assert.ok(await page.evaluate(() => document.querySelector('#timeline-view').compareDocumentPosition(document.querySelector('#header-view')) & Node.DOCUMENT_POSITION_FOLLOWING));
    const stepKinds = await page.$$eval('#tl-strip .tl-step .tl-kind', els => els.map(x => x.textContent));
    // the last agent run comes first (runs/ of the repo), then the page start
    assert.deepEqual(stepKinds.slice(0, 5), ['Last AI run notification', 'Network', 'Run index.html', 'Load the state', 'Start the page']);
    // the newest block is the last one: Last click, ...; the agent run block shows only the time ago
    assert.match(stepKinds[stepKinds.length - 1], /^Last [a-z]/);
    assert.match(await page.textContent('#tl-strip .tl-step.pin-left .tl-time'), /^(just now|\d+ (min|h|d) ago)$/);
    // (no Changes button and no Track box in the timeline)
    assert.equal(await page.locator('#tl-changes, #tl-track').count(), 0);
    assert.equal(await page.locator('#tl-strip .tl-step.on.pin-left').count(), 1);
    // when the row scrolls, the last agent run stays at the left and the newest block at the right
    assert.equal(await page.locator('#tl-strip .tl-step:last-child.pin-right').count(), 1);
    await page.evaluate(() => { const s = document.querySelector('#tl-strip'); s.style.scrollSnapType = 'none'; s.scrollLeft = (s.scrollWidth - s.clientWidth) / 2; });
    await page.waitForTimeout(100);
    const inSight = await page.evaluate(() => {
      const s = document.querySelector('#tl-strip').getBoundingClientRect(), a = document.querySelector('.tl-step.pin-left').getBoundingClientRect(), b = document.querySelector('.tl-step.pin-right').getBoundingClientRect();
      return [a.left >= s.left - 1 && a.right <= s.right + 1, b.left >= s.left - 1 && b.right <= s.right + 1, document.querySelector('#tl-strip').scrollWidth > s.width];
    });
    assert.deepEqual(inSight, [true, true, true]);

    // the AI run notification block: Details has three tabs, Index, Details and Steps
    const runs = await page.evaluate(() => Object.keys(window.agentOS.state.agents['agent-oss'].files.runs).sort());
    const lastRun = await page.evaluate(n => JSON.parse(window.agentOS.state.agents['agent-oss'].files.runs[n]), runs[runs.length - 1]);
    await page.locator('#tl-strip .tl-step').first().click();
    assert.equal((await tl()).selected, 'run:runs/' + runs[runs.length - 1]);
    await page.click('#details');
    await page.waitForSelector('#tl-detail .ar-views');
    assert.equal((await svd()).details, true);
    assert.equal(await page.getAttribute('#details', 'aria-pressed'), 'true');
    assert.equal(await page.isHidden('#sv-editor'), true);
    assert.match(await shownBlock(), new RegExp('^Block 1: AI run notification session ' + lastRun.session.slice(0, 3) + ' · run ' + lastRun.run + ' · '));
    assert.deepEqual(await page.$$eval('#tl-detail .ar-views button', els => els.map(x => x.textContent)), ['Index', 'Details', 'Steps']);
    // Index: the title, the summary, the actions for you, the chips, what started each part, the uses and the context
    assert.equal(await page.getAttribute('#tl-detail .ar-views [data-view="index"]', 'aria-selected'), 'true');
    assert.equal(await page.textContent('#tl-detail .ar-index h3'), lastRun.title);
    if (lastRun.summary) assert.equal(await page.textContent('#tl-detail .ar-summary'), lastRun.summary);
    if (lastRun.actions && lastRun.actions.length) assert.deepEqual(await page.$$eval('#tl-detail .ar-actions li', els => els.map(x => x.textContent)), lastRun.actions);
    else assert.match(await page.textContent('#tl-detail .ar-actions'), /^No action needed/);
    assert.ok(await page.locator('#tl-detail .ar-index .ar-head .tl-chip', { hasText: 'run ' + lastRun.run }).count() === 1);
    assert.deepEqual(await page.$$eval('#tl-detail .ar-why:not(.ar-info) dt', els => els.map(x => x.textContent)),
      ['What started this session', 'What started this run', 'What started this workflow', 'What started the subagents', 'What started the skills', 'MCP use', 'Skill use', 'Subagents', 'Workflow', 'Context']);
    // Details: one tree of what the run changed (green, yellow, red) and read (blue), with who did it
    await page.click('#tl-detail .ar-views [data-view="details"]');
    await page.waitForSelector('#tl-detail .ar-kv');
    assert.match(await page.textContent('#tl-detail .ar-scope'), /^The whole run/);
    const changed = lastRun.files.filter(f => f.action !== 'read'), read = lastRun.files.filter(f => f.action === 'read' && !changed.some(c => c.path === f.path));
    assert.match(await page.textContent('#tl-detail .ar-legend'), /^added \d+updated \d+deleted \d+read \d+$/);
    // the files are a tree of folders under Files/
    const top = changed.find(f => /^[^/]+\//.test(f.path)).path.split('/')[0];
    assert.equal(await page.locator('#tl-detail .ar-kv .kv-tree summary', { hasText: new RegExp('^' + top.replace('.', '\\.') + '/$') }).count(), 1);
    const titles = await page.$$eval('#tl-detail .ar-kv .kv-item', els => els.map(x => x.title));
    for (const f of changed.slice(0, 3)) assert.ok(titles.some(t => t.startsWith(f.path + ' (') && !t.endsWith('(read)')), f.path);
    for (const f of read.slice(0, 3)) assert.ok(titles.some(t => t === f.path + ' (read)'), f.path);
    assert.ok(await page.locator('#tl-detail .ar-kv .kv-item.read').count() >= 1);
    // the buttons show only what the main agent, a subagent or an MCP call did
    const subLanes = [...new Set(lastRun.steps.map(x => x.lane || 'main'))].filter(l => l !== 'main');
    assert.equal(await page.getAttribute('#tl-detail .ar-by [data-by="all"]', 'aria-pressed'), 'true');
    if (subLanes.length) {
      await page.click('#tl-detail .ar-by [data-by="subagent"]');
      assert.equal(await page.getAttribute('#tl-detail .ar-by [data-by="subagent"]', 'aria-pressed'), 'true');
      assert.ok((await page.$$eval('#tl-detail .ar-kv .kv-item', els => els.map(x => x.querySelector('.src') ? 1 : 0))).every(Boolean));
      await page.click('#tl-detail .ar-by [data-by="all"]');
    }
    // a click on an item shows why: who did it, in which steps
    await page.locator('#tl-detail .ar-kv .kv-item').first().click();
    await page.click('#tl-detail .ar-kv .kv-tabs button:has-text("Why")');
    assert.match(await page.textContent('#tl-detail .ar-kv .kv-main .ar-info'), /By.*Steps/s);
    // Steps: the lanes (the start card, a card for each step; a subagent has its own lane), then the steps one by one
    await page.click('#tl-detail .ar-views [data-view="steps"]');
    await page.waitForSelector('#tl-detail .ar-lanes');
    assert.match(await page.textContent('#tl-detail .ar-card.start'), new RegExp('Run ' + lastRun.run));
    assert.equal(await page.locator('#tl-detail .ar-card:not(.start)').count(), lastRun.steps.length);
    assert.equal(await page.locator('#tl-detail .ar-lane.sub').count(), subLanes.length);
    if (subLanes.length) assert.match(await page.textContent('#tl-detail .ar-lane.sub .ar-branch'), new RegExp('^' + subLanes[0] + ' is a subagent'));
    assert.deepEqual(await page.$$eval('#tl-detail .ar-flow-step b', els => els.map(x => x.textContent)), lastRun.steps.map(x => x.title));
    // a click on a step opens it: what it did, and its files; Details then shows only that step
    const k = lastRun.steps.findIndex(x => (x.files || []).filter(f => f.action !== 'read').length > 1);
    await page.click('#tl-detail .ar-card.step[data-step="' + k + '"]');
    assert.equal(await page.locator('#tl-detail .ar-card.step.on').count(), 1);
    assert.equal(await page.locator('#tl-detail .ar-flow-step.on').count(), 1);
    assert.equal(await page.locator('#tl-detail .ar-flow-step.on .ar-items li').count(), lastRun.steps[k].items.length);
    await page.click('#tl-detail .ar-flow-step.on .ar-to-details');
    await page.waitForSelector('#tl-detail .ar-kv');
    assert.match(await page.textContent('#tl-detail .ar-scope'), new RegExp('^Step ' + (k + 1) + ': '));
    const own = lastRun.steps[k].files.filter(f => f.action !== 'read');
    assert.deepEqual((await page.$$eval('#tl-detail .ar-kv .kv-item', els => els.map(x => x.title))).filter(t => !t.startsWith('mcp ') && / \((created|updated|deleted)\)$/.test(t)).map(t => t.replace(/ \(\w+\)$/, '')).sort(), [...new Set(own.map(f => f.path))].sort());
    await page.click('#tl-detail .ar-scope .ar-whole');
    assert.match(await page.textContent('#tl-detail .ar-scope'), /^The whole run/);
    await page.click('#tl-detail .ar-views [data-view="index"]');
    // its Changes: from the version before the run to the version it made (this page has only v1)
    await page.click('#changes');
    await page.waitForFunction(() => /The run made v\d+\./.test(document.querySelector('#tl-detail').textContent));
    assert.deepEqual([(await svd()).changes, (await svd()).details], [true, false]);

    // a click on a block: the state view shows it; with Track state off the click is not a block
    const before = await blockNames();
    await page.locator('#tl-strip .tl-step').nth(1).click();
    await page.waitForFunction(() => /^Block 2: Network/.test(document.querySelector('#sv-block').textContent));
    assert.equal((await tl()).selected, 'open');
    assert.deepEqual(await blockNames(), before);
    // (no block chosen again: the last agent run)
    await page.evaluate(() => window.agentOS.os.call('extension.views.timeline-view.functions.local.select', { id: null }));
    await page.waitForFunction(() => /^Block 1: AI run notification/.test(document.querySelector('#sv-block').textContent));
    await page.locator('#tl-strip .tl-step').nth(1).click();
    await page.waitForFunction(() => /^Block 2: Network/.test(document.querySelector('#sv-block').textContent));

    // network and environment are in the state; block 2 shows what changed in them since the version this page loaded
    const st0 = await page.evaluate(() => window.agentOS.state);
    assert.equal(st0.network.scripts['state-core.js'].expected, true);
    assert.equal(typeof st0.network.scripts['state-core.js'].ms, 'number');
    assert.ok(st0.network.scripts['state-core.js'].size > 1000);
    assert.equal(st0.network.api['read the versions'].count, 1);
    assert.ok(st0.network.packages['codemirror.js'].count >= 1);
    assert.equal(st0.environment['browser data'].storages['local storage'].limit, 'about 5 MB (the usual limit of a browser)');
    assert.equal(typeof st0.environment.browser.viewport, 'string');
    assert.equal(st0.environment['browser data'].storages['claude.ai database']['versions (commits)'].documents, 1);
    assert.match(st0.environment['browser data'].storages['claude.ai database'].limits, /256 KB/);
    assert.equal(typeof st0.environment.browser.cpu_cores, 'number');
    assert.equal(typeof st0.environment.browser.gpu, 'string');
    // everything the code registered, with who added it
    const env0 = await page.evaluate(() => window.agentOS.state.environment);
    assert.ok(env0['event listeners']['#sv-filter-input'].input.by.includes('local.init'), JSON.stringify(env0['event listeners']['#sv-filter-input']));
    assert.ok(env0['event listeners'].document.keydown.count >= 1);
    assert.equal(env0.document.title, 'Agent OS');
    assert.ok(env0.document.elements > 50);
    assert.equal(typeof env0.window.history_length, 'number');
    assert.ok('timeouts waiting' in env0.timers && 'intervals' in env0.timers);
    assert.ok(Array.isArray(env0.connections));
    assert.ok('geolocation' in env0.permissions && 'battery' in env0.devices);
    // a listener added in a call is a change of that call
    await page.evaluate(() => window.agentOS.os.call('extension.views.state-view.functions.local.filter', { text: '' }));
    await page.evaluate(() => { window.__probe = () => {}; document.body.addEventListener('dblclick', window.__probe); });
    await page.evaluate(() => window.agentOS.os.call('extension.views.state-view.functions.local.filter', { text: '' }));
    assert.deepEqual(await page.evaluate(() => window.agentOS.state.environment['event listeners'].body.dblclick), { count: 1, by: ['the page (no call)'] });
    // its Changes: the state cut down to the changes, with which function changed what
    await page.waitForFunction(() => /changes? in the state, made by /.test(document.querySelector('#tl-detail').textContent));
    assert.match(await page.locator('#tl-detail .tl-code').first().evaluate(e => e.cm.getValue()), /"network"/);
    assert.match(await page.textContent('#tl-detail .tl-table'), /network\.scripts\.state-core\.js\.ms.*loadState/);
    // the filter of the state view works on the changes too
    await page.fill('#sv-filter-input', 'state-core');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter === 'state-core');
    await page.waitForSelector('#tl-detail .sv-hidden');
    assert.ok((await page.$$eval('#tl-detail .tl-table tr', rows => rows.slice(1).map(r => r.textContent))).every(t => t.includes('state-core')));
    await page.fill('#sv-filter-input', '');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter === '');
    // one kind shows in its own view, a tree of all of them on the left, the chosen one on the right
    await page.click('#sv-switches [data-input*="environment"]');
    await page.waitForSelector('#sv-switches [data-input*="environment"][aria-pressed="true"]');
    assert.equal((await svd()).filter_kind, 'environment');
    await page.waitForSelector('#tl-detail .kv .kv-tree .kv-item');
    assert.ok((await page.$$eval('#tl-detail .kv-item', els => els.map(x => x.textContent))).includes('event listeners'));
    // a changed item opens first, on its Value; Changes shows what changed in it
    assert.ok(await page.locator('#tl-detail .kv-item.on.updated, #tl-detail .kv-item.on.added').count() === 1);
    assert.deepEqual(await page.$$eval('#tl-detail .kv-tabs button', els => els.map(x => x.textContent)), ['Value', 'Changes']);
    await page.click('#tl-detail .kv-tabs button:has-text("Changes")');
    await page.waitForSelector('#tl-detail .kv-main .st-legend');
    await page.locator('#tl-detail .kv-item', { hasText: /^document$/ }).click();
    assert.match(await page.textContent('#tl-detail .kv-head'), /^environment\.document/);
    await page.click('#sv-switches [data-input*="all"]');
    await page.waitForSelector('#sv-switches [data-input*="all"][aria-pressed="true"]');
    await page.waitForSelector('#tl-detail .st-legend');
    // updated values show the old value
    assert.ok(await page.$('#tl-detail .tl-code .was'));

    // its Details: Network (all requests, in groups) next to Environment
    await page.click('#details');
    await page.waitForSelector('#tl-detail .tl-netenv .tl-panel');
    assert.equal((await svd()).details, true);
    assert.deepEqual(await page.$$eval('#tl-detail .tl-netenv .tl-panel h3', els => els.map(x => x.textContent)), ['Network (all requests)', 'Environment']);
    const groups = await page.$$eval('#tl-detail .tl-netenv .tl-panel:first-child h4', els => els.map(x => x.textContent.split(' · ')[0]));
    for (const g of ['Html', 'Our scripts', 'API', 'State', 'Packages']) assert.ok(groups.includes(g), groups.join(' | '));
    const req = name => page.locator('#tl-detail .tl-req', { has: page.locator('.tl-req-top b', { hasText: new RegExp('^' + name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '$') }) }).first();
    assert.match(await req('state-core.js').textContent(), /time: last — · now \d+ ms.*expected.*Used for: The library of the runtime/);
    assert.match(await req('read the versions').textContent(), /db\.collection\('commits'\)\.orderBy\('n'\)\.get\(\)/);
    // a request opens its code on click
    await req('state-core.js').locator('.tl-req-top').click();
    await req('state-core.js').locator('.tl-code').waitFor();
    assert.match(await req('state-core.js').locator('.tl-code').first().evaluate(e => e.cm.getValue()), /StateCore/);
    // a file the browser does not let the page download as text says why, with a link
    await page.route('**/vendor/codemirror/5.65.16/mode/xml/xml.js', route => route.request().resourceType() === 'fetch' ? route.abort() : route.fallback());
    await req('xml.js').locator('.tl-req-top').click();
    await req('xml.js').locator('.tl-error').waitFor();
    assert.match(await req('xml.js').locator('.tl-error').textContent(), /could not download this file as text.*Open the file in a new tab/);
    assert.match(await req('xml.js').locator('.tl-error a').getAttribute('href'), /vendor\/codemirror\/5\.65\.16\/mode\/xml\/xml\.js$/);
    assert.match(await page.textContent('#tl-detail .tl-netenv .tl-panel:last-child'), /browser data \/ storages \/ local storage|storages \/ local storage \/ limit/);
    const part = name => page.locator('#tl-detail .tl-part', { has: page.locator('.tl-name', { hasText: name }) });
    await page.click('#tl-next');
    await page.waitForFunction(() => /^Block 3: Run index\.html/.test(document.querySelector('#sv-block').textContent));
    assert.match(await page.textContent('#tl-detail'), /a name for this page load: s\w+/);
    await part('Run the runtime script').locator('.tl-call-head').click();
    assert.match(await part('Run the runtime script').locator('.tl-table').textContent(), /loadState/);
    assert.match(await part('Run the runtime script').locator('.tl-code').first().evaluate(e => e.cm.getValue()), /window\.agentOS = \{/);
    // each part says what happens and why, and shows the lines of index.html that do it
    assert.match(await part('Note the start time').textContent(), /What happens The runtime writes down when it started.*Why Only the timeline uses it/);
    await part('Note the start time').locator('.tl-call-head').first().click();
    await part('Note the start time').locator('.tl-code').first().waitFor();
    assert.match(await part('Note the start time').locator('.tl-file-head').first().textContent(), /^index\.html, line \d+/);
    assert.match(await part('Note the start time').locator('.tl-code').first().evaluate(e => e.cm.getValue()), /var startedAt=performance\.now\(\);/);
    await part('Create the call tracker').locator('.tl-call-head').click();
    assert.match(await part('Create the call tracker').locator('.tl-table').textContent(), /extension\.functions\.render/);
    // Build os: each part of os opens with the functions that use it and its code, the runtime's call() too
    await part('Build os').locator('.tl-call-head').first().click();
    const osCall = page.locator('#tl-detail .tl-more .tl-part', { has: page.locator(':scope > .tl-call-head .tl-name', { hasText: /^os\.call$/ }) });
    await osCall.locator(':scope > .tl-call-head').click();
    assert.match(await osCall.locator(".tl-table").textContent(), /extension\.functions\.render\d+ times/);
    assert.match(await osCall.locator('.tl-code').first().evaluate(e => e.cm.getValue()), /function call\(name, input, viewPath, parent, via\)/);

    // the replay moves to the next block every 1.6 s
    assert.equal((await tl()).selected, 'runtime');
    await page.click('#tl-play');
    await page.waitForFunction(() => window.agentOS.state.extension.views['timeline-view']['ui-data'].selected !== 'runtime', null, { timeout: 5000 });
    assert.equal((await tl()).playing, true);
    await page.click('#tl-play');
    await page.waitForFunction(() => !window.agentOS.state.extension.views['timeline-view']['ui-data'].playing);
    assert.deepEqual(await blockNames(), before);

    // the blocks button hides the row of blocks
    await page.click('#tl-blocks');
    await page.waitForFunction(() => document.querySelector('#tl-strip').hidden);
    await page.click('#tl-blocks');
    await page.waitForFunction(() => !document.querySelector('#tl-strip').hidden);
    // Flows: the saved flows; First enter plays the first 4 blocks and stops
    await page.click('#tl-flows');
    await page.waitForSelector('#tl-flows-list:not([hidden]) .tl-flow');
    assert.match(await page.textContent('#tl-flows-list'), /First enter4 blocks: network, runtime, loadState, extension\.functions\.render/);
    await page.click('#tl-flows-list .tl-flow button');
    await page.waitForFunction(() => document.querySelector('#tl-flows-list').hidden);
    assert.equal((await tl()).selected, 'open');
    assert.match(await page.textContent('#tl-pos'), /^First enter: block 1 of 4/);
    await page.waitForFunction(() => /^First enter: block 4 of 4/.test(document.querySelector('#tl-pos').textContent), null, { timeout: 8000 });
    await page.waitForFunction(() => !window.agentOS.state.extension.views['timeline-view']['ui-data'].playing);
    assert.match(await shownBlock(), /^Block \d+: Start the page/);

    // Track state: what you do in the state view and the timeline is added as blocks
    await page.click('#sv-track');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].track_state === true);
    assert.ok((await blockNames()).includes('local.toggle-tracking'));
    await page.locator('#tl-strip .tl-step').first().click();
    await page.waitForFunction(() => Array.from(document.querySelectorAll('#tl-strip .tl-step-name')).some(x => x.textContent === 'local.select'));
    await page.click('#sv-track');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].track_state === false);
    assert.equal((await blockNames()).includes('local.select'), false);

    // the block of the State button click: Changes shows the state cut down to what it changed, and who changed it
    await page.locator('#tl-strip .tl-step', { has: page.locator('.tl-step-name', { hasText: 'local.open.state-view' }) }).last().click();
    await page.waitForFunction(() => /local\.open\.state-view/.test(document.querySelector('#sv-block').textContent));
    await page.click('#changes');
    await page.waitForSelector('#tl-detail .st-legend');
    assert.match(await page.locator('#tl-detail .tl-code').first().evaluate(e => e.cm.getValue()), /"state_open": true/);
    assert.ok(await page.locator('#tl-detail .tl-code .chg-updated').count() > 0);
    assert.match(await page.locator('#tl-detail .tl-table').textContent(), /extension\.views\.header-view\.ui-data\.state_openfalse {2}→ {2}truelocal\.open\.state-view/);
    // its Details: each call says what it does and why it ran, its name opens its code, and what it changed
    await page.click('#details');
    await page.locator('#tl-detail .tl-call').first().waitFor();
    assert.deepEqual((await page.locator('#tl-detail .tl-call .tl-name').allTextContents()).slice(0, 2), ['local.open.state-view', 'extension.functions.render']);
    assert.match(await page.locator('#tl-detail .tl-call').first().textContent(), /Why it ran You clicked a button of header-view/);
    await page.locator('#tl-detail .tl-call').first().locator('.tl-call-head').first().click();
    assert.match(await page.locator('#tl-detail .tl-call').first().locator('.tl-code').first().evaluate(e => e.cm.getValue()), /async function openStateView/);
    assert.ok((await page.locator('#tl-detail .tl-change').allTextContents()).includes('extension.views.header-view.ui-data.state_open' + 'false  →  true'));
    // the Timeline button hides the timeline; the state view keeps the block
    await page.click('#timeline-button');
    await page.waitForFunction(() => document.querySelector('#timeline-view').hidden);
    assert.equal((await svd()).timeline_open, false);
    assert.match(await shownBlock(), /local\.open\.state-view/);
    // back to the editor: Details and Changes off
    await page.click('#details');
    await page.waitForFunction(() => !window.agentOS.state.extension.views['state-view']['ui-data'].details);
    await page.click('#changes');
    await page.waitForFunction(() => !window.agentOS.state.extension.views['state-view']['ui-data'].changes);
    assert.equal(await page.isHidden('#tl-detail'), true);
    assert.equal(await page.isVisible('#sv-editor'), true);

    // the filter shows only the paths that have the text
    const shownText = () => page.evaluate(() => [...document.querySelectorAll('#sv-editor .CodeMirror-line')].map(l => l.textContent).join('\n'));
    const hiddenMarks = () => page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().filter(m => m.replacedWith && m.replacedWith.classList.contains('sv-hidden')).length);
    if (!(await svd()).show_empty) {
      await page.click('#sv-empty');
      await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].show_empty);
    }
    assert.equal(await page.locator('#sv-results').count(), 0);
    assert.equal(await hiddenMarks(), 0);
    await page.fill('#sv-filter-input', 'docs/render-steps');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter === 'docs/render-steps');
    await page.locator('#sv-editor .sv-hidden').first().waitFor();
    let shown = await shownText();
    assert.match(shown, /"agents"/);
    assert.match(shown, /"render-steps\.md"/);
    assert.doesNotMatch(shown, /"extension"/);
    assert.match(await page.textContent('#sv-editor .sv-hidden'), /^⋯ \d+ lines?$/);
    // Functions: a tree of the functions; the text is in no function
    await page.click('#sv-switches [data-input*="functions"]');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter_kind === 'functions');
    assert.equal(await page.getAttribute('#sv-switches [data-input*="functions"]', 'aria-pressed'), 'true');
    assert.equal(await page.getAttribute('#sv-switches [data-input*="all"]', 'aria-pressed'), 'false');
    assert.equal(await page.isHidden('#sv-editor'), true);
    assert.match(await page.textContent('#tl-detail'), /No functions have the filter text/);
    await page.press('#sv-filter-input', 'Escape');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter === '');
    await page.waitForSelector('#tl-detail .kv-tree .kv-item');
    assert.match(await page.textContent('#tl-detail > .tl-text'), /^\d+ functions in the state of v1\. Choose one on the left\.$/);
    assert.ok((await page.$$eval('#tl-detail .kv-item', els => els.map(x => x.textContent))).includes('get-state'));
    // Files: the files in their folders, a tree; a click shows the file on the right
    await page.click('#sv-switches [data-input*="files"]');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter_kind === 'files');
    await page.waitForSelector('#tl-detail .kv-tree summary');
    assert.equal(await page.locator('#tl-detail .kv-tree summary', { hasText: /^docs\/$/ }).count(), 1);
    await page.locator('#tl-detail .kv-item', { hasText: /^render-steps\.md$/ }).click();
    await page.waitForSelector('#tl-detail .fv.fv-md .md-page');
    assert.deepEqual(await page.$$eval('#tl-detail .kv-tabs button', els => els.map(x => x.textContent)), ['File']);
    await page.click('#sv-switches [data-input*="all"]');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].filter_kind === 'all');
    assert.equal(await page.isVisible('#sv-editor'), true);
    assert.equal(await hiddenMarks(), 0);
    // Show empty off hides the entries with an empty value ({} here), with no "⋯ N lines" mark
    assert.match(await shownText(), /"connection": \{\}/);
    // a text of only {} (an empty json file) shows as it is, not as "...", and it is empty too
    assert.match(await shownText(), /"settings\.local\.json": "\{\}\\n"/);
    await page.click('#sv-empty');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].show_empty === false);
    assert.equal(await page.isChecked('#sv-empty'), false);
    assert.doesNotMatch(await shownText(), /"connection": \{\}/);
    assert.doesNotMatch(await shownText(), /settings\.local\.json/);
    assert.equal(await hiddenMarks(), 0);
    assert.equal(await page.locator('#sv-editor .sv-hidden').count(), 0);
    await page.click('#sv-empty');
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].show_empty);
    assert.equal(await hiddenMarks(), 0);

    // the editor follows the live state: ui-data and runtime fills show up, comments stay
    shown = await page.evaluate(() => JSON.parse(document.querySelector('.CodeMirror').CodeMirror.getValue()));
    assert.equal(shown.extension.views['header-view']['ui-data'].state_open, true);
    assert.equal(shown.extension.views['state-view']['ui-data'].version, 'v1');

    // long strings show "…"; html opens in the html viewer, rendered with the view's ui-data
    const marks = await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().filter(m => m.replacedWith).map(m => m.replacedWith.title));
    assert.ok(marks.includes('agents/agent-oss/files/.claude/settings.json') && marks.includes('agents/agent-oss/files/.claude/CLAUDE.md') && marks.includes('agents/agent-oss/files/docs/how-it-works.md'), marks.join(' | '));
    // the pointer on "..." shows the start of the text, in the colors of its kind (md here)
    await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().find(m => m.replacedWith && m.replacedWith.title === 'agents/agent-oss/files/.claude/CLAUDE.md')
      .replacedWith.dispatchEvent(new MouseEvent('mouseenter')));
    await page.waitForSelector('.long-tip:not([hidden]) .CodeMirror');
    assert.match(await page.evaluate(() => document.querySelector('.long-tip .CodeMirror').CodeMirror.getValue()), /^# Agent OS/);
    assert.ok(await page.locator('.long-tip .cm-header').count() > 0);
    await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().find(m => m.replacedWith && m.replacedWith.title === 'agents/agent-oss/files/.claude/CLAUDE.md')
      .replacedWith.dispatchEvent(new MouseEvent('mouseleave')));
    assert.ok(await page.evaluate(() => document.querySelector('.long-tip').hidden));
    assert.ok(await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().filter(m => m.replacedWith).every(m => m.replacedWith.textContent === '"..."')));

    // code opens in the viewer on its own
    await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().find(m => m.replacedWith && m.replacedWith.title.startsWith('extension/views/state-view/functions/local.save/code'))
      .replacedWith.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true })));
    await page.waitForSelector('#sv-viewer:not([hidden]) .sv-viewer-body.code-only');
    assert.match(await page.evaluate(() => document.querySelector('#sv-viewer-code .CodeMirror').CodeMirror.getValue()), /^import os from 'os';\nimport ctx from 'ctx';\nimport core from 'state-core';\n\nasync function save\(\) \{/);
    await page.click('#sv-viewer-close');
    await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().find(m => m.replacedWith && m.replacedWith.title.startsWith('extension/views/header-view/html'))
      .replacedWith.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true })));
    await page.waitForSelector('#sv-viewer:not([hidden]) #sv-viewer-code .CodeMirror');
    // the view runs in the viewer with a copy of the state: its buttons work, and its ui-data shows below it
    const frame = page.frameLocator('#sv-viewer-view');
    await frame.locator('#header-view #state-button[aria-pressed="true"]').waitFor();
    await page.waitForFunction(() => /"state_open": true/.test(document.getElementById('sv-viewer-state').textContent));
    await frame.locator('#state-button').click();
    await frame.locator('#state-button[aria-pressed="false"]').waitFor();
    await page.waitForFunction(() => /after local\.open\.state-view/.test(document.getElementById('sv-viewer-state-head').textContent));
    assert.equal(await page.textContent('#sv-viewer-state .chg-updated'), '  "state_open": false,');
    await frame.locator('#docs-button').click();
    await frame.locator('#docs-view .doc-link').first().waitFor();
    // the copy changed, the live state did not
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data'].state_open), true);
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['header-view']['ui-data'].docs_open), false);
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['state-view']['ui-data'].viewer_path), 'extension/views/header-view/html');
    // editing the html starts the view again with the new html
    await page.evaluate(() => { const cm = document.querySelector('#sv-viewer-code .CodeMirror').CodeMirror; cm.setValue(cm.getValue().replace('aria-label="Docs"', 'aria-label="Docs" data-edited="yes"')); });
    await frame.locator('#docs-button[data-edited="yes"]').waitFor();
    await page.click('#sv-viewer-close');

    // an md file opens as a document you edit in place; its sections fold
    await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getAllMarks().find(m => m.replacedWith && m.replacedWith.title === 'agents/agent-oss/files/docs/state-view.md')
      .replacedWith.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true })));
    await page.waitForSelector('#sv-viewer-doc:not([hidden]) .md-page h2');
    assert.equal(await page.textContent('.md-page h2'), 'The state view');
    assert.equal(await page.isHidden('#sv-viewer-code'), true);
    // themes: a button switches the theme and keeps it in ui-data (the state tests left it on black)
    assert.equal(JSON.parse((await commitDoc('c000001')).state).extension.views['state-view']['ui-data'].md_theme, 'reader');
    await page.click('#md-themes [data-md-theme="reader"]');
    assert.equal(await page.getAttribute('#sv-viewer-doc', 'data-md-theme'), 'reader');
    assert.equal(await page.locator('#md-themes:not([hidden]) .md-theme').count(), 6);
    await page.click('#md-themes [data-md-theme="black"]');
    assert.equal(await page.getAttribute('#sv-viewer-doc', 'data-md-theme'), 'black');
    assert.equal(await page.getAttribute('#md-themes [data-md-theme="black"]', 'aria-pressed'), 'true');
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['state-view']['ui-data'].md_theme), 'black');
    await page.waitForFunction(() => getComputedStyle(document.getElementById('sv-viewer-doc')).backgroundColor === 'rgb(0, 0, 0)');
    await page.click('#md-themes [data-md-theme="reader"]');
    await page.click('.md-sec >> nth=0 >> .md-fold');
    assert.equal(await page.isHidden('.md-sec >> nth=0 >> .md-body'), true);
    await page.click('.md-sec >> nth=0 >> .md-fold');
    assert.equal(await page.isVisible('.md-sec >> nth=0 >> .md-body'), true);
    await page.click('.md-sec >> nth=0 >> h3 .md-t');
    await page.keyboard.press('End');
    await page.keyboard.type(' now');
    await page.keyboard.press('Enter');
    await page.keyboard.type('A new line');
    const md = await page.evaluate(() => document.querySelector('#sv-viewer-code .CodeMirror').CodeMirror.getValue());
    assert.match(md, /\n## Open the state view now\nA new line\n1\. Click the State button/);
    await page.click('#sv-viewer-close');
    assert.match(await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getValue()), /Open the state view now\\nA new line/);
    assert.equal(await page.isHidden('#sv-viewer'), true);

    // edit extension.data and save: a new version, and the border flashes green
    await page.evaluate(() => {
      const cm = document.querySelector('.CodeMirror').CodeMirror;
      const line = cm.getValue().split('\n').findIndex(l => l.trim() === '"data": {},');
      const ch = cm.getLine(line).indexOf('{}') + 1;
      cm.replaceRange('"x": 1', { line, ch });
    });
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].unsaved === true);
    assert.match(await page.textContent('#status'), /Unsaved/);
    await page.click('#save');
    await page.waitForFunction(() => window.agentOS.history.commits.length === 2);
    assert.ok(await page.isVisible('#sv-editor.saved'));
    const commit = await commitDoc('c000002');
    // (a version also keeps network and environment as they were when it was saved)
    assert.equal(JSON.parse(commit.state).extension.data.x, 1);
    assert.ok(JSON.parse(commit.state).network.scripts['state-core.js'].ms >= 0);
    assert.equal(JSON.parse(commit.state).extension.views['state-view']['ui-data'].current_state_version, 2);
    assert.match(await page.textContent('#pos'), /^v2 just now$/);

    // changes view and history steps: after a save, Changes shows what the new version changed
    await page.click('#changes');
    await page.waitForSelector('#tl-detail .st-legend');
    assert.match(await page.textContent('#tl-detail > .tl-text'), /in the state from v1 to v2\./);
    const added = await page.evaluate(() => { const cm = document.querySelector('#tl-detail .tl-code').cm; let n = 0; cm.eachLine(l => { if (/chg-added/.test(l.bgClass || '')) n++; }); return n; });
    assert.ok(added >= 1, 'added lines marked');
    await page.focus('#changes');
    await page.keyboard.press('ArrowLeft');
    assert.match(await page.textContent('#pos'), /^v1 /);
    await page.keyboard.press('ArrowRight');
    assert.match(await page.textContent('#pos'), /^v2 /);

    // comments are kept, a slip is fixed on save, and Cmd+S saves from anywhere
    await page.click('#changes');
    await page.evaluate(() => {
      const cm = document.querySelector('.CodeMirror').CodeMirror;
      const line = cm.getValue().split('\n').findIndex(l => l.includes('"common_app_storage": {}'));
      cm.replaceRange('// shared by all apps\n    ', { line, ch: cm.getLine(line).indexOf('"common') });
      const apps = cm.getValue().split('\n').findIndex(l => l.includes('"apps": {}'));
      cm.replaceRange(',', { line: apps, ch: cm.getLine(apps).length });
    });
    await page.waitForFunction(() => window.agentOS.state.extension.views['state-view']['ui-data'].fixable === true);
    assert.match(await page.textContent('#status'), /save fixes them/);
    await page.focus('#changes');
    await page.keyboard.press('Meta+s');
    await page.waitForFunction(() => window.agentOS.history.commits.length === 3);
    const c3 = await commitDoc('c000003');
    assert.match(c3.state, /^[ \t]*\/\/ shared by all apps[ \t]*$/m);
    assert.doesNotThrow(() => JSON.parse(c3.state.replace(/^[ \t]*\/\/ shared by all apps[ \t]*$/m, '')));
    assert.ok(c3.paths.filter(p => !/ (network|environment)\./.test(p)).every(p => p.includes('.ui-data.')), c3.paths.join(', '));
    // the call log keeps a short form of a long output; the function's output in the state is whole
    const fixedSave = await page.evaluate(() => window.agentOS.state.extension.views['state-view'].functions['local.save'].output);
    assert.equal(fixedSave.fixed, true);

    // no function reported errors, and the editor still shows the comment after the live state synced in
    const errs = await page.evaluate(() => { const out = []; (function walk(o, p) { if (!o || typeof o !== 'object') return; if (Array.isArray(o.errors) && o.errors.length) out.push(p + ': ' + o.errors.join('; ')); Object.keys(o).forEach(k => k !== 'output' && walk(o[k], p + '.' + k)); })(window.agentOS.state, ''); return out; });
    assert.deepEqual(errs, []);
    assert.match(await page.evaluate(() => document.querySelector('.CodeMirror').CodeMirror.getValue()), /^[ \t]*\/\/ shared by all apps[ \t]*$/m);

    // a newer version saved somewhere else runs here without a reload; the open views stay open
    if (!(await svd()).timeline_open) await page.click('#timeline-button');
    await page.waitForSelector('#tl-strip .tl-step');
    await page.evaluate(() => {
      const head = window.agentOS.history.commits[window.agentOS.history.commits.length - 1];
      const st = JSON.parse(head.state.replace(/^[ \t]*\/\/ shared by all apps[ \t]*$/m, ''));
      st.extension.data.from_elsewhere = true;
      st.agents['agent-oss'].files.docs['state-view.md'] += '\nA new line from main.';
      // as saved: the views closed
      st.extension.views['state-view']['ui-data'].timeline_open = false;
      const source = { git: '0123456789abcdef', branch: 'main', message: 'Add a line', request: 'add a line', session: 'https://claude.ai/code/test',
        explain: [{ part: 'state-view.md', before: 'It had no last line.', now: 'It has a last line.' }] };
      // (a release keeps the state in a file of the page: state_file)
      window.__blobs.v4 = JSON.stringify(st, null, 2);
      window.__docs['commits/c000004'] = { n: 4, parent: 3, at: new Date().toISOString(), state_file: 'v4', summary: { added: 1, updated: 1, deleted: 0 }, paths: ['added extension.data.from_elsewhere'], source };
      window.__listeners.forEach(f => f());
    });
    await page.waitForFunction(() => window.agentOS.state.extension.data.from_elsewhere === true);
    await page.waitForFunction(() => /^v4 /.test(document.querySelector('#pos') && document.querySelector('#pos').textContent));
    assert.equal(await page.evaluate(() => window.agentOS.history.commits.length), 4);
    assert.equal((await svd()).timeline_open, true);
    // the timeline shows a New version block: State changes from v3 to v4, then where it came from, before and now, and the file side by side
    const newer = page.locator('#tl-strip .tl-step', { has: page.locator('.tl-step-name', { hasText: /^loadNewerVersion$/ }) }).last();
    await newer.waitFor();
    assert.match(await newer.textContent(), /New version.*\d+ changes?/);
    await newer.click();
    await page.waitForFunction(() => / New version /.test(document.querySelector('#sv-block').textContent));
    // (the state view goes to the version it brought)
    assert.match(await page.textContent('#pos'), /^v4 /);
    if (!(await svd()).changes) await page.click('#changes');
    await page.waitForSelector('#tl-detail .st-legend');
    assert.match(await page.locator('#tl-detail .tl-code').first().evaluate(e => e.cm.getValue()), /"from_elsewhere": true/);
    assert.match(await page.textContent('#tl-detail'), /from v3 to v4/);
    // a long text shows as "...", as in the state view: a click opens it in the viewer
    const long = page.locator('#tl-detail .tl-code .long').first();
    await long.waitFor();
    await long.dispatchEvent('mousedown');
    // (the viewer is the file viewer: a file shows by its kind, with its size)
    await page.waitForSelector('.tl-viewer .fv .fv-body');
    assert.match(await page.textContent('.tl-viewer .fv-size'), /^[\d.]+ KB · ≈ /);
    await page.keyboard.press('Escape');
    await page.waitForSelector('.tl-viewer', { state: 'detached' });
    // an updated text: the pointer on it (or on its "was "..."") shows its changes, the new line green
    const upd = page.locator('#tl-detail .tl-code .long[title$="docs/state-view.md"]').first();
    await upd.dispatchEvent('mouseenter');
    await page.waitForSelector('.long-tip:not([hidden]) .CodeMirror');
    assert.ok(await page.locator('.long-tip .chg-added').count() >= 1);
    assert.match(await page.evaluate(() => document.querySelector('.long-tip .CodeMirror').CodeMirror.getValue()), /A new line from main\./);
    await upd.dispatchEvent('mouseleave');
    const was = page.locator('#tl-detail .tl-code .was', { hasText: 'was "..."' }).first();
    await was.dispatchEvent('mouseenter');
    await page.waitForSelector('.long-tip:not([hidden]) .chg-added');
    await was.dispatchEvent('mouseleave');
    // Files: the tree of all the files on the left; the changed file opens first, with File and Changes tabs
    await page.click('#sv-switches [data-input*="files"]');
    await page.waitForSelector('#tl-detail .kv-tree');
    assert.ok(await page.locator('#tl-detail .kv-tree summary', { hasText: /^docs\/$/ }).count() === 1);
    assert.equal(await page.textContent('#tl-detail .kv-item.on'), 'state-view.md');
    assert.deepEqual(await page.$$eval('#tl-detail .kv-tabs button', els => els.map(x => x.textContent)), ['File', 'Changes']);
    // the file viewer: an md file reads as a page with its contents on the left; Source shows its text
    await page.waitForSelector('#tl-detail .fv.fv-md .md-page');
    assert.match(await page.textContent('#tl-detail .fv .md-page'), /A new line from main\./);
    // with Changes, the read mode of an updated md file shows its changes: the new line is green
    assert.deepEqual(await page.$$eval('#tl-detail .md-page .chg-added', els => els.map(x => x.textContent)), ['A new line from main.']);
    assert.equal(await page.textContent('#tl-detail .fv-badge'), 'MD');
    // the head: the kind, the size and the tokens (no name, no lines), and icon buttons with their names as titles
    assert.match(await page.textContent('#tl-detail .fv-size'), /^[\d.]+ KB · ≈ [\d.]+k? tokens?$/);
    assert.deepEqual(await page.$$eval('#tl-detail .fv-head button', els => els.map(x => [x.title, x.textContent.trim()])),
      [['Read', ''], ['Source', ''], ['Contents', ''], ['Copy', ''], ['Full screen', '']]);
    // Contents is hidden at first; its button shows it, and again hides it
    assert.equal(await page.locator('#tl-detail .fv-side').count(), 0);
    await page.click('#tl-detail .fv-side-btn');
    assert.ok(await page.locator('#tl-detail .fv-side .fv-sym').count() >= 3);
    assert.equal(await page.getAttribute('#tl-detail .fv-side-btn', 'aria-pressed'), 'true');
    await page.click('#tl-detail .fv-seg button[title="Source"]');
    assert.match(await page.locator('#tl-detail .fv .fv-code').evaluate(e => e.cm.getValue()), /A new line from main\./);
    assert.equal(await page.getAttribute('#tl-detail .fv-side-btn', 'title'), 'Functions');
    await page.click('#tl-detail .fv-seg button[title="Read"]');
    await page.waitForSelector('#tl-detail .fv .md-page');
    // md: one Style select with the six themes of the state view; a choice sets state-view ui-data.md_theme and the look of the page
    assert.deepEqual(await page.$$eval('#tl-detail .fv .fv-style option', els => els.map(x => x.value)), ['reader', 'white', 'black', 'sepia', 'night', 'mono']);
    await page.selectOption('#tl-detail .fv .fv-style', 'sepia');
    await page.waitForFunction(() => document.querySelector('#tl-detail .fv-doc').dataset.mdTheme === 'sepia');
    assert.equal(await page.evaluate(() => window.agentOS.state.extension.views['state-view']['ui-data'].md_theme), 'sepia');
    await page.selectOption('#tl-detail .fv .fv-style', 'reader');
    await page.waitForFunction(() => document.querySelector('#tl-detail .fv-doc').dataset.mdTheme === 'reader');
    // Full screen: the file viewer covers the page; Escape gives it back its place
    await page.click('#tl-detail .fv-full-btn');
    await page.waitForSelector('#tl-detail .fv.fv-full');
    assert.deepEqual(await page.$eval('#tl-detail .fv.fv-full', e => { const r = e.getBoundingClientRect(); return [r.left, r.top, r.width, r.height]; }), await page.evaluate(() => [0, 0, innerWidth, innerHeight]));
    await page.keyboard.press('Escape');
    await page.waitForSelector('#tl-detail .fv.fv-full', { state: 'detached' });
    assert.ok(await page.locator('#tl-detail .kv').count() === 1, 'Escape leaves the step open');
    await page.click('#tl-detail .kv-tabs button:has-text("Changes")');
    await page.waitForSelector('#tl-detail .kv-main .tl-files');
    await page.locator('#tl-detail .kv-main .tl-files .tl-file').nth(1).locator('.chg-added').first().waitFor();
    // a file the block did not change has only its File tab
    await page.locator('#tl-detail .kv-item', { hasText: /^index\.html$/ }).click();
    assert.deepEqual(await page.$$eval('#tl-detail .kv-tabs button', els => els.map(x => x.textContent)), ['File']);
    // code has its outline (here the ids and scripts of index.html); a click on it goes to the line; Find marks the matches
    await page.waitForSelector('#tl-detail .fv.fv-html .fv-side .fv-sym');
    assert.ok((await page.$$eval('#tl-detail .fv-sym-name', els => els.map(x => x.textContent))).includes('div#index-view'));
    await page.locator('#tl-detail .fv-sym', { hasText: 'div#index-view' }).first().click();
    await page.fill('#tl-detail .fv-find', 'agentOS');
    assert.match(await page.textContent('#tl-detail .fv-count'), /^\d+ match/);
    await page.press('#tl-detail .fv-find', 'Enter');
    assert.match(await page.textContent('#tl-detail .fv-count'), /^1 of \d+/);
    // a json file is a tree
    await page.locator('#tl-detail .kv-item', { hasText: /^owner-draft\.jsonc$/ }).click();
    await page.waitForSelector('#tl-detail .fv.fv-json .jv-row');
    assert.ok(await page.locator('#tl-detail .jv-key').count() > 3);
    // a function has the tab Pseudo code: its docs, then numbered lines with keywords
    await page.click('#sv-switches [data-input*="functions"]');
    await page.locator('#tl-detail .kv-item', { hasText: /^get-state$/ }).click();
    assert.deepEqual(await page.$$eval('#tl-detail .kv-tabs button', els => els.map(x => x.textContent)), ['Function', 'Pseudo code']);
    await page.click('#tl-detail .kv-tabs button:has-text("Pseudo code")');
    await page.waitForSelector('#tl-detail .fv-pseudo .ps-line');
    assert.equal(await page.locator('#tl-detail .ps-line').count(), 4);
    assert.deepEqual(await page.$$eval('#tl-detail .ps-kw', els => els.map(x => x.textContent)), ['READ', 'IF', 'THROW', 'RETURN']);
    assert.equal(await page.locator('#tl-detail .ps-line').nth(2).locator('.ps-guide').count(), 1);
    assert.match(await page.textContent('#tl-detail .ps-docs'), /Returns the JSON state/);
    await page.click('#sv-switches [data-input*="all"]');
    await page.waitForSelector('#tl-detail .st-legend');
    await page.click('#details');
    await page.waitForSelector('#tl-detail .tl-explain');
    assert.match(await page.textContent('#tl-detail .tl-part'), /git commit 0123456 \(Add a line\)/);
    assert.match(await page.textContent('#tl-detail .tl-explain'), /state-view\.mdIt had no last line\.It has a last line\./);
    const filePart = part('docs/state-view.md');
    assert.match(await filePart.textContent(), /This file was updated/);
    await filePart.locator('.tl-call-head').click();
    await filePart.locator('.tl-files .tl-code').nth(1).waitFor();
    await filePart.locator('.tl-files .tl-code').nth(1).locator('.chg-added').first().waitFor();
    await page.click('#details');

    // a newer version with a new agent run: an Agent run block after its New version block. With no block chosen, the
    // timeline chooses that run (Last agent run, at the left), so the Files view shows the files of the new version
    await page.evaluate(() => {
      const os = window.agentOS, head = os.history.commits[os.history.commits.length - 1];
      const st = JSON.parse(head.state.replace(/^[ \t]*\/\/ shared by all apps[ \t]*$/m, ''));
      const files = st.agents['agent-oss'].files, runs = files.runs, run = JSON.parse(runs[Object.keys(runs).filter(k => /\.json$/.test(k)).sort().pop()]);
      Object.assign(run, { session: 'zzztest', run: 99, started: new Date().toISOString(), ended: new Date().toISOString() });
      runs['zzztest-99.json'] = JSON.stringify(run);
      files['from-the-run.md'] = '# From the run';
      window.__blobs.v5 = JSON.stringify(st, null, 2);
      window.__docs['commits/c000005'] = { n: 5, parent: 4, at: new Date().toISOString(), state_file: 'v5', summary: { added: 2, updated: 0, deleted: 0 },
        paths: ['added agents.agent-oss.files.runs.zzztest-99.json', 'added agents.agent-oss.files.from-the-run.md'], source: { git: 'fedcba9876543210', branch: 'main', message: 'A run', request: 'a run', session: 'https://claude.ai/code/test', explain: [] } };
      window.__listeners.forEach(f => f());
    });
    await page.waitForFunction(() => window.agentOS.history.commits.length === 5);
    await page.evaluate(() => window.agentOS.os.call('extension.views.timeline-view.functions.local.select', { id: null }));
    await page.waitForFunction(() => /session zzz · run 99/.test(document.querySelector('#tl-strip .tl-step.on') && document.querySelector('#tl-strip .tl-step.on').textContent));
    assert.equal(await page.textContent('#tl-strip .tl-step.on .tl-kind'), 'Last AI run notification');
    assert.equal(await page.locator('#tl-strip .tl-step.on.pin-left, #tl-strip .tl-step.on.pin-right').count(), 1);
    assert.equal(await page.textContent('#tl-strip .tl-step .tl-kind'), 'AI run notification');
    assert.match(await page.textContent('#pos'), /^v5 /);
    await page.click('#sv-switches [data-input*="files"]');
    await page.waitForSelector('#tl-detail .kv-tree');
    assert.equal(await page.locator('#tl-detail .kv-item', { hasText: /^from-the-run\.md$/ }).count(), 1);
    await page.click('#sv-switches [data-input*="all"]');

    // every call, with its parent, is in the stored call log
    await page.waitForFunction(() => Object.keys(window.__docs).some(k => k.startsWith('calls/') && window.__docs[k].items.some(i => i.name === 'loadNewerVersion')), null, { timeout: 5000 });
    const log = await page.evaluate(() => Object.entries(window.__docs).find(([k]) => k.startsWith('calls/'))[1]);
    const names = new Set(log.items.map(i => i.name));
    // (the log keeps the newest calls: at most 400, and at most 240 KB; the first ones, like loadState, can be cut)
    assert.ok(names.has('loadState') || log.items.length < log.count, 'loadState, or a log that was cut');
    assert.ok(JSON.stringify(log).length <= 240000);
    // the log is the newest calls of the page, in order, without a gap
    const all = await page.evaluate(() => window.agentOS.calls.map(c => c.id));
    assert.deepEqual(log.items.map(i => i.id), all.slice(all.indexOf(log.items[0].id), all.indexOf(log.items[0].id) + log.items.length));
    for (const n of ['loadNewerVersion', 'extension.functions.render', 'local.refresh']) assert.ok(names.has(n), n);
    assert.ok(log.items.every(i => i.ok && i.at && typeof i.ms === 'number'), JSON.stringify(log.items.filter(i => !i.ok).slice(0, 3)));

    // the Reload button of the timeline: the page loads again, the timeline opens and replays from the first step,
    // the last agent run
    // (the timeline stayed open after the new version)
    assert.equal(await page.isHidden('#timeline-view'), false);
    await Promise.all([page.waitForNavigation(), page.click('#tl-reload')]);
    await page.waitForFunction(() => window.agentOS && window.agentOS.state && window.agentOS.state.extension.views['timeline-view']['ui-data'].playing);
    await page.waitForSelector('#sv-block b');
    // (the replay started at the last agent run)
    assert.deepEqual(await page.evaluate(() => window.agentOS.calls.filter(c => c.name === 'local.select').map(c => c.input.input.id).slice(0, 1).map(id => /^run:runs\//.test(id))), [true]);
    assert.equal((await svd()).timeline_open, true);
    assert.equal(await page.evaluate(() => sessionStorage.getItem('agent-os.timeline-replay')), null);
    // (the first draw of the state view with the 2 MB state takes about 6 s: the replay goes on after it)
    await page.waitForFunction(() => ['runtime', 'open'].includes(window.agentOS.state.extension.views['timeline-view']['ui-data'].selected) || /^Block [3-9]/.test(document.querySelector('#sv-block').textContent), null, { timeout: 15000 });
    // the replay goes on past the blocks that were there when it started (the page was still starting)
    await page.waitForFunction(() => /^Block \d+: Start the page/.test(document.querySelector('#sv-block').textContent), null, { timeout: 8000 });
    assert.deepEqual(errors, []);
  } finally {
    await browser.close();
    server.close();
  }
});
