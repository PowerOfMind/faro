---
title: Backend, data and authentication
desc: Backend tools help developers choose APIs, databases, ORMs and authentication. Compare managed services and hosting with design advice.
pkgs: hono, express, drizzle-orm, prisma, "better-auth", "next-auth"
---
| Need | Default | Alternative |
|---|---|---|
| Minimal API on Node/edge | **Hono** | Express (very widespread), Fastify |
| Full-stack framework | **Next.js**, SvelteKit, Nuxt, Remix/React Router | Astro (content) |
| Structured backend (Angular style) | **NestJS** | Fastify + your own modules |
| Relational database | **PostgreSQL** | SQLite (Turso/D1) for small projects |
| ORM / typed queries | **Drizzle** | Prisma, Kysely |
| Database as a service | **Supabase**, Neon | Firebase (document), PlanetScale |
| Cache / queues | **Redis** (Upstash in serverless) | |
| Managed auth | **Clerk**, Supabase Auth, Firebase Auth | Auth.js, Better Auth (self-hosted) |
| Payments | **Stripe** (Checkout + webhooks) | Lemon Squeezy / Paddle as merchant of record |
| Transactional email | **Resend**, Postmark | SES |
| File uploads | S3/R2 with signed URLs | UploadThing |
| Search | Postgres FTS, **Meilisearch**, Typesense | Algolia |
| Validation at the edge | **Zod** | Valibot |
| Scheduled jobs | GitHub Actions cron, Vercel/Cloudflare Cron | BullMQ |

## Static and serverless hosting
| What | Where |
|---|---|
| Static site | GitHub Pages, Cloudflare Pages, Netlify, Vercel |
| Functions / edge | Vercel, Cloudflare Workers, Netlify, Deno Deploy |
| Containers | Fly.io, Railway, Render, Cloud Run |

## Design rules
- Start with **one** database and one server; split when it hurts.
- Validate inputs on the server (see [Security](@/seguridad/auth-y-datos)).
- Versioned migrations (`drizzle-kit`, `prisma migrate`), never manual changes in production.
- Watch costs: spending limits and alerts at every provider.

> [!AI] With AI
> For auth and payments do not accept "your own implementation". Use the service or library and limit the AI's work to the integration.

=== esquema
# Pieces
- API — Hono, Express or Fastify.
- Full-stack — Next.js, SvelteKit, Nuxt, Remix.
- Data — PostgreSQL with Drizzle or Prisma.
- Services — Supabase, Neon, Firebase.
- Payments — Stripe with webhooks.
# Rules
- Managed auth — never your own.
- Versioned migrations — nothing by hand in production.
=== test
? For authentication, what is advisable?
* A proven service or library
- Your own implementation
- Storing passwords in clear
! Subtle auth failures are expensive.
? How do you change the database schema in production?
* With versioned migrations
- By hand in the console
- By restarting
! They are reproducible and reversible.
? Hosting for a static site:
- Only a VPS
* GitHub Pages, Cloudflare Pages, Netlify or Vercel
- A database
! They serve HTML without your own server.
