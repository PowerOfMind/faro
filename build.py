#!/usr/bin/env python3
"""Generador estático sin dependencias. Uso: python build.py  ->  dist/
Contenido: content/<seccion>/<NN-slug>.md  (cabecera: title, desc, pkgs, updated)."""
import html, json, os, re, shutil, sys, unicodedata
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "dist"
SITE = "Faro"
LEMA = "Atajos para cuando la IA no te da la solución"
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")

SECCIONES = [
    ("ia", "IA y agentes", "Usar Claude, ChatGPT y compañía; skills, MCP y agentes."),
    ("atascado", "Cuando la IA no resuelve", "Errores que se repiten y el método para salir del bucle."),
    ("seguridad", "Seguridad con IA", "Qué se rompe cuando una app se genera con IA y cómo evitarlo."),
    ("seo-geo", "SEO y GEO", "Que te encuentren buscadores y que te citen los modelos."),
    ("lit", "Lit y Web Components", "Resumen de Lit 3: reactividad, plantillas, estilos y datos."),
    ("js-ts", "JavaScript y TypeScript", "Lo esencial que más se busca."),
    ("frameworks", "React y Angular", "Cómo pensar cada uno y sus trampas."),
    ("librerias", "Librerías rápidas", "Qué usar para cada problema, en una línea."),
]

def esc(s): return html.escape(s, quote=False)

def slugify(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

# ---------- Markdown mínimo ----------
def inline(t, base):
    out = []
    for p in re.split(r"(`[^`]+`)", t):
        if len(p) > 1 and p[0] == "`" and p[-1] == "`":
            out.append("<code>" + esc(p[1:-1]) + "</code>")
            continue
        p = esc(p)
        p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
        p = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", p)
        def link(m):
            u = m.group(2)
            if u.startswith("@/"):
                return f'<a href="{base}{u[2:]}.html">{m.group(1)}</a>'
            ext = ' rel="noopener" target="_blank"' if u.startswith("http") else ""
            return f'<a href="{u}"{ext}>{m.group(1)}</a>'
        p = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, p)
        out.append(p)
    return "".join(out)

BLOCK = re.compile(r"^(```|#{2,3} |\||>|\s*([-*]|\d+\.) )")
CALLOUTS = {"TIP": "Truco", "WARN": "Cuidado", "AI": "Con IA", "SEC": "Seguridad", "NOTE": "Nota"}

