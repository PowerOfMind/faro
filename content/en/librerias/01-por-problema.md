---
title: Which library do I use for...
desc: Frontend libraries solve common development needs. Compare practical defaults and alternatives for data, styling, testing and tooling.
pkgs: vite, vitest, zod, "@tanstack/react-query", zustand, tailwindcss, "date-fns", playwright, eslint
---
A default option and when to look at another. Always check maintenance and version (see below).

| Problem | Default | Alternative / when |
|---|---|---|
| Bundling / dev server | **Vite** | Webpack if you inherit a project; Turbopack inside Next |
| Unit tests | **Vitest** | Jest if you already use it |
| End-to-end tests | **Playwright** | Cypress |
| Validate data / schemas | **Zod** | Valibot (lighter), ArkType |
| Server data on the client | **TanStack Query** | SWR; RTK Query with Redux |
| Simple global state (React) | **Zustand** | Jotai; Redux Toolkit if the team uses it |
| Forms (React) | **React Hook Form** + Zod | TanStack Form |
| Utility styles | **Tailwind CSS** | CSS Modules; native CSS with variables and `@layer` |
| Accessible unstyled components | **Radix UI**, React Aria | Base UI; **shadcn/ui** as a copyable collection |
| Icons | **Lucide** | Heroicons, Phosphor |
| Dates | **date-fns** or `Intl` | Day.js; Temporal once you have support |
| Charts | **Recharts**, ECharts | D3 if you need total control |
| Sortable/filterable tables | **TanStack Table** | AG Grid (large volumes) |
| Animation | CSS + View Transitions | **Motion** (Framer Motion), GSAP |
| Routing (React SPA) | **React Router**, TanStack Router | The framework's router |
| Markdown on the web | **markdown-it**, remark/rehype | MDX for components inside |
| Sanitise HTML | **DOMPurify** | native `sanitizer` when available |
| Lint and format | **ESLint** + **Prettier** | Biome (all in one) |
| Package manager | **npm** / **pnpm** | Bun, Yarn |

## Criteria for accepting a library
1. A recent last release and issues being handled.
2. Size (bundlephobia) reasonable for what you do.
3. TypeScript types included.
4. A compatible licence.
5. No simpler native alternative (see [modern JS](@/js-ts/js-moderno)).

> [!AI] Names the AI confuses
> Ask for the exact version and package: `@tanstack/react-query` (v5) is not `react-query` (v3). `date-fns` v3/v4 changed imports. `react-router` v6/v7 is not v5.

=== esquema
# Defaults
- Build — Vite.
- Tests — Vitest, and Playwright for e2e.
- Validation — Zod (or Valibot if size matters).
- Server data — TanStack Query.
- Styles — Tailwind or native CSS.
# Criteria
- Maintenance — a recent release and issues being handled.
- Size and types — reasonable and included.
=== test
? What do you use to validate external data with types?
* Zod or Valibot
- An if per field
- Nothing
! Types do not exist at runtime.
? Which criterion do you check before accepting a library?
* Recent maintenance, size and licence
- Only the stars
- That the AI suggests it
! A library without maintenance is debt.
? react-query v3 versus @tanstack/react-query v5:
* They are different versions with a different API
- Identical
- One is for Vue
! The AI mixes names and versions.
