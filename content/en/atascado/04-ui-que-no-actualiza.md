---
title: The UI does not update or flickers
desc: Stale state, hydration mismatch, keys, looping effects and mutations.
---
## Stale state (stale closure)
A callback captured the old value.
```jsx
// bad: always uses count from the first render
useEffect(() => { const id = setInterval(() => setCount(count + 1), 1000); return () => clearInterval(id); }, []);
// good: functional form
setCount(c => c + 1);
```

## It does not re-render
| Framework | Typical cause |
|---|---|
| React | You mutated state in place (`arr.push`) instead of creating a new one |
| Lit | You mutated an object/array, or a class field shadows the accessor (see [reactivity](@/lit/reactividad)) |
| Angular | `OnPush` with mutation; use signals or new references |
| Vue | Reassigning a whole `reactive` loses reactivity |

## Effects that fire endlessly
- An object or function created on every render inside the effect's dependencies.
- An effect that changes what it listens to.
- Fix: primitive dependencies, `useMemo` / `useCallback` if needed, or move the logic into an event handler (many `useEffect`s are unnecessary).

## Hydration mismatch (SSR)
The server's HTML differs from the first client render.
- Causes: `Date.now()`, `Math.random()`, `window`/`localStorage` in render, time zones, browser extensions.
- Fix: compute those values after mount (`useEffect`) or mark them client-only.

## Keys in lists
`key={index}` with lists that reorder mixes state between rows (inputs that "jump"). Use a stable id.

## If nothing changes anyway
1. Are you editing the right file? (Is there a `dist/` or generated copy?)
2. Service worker or bundler cache? Restart the dev server.
3. Are you testing the production URL while changing local code?

> [!TIP] Debug in 2 minutes
> React DevTools / Angular DevTools: look at the state that is really there, not the one you believe.

=== esquema
# Causes
- Mutation — arr.push instead of creating a new array.
- Stale closure — a callback captured the old value.
- Unstable dependency — a new object on every render inside an effect.
# SSR
- Hydration mismatch — Date.now() or window during render.
- key={index} — mixes state between rows when reordering.
=== test
? You mutate a state array and the UI does not change. Why?
* The reference is the same, so the change is not detected
- The browser caches it
- A return is missing
! Create a new copy: [...items, x].
? setCount(count + 1) inside a setInterval with deps [] always sets 1. Fix?
- Remove the interval
* Functional form: setCount(c => c + 1)
- Use var
! The function always receives the current value.
? What causes a "hydration mismatch"?
* Server HTML different from the first client render
- Missing CSS
- A busy port
! It happens with values that depend on time, randomness or window.
