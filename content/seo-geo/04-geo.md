---
title: GEO: que te citen los modelos
desc: GEO para mejorar la visibilidad de contenidos en respuestas de IA, con prácticas de SEO, fuentes citables y control de rastreadores.
---
**GEO** busca que buscadores con IA (AI Overviews, ChatGPT con búsqueda, Perplexity, Copilot) te usen como **fuente citada**. Es SEO con matices: ya no compites solo por un clic, sino por aparecer dentro de la respuesta.

## Lo que sí tiene fundamento
1. **SEO sólido primero.** Los sistemas con búsqueda parten de resultados web; si no estás indexado y accesible, no existes.
2. **HTML legible sin JS.** Los bots de IA suelen no ejecutar JavaScript (ver [SPA y SSR](@/seo-geo/spa-y-renderizado)).
3. **Respuestas directas.** Un encabezado en forma de pregunta y, debajo, la respuesta en 1-2 frases, y luego el detalle.
4. **Hechos citables.** Cifras con fuente, definiciones claras, fechas, tablas. Las afirmaciones vagas no se citan.
5. **Autoría y fecha visibles.** Señales de confianza (E-E-A-T): quién escribe, cuándo actualizó, fuentes.
6. **Datos estructurados** coherentes con el contenido (ver [schema.org](@/seo-geo/datos-estructurados)).
7. **Menciones externas**: ser citado o enlazado en otros sitios fiables pesa.
8. **Actualizar** lo que caduca (versiones, precios) y mostrar la fecha de revisión.

## Controlar a los bots
`robots.txt` distingue bots de entrenamiento y de búsqueda. Ejemplos de agentes: `GPTBot` (entrenamiento OpenAI), `OAI-SearchBot` (búsqueda), `ClaudeBot`, `PerplexityBot`, `Google-Extended` (control de uso para Gemini). Bloquear el de entrenamiento no tiene por qué quitarte de los resultados de búsqueda. Revisa los nombres vigentes en la documentación de cada empresa.
```text
User-agent: GPTBot
Disallow: /
User-agent: OAI-SearchBot
Allow: /
```

## `llms.txt`
Propuesta de fichero en Markdown en la raíz que resume el sitio y enlaza a las páginas clave para modelos. Es barato de generar (este sitio lo hace). **No hay evidencia sólida de que mejore las citas** y los grandes buscadores no lo han adoptado como estándar: trátalo como extra, no como estrategia.

## Qué evitar
- Prometer "posicionar en ChatGPT" con trucos. No hay un truco.
- Texto genérico generado en masa: aporta poco y degrada la confianza.
- Medir solo clics: mide también menciones y tráfico de referencia desde herramientas de IA.

> [!NOTE] Cómo medir
> Busca tus preguntas objetivo en varios asistentes con búsqueda, anota si te citan, y repite cada mes. Los analytics muestran visitas con referrer de dominios de asistentes.

=== esquema
# Qué funciona
- SEO sólido primero — si no estás indexado, no existes.
- HTML legible sin JS — los bots de IA suelen no ejecutarlo.
- Respuesta directa — pregunta y 1-2 frases de respuesta.
- Hechos citables — cifras con fuente, fechas, tablas.
- Autoría y fecha — señales de confianza.
# Cautela
- llms.txt — barato, sin evidencia sólida de efecto.
- Bots de IA — distingue entrenamiento y búsqueda en robots.txt.
=== test
? ¿Qué es GEO?
* Optimizar para que los buscadores con IA te citen como fuente
- Un formato de imagen
- Un tipo de servidor
! Es SEO con foco en aparecer dentro de la respuesta generada.
? ¿Mejora llms.txt las citas, según la evidencia actual?
- Sí, de forma clara
* No hay evidencia sólida: es un extra, no una estrategia
- Es obligatorio
! Los grandes buscadores no lo han adoptado como estándar.
? ¿Qué contenido se cita más?
* Hechos concretos con fuente y fecha visibles
- Texto genérico en masa
- Frases vagas
! Los modelos citan afirmaciones verificables.
