---
title: Qué librería uso para...
desc: Tabla de decisión rápida para el frontend y las herramientas de cada día.
pkgs: vite, vitest, zod, "@tanstack/react-query", zustand, tailwindcss, "date-fns", playwright, eslint
---
Una opción por defecto y cuándo mirar otra. Comprueba siempre mantenimiento y versión (ver abajo).

| Problema | Por defecto | Alternativa / cuándo |
|---|---|---|
| Empaquetar / servidor de desarrollo | **Vite** | Webpack si heredas un proyecto; Turbopack dentro de Next |
| Tests unitarios | **Vitest** | Jest si ya lo usas |
| Tests end-to-end | **Playwright** | Cypress |
| Validar datos / esquemas | **Zod** | Valibot (más ligero), ArkType |
| Datos del servidor en cliente | **TanStack Query** | SWR; RTK Query con Redux |
| Estado global simple (React) | **Zustand** | Jotai; Redux Toolkit si el equipo lo usa |
| Formularios (React) | **React Hook Form** + Zod | TanStack Form |
| Estilos utilitarios | **Tailwind CSS** | CSS Modules; CSS nativo con variables y `@layer` |
| Componentes accesibles sin estilo | **Radix UI**, React Aria | Base UI; **shadcn/ui** como colección copiable |
| Iconos | **Lucide** | Heroicons, Phosphor |
| Fechas | **date-fns** o `Intl` | Day.js; Temporal cuando tengas soporte |
| Gráficos | **Recharts**, ECharts | D3 si necesitas control total |
| Tablas con orden/filtro | **TanStack Table** | AG Grid (grandes volúmenes) |
| Animación | CSS + View Transitions | **Motion** (Framer Motion), GSAP |
| Routing (React SPA) | **React Router**, TanStack Router | Router del framework |
| Markdown en la web | **markdown-it**, remark/rehype | MDX para componentes dentro |
| Sanear HTML | **DOMPurify** | `sanitizer` nativo cuando esté disponible |
| Lint y formato | **ESLint** + **Prettier** | Biome (todo en uno) |
| Gestor de paquetes | **npm** / **pnpm** | Bun, Yarn |

## Criterios para aceptar una librería
1. Último release reciente y issues atendidos.
2. Tamaño (bundlephobia) razonable para lo que haces.
3. Tipos TypeScript incluidos.
4. Licencia compatible.
5. Sin alternativa nativa más simple (ver [JS moderno](@/js-ts/js-moderno)).

> [!AI] Nombres que la IA confunde
> Pide versión y paquete exacto: `@tanstack/react-query` (v5) no es `react-query` (v3). `date-fns` v3/v4 cambió importaciones. `react-router` v6/v7 no es v5.

=== esquema
# Por defecto
- Build — Vite.
- Tests — Vitest, y Playwright para e2e.
- Validación — Zod (o Valibot si pesa).
- Datos de servidor — TanStack Query.
- Estilos — Tailwind o CSS nativo.
# Criterios
- Mantenimiento — release reciente e issues atendidos.
- Tamaño y tipos — razonable e incluidos.
=== test
? ¿Qué usas para validar datos externos con tipos?
* Zod o Valibot
- Un if por campo
- Nada
! Los tipos no existen en ejecución.
? ¿Qué criterio miras antes de aceptar una librería?
* Mantenimiento reciente, tamaño y licencia
- Solo las estrellas
- Que la sugiera la IA
! Una librería sin mantenimiento es deuda.
? react-query v3 frente a @tanstack/react-query v5:
* Son versiones distintas con API distinta
- Idénticas
- Una es de Vue
! La IA mezcla nombres y versiones.
