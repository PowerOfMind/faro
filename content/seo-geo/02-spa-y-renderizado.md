---
title: SPA, SSR y SSG para SEO
desc: Qué ve el rastreador según cómo renderizas.
---
## Qué ve cada rastreador
Google ejecuta JavaScript, pero lo hace en una segunda fase, con retraso y límites. Muchos otros rastreadores, previsualizaciones sociales y **bots de IA** no ejecutan JS o lo hacen de forma limitada. Lo que no esté en el HTML inicial puede no existir para ellos.

| Estrategia | HTML inicial | SEO | Cuándo |
|---|---|---|---|
| SPA (CSR) | Casi vacío | Peor | Apps tras login |
| **SSG** (estático) | Completo, prerenderizado | Excelente | Docs, blogs, marketing, este sitio |
| **SSR** | Completo, en cada petición | Muy bueno | Contenido dinámico y personalizado |
| ISR / revalidación | Estático que se refresca | Muy bueno | Catálogos, noticias |
| Prerender solo para bots | Completo para bots | Aceptable | Parche para SPA existente |

## Metadatos por ruta
En una SPA, `<title>` y `meta` deben cambiar por ruta **y estar en el HTML servido**. Usa las APIs del framework: `generateMetadata` (Next), `Title`/`Meta` (Angular), `@unhead/vue` (Nuxt/Vue), `<svelte:head>`.

## Comprobar lo que ve un bot
```bash
curl -s https://tu-sitio.com/ruta | head -50        # ¿está el contenido y el título?
```
Si el `curl` no muestra tu texto, un rastreador sin JS tampoco.

## Navegación
- Enlaces reales `<a href>`; los `onClick` con `navigate()` no se rastrean.
- No uses `#` para rutas (`/#/pagina`): usa History API.
- Paginación y filtros con URLs propias si quieres que se indexen.

## Idiomas
`hreflang` entre versiones y `x-default`. Contenido traducido de verdad, no solo el menú.

> [!TIP] Para sitios de contenido
> Un generador estático (Astro, Eleventy, Next con export, o uno propio como este) da HTML completo, rápido y barato de alojar.

=== esquema
# Estrategias
- SPA — HTML casi vacío; peor para SEO.
- SSG — HTML completo prerenderizado; ideal para contenido.
- SSR — HTML completo en cada petición.
# Reglas
- Metadatos por ruta — en el HTML servido.
- Enlaces reales a href — no solo onClick.
- hreflang — entre versiones de idioma.
=== test
? Los bots de IA, ¿ejecutan JavaScript?
- Siempre
* Muchos no, o de forma limitada
- Nunca ven HTML
! Lo que no está en el HTML inicial puede no existir para ellos.
? ¿Qué es mejor para un sitio de documentación?
* Generación estática (SSG)
- SPA sin SSR
- iframes
! HTML completo, rápido y barato de alojar.
? ¿Cómo compruebas qué ve un bot?
- Con el inspector
* curl a la URL
- Con Lighthouse solo
! Si curl no muestra tu texto, tampoco un rastreador sin JS.
