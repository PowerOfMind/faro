---
title: Backend, datos y autenticación
desc: Servidor, bases de datos, ORMs, auth y servicios gestionados.
pkgs: hono, express, drizzle-orm, prisma, "better-auth", "next-auth"
---
| Necesidad | Por defecto | Alternativa |
|---|---|---|
| API mínima en Node/edge | **Hono** | Express (muy extendido), Fastify |
| Framework full-stack | **Next.js**, SvelteKit, Nuxt, Remix/React Router | Astro (contenido) |
| Backend con estructura (Angular style) | **NestJS** | Fastify + módulos propios |
| Base de datos relacional | **PostgreSQL** | SQLite (Turso/D1) para proyectos pequeños |
| ORM / consultas tipadas | **Drizzle** | Prisma, Kysely |
| BBDD como servicio | **Supabase**, Neon | Firebase (documental), PlanetScale |
| Cache / colas | **Redis** (Upstash en serverless) | |
| Auth gestionada | **Clerk**, Supabase Auth, Firebase Auth | Auth.js, Better Auth (autoalojado) |
| Pagos | **Stripe** (Checkout + webhooks) | Lemon Squeezy / Paddle como "merchant of record" |
| Email transaccional | **Resend**, Postmark | SES |
| Subida de ficheros | S3/R2 con URLs firmadas | UploadThing |
| Búsqueda | Postgres FTS, **Meilisearch**, Typesense | Algolia |
| Validación en el borde | **Zod** | Valibot |
| Jobs programados | GitHub Actions cron, Vercel/Cloudflare Cron | BullMQ |

## Alojamiento estático y serverless
| Qué | Dónde |
|---|---|
| Sitio estático | GitHub Pages, Cloudflare Pages, Netlify, Vercel |
| Funciones / edge | Vercel, Cloudflare Workers, Netlify, Deno Deploy |
| Contenedores | Fly.io, Railway, Render, Cloud Run |

## Reglas de diseño
- Empieza con **una** base de datos y un servidor; divide cuando duela.
- Valida entradas en el servidor (ver [Seguridad](@/seguridad/auth-y-datos)).
- Migraciones versionadas (`drizzle-kit`, `prisma migrate`), nunca cambios a mano en producción.
- Vigila costes: límites de gasto y alertas en cada proveedor.

> [!AI] Con IA
> Para auth y pagos no aceptes "tu propia implementación". Usa el servicio o librería y limita el trabajo de la IA a la integración.
