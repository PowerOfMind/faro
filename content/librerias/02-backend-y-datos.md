---
title: Backend, datos y autenticación
desc: Backend y datos para elegir herramientas de servidor, bases de datos y autenticación, con alternativas para pagos, correo y almacenamiento.
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

=== esquema
# Piezas
- API — Hono, Express o Fastify.
- Full-stack — Next.js, SvelteKit, Nuxt, Remix.
- Datos — PostgreSQL con Drizzle o Prisma.
- Servicios — Supabase, Neon, Firebase.
- Pagos — Stripe con webhooks.
# Reglas
- Auth gestionada — nunca la tuya propia.
- Migraciones versionadas — nada a mano en producción.
=== test
? Para autenticación, ¿qué conviene?
* Un servicio o librería probada
- Tu propia implementación
- Guardar contraseñas en claro
! Los fallos sutiles de auth son caros.
? ¿Cómo cambias el esquema de la BBDD en producción?
* Con migraciones versionadas
- A mano en la consola
- Reiniciando
! Son reproducibles y reversibles.
? Hosting de un sitio estático:
- Solo un VPS
* GitHub Pages, Cloudflare Pages, Netlify o Vercel
- Una base de datos
! Sirven HTML sin servidor propio.
