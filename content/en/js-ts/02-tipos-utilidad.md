---
title: Utility types and generics
desc: Partial, Pick, Omit, Record, ReturnType, satisfies and friends.
pkgs: typescript
---
## The everyday ones
| Utility | Result |
|---|---|
| `Partial<T>` | All properties optional |
| `Required<T>` | All required |
| `Readonly<T>` | Read-only |
| `Pick<T, 'a' \| 'b'>` | Only those keys |
| `Omit<T, 'a'>` | All except those |
| `Record<K, V>` | Object with keys K and values V |
| `ReturnType<typeof f>` | The type `f` returns |
| `Parameters<typeof f>` | Tuple of parameters |
| `Awaited<Promise<T>>` | `T` |
| `NonNullable<T>` | Without `null` or `undefined` |

```ts
type UpdateUser = Partial<Omit<User, 'id'>>;
const labels: Record<Status, string> = { idle: 'Ready', loading: 'Loading', error: 'Error' };
```

## Deriving types from values
```ts
const ROLES = ['admin', 'user'] as const;
type Role = typeof ROLES[number];            // 'admin' | 'user'
type Key = keyof typeof cfg;
```

## `satisfies`
Validates against a type **without widening** the literal:
```ts
const routes = { home: '/', about: '/about' } satisfies Record<string, string>;
routes.home;   // still '/', not string
```

## Constrained generics
```ts
function pluck<T, K extends keyof T>(items: T[], key: K): T[K][] { return items.map(i => i[key]); }
```

## Conditional and mapped types (when needed)
```ts
type Nullable<T> = { [K in keyof T]: T[K] | null };
type ElementOf<T> = T extends (infer U)[] ? U : never;
```
If a type needs five lines of magic, it is probably worth simplifying the design.

=== esquema
# Utilities
- Partial and Required — optional or required properties.
- Pick and Omit — keep or drop keys.
- Record — object with keys K and values V.
- ReturnType and Parameters — of a function.
- Awaited — the value of a promise.
# Derive
- typeof ROLES[number] — a union from an as const array.
- satisfies — checks without widening.
=== test
? What does Omit<User, 'id'> do?
* All properties except id
- Only id
- Makes id optional
! It is the complement of Pick.
? Get the union of values of an as const array:
- typeof ROLES
* typeof ROLES[number]
- keyof ROLES
! Indexing with number gives the element type.
? What does satisfies give you?
* Validates against a type without losing the literal
- Converts to any
- Runs code
! It keeps types precise.
