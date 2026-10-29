---
title: Authentication, authorisation and database
desc: Who you are is not what you can do; IDOR, RLS and sessions.
---
## Do not write it yourself
For login use a proven solution (a managed provider or a mature library: Auth.js, Better Auth, Clerk, Supabase Auth, Firebase Auth). Hash with **Argon2id** or **bcrypt** if you store passwords. An AI can generate a login that "works" with subtle flaws (non-constant-time comparison, tokens that never expire, no attempt limit).

## Authentication ≠ authorisation
- **Authentication**: who are you?
- **Authorisation**: can you do **this** to **this resource**?

The classic failure (IDOR): the server only checks that a session exists.
```ts
// bad
const order = await db.order.findById(req.params.id);
// good: scope by owner
const order = await db.order.findFirst({ where: { id, userId: session.userId } });
if (!order) return res.status(404).end();
```
Authorise **on the server, on every request**. Hiding a button is not access control.

## Databases exposed to the client
With Supabase/Firebase the client talks straight to the database, so **the rules are your backend**.
- Supabase: enable **Row Level Security** on every table and create policies (`auth.uid() = user_id`). With no policies nobody gets in; with RLS off, **everybody** does.
- Firebase: Firestore/Storage rules never `allow read, write: if true`.
- The `service_role` key bypasses RLS: server only.

## Sessions and tokens
- `HttpOnly`, `Secure`, `SameSite` cookies; reasonable expiry and rotation on login.
- JWT: verify signature and `exp`, pin the expected algorithm; do not put sensitive data inside.
- Limit login and password-recovery attempts.

## Payments
Never trust the price or the "paid" flag the client sends. Confirm through the provider's **signed webhook** and verify the signature.

> [!SEC] Quick test
> Log in as user A, copy a request from the Network tab, replay it with the id of a user B resource. If it answers, you have an IDOR.

=== esquema
# Concepts
- Authentication — who you are.
- Authorisation — what you can do on which resource.
- IDOR — access to other people's resources by changing an id.
# Data
- RLS (Supabase) — per-row policies; without them, nobody or everybody.
- Firebase rules — never allow read, write: if true.
- service_role — bypasses RLS, server only.
=== test
? How do you avoid an IDOR?
- By hiding the button
* By scoping the query by owner on the server
- With a longer id
! Authorisation is checked on every request.
? A Supabase table with RLS disabled and a public key in the client. Risk?
* Anyone can read and write
- None
- Read-only
! Without RLS the client has full access.
? How do you confirm a payment?
- With the "paid" flag the client sends
* With a signed webhook from the provider
- With a cookie
! The client can lie.
