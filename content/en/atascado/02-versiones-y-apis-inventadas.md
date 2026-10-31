---
title: Outdated or invented APIs
desc: Outdated or invented APIs can break generated code. Learn to check installed versions, TypeScript definitions and migration guides.
---
## Why it happens
The model learns from code of **many versions at once**. It mixes `react-router` v5 with v7, Next `pages/` with `app/`, Angular NgModules with standalone, Tailwind 3 with 4, Lit 2 with 3.

## Symptoms
- `X is not a function` / `Module not found` / `has no exported member`.
- A parameter that "does nothing".
- Examples that use `lit-element`, `componentWillMount`, `getServerSideProps` in a project that does not support them.

## What to do
1. Give it the version **and** the paradigm: "Next 15 App Router", "Angular standalone with signals".
2. Paste the doc fragment or the real `.d.ts`: `node_modules/<pkg>/dist/*.d.ts` is the truth for your version.
3. `npm ls <pkg>` to see which version is really installed (there may be two).
4. Read the migration guide for the latest major version.
5. In TypeScript, the type error often exposes the non-existent API: do not silence it with `any`.

```bash
npm ls react lit            # real versions
npm view react versions --json | tail -5
npm view lit dist-tags
```

> [!AI] Asking the AI to correct itself
> "Check every import and every method in your answer against version X. Flag the ones you are not sure exist."

> [!TIP] Pin the context
> Put the key versions in the project map (`CLAUDE.md`) so every session has them.

=== esquema
# Causes
- Mixed versions — the model saw React Router v5 and v7 at once.
- Old paradigm — NgModules, pages/, class components.
# Fixes
- State version and paradigm — "Next 15 App Router".
- The real .d.ts — node_modules/<pkg>/dist/*.d.ts is the truth.
- npm ls — which version is really installed.
=== test
? An API "does nothing" or "is not a function". First suspicion?
* Code from another version of the library
- A browser bug
- The RAM
! Models mix APIs from different versions.
? What is the source of truth for your version's types?
- The first search result
* The .d.ts inside node_modules
- An old forum answer
! It is exactly the installed code.
? What do you do with a type error that reveals a non-existent API?
- as any to silence it
* Understand the real type and fix the usage
- Turn TypeScript off
! Silencing it hides the problem, it does not fix it.
