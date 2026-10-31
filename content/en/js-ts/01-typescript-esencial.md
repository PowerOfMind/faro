---
title: Essential TypeScript
desc: TypeScript essentials give developers practical types for everyday code, from interfaces and generics to unions, errors and configuration.
pkgs: typescript
---
## The basics
```ts
type User = { id: number; name: string; email?: string };      // optional
interface Repo<T> { get(id: number): Promise<T>; }              // generic
type Status = 'idle' | 'loading' | 'error';                     // literal union
const cfg = { mode: 'dark' } as const;                          // immutable and literal
function isString(x: unknown): x is string { return typeof x === 'string'; }  // type guard
```

## `type` or `interface`
For objects it is almost the same. `interface` can be extended and merged; `type` is for unions, tuples and computed types. Pick one and be consistent.

## `unknown` over `any`
`any` switches checking off. `unknown` forces you to check before use. External data (JSON, `fetch`) is `unknown`: **validate it** with Zod/Valibot, because types do not exist at runtime.

## Discriminated unions
```ts
type Res = {ok: true; data: string} | {ok: false; error: Error};
function f(r: Res) { if (r.ok) r.data; else r.error; }   // TS narrows the type
```

## Typical errors
| Message | Cause and fix |
|---|---|
| `Object is possibly 'undefined'` | Check first, `?.`, `??`; avoid `!` unless certain |
| `Type 'X' is not assignable to 'Y'` | Review the shape; do not silence it with `as any` |
| `Cannot find module` | `moduleResolution`, paths, or missing `@types/...` |
| `Property does not exist on type` | The type is too wide: narrow it |
| Works in the editor, fails in build | Different TS versions; use the project's |

## A sensible `tsconfig`
```json
{ "compilerOptions": { "strict": true, "target": "ES2022", "module": "ESNext",
  "moduleResolution": "Bundler", "noUncheckedIndexedAccess": true, "skipLibCheck": true } }
```

> [!NOTE] TypeScript 7
> The 7.x line is the compiler rewritten in native code (much faster). If you migrate, check the release notes: some old `tsconfig` options have been removed or changed. The language and the types on this page do not change.

> [!AI] Dangerous shortcuts
> Faced with a type error, the AI often adds `as any` or `// @ts-ignore`. Ask it to understand the real type instead of silencing it.

=== esquema
# Types
- unknown — forces a check; better than any.
- Discriminated union — narrows the type with a property.
- as const — immutable literals.
- satisfies — validates without widening.
# External data
- JSON and fetch — are unknown; validate with Zod or Valibot.
- tsconfig — strict and noUncheckedIndexedAccess.
=== test
? Why unknown over any?
* It forces you to check the type before using it
- It is faster
- It turns checking off
! any switches TypeScript off; unknown keeps it on.
? Do TypeScript types exist at runtime?
- Yes
* No: that is why external data is validated
- Only in production
! They are erased on compile.
? "possibly undefined" error. Fix?
* Check first, ?. or ??
- Add as any
- Use @ts-ignore
! Silencing it hides a real failure.
