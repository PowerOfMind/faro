#!/usr/bin/env python3
"""Vigilante de novedades (sin dependencias).
1) Lee los paquetes npm citados en `pkgs:` de content/**/*.md y guarda su última versión en data/versions.json.
2) Lee las fuentes de data/fuentes.json (feeds Atom/RSS de releases y blogs oficiales) y guarda la entrada más reciente.
3) Si algo cambió, escribe data/changes.md (lo usa el flujo semanal para abrir una incidencia). Un fallo de red no rompe nada."""
import json, re, sys, urllib.parse, urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "lighthub-vigilante/1.0 (+https://github.com)"}

def get(url, timeout=20):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")

def paquetes():
    out = set()
    for f in (ROOT / "content").rglob("*.md"):
        m = re.search(r"^pkgs:\s*(.+)$", f.read_text(encoding="utf-8"), re.M)
        if m:
            out |= {p.strip().strip('"') for p in m.group(1).split(",") if p.strip()}
    return sorted(out)

def major(v): return v.split(".")[0] if v else ""

def main():
    hoy = date.today().isoformat()
    cambios = []

    vp = ROOT / "data" / "versions.json"
    vers = json.loads(vp.read_text(encoding="utf-8")) if vp.exists() else {"pkgs": {}}
    for p in paquetes():
        try:
            v = json.loads(get(f"https://registry.npmjs.org/{urllib.parse.quote(p, safe='@')}/latest"))["version"]
        except Exception as e:
            print(f"! {p}: {e}", file=sys.stderr)
            continue
        old = vers["pkgs"].get(p, {}).get("v")
        if old and old != v:
            marca = "**MAYOR**" if major(old) != major(v) else "menor/parche"
            cambios.append(f"- `{p}`: {old} → {v} ({marca})")
        vers["pkgs"][p] = {"v": v}
    vers["checked"] = hoy
    vp.write_text(json.dumps(vers, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")

    fp = ROOT / "data" / "fuentes.json"
    fu = json.loads(fp.read_text(encoding="utf-8"))
    for nombre, s in fu["fuentes"].items():
        try:
            xml = get(s["url"])
            bloque = re.search(r"<(entry|item)[\s>].*?</\1>", xml, re.S).group(0)
            titulo = re.sub(r"<!\[CDATA\[|\]\]>", "", re.search(r"<title[^>]*>(.*?)</title>", bloque, re.S).group(1)).strip()
        except Exception as e:
            print(f"! {nombre}: {e}", file=sys.stderr)
            continue
        if s.get("ultimo") and s["ultimo"] != titulo:
            cambios.append(f"- **{nombre}**: «{titulo}» ({s['url']})")
        s["ultimo"] = titulo
    fu["checked"] = hoy
    fp.write_text(json.dumps(fu, indent=1, ensure_ascii=False), encoding="utf-8")

    ch = ROOT / "data" / "changes.md"
    if cambios:
        ch.write_text(f"Novedades detectadas el {hoy}. Revisa las páginas afectadas (campo `pkgs:` o sección relacionada).\n\n" + "\n".join(cambios) + "\n", encoding="utf-8")
        print("\n".join(cambios))
    elif ch.exists():
        ch.unlink()
    print(f"OK {len(vers['pkgs'])} paquetes, {len(fu['fuentes'])} fuentes, {len(cambios)} cambios")

if __name__ == "__main__":
    main()
