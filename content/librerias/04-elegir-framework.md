---
title: Elegir: React, Angular, Lit y otros
desc: Elegir framework para una aplicación o sitio web, comparando React, Angular, Lit y otras opciones según el equipo y las necesidades.
---
| Si necesitas... | Considera | Nota |
|---|---|---|
| Ecosistema enorme y empleo | **React** (+ Next.js / React Router) | Libre en decisiones: necesitas elegir router, datos, estilos |
| Todo incluido, equipos grandes, convenciones | **Angular** | Más estructura; curva inicial mayor |
| Componentes reutilizables entre frameworks, design systems | **Lit / Web Components** | Estándar del navegador; no es un framework de aplicación completo |
| Sitio de contenido rápido (docs, blog) | **Astro**, Eleventy, generador propio | HTML estático, JS solo donde hace falta |
| Curva suave, plantillas claras | **Vue** (+ Nuxt) | Muy popular en ciertos mercados |
| Poco JS en el cliente, sintaxis simple | **Svelte** (+ SvelteKit) | Compila a JS ligero |
| HTML primero, interactividad mínima | **htmx**, Alpine | Menos herramientas |
| Móvil multiplataforma | React Native, Flutter, Ionic/Capacitor | Otro conjunto de decisiones |

## Cómo decidir
1. **¿Qué sabe tu equipo?** El mejor framework es el que dominan.
2. **¿Es contenido o aplicación?** Contenido → estático/SSR. Aplicación tras login → SPA está bien.
3. **¿Cuánto vivirá?** Los estándares (Web Components) envejecen mejor que cualquier framework.
4. **¿Qué tal lo maneja la IA?** React y Next tienen más ejemplos en el entrenamiento; Angular y Lit, menos, así que aporta más contexto y versión.
5. **¿Hay que contratar?** Mira el mercado local.

## Combinaciones habituales
- Design system en **Lit** consumido desde React y Angular.
- **Next.js** para marketing + app.
- **Astro** con islas (React, Lit, Svelte) para sitios de contenido.

> [!NOTE] Estabilidad
> Cambiar de framework a mitad de proyecto casi nunca compensa. Mejor mejorar el que tienes: rendimiento, tests, tipos.

=== esquema
# Criterios
- Equipo — el mejor es el que dominan.
- Contenido o aplicación — estático/SSR o SPA.
- Vida del proyecto — los estándares envejecen mejor.
- IA — React tiene más ejemplos; en otros aporta versión y contexto.
# Casos
- Design system — Lit consumido desde React y Angular.
- Sitio de contenido — Astro o generador estático.
=== test
? Para un blog o documentación, ¿qué suele convenir?
* HTML estático (Astro, Eleventy o similar)
- Una SPA con login
- Una app móvil
! Es rápido, indexable y barato.
? ¿Qué criterio pesa más al elegir framework?
* Qué domina el equipo
- La moda del momento
- El nombre
! La productividad real manda.
? Un design system usado por equipos con React y Angular:
- Dos librerías separadas
* Web Components (Lit) compartidos
- Copiar y pegar
! Los Web Components funcionan en cualquier framework.
