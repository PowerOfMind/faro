---
title: SEO técnico en una página
desc: Lo mínimo que decide si te indexan y cómo te muestran.
---
## Imprescindibles
| Elemento | Regla |
|---|---|
| `<title>` | Único por página, ~50-60 caracteres, palabra clave al principio |
| `meta description` | ~140-160 caracteres, escrita para convencer del clic |
| `<h1>` | Uno, describe la página |
| `<html lang>` | Idioma correcto (`es`) |
| `canonical` | URL preferida; evita duplicados por parámetros |
| Imágenes | `alt` descriptivo, `width`/`height`, formato moderno (WebP/AVIF) |
| URLs | Cortas, legibles, estables; redirige con 301 si cambian |
| Enlaces internos | Texto descriptivo, no "pulsa aquí" |

```html
<title>Guía de Lit 3: propiedades reactivas</title>
<meta name="description" content="Cómo funcionan @property y @state en Lit 3, cuándo se re-renderiza y la trampa de los class fields.">
<link rel="canonical" href="https://ejemplo.com/lit/reactividad">
<meta property="og:title" content="..."><meta property="og:image" content="https://ejemplo.com/og.png">
```

## Rastreo e indexación
- `robots.txt` indica qué rastrear; **no** impide que una URL aparezca. Para no indexar usa `<meta name="robots" content="noindex">`.
- `sitemap.xml` con URLs canónicas, referenciado en `robots.txt` y enviado en Search Console.
- Un 404 real devuelve estado 404 (no 200 con "no encontrado").
- Usa **Google Search Console**: cobertura, rendimiento, inspección de URL (muestra el HTML renderizado que ve Google).

## Rendimiento (Core Web Vitals)
| Métrica | Objetivo | Palanca |
|---|---|---|
| LCP | < 2,5 s | Imagen principal optimizada, `fetchpriority="high"`, menos JS bloqueante |
| INP | < 200 ms | Menos JS en el hilo principal, dividir tareas largas |
| CLS | < 0,1 | Reserva espacio a imágenes, anuncios y fuentes |

Mide con PageSpeed Insights (datos reales) y Lighthouse (laboratorio).

> [!AI] La IA y el SEO
> Suele generar páginas con `<title>` repetido, múltiples `h1` o contenido solo en JS. Comprueba "Ver código fuente" (no el inspector) para saber qué ve un rastreador sin JS.

=== esquema
# Imprescindibles
- title — único, ~50-60 caracteres.
- meta description — ~140-160, escrita para el clic.
- h1 — uno por página.
- canonical — la URL preferida.
# Rastreo
- robots.txt — rastreo, no indexación; para no indexar usa noindex.
- sitemap.xml — URLs canónicas.
- Core Web Vitals — LCP, INP y CLS.
=== test
? ¿Impide robots.txt que una URL aparezca en buscadores?
- Sí, siempre
* No: para no indexar se usa noindex
- Solo en móvil
! robots.txt controla el rastreo, no la indexación.
? Objetivo de LCP:
* Menos de 2,5 s
- Menos de 10 s
- Da igual
! Es la métrica de carga del contenido principal.
? ¿Qué ves con "Ver código fuente" que no ves en el inspector?
* El HTML que recibe un rastreador sin ejecutar JS
- El CSS compilado
- Las cookies
! Muestra lo que existe antes de ejecutar JavaScript.
