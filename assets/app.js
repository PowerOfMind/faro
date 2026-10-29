(function () {
  var d = document, b = d.body, base = b.dataset.base || '';
  function $(s, r) { return (r || d).querySelector(s); }
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) {} }

  // tema
  $('#theme').onclick = function () {
    var cur = d.documentElement.dataset.theme || (matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light');
    var n = cur === 'dark' ? 'light' : 'dark';
    d.documentElement.dataset.theme = n; store('faro-theme', n);
  };

  // menú móvil
  var menu = $('#menu'), scrim = $('#scrim');
  function toggle(open) {
    b.classList.toggle('open', open); scrim.hidden = !open;
    menu.setAttribute('aria-expanded', open); if (open) $('#nav a').focus({ preventScroll: true });
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
    var txt = $('code', t.parentNode).textContent;
    (navigator.clipboard ? navigator.clipboard.writeText(txt) : Promise.reject()).then(function () {
      t.textContent = 'Copiado'; setTimeout(function () { t.textContent = 'Copiar'; }, 1400);
    }, function () { t.textContent = 'Selecciona y copia'; });
  });

  // resaltado mínimo
  var KW = /\b(const|let|var|function|return|if|else|for|while|import|from|export|default|class|extends|new|this|async|await|type|interface|static|true|false|null|undefined|def|in|of|try|catch|throw|as|implements|public|private|readonly)\b/;
  var RX = new RegExp('(\\/\\/[^\\n]*|\\/\\*[\\s\\S]*?\\*\\/|^\\s*#[^\\n]*)|("(?:\\\\.|[^"\\\\])*"|\'(?:\\\\.|[^\'\\\\])*\'|`(?:\\\\.|[^`\\\\])*`)|(' + KW.source + ')|(\\b\\d+(?:\\.\\d+)?\\b)', 'gm');
  function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
  d.querySelectorAll('.code code').forEach(function (c) {
    var lang = (c.className.match(/language-(\w+)/) || [])[1] || '';
    if (/^(html|css|json|text|)$/.test(lang) && lang !== 'json') { if (lang !== 'css' && lang !== 'html') return; }
    var s = c.textContent, o = '', last = 0, m; RX.lastIndex = 0;
    while ((m = RX.exec(s))) {
      o += esc(s.slice(last, m.index));
      var cls = m[1] ? 't-c' : m[2] ? 't-s' : m[3] ? 't-k' : 't-n';
      if (lang === 'html' || lang === 'css') { if (cls === 't-k' || cls === 't-n') { o += esc(m[0]); last = RX.lastIndex; continue; } }
      o += '<span class="' + cls + '">' + esc(m[0]) + '</span>'; last = RX.lastIndex;
    }
    c.innerHTML = o + esc(s.slice(last));
  });

  // búsqueda
  var q = $('#q'), res = $('#res'), idx = null, sel = -1;
  function norm(s) { return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
  function closeRes() { res.hidden = true; sel = -1; }
  function load() {
    if (idx) return Promise.resolve();
    return fetch(base + 'search.json').then(function (r) { return r.json(); }).then(function (j) {
      idx = j.map(function (p) { p.n = norm(p.t + ' ' + p.d + ' ' + p.x); p.tn = norm(p.t); return p; });
    }).catch(function () { idx = []; });
  }
  function run() {
    var terms = norm(q.value).split(/\s+/).filter(Boolean);
    if (!terms.length) return closeRes();
    var hits = idx.map(function (p) {
      var sc = 0;
      for (var i = 0; i < terms.length; i++) {
        if (p.n.indexOf(terms[i]) < 0) return null;
        sc += p.tn.indexOf(terms[i]) >= 0 ? 5 : 1;
      }
      return { p: p, sc: sc };
    }).filter(Boolean).sort(function (a, b) { return b.sc - a.sc; }).slice(0, 8);
    res.innerHTML = hits.length ? hits.map(function (h) {
      return '<li><a href="' + base + h.p.u + '">' + esc(h.p.t) + '<small>' + esc(h.p.s) + '</small></a></li>';
    }).join('') : '<li style="padding:8px 10px;color:var(--muted)">Sin resultados</li>';
    res.hidden = false; sel = -1;
  }
  q.addEventListener('input', function () { load().then(run); });
  q.addEventListener('focus', function () { load(); });
  q.addEventListener('keydown', function (e) {
    var a = res.querySelectorAll('a'); if (!a.length || res.hidden) return;
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault(); sel = (sel + (e.key === 'ArrowDown' ? 1 : -1) + a.length) % a.length;
      a.forEach(function (x, i) { x.classList.toggle('on', i === sel); });
    } else if (e.key === 'Enter' && a[Math.max(sel, 0)]) { location.href = a[Math.max(sel, 0)].href; }
  });
  d.addEventListener('click', function (e) { if (!e.target.closest('.search')) closeRes(); });
})();
