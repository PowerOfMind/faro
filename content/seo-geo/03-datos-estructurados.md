---
title: Datos estructurados (schema.org)
desc: JSON-LD para que buscadores y modelos entiendan qué es cada página.
---
Los datos estructurados describen la página en un formato que las máquinas leen sin interpretar el texto. Se añaden como **JSON-LD** en el `<head>`.

## Tipos más útiles
| Página | Tipo |
|---|---|
| Artículo / guía | `Article`, `TechArticle` |
| Migas de pan | `BreadcrumbList` |
| Preguntas y respuestas | `FAQPage` (los rich results de FAQ están muy limitados en Google, pero sigue aportando estructura) |
| Organización / sitio | `Organization`, `WebSite` |
| Producto | `Product` + `Offer` + `AggregateRating` |
| Receta, evento, vídeo | `Recipe`, `Event`, `VideoObject` |

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Propiedades reactivas en Lit 3",
  "inLanguage": "es",
  "dateModified": "2026-10-29",
  "author": {"@type": "Person", "name": "Tu nombre"}
}
</script>
```

## Reglas
- Marca solo lo que **se ve en la página**. Datos que el usuario no ve pueden causar penalización.
- Una fuente de verdad: genera el JSON-LD desde los mismos datos que la página (como hace este sitio).
- Valida con **Rich Results Test** y el **Schema Markup Validator**.
- Fechas ISO 8601; URLs absolutas.

> [!AI] Cuidado
> La IA inventa propiedades o ratings. No marques valoraciones que no existen: es contra las políticas y arriesgas acción manual.
