// Smoke test of the File Tree page before publishing (ide-build step 5).
// Loads the page with a stand-in for the artifact runtime, opens items on a desktop and a phone width,
// and fails when the page throws, a tab is missing, or the page is wider than a phone screen.
//   node check_page.js <page dir> [out dir for screenshots] [node ids...]
// Needs Playwright with Chromium: PLAYWRIGHT (module path) and CHROMIUM (browser path) override the defaults.
const fs = require('fs'), path = require('path');
const { chromium } = require(process.env.PLAYWRIGHT || '/opt/node22/lib/node_modules/playwright');
const DIR = path.resolve(process.argv[2] || path.join(__dirname, '../explorer'));
const OUT = process.argv[3] && process.argv[3] !== '-' ? path.resolve(process.argv[3]) : null;
const IDS = process.argv.slice(4).length ? process.argv.slice(4) : ['n-0', 'n-2.1', 'n-53', 'n-10.1.1.3', 'n-11'];
const mock = () => {   // in-memory db, sample and user, the parts of window.claude the page uses
  const store = {}, subs = {};
  const snap = c => ({ docs: Object.entries(store[c] || {}).map(([id, v]) => ({ id, data: () => JSON.parse(JSON.stringify(v)) })) });
  const fire = c => (subs[c] || []).forEach(cb => setTimeout(() => cb(snap(c)), 5));
  const doc = (c, id) => ({
    set: async v => { (store[c] ||= {})[id] = JSON.parse(JSON.stringify(v)); fire(c); },
    update: async v => { if (!store[c]?.[id]) throw { code: 'not_found' }; Object.assign(store[c][id], v); fire(c); },
    delete: async () => { delete (store[c] || {})[id]; fire(c); },
  });
  const db = {
    collection: c => ({ onSnapshot: cb => { (subs[c] ||= []).push(cb); setTimeout(() => cb(snap(c)), 5); return () => {}; },
      add: async v => { const id = 'd' + Math.random().toString(36).slice(2, 8); await doc(c, id).set(v); return { id }; } }),
    doc: p => { const [c, id] = p.split('/'); return doc(c, id); },
  };
  const sample = async () => ({ text: 'ok', truncated: false }); sample.json = async () => null;
  window.claude = { use: async n => n === 'db' ? db : n === 'sample' ? sample : n === 'user' ? { id: async () => 'u1' } : null };
};
(async () => {
  const b = await chromium.launch(process.env.CHROMIUM ? { executablePath: process.env.CHROMIUM } :
    fs.existsSync('/opt/pw-browsers/chromium-1194/chrome-linux/chrome') ? { executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' } : {});
  const data = JSON.parse(fs.readFileSync(path.join(DIR, 'file-tree.data.json'), 'utf8'));
  const known = new Set(data.nodes.map(n => n.id));
  let bad = 0;
  for (const [label, vp] of [['desktop', { width: 1400, height: 900 }], ['phone', { width: 390, height: 844 }]]) {
    for (const id of IDS) {
      if (!known.has(id)) { console.log(`MISSING ${id}: not in the data`); bad++; continue; }
      const p = await b.newPage({ viewport: vp }); const errs = [];
      p.on('pageerror', e => errs.push(String(e)));
      await p.addInitScript('(' + mock + ')()');
      await p.route('http://local.test/**', r => { const f = path.join(DIR, new URL(r.request().url()).pathname);
        r.fulfill({ body: fs.readFileSync(f), contentType: f.endsWith('.json') ? 'application/json' : 'text/html; charset=utf-8' }); });
      await p.route(/fonts\.(googleapis|gstatic)\.com/, r => r.abort());
      await p.goto('http://local.test/file-tree-explorer.html#' + id);
      await p.waitForSelector('.tab', { timeout: 15000 }).catch(() => errs.push('no tabs rendered'));
      await p.waitForTimeout(400);
      const tabs = await p.$$eval('.tab', t => t.map(x => x.dataset.tab).filter(Boolean));
      for (const t of ['how', 'file']) if (tabs.includes(t)) {   // click it as a person would, even when the tab bar scrolls
        await p.evaluate(t => [...document.querySelectorAll(`.tab[data-tab="${t}"]`)].find(e => e.offsetParent)?.click(), t); await p.waitForTimeout(200); }
      const wide = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
      const sel = await p.evaluate(() => document.querySelector('#tree .row.sel, #tree .row[aria-selected="true"]')?.dataset.id || '');
      const ok = !errs.length && tabs.length && (label === 'desktop' || wide <= 1);
      if (!ok) bad++;
      console.log(`${ok ? 'ok  ' : 'FAIL'} ${label} ${id} tabs=${tabs.join(',')} overflow=${wide}px selected=${sel} ${errs.join(' | ')}`);
      if (OUT) { fs.mkdirSync(OUT, { recursive: true }); await p.screenshot({ path: path.join(OUT, `${label}-${id}.png`) }); }
      await p.close();
    }
  }
  await b.close();
  console.log(bad ? `${bad} problem(s)` : 'page ok');
  process.exit(bad ? 1 : 0);
})().catch(e => { console.error('FAIL', e); process.exit(1); });
