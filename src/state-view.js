(function(){
'use strict';
var FONTS='https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap';
var RESET=':root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,-apple-system,sans-serif}img{max-width:100%}[hidden]{display:none!important}';
var STATE_PILLS={ok:1,mock:1,off:1};

var data=JSON.parse(document.getElementById('page-data').textContent);
var savedText=pretty(data);
var ui=load()||{};
var view=ui.view==='state'?'state':'home';
var mode=ui.mode==='raw'?'raw':'tree';
var collapsed=new Set(ui.collapsed||defaultCollapsed());
var selected=null,query='',api=null,canSave=false,busy=false,editing=false,rawText=null,errMsg='';

function pretty(v){return JSON.stringify(v,null,2)}
function pk(path){return JSON.stringify(path)}
function load(){try{return JSON.parse(localStorage.getItem('agent-os-ui')||'null')}catch(e){return null}}
function persist(){try{localStorage.setItem('agent-os-ui',JSON.stringify({view:view,mode:mode,collapsed:Array.from(collapsed)}))}catch(e){}}
function isObj(v){return v!==null&&typeof v==='object'}
function typeOf(v){return Array.isArray(v)?'arr':v===null?'null':typeof v==='object'?'obj':typeof v==='string'?'str':typeof v==='number'?'num':'bool'}
function dirty(){return (mode==='raw'&&rawText!==null?rawText:pretty(data))!==savedText}
function walk(v,path,fn){fn(v,path);if(isObj(v))Object.keys(v).forEach(function(k){walk(v[k],path.concat(Array.isArray(v)?+k:k),fn)})}
function defaultCollapsed(){var out=[];walk(data,[],function(v,p){if(isObj(v)&&p.length>=4&&Object.keys(v).length)out.push(pk(p))});return out}
function getAt(path){var v=data;for(var i=0;i<path.length;i++)v=v[path[i]];return v}
function setAt(path,val){if(!path.length){data=val;return}var p=getAt(path.slice(0,-1));p[path[path.length-1]]=val}
function el(tag,cls,text){var e=document.createElement(tag);if(cls)e.className=cls;if(text!=null)e.textContent=text;return e}
function svgCaret(){var s=document.createElementNS('http://www.w3.org/2000/svg','svg');s.setAttribute('width','10');s.setAttribute('height','10');s.setAttribute('viewBox','0 0 10 10');var p=document.createElementNS('http://www.w3.org/2000/svg','path');p.setAttribute('d','M3 1.5 7 5 3 8.5');p.setAttribute('fill','none');p.setAttribute('stroke','currentColor');p.setAttribute('stroke-width','1.6');p.setAttribute('stroke-linecap','round');p.setAttribute('stroke-linejoin','round');s.appendChild(p);return s}
// Under a "files" key, empty-or-object entries read as folders and files: a name with an extension is a file.
function fileKind(path,key){var i=path.indexOf('files');if(i<0||typeof key!=='string')return null;return /\.[a-z0-9]+$/i.test(key)&&key.charAt(0)!=='.'||/\.(md|json|ya?ml|txt|sh|js|ts|py)$/i.test(key)?'file':'folder'}

/* ---------- app shell ---------- */
var app=document.getElementById('app');
function render(){
  app.textContent='';
  var top=el('header','top'),tw=el('div','wrap');
  var brand=el('div','brand');brand.appendChild(el('span','brand-mark','{}'));brand.appendChild(el('span',null,'Agent OS'));brand.appendChild(el('small',null,'state.json'));
  tw.appendChild(brand);
  var tgl=el('button','btn');tgl.type='button';tgl.id='toggle-state';tgl.setAttribute('aria-pressed',String(view==='state'));
  tgl.appendChild(el('span',null,view==='state'?'Close state view':'State view'));
  tgl.onclick=function(){view=view==='state'?'home':'state';persist();render()};
  tw.appendChild(tgl);top.appendChild(tw);app.appendChild(top);
  if(view==='home')renderHome();else renderState();
}
function renderHome(){
  var m=el('main','home wrap');
  m.appendChild(el('h1',null,'Agent OS'));
  m.appendChild(el('p',null,'Everything this project knows lives in state.json. Pick a section to open it in the state view, where you can fold, edit and save it.'));
  var cards=el('div','cards');
  Object.keys(data).forEach(function(k){
    var v=data[k],c=el('button','card');c.type='button';
    var h=el('h2');var i=el('span','ico obj',Array.isArray(v)?'[]':'{}');h.appendChild(i);h.appendChild(el('span',null,k));c.appendChild(h);
    var kids=isObj(v)?Object.keys(v):[];
    var n=0;walk(v,[],function(){n++});
    c.appendChild(el('span','sub',kids.length+' sections · '+(n-1)+' entries'));
    var chips=el('div','chips');kids.slice(0,8).forEach(function(x){chips.appendChild(el('span','chip',x))});if(kids.length>8)chips.appendChild(el('span','chip','+'+(kids.length-8)));
    c.appendChild(chips);
    c.onclick=function(){view='state';mode='tree';collapsed.delete(pk([k]));selected=pk([k]);persist();render();var r=app.querySelector('.row.sel');if(r)r.scrollIntoView({block:'center'})};
    cards.appendChild(c);
  });
  m.appendChild(cards);app.appendChild(m);
}

/* ---------- state view ---------- */
function renderState(){
  var sv=el('section','sv');
  var bar=el('div','sv-bar'),bw=el('div','wrap');
  var seg=el('div','seg');
  [['tree','Tree'],['raw','Raw JSON']].forEach(function(o){var b=el('button',null,o[1]);b.type='button';b.setAttribute('aria-pressed',String(mode===o[0]));b.onclick=function(){switchMode(o[0])};seg.appendChild(b)});
  bw.appendChild(seg);
  if(mode==='tree'){
    var s=el('input','search');s.id='search';s.type='search';s.placeholder='Find a key or value';s.value=query;
    s.oninput=function(){query=s.value.trim().toLowerCase();renderTree()};
    bw.appendChild(s);
    var ex=el('button','btn','Expand all');ex.type='button';ex.onclick=function(){collapsed.clear();persist();renderTree()};
    var co=el('button','btn','Collapse all');co.type='button';co.onclick=function(){walk(data,[],function(v,p){if(isObj(v)&&p.length)collapsed.add(pk(p))});persist();renderTree()};
    bw.appendChild(ex);bw.appendChild(co);
  }
  var st=el('span','status');st.id='status';bw.appendChild(st);
  var rv=el('button','btn','Revert');rv.type='button';rv.id='revert';rv.onclick=function(){data=JSON.parse(savedText);rawText=null;errMsg='';render()};
  var sb=el('button','btn primary');sb.type='button';sb.id='save';sb.appendChild(el('span',null,'Save'));sb.appendChild(el('span','k','⌘S'));sb.onclick=save;
  bw.appendChild(rv);bw.appendChild(sb);
  bar.appendChild(bw);sv.appendChild(bar);

  var box=el('div','tree-box wrap');
  if(mode==='tree'){
    var info=el('div','crumbs');info.id='crumbs';
    box.appendChild(info);
    var t=el('div','tree');t.id='tree';t.setAttribute('role','tree');box.appendChild(t);
    var hint=el('div','hint');hint.innerHTML='Click a value to edit it, double-click a key to rename it. Type <code>{}</code> in a value to turn it into an object. <code>+</code> adds an entry, <code>×</code> removes one. Changes stay on this page until you press Save.';
    box.appendChild(hint);
  }else{
    var ta=el('textarea','raw');ta.id='raw';ta.spellcheck=false;ta.setAttribute('aria-label','state.json');ta.value=rawText!==null?rawText:pretty(data);
    ta.oninput=function(){rawText=ta.value;try{data=JSON.parse(ta.value);errMsg=''}catch(e){errMsg=e.message}status()};
    ta.onkeydown=function(e){if(e.key==='Tab'){e.preventDefault();ta.setRangeText('  ',ta.selectionStart,ta.selectionEnd,'end');ta.oninput()}};
    box.appendChild(ta);
  }
  sv.appendChild(box);app.appendChild(sv);
  if(mode==='tree')renderTree();
  status();
}
function switchMode(m){
  if(m===mode)return;
  if(mode==='raw'&&errMsg){status();return}
  mode=m;rawText=null;persist();render();
}
function status(){
  var st=document.getElementById('status'),sb=document.getElementById('save'),rv=document.getElementById('revert');if(!st)return;
  var d=dirty();
  sb.disabled=!canSave||!d||!!errMsg||busy||editing;rv.disabled=!d||busy;
  if(errMsg){st.className='status bad';st.textContent='Invalid JSON: '+errMsg}
  else if(busy){st.className='status';st.textContent='Saving…'}
  else if(d){st.className='status dirty';st.textContent=canSave?'Unsaved changes':'Unsaved (view only)'}
  else{st.className='status ok';st.textContent=canSave?'Saved':'View only'}
}

/* ---------- tree ---------- */
function matches(v,key){
  if(!query)return false;
  if(String(key).toLowerCase().indexOf(query)>=0)return true;
  return !isObj(v)&&String(v).toLowerCase().indexOf(query)>=0;
}
function anyMatch(v,key){if(matches(v,key))return true;return isObj(v)&&Object.keys(v).some(function(k){return anyMatch(v[k],k)})}
function renderTree(){
  var t=document.getElementById('tree');if(!t)return;t.textContent='';
  var keys=Object.keys(data);var shown=0;
  keys.forEach(function(k){if(!query||anyMatch(data[k],k)){t.appendChild(node(k,data[k],[k],'obj'));shown++}});
  if(!shown)t.appendChild(el('div','empty',query?'Nothing matches “'+query+'”.':'state.json is empty.'));
  var add=el('div','row');add.appendChild(el('span','caret-sp'));var ab=el('button','btn','+ Add top-level entry');ab.type='button';ab.onclick=function(){addChild([])};add.appendChild(ab);t.appendChild(add);
  crumbs();status();
}
function crumbs(){
  var c=document.getElementById('crumbs');if(!c)return;c.textContent='';
  var path=selected?JSON.parse(selected):null;
  if(!path){c.appendChild(el('span',null,'Select a row to see where it sits.'));legend(c);return}
  c.appendChild(el('span',null,'state'));
  path.forEach(function(p,i){c.appendChild(el('span',null,'›'));c.appendChild(el(i===path.length-1?'b':'span',null,String(p)))});
  legend(c);
}
function legend(c){
  var l=el('div','legend');
  [['object','var(--t-obj)'],['text','var(--t-str)'],['number','var(--t-num)'],['true/false','var(--t-bool)'],['file / folder','var(--t-file)']].forEach(function(x){var s=el('span');var i=el('i');i.style.background=x[1];s.appendChild(i);s.appendChild(document.createTextNode(x[0]));l.appendChild(s)});
  c.appendChild(l);
}
function node(key,v,path,parentType){
  var id=pk(path),type=typeOf(v),container=isObj(v),n=container?Object.keys(v).length:0;
  var open=container&&n>0&&(query?true:!collapsed.has(id));
  var wrap=el('div','node');
  var row=el('div','row'+(open?' open':'')+(selected===id?' sel':'')+(matches(v,key)?' hit':''));
  row.tabIndex=0;row.setAttribute('role','treeitem');if(container&&n)row.setAttribute('aria-expanded',String(open));
  row.onclick=function(e){if(e.target.closest('button,input,.val,.pill,.toggle'))return;select(id)};
  row.onkeydown=function(e){if(e.target!==row)return;if(container&&n&&(e.key==='ArrowRight'||e.key==='ArrowLeft')){e.preventDefault();setOpen(id,e.key==='ArrowRight')}if(e.key==='Enter'&&container&&n){e.preventDefault();setOpen(id,!open)}};
  if(container&&n){var cb=el('button','caret');cb.type='button';cb.setAttribute('aria-label',open?'Collapse':'Expand');cb.appendChild(svgCaret());cb.onclick=function(){setOpen(id,!open)};row.appendChild(cb)}
  else row.appendChild(el('span','caret-sp'));
  var fk=container&&!Array.isArray(v)?fileKind(path.slice(0,-1),key):null;
  var ico=el('span','ico '+(fk||type));
  ico.textContent=fk==='folder'?'▤':fk==='file'?'≡':type==='obj'?'{}':type==='arr'?'[]':type==='str'?'Aa':type==='num'?'#':type==='bool'?'◐':'∅';
  ico.title=fk||({obj:'object',arr:'list',str:'text',num:'number',bool:'true/false',null:'empty'})[type];
  row.appendChild(ico);
  var kEl=el('span','key'+(parentType==='arr'?' idx':''),String(key));
  if(parentType!=='arr'){kEl.title='Double-click to rename';kEl.ondblclick=function(){editKey(kEl,path)}}
  row.appendChild(kEl);
  if(!container){row.appendChild(el('span','colon',':'));row.appendChild(valueEl(v,path,key))}
  else if(!n)row.appendChild(el('span','empty',fk==='file'?'empty file':fk==='folder'?'empty folder':(type==='arr'?'empty list':'empty')));
  else row.appendChild(el('span','meta',n+(type==='arr'?(n===1?' item':' items'):(n===1?' key':' keys'))));
  var acts=el('span','acts');
  if(container){var a=el('button',null,'+');a.type='button';a.title='Add an entry inside';a.setAttribute('aria-label','Add an entry inside '+key);a.onclick=function(){addChild(path)};acts.appendChild(a)}
  var d=el('button','del','×');d.type='button';d.title='Remove';d.setAttribute('aria-label','Remove '+key);d.onclick=function(){removeAt(path)};acts.appendChild(d);
  row.appendChild(acts);
  wrap.appendChild(row);
  if(open){var kids=el('div','kids');kids.setAttribute('role','group');Object.keys(v).forEach(function(k){if(!query||anyMatch(v[k],k))kids.appendChild(node(Array.isArray(v)?+k:k,v[k],path.concat(Array.isArray(v)?+k:k),type))});wrap.appendChild(kids)}
  return wrap;
}
function valueEl(v,path,key){
  var type=typeOf(v),e;
  if(type==='bool'){e=el('button','toggle'+(v?' on':''));e.type='button';e.appendChild(el('i'));e.appendChild(document.createTextNode(String(v)));e.setAttribute('aria-pressed',String(v));e.onclick=function(){setAt(path,!v);changed()};return e}
  if(key==='state'&&type==='str'&&STATE_PILLS[v]){e=el('span','pill '+v,v);}
  else e=el('span','val '+type,type==='null'?'null':String(v));
  e.tabIndex=0;e.title='Click to edit';
  e.onclick=function(){editVal(e,path,v)};
  e.onkeydown=function(ev){if(ev.key==='Enter'){ev.preventDefault();editVal(e,path,v)}};
  return e;
}
function inputFor(text,onCommit){
  var i=el('input','edit');i.value=text;i.size=Math.max(6,Math.min(60,text.length+2));editing=true;status();
  var done=false;
  function fin(ok){if(done)return;done=true;editing=false;if(ok)onCommit(i.value);else renderTree()}
  i.onkeydown=function(e){if(e.key==='Enter'){e.preventDefault();fin(true)}else if(e.key==='Escape'){e.preventDefault();fin(false)}};
  i.oninput=function(){i.size=Math.max(6,Math.min(60,i.value.length+2))};
  i.onblur=function(){fin(true)};
  return i;
}
function editVal(e,path,v){
  var i=inputFor(v===null?'null':String(v),function(txt){
    var nv;
    if(txt.trim()==='{}')nv={};else if(txt.trim()==='[]')nv=[];
    else if(typeof v==='string')nv=txt;
    else{try{nv=JSON.parse(txt)}catch(_){nv=txt}if(isObj(nv))nv=txt}
    setAt(path,nv);changed();
  });
  e.replaceWith(i);i.focus();i.select();
}
function editKey(kEl,path){
  var old=path[path.length-1];
  var i=inputFor(String(old),function(txt){
    var name=txt.trim();var parent=getAt(path.slice(0,-1));
    if(!name||name===old){renderTree();return}
    if(Object.prototype.hasOwnProperty.call(parent,name)){renderTree();flash('“'+name+'” already exists here.');return}
    var rebuilt={};Object.keys(parent).forEach(function(k){rebuilt[k===old?name:k]=parent[k]});
    setAt(path.slice(0,-1),rebuilt);
    var np=pk(path.slice(0,-1).concat(name));if(collapsed.has(pk(path))){collapsed.delete(pk(path));collapsed.add(np)}selected=np;
    changed();
  });
  kEl.replaceWith(i);i.focus();i.select();
}
function addChild(path){
  var target=getAt(path),np;
  if(Array.isArray(target)){target.push('');np=path.concat(target.length-1)}
  else{var base='new_key',name=base,n=2;while(Object.prototype.hasOwnProperty.call(target,name))name=base+'_'+(n++);target[name]={};np=path.concat(name)}
  collapsed.delete(pk(path));selected=pk(np);changed();
  var row=document.querySelector('.row.sel .key');if(row&&!Array.isArray(target))editKey(row,np);
}
function removeAt(path){
  var parent=getAt(path.slice(0,-1)),k=path[path.length-1];
  if(Array.isArray(parent))parent.splice(k,1);else delete parent[k];
  selected=null;changed();flash('Removed '+k+'. Revert brings it back until you save.');
}
function select(id){selected=selected===id?null:id;renderTree();var r=document.querySelector('.row.sel');if(r)r.focus({preventScroll:true})}
function setOpen(id,o){if(o)collapsed.delete(id);else collapsed.add(id);selected=id;persist();renderTree();var r=document.querySelector('.row.sel');if(r)r.focus({preventScroll:true})}
function changed(){persist();renderTree()}
function flash(msg){var st=document.getElementById('status');if(!st)return;st.className='status';st.textContent=msg;setTimeout(status,2600)}

/* ---------- save: republish this page with the new state ---------- */
function buildDoc(text){
  return '<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>'+RESET+'</style></head><body>'+
    '<title>'+document.title+'</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n<link rel="stylesheet" href="'+FONTS+'">\n'+
    '<style id="page-style">'+document.getElementById('page-style').textContent+'</style>\n<div id="app"></div>\n'+
    '<script type="application/json" id="page-data">'+text.replace(/<\//g,'<\\/')+'<\/script>\n'+
    '<script id="page-app">'+document.getElementById('page-app').textContent+'<\/script></body></html>';
}
function save(){
  if(!api||errMsg||busy||!dirty())return;
  var text=pretty(data);busy=true;status();
  api.publish(buildDoc(text)).then(function(){savedText=text;rawText=null;busy=false;status()},function(e){
    busy=false;var c=e&&e.code;
    if(c==='not_granted'||c==='not_writer'){canSave=false;status()}
    else{status();var st=document.getElementById('status');st.className='status bad';st.textContent=c==='conflict'?'Someone saved first; reloading their version.':'Could not save: '+((e&&e.message)||c||'unknown error')}
  });
}
document.addEventListener('keydown',function(e){if((e.metaKey||e.ctrlKey)&&e.key==='s'){e.preventDefault();if(view==='state')save()}});

render();
if(window.claude&&claude.use){claude.use('artifact').then(function(a){api=a;canSave=!!a;status()},function(){})}
})();
