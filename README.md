# LightHub Dev

Atajos para cuando la IA no te da la solución: guías cortas de Lit, JS/TS, React, Angular, React Native y Expo, IA y agentes, seguridad con IA y SEO/GEO. Sitio **estático** (HTML generado, sin dependencias de ejecución).

## Uso
```bash
python build.py                 # genera dist/
python -m http.server 8793 -d dist
python tools/check_updates.py   # comprueba versiones npm y fuentes oficiales
```

## Contenido
Cada página tiene pestañas: **Lección** (Markdown), **Esquema**, **Test** y **Pruébalo** (código editable que se ejecuta en un iframe aislado). Se escriben en el mismo `.md` tras marcadores `=== esquema`, `=== test`, `=== prueba` (formato en cualquier página de `content/lit/`).
Idiomas: español en la raíz y otros en `content/<lang>/<seccion>/` con el **mismo nombre de fichero**; el selector solo enlaza a traducciones que existen. Añadir un idioma: entrada en `LANGS` y `T` de `build.py`.
`content/<seccion>/<NN-slug>.md` con cabecera `title`, `desc`, `pkgs` (paquetes npm cuya versión se muestra y vigila) y `updated` (opcional). Callouts: `> [!TIP]`, `[!WARN]`, `[!AI]`, `[!SEC]`, `[!NOTE]`. Enlaces internos: `(@/seccion/slug)`; el build falla si alguno está roto.
Las secciones se declaran en `T` de `build.py` para cada idioma; el nombre del sitio, en `SITE`.

## Cómo se mantiene al día
- `.github/workflows/vigilante.yml` (lunes): ejecuta `tools/check_updates.py`, guarda `data/versions.json` y `data/fuentes.json`, redespliega y abre una incidencia si hay versiones nuevas o entradas nuevas en blogs/releases oficiales.
- `.github/workflows/pages.yml`: construye y publica en GitHub Pages en cada push a `main`.
- Fuentes vigiladas: `data/fuentes.json`.

## Despliegue

El proyecto de Vercel `lighthub-dev`, conectado a `PowerOfMind/lighthub-dev`, construye y despliega producción con cada push a `main`. La configuración de la raíz ejecuta `SITE_URL=https://lighthub-dev.vercel.app python3 build.py`, sin instalar dependencias, y publica `dist/`. GitHub Pages también se publica con cada push a `main`.

Para desplegar manualmente en Vercel, construye primero con `SITE_URL=https://lighthub-dev.vercel.app` y después, desde `dist/`, ejecuta `vercel link --yes --project lighthub-dev` y `vercel deploy --prod --yes`. El generador elimina las opciones de construcción del `vercel.json` de `dist/` y conserva las cabeceras y redirecciones.

En Vercel se mide el número de visitas con Vercel Web Analytics, sin cookies ni identificación de personas, mediante datos agregados y sin fingerprinting persistente. GitHub Pages no incluye esta analítica. Más información en la página de privacidad.

## SEO/GEO del propio sitio
Título y descripción únicos, canonical, Open Graph, JSON-LD `TechArticle`, `sitemap.xml`, `robots.txt` y `llms.txt` (con `SITE_URL` definido).
