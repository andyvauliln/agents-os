STYLE = r"""<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;0,7..72,700;1,7..72,400&family=JetBrains+Mono:wght@400;500&display=swap");
/* CodeMirror 5.65.16 base styles (MIT), from vendor/codemirror/5.65.16/lib/codemirror.css. Inline: the page keeps its styles in index-view. */
__CMCSS__
:root{--bg:#f3f5f8;--panel:#ffffff;--gutter:#f7f8fa;--fg:#17202c;--muted:#6a7584;--line:#dde2e9;--accent:#3152d4;--on-accent:#ffffff;--sel:#dbe3fb;
  --key:#17202c;--key-empty:#8b95a5;--str:#18794e;--num:#b4530b;--atom:#7b3fc4;--warn:#a35a00;--bad:#c0322b;--ok:#1f9d55;
  --add:#18794e;--add-bg:#e3f4ea;--upd:#a35a00;--upd-bg:#fbefd6;--del:#c0322b;--del-bg:#fbe4e2;
  --mono:"JetBrains Mono",ui-monospace,"SF Mono",Menlo,Consolas,monospace;--sans:system-ui,-apple-system,"Segoe UI",sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0f141b;--panel:#161d27;--gutter:#131922;--fg:#e4e9f0;--muted:#8c98aa;--line:#263040;--accent:#8aa4ff;--on-accent:#0f141b;--sel:#27355c;
  --key:#e4e9f0;--key-empty:#77839a;--str:#6fd3a0;--num:#f0a35e;--atom:#c39bff;--warn:#f0b35e;--bad:#ff8a80;--ok:#4ade80;
  --add:#6fd3a0;--add-bg:#163325;--upd:#f0c05e;--upd-bg:#3a2e12;--del:#ff8a80;--del-bg:#3d1a1a;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0f141b;--panel:#161d27;--gutter:#131922;--fg:#e4e9f0;--muted:#8c98aa;--line:#263040;--accent:#8aa4ff;--on-accent:#0f141b;--sel:#27355c;
  --key:#e4e9f0;--key-empty:#77839a;--str:#6fd3a0;--num:#f0a35e;--atom:#c39bff;--warn:#f0b35e;--bad:#ff8a80;--ok:#4ade80;
  --add:#6fd3a0;--add-bg:#163325;--upd:#f0c05e;--upd-bg:#3a2e12;--del:#ff8a80;--del-bg:#3d1a1a;color-scheme:dark}
[hidden]{display:none!important}
body{background:var(--bg);color:var(--fg);font-family:var(--sans)}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--panel)}
#index-view{height:100%;display:flex;flex-direction:column}
button{font:inherit}
button:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
#header-view,#state-view{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
#header-view{position:sticky;top:env(safe-area-inset-top,0px);z-index:3;background:var(--panel);border-bottom:1px solid var(--line);padding-block:8px;min-height:36px;display:flex;justify-content:flex-end;align-items:center}
#state-view{flex:1;min-height:0;display:flex;flex-direction:column;gap:10px;padding-block:12px;position:relative}
.sv-bar{display:flex;flex-wrap:wrap;align-items:center;gap:8px}
#sv-editor{flex:1;min-height:240px;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--panel);transition:border-color .3s,box-shadow .3s}
#sv-editor.saved{border-color:var(--ok);box-shadow:0 0 0 2px var(--ok)}
.btn{display:inline-flex;align-items:center;justify-content:center;width:34px;height:32px;padding:0;border-radius:7px;border:1px solid var(--line);background:var(--panel);color:var(--fg);cursor:pointer}
.btn[aria-pressed="true"]{background:var(--sel);border-color:var(--accent);color:var(--accent)}
.btn.primary{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.btn:disabled{opacity:.4;cursor:default}
.pos{font:12px var(--mono);color:var(--muted)}
.pos b{color:var(--fg);font-weight:500}
.path{font:12px var(--mono);color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0}
.status{font-size:12px;color:var(--warn);margin-left:auto}
.status.bad{color:var(--bad)}
.long{color:var(--str);cursor:pointer;border-bottom:1px dotted currentColor}
.sv-viewer{position:absolute;inset:12px max(16px,env(safe-area-inset-right,0px)) 12px max(16px,env(safe-area-inset-left,0px));z-index:4;display:flex;flex-direction:column;gap:8px;background:var(--bg)}
.sv-viewer-bar{display:flex;align-items:center;gap:8px;justify-content:space-between}
.sv-viewer-body{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:8px}
@media (max-width:640px){.sv-viewer-body{grid-template-columns:1fr;grid-template-rows:1fr 1fr}}
.sv-viewer-body.code-only{grid-template-columns:1fr;grid-template-rows:1fr}
.code-only #sv-viewer-view{display:none}
#sv-viewer-code,#sv-viewer-view{min-height:0;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--panel)}
#sv-viewer-view{width:100%;height:100%;box-sizing:border-box}
.CodeMirror{height:100%;font:13px/1.6 var(--mono);background:var(--panel);color:var(--fg)}
.CodeMirror-gutters{background:var(--gutter);border-right:1px solid var(--line)}
.CodeMirror-linenumber{color:var(--muted)}
.CodeMirror-cursor{border-left-color:var(--fg)}
.CodeMirror-selected,.CodeMirror-focused .CodeMirror-selected{background:var(--sel)}
.CodeMirror-scrollbar-filler,.CodeMirror-gutter-filler{background:var(--panel)}
.CodeMirror-foldgutter{width:14px}
.CodeMirror-foldgutter-open,.CodeMirror-foldgutter-folded{cursor:pointer;color:var(--muted);text-align:center}
.CodeMirror-foldgutter-open:after{content:"▾"}
.CodeMirror-foldgutter-folded:after{content:"▸";color:var(--accent)}
.CodeMirror-foldmarker{color:var(--accent);background:var(--sel);border-radius:4px;padding:0 5px;margin:0 2px;cursor:pointer;font-family:var(--mono)}
div.CodeMirror span.CodeMirror-matchingbracket{color:var(--accent);font-weight:600}
div.CodeMirror span.CodeMirror-nonmatchingbracket{color:var(--bad)}
.cm-s-agent .cm-string{color:var(--str)}
.cm-s-agent .cm-string.cm-key{color:var(--key);font-weight:500}
.cm-s-agent .cm-string.cm-key.cm-emptykey{color:var(--key-empty);font-weight:400}
.cm-s-agent .cm-number{color:var(--num)}
.cm-s-agent .cm-atom{color:var(--atom)}
.cm-s-agent .cm-emptyobj{color:var(--key-empty)}
.cm-s-agent .cm-comment{color:var(--muted);font-style:italic}
.cm-s-agent .cm-tag{color:var(--accent)}
.cm-s-agent .cm-attribute{color:var(--num)}
.bad-line{background:var(--del-bg)}
.chg-added{background:var(--add-bg);box-shadow:inset 3px 0 var(--add)}
.chg-updated{background:var(--upd-bg);box-shadow:inset 3px 0 var(--upd)}
.chg-deleted{background:var(--del-bg);box-shadow:inset 3px 0 var(--del)}
.chg-deleted .CodeMirror-line{text-decoration:line-through;text-decoration-color:var(--del)}
.was{font:11px var(--mono);color:var(--upd);margin-left:10px;opacity:.9}
.CodeMirror-readonly .CodeMirror-cursor{display:none}
</style>"""
