---
title: Modern JavaScript worth knowing
desc: Native utilities that replace libraries, and the classic traps.
---
## No library needed any more
| Before | Now |
|---|---|
| lodash `cloneDeep` | `structuredClone(obj)` |
| lodash `groupBy` | `Object.groupBy(arr, fn)` / `Map.groupBy` |
| lodash `last`, `at` | `arr.at(-1)` |
| Copy and sort without mutating | `toSorted()`, `toReversed()`, `with()`, `toSpliced()` |
| `Array.from(new Set(a))` | `[...new Set(a)]` |
| basic axios | `fetch` |
| uuid | `crypto.randomUUID()` |
| Debouncing scroll events | `IntersectionObserver`, `ResizeObserver` |
| A CSS selector in JS for modals | `<dialog>`, `popover` |

```js
const last = list.at(-1);
const sorted = list.toSorted((a, b) => a.n - b.n);   // does not mutate
const copy = structuredClone(state);
```

## Operators
- `??` only for `null`/`undefined`; `||` also for `0` and `''`.
- `?.` avoids errors in chains; `a?.b ?? 'x'`.
- `??=`, `||=`, `&&=` logical assignment.

## Classic traps
| Trap | Reality |
|---|---|
| `0.1 + 0.2 !== 0.3` | Floating point: for money use integers (cents) or `Intl.NumberFormat` |
| `typeof null === 'object'` | Check `=== null` |
| `[1,10,2].sort()` | Sorts as text: pass a numeric comparator |
| `parseInt('08abc')` | Accepts junk: use `Number()` and validate |
| `Date` and time zones | `new Date('2026-10-29')` is UTC, not local |
| Object equality | `{} === {}` is `false`: compare by value or by id |
| `this` in callbacks | Use arrow functions or `.bind` |

## Dates and internationalisation
`Intl.DateTimeFormat`, `Intl.NumberFormat`, `Intl.RelativeTimeFormat` format without libraries. **Temporal** is the modern date API: it is arriving in browsers; check support on caniuse and use a polyfill if you need it.

## Modules
Native `import`/`export`, dynamic `import()` to load on demand, `import.meta.url`. See [Dependencies that do not add up](@/atascado/dependencias) for ESM vs CJS.

=== esquema
# Native
- structuredClone — deep copy.
- toSorted and at — sort without mutating, negative index.
- crypto.randomUUID — ids.
- Intl — date and number formats.
# Traps
- ?? vs || — ?? only for null/undefined.
- Floating point — money in cents.
- sort() — sorts as text by default.
=== test
? Which deep copy is native?
* structuredClone
- Object.copy
- JSON.deepCopy
! It is available in current browsers and Node.
? Difference between ?? and ||:
* ?? only acts on null or undefined
- They are the same
- ?? acts on 0 and ''
! || also treats 0 and the empty string as falsy.
? [1, 10, 2].sort() sorts...
- Numerically
* As text
- Randomly
! Pass a numeric comparator.
