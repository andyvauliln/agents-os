// Pure logic for the Agent OS page: state paths, templates, diffs, the changes view, commits,
// history steps, test checks and the call log.
// Works in the browser (window.StateCore) and in Node (require) so it can be tested without a page.
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.StateCore = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  function isObj(v) { return v !== null && typeof v === 'object' && !Array.isArray(v); }
  function same(a, b) { return JSON.stringify(a) === JSON.stringify(b); }
  function pathText(path) { return path.join('.'); }

  // Every change between two states: objects are compared key by key, anything else as a whole value.
  function diff(before, after, path) {
    path = path || [];
    var out = [];
    if (isObj(before) && isObj(after)) {
      Object.keys(after).forEach(function (k) {
        var p = path.concat(k);
        if (!(k in before)) out.push({ type: 'added', path: p, after: after[k] });
        else out = out.concat(diff(before[k], after[k], p));
      });
      Object.keys(before).forEach(function (k) {
        if (!(k in after)) out.push({ type: 'deleted', path: path.concat(k), before: before[k] });
      });
      return out;
    }
    if (!same(before, after)) out.push({ type: 'updated', path: path, before: before, after: after });
    return out;
  }

  function summarize(changes) {
    var s = { added: 0, updated: 0, deleted: 0 };
    changes.forEach(function (c) { s[c.type]++; });
    return s;
  }

  // The state cut down to what changed, as JSON text, with the line range and kind of each change.
  // Kept keys follow the new state's order; deleted keys come back where they stood in the old one.
  function changesView(before, after) {
    var lines = [], marks = [];
    function keysOf(b, a) {
      var keys = Object.keys(a);
      Object.keys(b).forEach(function (k, i) {
        if (k in a) return;
        var prev = Object.keys(b).slice(0, i).reverse().find(function (x) { return keys.indexOf(x) >= 0; });
        keys.splice(prev === undefined ? 0 : keys.indexOf(prev) + 1, 0, k);
      });
      return keys;
    }
    function changed(b, a) { return !same(b, a); }
    function emitValue(value, indent, prefix, suffix, type, path, before) {
      var text = JSON.stringify(value, null, 2).split('\n');
      var from = lines.length;
      text.forEach(function (t, i) {
        lines.push((i === 0 ? indent + prefix : indent) + t + (i === text.length - 1 ? suffix : ''));
      });
      marks.push({ type: type, path: path, from: from, to: lines.length - 1, before: before });
    }
    function emitObject(b, a, indent, path) {
      var keys = keysOf(b, a).filter(function (k) { return changed(b[k], a[k]) || !(k in a) || !(k in b); });
      keys.forEach(function (k, i) {
        var comma = i < keys.length - 1 ? ',' : '';
        var prefix = JSON.stringify(k) + ': ';
        var p = path.concat(k);
        if (!(k in b)) emitValue(a[k], indent, prefix, comma, 'added', p);
        else if (!(k in a)) emitValue(b[k], indent, prefix, comma, 'deleted', p);
        else if (isObj(b[k]) && isObj(a[k])) {
          lines.push(indent + prefix + '{');
          emitObject(b[k], a[k], indent + '  ', p);
          lines.push(indent + '}' + comma);
        } else emitValue(a[k], indent, prefix, comma, 'updated', p, b[k]);
      });
    }
    if (isObj(before) && isObj(after)) {
      lines.push('{');
      emitObject(before, after, '  ', []);
      lines.push('}');
    } else if (changed(before, after)) emitValue(after, '', '', '', 'updated', [], before);
    var empty = marks.length === 0;
    return { text: empty ? '{}' : lines.join('\n'), marks: marks, empty: empty };
  }

  // A commit records the whole state as text, plus what changed against its parent
  // (outputs, timings and test results filled in by the runtime do not count as changes).
  function makeCommit(parent, text, at) {
    var state = stripRuntime(JSON.parse(text));
    var base = parent ? stripRuntime(JSON.parse(parent.state)) : {};
    var changes = diff(base, state);
    return {
      n: parent ? parent.n + 1 : 1,
      parent: parent ? parent.n : null,
      at: at,
      state: text,
      summary: summarize(changes),
      paths: changes.slice(0, 100).map(function (c) { return c.type + ' ' + pathText(c.path); })
    };
  }
  function commitId(n) { return 'c' + String(n).padStart(6, '0'); }

  // Positions run over the commits, then the unsaved draft if there is one.
  function historyLength(commits, draft) { return commits.length + (draft !== null ? 1 : 0); }
  function step(pos, delta, commits, draft) {
    var last = historyLength(commits, draft) - 1;
    return Math.max(0, Math.min(last, pos + delta));
  }
  function textAt(pos, commits, draft) {
    return pos < commits.length ? commits[pos].state : draft;
  }
  // What the changes view compares at a position: the version before it, and it.
  function pairAt(pos, commits, draft) {
    var after = textAt(pos, commits, draft);
    var before = pos === 0 ? '{}' : textAt(pos - 1, commits, draft);
    return { before: JSON.parse(before), after: JSON.parse(after) };
  }

  // Every call goes through track(): its name, input, result or error, time taken, and related data
  // the call adds with ctx.relate({...}) (commit numbers, paths, positions).
  function createTracker(opts) {
    opts = opts || {};
    var now = opts.now || function () { return new Date().toISOString(); };
    var clock = opts.clock || function () { return Date.now(); };
    var records = [], seq = 0;
    var keep = opts.brief || function (v) { return v === undefined ? null : v; };
    function finish(rec, t0) {
      rec.ms = clock() - t0;
      records.push(rec);
      if (opts.onRecord) opts.onRecord(rec, records);
      return rec;
    }
    function track(name, input, fn) {
      var rec = { id: ++seq, name: name, at: now(), input: input === undefined ? null : input, ok: true, output: null, error: null, related: {} };
      var ctx = { id: rec.id, relate: function (o) { Object.keys(o).forEach(function (k) { rec.related[k] = o[k]; }); } };
      var t0 = clock(), out;
      try { out = fn(ctx); } catch (e) { rec.ok = false; rec.error = String(e && e.message || e); finish(rec, t0); throw e; }
      if (out && typeof out.then === 'function') {
        return out.then(function (v) { rec.output = keep(v); finish(rec, t0); return v; },
          function (e) { rec.ok = false; rec.error = String(e && (e.message || e.code) || e); finish(rec, t0); throw e; });
      }
      rec.output = keep(out);
      finish(rec, t0);
      return out;
    }
    return { track: track, records: records };
  }

  function clone(v) { return v === undefined ? undefined : JSON.parse(JSON.stringify(v)); }
  function walk(v, path, fn) {
    fn(v, path);
    if (v !== null && typeof v === 'object') Object.keys(v).forEach(function (k) { walk(v[k], path.concat(k), fn); });
  }
  // Paths are dotted, and keys can hold dots ("local.init", "CLAUDE.md"):
  // when a segment does not exist, it is joined with the next one and tried again.
  function getPath(obj, path) {
    var parts = String(path).split('.'), v = obj, i = 0;
    while (i < parts.length) {
      if (v === null || typeof v !== 'object') return undefined;
      var k = parts[i], j = i;
      while (!(k in v) && j < parts.length - 1) { j++; k += '.' + parts[j]; }
      if (!(k in v)) return undefined;
      v = v[k]; i = j + 1;
    }
    return v;
  }
  function setPath(obj, path, value) {
    var parts = String(path).split('.');
    // Prefer a parent that already has the key (the key may hold dots); otherwise the last segment is the key.
    for (var i = 1; i < parts.length; i++) {
      var parent = getPath(obj, parts.slice(0, i).join('.')), key = parts.slice(i).join('.');
      if (isObj(parent) && key in parent) { parent[key] = value; return; }
    }
    var p = parts.length > 1 ? getPath(obj, parts.slice(0, -1).join('.')) : obj;
    if (!isObj(p)) throw new Error('No object at ' + parts.slice(0, -1).join('.'));
    p[parts[parts.length - 1]] = value;
  }

  // Fields the runtime fills in while functions run; they are not part of what the owner edits.
  function stripRuntime(state) {
    var copy = clone(state);
    walk(copy, [], function (v, path) {
      if (path[path.length - 2] !== 'functions' || !isObj(v)) return;
      delete v.output; delete v.performance;
      if (isObj(v.calls)) Object.keys(v.calls).forEach(function (k) { if (isObj(v.calls[k])) delete v.calls[k].output; });
      if (isObj(v.tests)) Object.keys(v.tests).forEach(function (k) { if (isObj(v.tests[k])) delete v.tests[k].result; });
    });
    return copy;
  }

  // A small, JSON-safe version of a value for logs and output fields.
  function brief(v) {
    if (v === undefined || typeof v === 'function') return null;
    if (typeof v === 'string') return v.length > 200 ? { type: 'text', length: v.length } : v;
    if (v === null || typeof v !== 'object') return v;
    if (typeof Node !== 'undefined' && v instanceof Node) return { type: 'element', tag: v.nodeName };
    var text;
    try { text = JSON.stringify(v); } catch (e) { return { type: 'object' }; }
    return text.length > 600 ? { type: Array.isArray(v) ? 'list' : 'object', keys: Object.keys(v).slice(0, 30) } : JSON.parse(text);
  }

  // Fills a view's html: ${...} expressions see the view's ui-data as d, and e() escapes text.
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function template(html, data) { return new Function('d', 'e', 'return `' + html + '`;')(data, esc); }

  // Checks a test's expect block: output (fields that must match), output-has (keys), dom / dom-absent (selectors).
  function checkExpect(expect, out, hasDom) {
    var fails = [];
    if (expect.output !== undefined) Object.keys(expect.output).forEach(function (k) {
      if (!out || !same(out[k], expect.output[k])) fails.push('output.' + k + ' is ' + JSON.stringify(out && out[k]) + ', expected ' + JSON.stringify(expect.output[k]));
    });
    (expect['output-has'] || []).forEach(function (k) { if (!out || !(k in out)) fails.push('output has no ' + k); });
    (expect.dom || []).forEach(function (sel) { if (!hasDom(sel)) fails.push('no element ' + sel); });
    (expect['dom-absent'] || []).forEach(function (sel) { if (hasDom(sel)) fails.push('element still there: ' + sel); });
    return fails;
  }

  return {
    clone: clone, walk: walk, getPath: getPath, setPath: setPath, stripRuntime: stripRuntime,
    brief: brief, template: template, esc: esc, checkExpect: checkExpect,
    diff: diff, summarize: summarize, changesView: changesView,
    makeCommit: makeCommit, commitId: commitId,
    historyLength: historyLength, step: step, textAt: textAt, pairAt: pairAt,
    createTracker: createTracker
  };
});
