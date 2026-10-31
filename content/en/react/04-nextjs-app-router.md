---
title: Next.js App Router
desc: A practical guide to next.js app router, common mistakes, decisions, and checks to help you solve problems with confidence.
pkgs: next, react, react-dom
---
## Server and client
In App Router, pages and layouts are Server Components by default. Use `"use client"` for state, events or browser APIs; do not expose secrets through props sent to the client.

## Routes and states
`app/page.tsx` defines a page; folders and `[id]` segments define routes. `layout.tsx` shares UI, `loading.tsx` shows a fallback and `error.tsx` handles segment errors as a Client Component.

## Data and hydration
Fetch data in an async Server Component and handle errors. Cache behavior and defaults depend on version and configuration: check the docs for your version. To avoid hydration errors, the first client render must match the server HTML; avoid random dates or `window` there.

## Quick decisions
| Question | Answer |
|---|---|
| What are pages by default? | Server Components |
| Where do state and event handlers belong? | In a Client Component |
| Which file shows loading UI? | loading.tsx |

> [!AI] With AI
> Describe your version, environment, expected and actual results, and a minimal reproduction. Ask for a testable explanation and references to the official documentation.

Documentation: [official guide](https://nextjs.org/docs/app/getting-started/server-and-client-components).

Related: [continue with a related guide](@/react/hooks-propios-y-rendimiento).

=== esquema
# Key ideas
- Server and client — In App Router, pages and layouts are Server Components by default.
- Routes and states — `app/page.tsx` defines a page; folders and `[id]` segments define routes.
- Data and hydration — Fetch data in an async Server Component and handle errors.
=== test
? What are pages by default?
* Server Components
- In a Client Component
- loading.tsx
! Server Components.
? Where do state and event handlers belong?
* In a Client Component
- loading.tsx
- A dynamic segment
! In a Client Component.
? Which file shows loading UI?
* loading.tsx
- A dynamic segment
- Different initial server and client HTML
! loading.tsx.
? What does [id] define?
* A dynamic segment
- Different initial server and client HTML
- Server Components
! A dynamic segment.
? What causes a hydration mismatch?
* Different initial server and client HTML
- Server Components
- In a Client Component
! Different initial server and client HTML.
