(function () {
  var d = document, b = d.body, base = b.dataset.base || '';
  function $(s, r) { return (r || d).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || d).querySelectorAll(s)); }
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) {} }
  function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }

  // tema
  $('#theme').onclick = function () {
    var cur = d.documentElement.dataset.theme || (matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light');
    var n = cur === 'dark' ? 'light' : 'dark';
    d.documentElement.dataset.theme = n; store('lighthub-theme', n);
  };

  // menú móvil
  var menu = $('#menu'), scrim = $('#scrim');
  function toggle(open) {
    b.classList.toggle('open', open); scrim.hidden = !open;
    menu.setAttribute('aria-expanded', open); if (open) $('#nav .trow').focus({ preventScroll: true });
  }
  menu.onclick = function () { toggle(!b.classList.contains('open')); };
  scrim.onclick = function () { toggle(false); };
  d.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { toggle(false); closeRes(); }
    if (e.key === '/' && !/input|textarea/i.test(e.target.tagName)) { e.preventDefault(); q.focus(); }
  });

  // copiar
  d.addEventListener('click', function (e) {
    var t = e.target; if (!t.classList.contains('copy')) return;
    var label = b.dataset.copy || 'Copy', done = b.dataset.copied || 'Copied';
    var txt = $('code', t.parentNode).textContent;
    (navigator.clipboard ? navigator.clipboard.writeText(txt) : Promise.reject()).then(function () {
      t.textContent = done; setTimeout(function () { t.textContent = label; }, 1400);
    }, function () { t.textContent = '…'; });
  });

  // resaltado mínimo
  var KW = /\b(const|let|var|function|return|if|else|for|while|import|from|export|default|class|extends|new|this|async|await|type|interface|static|true|false|null|undefined|def|in|of|try|catch|throw|as|implements|public|private|readonly|accessor)\b/;
  var RX = new RegExp('(\\/\\/[^\\n]*|\\/\\*[\\s\\S]*?\\*\\/|^\\s*#[^\\n]*)|("(?:\\\\.|[^"\\\\])*"|\'(?:\\\\.|[^\'\\\\])*\'|`(?:\\\\.|[^`\\\\])*`)|(' + KW.source + ')|(\\b\\d+(?:\\.\\d+)?\\b)', 'gm');
  $$('.code code, .qc code').forEach(function (c) {
    var lang = (c.className.match(/language-(\w+)/) || [])[1] || 'js';
    if (lang === 'text') return;
    var s = c.textContent, o = '', last = 0, m; RX.lastIndex = 0;
    while ((m = RX.exec(s))) {
      o += esc(s.slice(last, m.index));
      var cls = m[1] ? 't-c' : m[2] ? 't-s' : m[3] ? 't-k' : 't-n';
      if ((lang === 'html' || lang === 'css') && (cls === 't-k' || cls === 't-n')) { o += esc(m[0]); last = RX.lastIndex; continue; }
      o += '<span class="' + cls + '">' + esc(m[0]) + '</span>'; last = RX.lastIndex;
    }
    c.innerHTML = o + esc(s.slice(last));
  });

  // pestañas
  var tabs = $$('[role=tab]'), panels = $$('.panel');
  var used = {};
  function select(name, focus) {
    var ok = false;
    tabs.forEach(function (t) {
      var on = t.id === 't-' + name; ok = ok || on;
      t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1; if (on && focus) t.focus();
    });
    if (!ok) return false;
    panels.forEach(function (p) { p.hidden = p.id !== 'p-' + name; });
    if (name === 'prueba' && !used.prueba) { used.prueba = 1; $$('.try').forEach(run); }
    return true;
  }
  function fromHash() {
    var h = decodeURIComponent(location.hash.slice(1));
    if (!tabs.length) return;
    if (select(h)) return;
    var el = h && d.getElementById(h);
    var p = el && el.closest('.panel');
    select(p ? p.id.slice(2) : 'leccion');
    if (el) el.scrollIntoView();
  }
  tabs.forEach(function (t, i) {
    t.onclick = function () { select(t.id.slice(2)); history.replaceState(null, '', '#' + t.id.slice(2)); };
    t.onkeydown = function (e) {
      var n = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : -1;
      if (n >= 0 && n < tabs.length) { e.preventDefault(); select(tabs[n].id.slice(2), true); }
    };
  });
  addEventListener('hashchange', fromHash);

  // test
  function shuffle(box) {
    var o = $$('.o', box); o.sort(function () { return Math.random() - .5; }).forEach(function (x) { box.appendChild(x); });
  }
  $$('.quiz').forEach(function (qz) {
    var qs = $$('.q', qz), score = $('.score', qz), retry = $('.retry', qz), bar = $('.bar i', qz), right = 0, done = 0;
    function reset() {
      right = 0; done = 0; score.textContent = ''; retry.hidden = true; bar.style.width = '0';
      qs.forEach(function (q) {
        $$('.o', q).forEach(function (o) { o.disabled = false; o.className = 'o opt'; }); $('.fb', q).hidden = true; q.dataset.done = ''; shuffle($('.opts', q));
      });
    }
    qs.forEach(function (q) {
      $$('.o', q).forEach(function (o) {
        o.onclick = function () {
          if (q.dataset.done) return; q.dataset.done = 1; done++;
          var good = o.hasAttribute('data-c'); if (good) right++;
          $$('.o', q).forEach(function (x) { x.disabled = true; if (x.hasAttribute('data-c')) x.classList.add('ok'); });
          if (!good) o.classList.add('ko');
          var fb = $('.fb', q); fb.hidden = false; fb.textContent = (good ? qz.dataset.ok : qz.dataset.ko) + ' ' + fb.textContent.replace(/^(¡Correcto!|Incorrecto\.|Correct!|Not quite\.) /, '');
          bar.style.width = (done / qs.length * 100) + '%';
          if (done === qs.length) { score.textContent = qz.dataset.score + ': ' + right + '/' + qs.length; retry.hidden = false; }
        };
      });
    });
    retry.onclick = reset; reset();
  });

  // pruébalo
  var IMPORTS = { imports: {
    'lit': 'https://esm.sh/lit@3.2.1', 'lit/': 'https://esm.sh/lit@3.2.1/',
    '@lit/reactive-element': 'https://esm.sh/@lit/reactive-element@2.0.4', '@lit/reactive-element/': 'https://esm.sh/@lit/reactive-element@2.0.4/',
    'lit-html': 'https://esm.sh/lit-html@3.2.1', 'lit-html/': 'https://esm.sh/lit-html@3.2.1/',
    '@lit/context': 'https://esm.sh/@lit/context@1.1.3', '@lit/task': 'https://esm.sh/@lit/task@1.0.1' } };
  var VARS = ['--bg', '--surface', '--surface-2', '--text', '--muted', '--line', '--primary', '--primary-ink', '--primary-soft', '--ok', '--bad', '--warn'];
  var seq = 0;
  function run(sec) {
    var id = sec.dataset.id = sec.dataset.id || String(++seq), cs = getComputedStyle(d.documentElement);
    var vars = VARS.map(function (v) { return v + ':' + cs.getPropertyValue(v); }).join(';');
    var js = $('.tj', sec).value.replace(/<\/script/gi, '<\\/script');
    var doc = '<!doctype html><html><head><meta charset="utf-8"><script type="importmap">' + JSON.stringify(IMPORTS) + '<\/script>' +
      '<style>:root{' + vars + '}body{font:15px/1.5 system-ui;color:var(--text);background:var(--surface);margin:0;padding:12px}button{font:inherit;padding:6px 12px;border-radius:8px;border:1px solid var(--line);background:var(--surface-2);color:var(--text);cursor:pointer}pre{white-space:pre-wrap;background:var(--surface-2);padding:8px;border-radius:8px}</style>' +
      '<script>(function(){function s(a){return a.map(function(x){try{return typeof x==="string"?x:JSON.stringify(x)}catch(e){return String(x)}}).join(" ")}' +
      '["log","warn","error"].forEach(function(k){var o=console[k];console[k]=function(){parent.postMessage({lighthub:' + id + ',k:k,t:s([].slice.call(arguments))},"*");o.apply(console,arguments)}});' +
      'addEventListener("error",function(e){parent.postMessage({lighthub:' + id + ',k:"error",t:e.message},"*")})})()<\/script></head><body>' +
      $('.th', sec).value + '<script type="module">' + js + '<\/script></body></html>';
    var con = $('.con', sec); con.textContent = ''; con.hidden = true;
    $('.out', sec).srcdoc = doc;
  }
  addEventListener('message', function (e) {
    if (!e.data || !e.data.lighthub) return;
    var sec = $$('.try').filter(function (s) { return s.dataset.id === String(e.data.lighthub); })[0]; if (!sec) return;
    var con = $('.con', sec); con.hidden = false;
    var line = d.createElement('div'); if (e.data.k === 'error') line.className = 'e'; line.textContent = e.data.t; con.appendChild(line);
  });
  $$('.try').forEach(function (sec) {
    var h = $('.th', sec).value, j = $('.tj', sec).value;
    $('.run', sec).onclick = function () { run(sec); };
    $('.reset', sec).onclick = function () { $('.th', sec).value = h; $('.tj', sec).value = j; run(sec); };
    $$('textarea', sec).forEach(function (ta) {
      ta.addEventListener('keydown', function (e) {
        if (e.key === 'Tab' && !e.shiftKey) { e.preventDefault(); var s = ta.selectionStart; ta.setRangeText('  ', s, ta.selectionEnd, 'end'); }
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') { e.preventDefault(); run(sec); }
      });
    });
  });

  // búsqueda
  var q = $('#q'), res = $('#res'), idx = null, sel = -1;
  function norm(s) { return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
  function closeRes() { res.hidden = true; sel = -1; }
  function load() {
    if (idx) return Promise.resolve();
    return fetch(b.dataset.search).then(function (r) { return r.json(); }).then(function (j) {
      idx = j.map(function (p) { p.n = norm(p.t + ' ' + p.d + ' ' + p.x); p.tn = norm(p.t); return p; });
    }).catch(function () { idx = []; });
  }
  function run2() {
    var terms = norm(q.value).split(/\s+/).filter(Boolean);
    if (!terms.length) return closeRes();
    var hits = idx.map(function (p) {
      var sc = 0;
      for (var i = 0; i < terms.length; i++) { if (p.n.indexOf(terms[i]) < 0) return null; sc += p.tn.indexOf(terms[i]) >= 0 ? 5 : 1; }
      return { p: p, sc: sc };
    }).filter(Boolean).sort(function (a, b) { return b.sc - a.sc; }).slice(0, 8);
    res.innerHTML = hits.length ? hits.map(function (h) {
      return '<li><a href="' + base + h.p.u + '">' + esc(h.p.t) + '<small>' + esc(h.p.s) + '</small></a></li>';
    }).join('') : '<li style="padding:8px 10px;color:var(--muted)">—</li>';
    res.hidden = false; sel = -1;
  }
  q.addEventListener('input', function () { load().then(run2); });
  q.addEventListener('focus', function () { load(); });
  q.addEventListener('keydown', function (e) {
    var a = $$('a', res); if (!a.length || res.hidden) return;
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault(); sel = (sel + (e.key === 'ArrowDown' ? 1 : -1) + a.length) % a.length;
      a.forEach(function (x, i) { x.classList.toggle('on', i === sel); });
    } else if (e.key === 'Enter' && a[Math.max(sel, 0)]) { location.href = a[Math.max(sel, 0)].href; }
  });
  d.addEventListener('click', function (e) { if (!e.target.closest('#q,#res')) closeRes(); });
  // lo leído: se guarda en el navegador y alimenta marcas y progreso
  var seen = {};
  try { seen = JSON.parse(store('lighthub-seen') || '{}'); } catch (e) {}
  if (b.dataset.k) { seen[b.dataset.k] = 1; store('lighthub-seen', JSON.stringify(seen)); }
  $$('.trow').forEach(function (a) { if (seen[a.dataset.k]) a.classList.add('seen'); });
  $$('.card[data-sec]').forEach(function (c) {
    var rows = $$('#side .grp[data-sec="' + c.dataset.sec + '"] .trow'), n = 0, next = null;
    rows.forEach(function (a) { if (seen[a.dataset.k]) n++; else if (!next) next = a; });
    $('.bar i', c).style.width = (rows.length ? n / rows.length * 100 : 0) + '%';
    var rd = $('.rd', c); rd.textContent = rd.dataset.tpl.replace('{a}', n).replace('{b}', rows.length);
    var go = $('.go', c);
    if (n && next) { go.href = next.href; go.textContent = go.dataset.cont; }
  });
  var cur = $('#side .trow.cur'), side = $('#side'); if (cur) side.scrollTop = Math.max(0, cur.offsetTop - side.clientHeight / 3);
  fromHash();
})();
