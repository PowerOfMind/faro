---
title: Choosing: React, Angular, Lit and others
desc: Practical criteria, not fashion.
---
| If you need... | Consider | Note |
|---|---|---|
| A huge ecosystem and jobs | **React** (+ Next.js / React Router) | Free in decisions: you must choose router, data, styling |
| Everything included, big teams, conventions | **Angular** | More structure; steeper start |
| Reusable components across frameworks, design systems | **Lit / Web Components** | A browser standard; not a full application framework |
| A fast content site (docs, blog) | **Astro**, Eleventy, your own generator | Static HTML, JS only where needed |
| A gentle curve, clear templates | **Vue** (+ Nuxt) | Very popular in some markets |
| Little client JS, simple syntax | **Svelte** (+ SvelteKit) | Compiles to light JS |
| HTML first, minimal interactivity | **htmx**, Alpine | Fewer tools |
| Cross-platform mobile | React Native, Flutter, Ionic/Capacitor | A different set of decisions |

## How to decide
1. **What does your team know?** The best framework is the one they master.
2. **Content or application?** Content → static/SSR. An app behind login → an SPA is fine.
3. **How long will it live?** Standards (Web Components) age better than any framework.
4. **How well does AI handle it?** React and Next have more examples in training; Angular and Lit fewer, so give more context and the version.
5. **Do you need to hire?** Look at the local market.

## Usual combinations
- A design system in **Lit** consumed from React and Angular.
- **Next.js** for marketing + app.
- **Astro** with islands (React, Lit, Svelte) for content sites.

> [!NOTE] Stability
> Switching framework mid-project almost never pays off. Better to improve the one you have: performance, tests, types.

=== esquema
# Criteria
- Team — the best one is the one they master.
- Content or application — static/SSR or SPA.
- Project lifetime — standards age better.
- AI — React has more examples; for others give version and context.
# Cases
- Design system — Lit consumed from React and Angular.
- Content site — Astro or a static generator.
=== test
? For a blog or documentation, what usually makes sense?
* Static HTML (Astro, Eleventy or similar)
- An SPA with login
- A mobile app
! It is fast, indexable and cheap.
? Which criterion weighs most when choosing a framework?
* What the team masters
- The fashion of the moment
- The name
! Real productivity rules.
? A design system used by teams with React and Angular:
- Two separate libraries
* Shared Web Components (Lit)
- Copy and paste
! Web Components work in any framework.