def md(src, base, heads=None):
    L, i, h = src.split("\n"), 0, []
    while i < len(L):
        l = L[i]
        if not l.strip():
            i += 1
        elif l.startswith("```"):
            lang, buf = l[3:].strip(), []
            i += 1
            while i < len(L) and not L[i].startswith("```"):
                buf.append(L[i]); i += 1
            i += 1
            h.append(f'<div class="code" data-lang="{esc(lang)}"><button class="copy" type="button">Copiar</button>'
                     f'<pre><code class="language-{esc(lang)}">{esc(chr(10).join(buf))}</code></pre></div>')
        elif re.match(r"#{2,3} ", l):
            n = 2 if l.startswith("## ") else 3
            txt = l[n + 1:].strip()
            sid = slugify(txt)
            if heads is not None and n == 2: heads.append((sid, txt))
            h.append(f'<h{n} id="{sid}"><a class="anc" href="#{sid}" aria-label="Enlace a la sección">#</a>{inline(txt, base)}</h{n}>')
            i += 1
        elif l.startswith("|"):
            rows = []
            while i < len(L) and L[i].startswith("|"):
                rows.append([c.strip().replace("§", "|") for c in L[i].strip().strip("|").replace("\\|", "§").split("|")]); i += 1
            head, body = rows[0], [r for r in rows[2:]]
            t = "<div class='tbl'><table><thead><tr>" + "".join(f"<th>{inline(c, base)}</th>" for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{inline(c, base)}</td>" for c in r) + "</tr>" for r in body)
            h.append(t + "</tbody></table></div>")
        elif l.startswith(">"):
            q = []
            while i < len(L) and L[i].startswith(">"):
                q.append(re.sub(r"^> ?", "", L[i])); i += 1
            m = re.match(r"\[!(\w+)\]\s*(.*)", q[0])
            if m and m.group(1) in CALLOUTS:
                k = m.group(1)
                rest = ([m.group(2)] if m.group(2) else []) + q[1:]
                h.append(f'<aside class="callout {k.lower()}"><b>{CALLOUTS[k]}</b>{md(chr(10).join(rest), base)}</aside>')
            else:
                h.append("<blockquote>" + md("\n".join(q), base) + "</blockquote>")
        elif re.match(r"\s*([-*]|\d+\.) ", l):
            tag = "ol" if re.match(r"\s*\d+\.", l) else "ul"
            items = []
            while i < len(L) and re.match(r"\s*([-*]|\d+\.) ", L[i]):
                items.append(re.sub(r"^\s*([-*]|\d+\.) ", "", L[i])); i += 1
            h.append(f"<{tag}>" + "".join(f"<li>{inline(x, base)}</li>" for x in items) + f"</{tag}>")
        else:
            p = []
            while i < len(L) and L[i].strip() and not (p and BLOCK.match(L[i])):
                p.append(L[i].strip()); i += 1
            h.append(f"<p>{inline(' '.join(p), base)}</p>")
    return "\n".join(h)

# ---------- Carga ----------
def parse(path):
    raw = path.read_text(encoding="utf-8")
    meta, body = {}, raw
    if raw.startswith("---"):
        _, fm, body = raw.split("---", 2)
        for ln in fm.strip().splitlines():
            k, _, v = ln.partition(":")
            meta[k.strip()] = v.strip().replace('"', "")
    return meta, body.strip()

def cargar():
    pages = []
    for sec, stitle, _ in SECCIONES:
        d = ROOT / "content" / sec
        for f in sorted(d.glob("*.md")) if d.exists() else []:
            meta, body = parse(f)
            slug = re.sub(r"^\d+-", "", f.stem)
            pages.append(dict(sec=sec, stitle=stitle, slug=slug, url=f"{sec}/{slug}.html", body=body,
                              title=meta.get("title", slug), desc=meta.get("desc", ""),
                              pkgs=[p.strip() for p in meta.get("pkgs", "").split(",") if p.strip()],
                              updated=meta.get("updated", "")))
    return pages

# ---------- Plantillas ----------
def sidebar(pages, base, cur):
    s = ["<nav id='nav' aria-label='Temas'>"]
    for sec, st, _ in SECCIONES:
        ps = [p for p in pages if p["sec"] == sec]
        if not ps: continue
        op = " open" if cur and cur["sec"] == sec else ""
        s.append(f"<details{op}><summary>{esc(st)}</summary><ul>")
        for p in ps:
            c = ' aria-current="page"' if cur and p is cur else ""
            s.append(f'<li><a href="{base}{p["url"]}"{c}>{esc(p["title"])}</a></li>')
        s.append("</ul></details>")
    s.append("</nav>")
    return "".join(s)

def versiones(p, vers):
    if not p["pkgs"]: return ""
    rows = []
    for k in p["pkgs"]:
        v = vers.get("pkgs", {}).get(k)
        rows.append(f"<li><code>{esc(k)}</code> <span>{esc(v['v']) if v else 'sin comprobar'}</span></li>")
    return (f"<aside class='vers'><b>Versiones en npm</b> (comprobado {esc(vers.get('checked', '—'))})"
            f"<ul>{''.join(rows)}</ul></aside>")

def shell(pages, base, cur, title, desc, main, canon_path, ld="", index=False):
    full = f"{title} · {SITE}" if cur else f"{SITE} · {LEMA}"
    canon = f'<link rel="canonical" href="{SITE_URL}/{canon_path}">' if SITE_URL else ""
    og = f'<meta property="og:url" content="{SITE_URL}/{canon_path}">' if SITE_URL else ""
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full)}</title><meta name="description" content="{html.escape(desc)}">{canon}
<meta property="og:title" content="{html.escape(full)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="{'article' if cur else 'website'}">{og}
<meta name="theme-color" content="#0b1b2b"><link rel="icon" href="{base}assets/icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{base}assets/style.css">{ld}
<script>try{{var t=localStorage.getItem('faro-theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head><body data-base="{base}">
<a class="skip" href="#main">Saltar al contenido</a>
<header class="top"><button id="menu" class="ib" aria-controls="nav" aria-expanded="false" aria-label="Abrir menú">☰</button>
<a class="brand" href="{base}index.html"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3 7h-6zM9 9h6l1 11H8zM3 22h18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>{SITE}</a>
<div class="search"><input id="q" type="search" placeholder="Buscar (pulsa /)" aria-label="Buscar" autocomplete="off"><ul id="res" hidden></ul></div>
<button id="theme" class="ib" aria-label="Cambiar tema">◐</button></header>
<div class="wrap"><aside class="side">{sidebar(pages, base, cur)}</aside><div id="scrim" hidden></div>
<main id="main">{main}</main></div>
<footer>{SITE} · contenido estático, revisado cada semana contra la documentación oficial. <a href="{base}novedades.html">Novedades</a></footer>
<script src="{base}assets/app.js" defer></script></body></html>"""

def pagina(p, pages, vers):
    base = "../"
    heads = []
    body = md(p["body"], base, heads)
    toc = ""
    if len(heads) > 2:
        toc = "<nav class='toc' aria-label='En esta página'><b>En esta página</b>" + "".join(f'<a href="#{i}">{esc(t.replace(chr(96), ""))}</a>' for i, t in heads) + "</nav>"
    idx = [x for x in pages if x["sec"] == p["sec"]]
    k = idx.index(p)
    prev = f'<a href="{base}{idx[k-1]["url"]}">← {esc(idx[k-1]["title"])}</a>' if k else "<span></span>"
    nxt = f'<a href="{base}{idx[k+1]["url"]}">{esc(idx[k+1]["title"])} →</a>' if k + 1 < len(idx) else "<span></span>"
    upd = p["updated"] or date.today().isoformat()
    main = (f'<article><p class="crumb"><a href="{base}index.html">Inicio</a> / {esc(p["stitle"])}</p><h1>{esc(p["title"])}</h1>'
            f'<p class="lead">{esc(p["desc"])}</p>{toc}{body}{versiones(p, vers)}'
            f'<p class="meta">Revisado: {esc(upd)}</p><div class="pn">{prev}{nxt}</div></article>')
    ld = ('<script type="application/ld+json">' + json.dumps({
        "@context": "https://schema.org", "@type": "TechArticle", "headline": p["title"], "description": p["desc"],
        "inLanguage": "es", "dateModified": upd, **({"url": f"{SITE_URL}/{p['url']}"} if SITE_URL else {})
    }, ensure_ascii=False) + "</script>")
    return shell(pages, base, p, p["title"], p["desc"], main, p["url"], ld)

def portada(pages, vers):
    cards = []
    for sec, st, d in SECCIONES:
        ps = [p for p in pages if p["sec"] == sec]
        if not ps: continue
        li = "".join(f'<li><a href="{x["url"]}">{esc(x["title"])}</a></li>' for x in ps[:5])
        mas = f' <a class="more" href="{ps[0]["url"]}">Ver los {len(ps)} →</a>' if len(ps) > 5 else ""
        cards.append(f"<section class='card'><h2>{esc(st)}</h2><p>{esc(d)}</p><ul>{li}</ul>{mas}</section>")
    main = (f"<div class='hero'><h1>{SITE}</h1><p class='lead'>{LEMA}. Resúmenes cortos, con código que se copia y "
            f"los fallos típicos. Se genera como sitio estático y se contrasta cada semana con la documentación oficial "
            f"(última comprobación: {esc(vers.get('checked', '—'))}).</p></div><div class='grid'>{''.join(cards)}</div>")
    return shell(pages, "", None, SITE, LEMA + ". Guías breves de Lit, JS/TS, React, Angular, IA, seguridad y SEO/GEO.", main, "index.html")

def novedades(pages, vers):
    path = ROOT / "data" / "fuentes.json"
    src = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    rows = "".join(f"<tr><td><a href='{esc(v.get('url',''))}' rel='noopener' target='_blank'>{esc(k)}</a></td><td>{esc(v.get('ultimo','—'))}</td></tr>"
                   for k, v in src.get("fuentes", {}).items())
    main = (f"<article><h1>Novedades vigiladas</h1><p class='lead'>Último dato de cada fuente oficial, comprobado el {esc(vers.get('checked','—'))}. "
            f"Un flujo semanal compara y abre una incidencia si algo cambia.</p>"
            f"<div class='tbl'><table><thead><tr><th>Fuente</th><th>Último dato</th></tr></thead><tbody>{rows}</tbody></table></div></article>")
    return shell(pages, "", None, "Novedades", "Fuentes oficiales vigiladas", main, "novedades.html")

def main():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "assets", OUT / "assets")
    vp = ROOT / "data" / "versions.json"
    vers = json.loads(vp.read_text(encoding="utf-8")) if vp.exists() else {}
    pages = cargar()
    ok = {p["url"][:-5] for p in pages}
    mal = [(p["url"], m) for p in pages for m in re.findall(r"\(@/([^)]+)\)", p["body"]) if m not in ok]
    if mal:
        sys.exit("Enlaces rotos: " + ", ".join(f"{a} -> {b}" for a, b in mal))
    (OUT / "index.html").write_text(portada(pages, vers), encoding="utf-8")
    (OUT / "novedades.html").write_text(novedades(pages, vers), encoding="utf-8")
    idx = []
    for p in pages:
        (OUT / p["sec"]).mkdir(exist_ok=True)
        (OUT / p["url"]).write_text(pagina(p, pages, vers), encoding="utf-8")
        txt = re.sub(r"```.*?```", " ", p["body"], flags=re.S)
        txt = re.sub(r"[#*`|>\[\]()-]+", " ", txt)
        idx.append(dict(t=p["title"], s=p["stitle"], u=p["url"], d=p["desc"], x=re.sub(r"\s+", " ", txt)[:1500]))
    (OUT / "search.json").write_text(json.dumps(idx, ensure_ascii=False), encoding="utf-8")
    (OUT / "robots.txt").write_text("User-agent: *\nAllow: /\n" + (f"Sitemap: {SITE_URL}/sitemap.xml\n" if SITE_URL else ""))
    llms = [f"# {SITE}", f"> {LEMA}. Guías breves y verificadas contra documentación oficial.", ""]
    for sec, st, d in SECCIONES:
        ps = [p for p in pages if p["sec"] == sec]
        if ps:
            llms.append(f"## {st}")
            llms += [f"- [{p['title']}]({SITE_URL + '/' if SITE_URL else ''}{p['url']}): {p['desc']}" for p in ps]
            llms.append("")
    (OUT / "llms.txt").write_text("\n".join(llms), encoding="utf-8")
    if SITE_URL:
        urls = ["index.html", "novedades.html"] + [p["url"] for p in pages]
        (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            + "".join(f"<url><loc>{SITE_URL}/{u}</loc></url>" for u in urls) + "</urlset>")
    print(f"{len(pages)} páginas -> {OUT}")

if __name__ == "__main__":
    main()
