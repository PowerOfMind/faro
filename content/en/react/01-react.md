---
title: React: mental model and traps
desc: React fundamentals help developers reason about rendering, state and effects. Review common mistakes and an overview of React 19 features.
pkgs: react, react-dom, next
---
## Mental model
A component is a **function of (props, state) → UI**. React calls it again when state changes; the result is compared and the DOM updated. Functions must be pure: no side effects while rendering.

## Rules
- **Immutable** state: `setItems([...items, x])`, never `items.push(x)`.
- Hooks only at the top level of components and custom hooks; never in conditions or loops.
- A stable `key` in lists (id, not index if it reorders).
- Derived state is **computed**, not stored (`const total = items.length`).
- Lift state to the common ancestor; Context for rarely-changing global data.

## `useEffect`: to sync with the outside world
Needed for subscriptions, timers, initial fetch or integrating libraries. **Not** for transforming data or reacting to a click (that goes in the handler).
```jsx
useEffect(() => {
  const c = new AbortController();
  fetch(`/api/u/${id}`, {signal: c.signal}).then(r => r.json()).then(setUser);
  return () => c.abort();          // cleanup
}, [id]);
```
For server data use **TanStack Query** (or your framework's data loading), not a hand-written `useEffect`.

## What is new in React 19 (summary)
- **Actions** and the hooks `useActionState`, `useFormStatus`, `useOptimistic` for forms.
- **`use(promise | context)`** to read promises and context with Suspense.
- `ref` as a normal prop (no `forwardRef` in new components).
- **Custom elements** supported natively (properties and events).
- **Server Components** and Server Actions (in frameworks like Next); the **React Compiler** memoises automatically when enabled.

## Errors that repeat
| Symptom | Cause |
|---|---|
| Infinite render loop | `setState` during render or an unstable dependency in `useEffect` |
| Old value in a callback | Closure over old state (see [UI does not update](@/atascado/ui-que-no-actualiza)) |
| `Hydration failed` | Content differs between server and client |
| `Too many re-renders` | `onClick={fn()}` instead of `onClick={fn}` |
| State that "gets lost" | The component changes position/`key` and remounts |

> [!AI] With AI
> Ask for "React 19, function components, no `useEffect` unless essential". Without that it tends to overuse effects and `useMemo`.

=== esquema
# Model
- Component — a function from props and state to UI.
- Immutable state — new copies, never push.
- Derived state — computed, not stored.
# Effects
- useEffect — to sync with the outside world.
- Cleanup — the return in the effect.
- Server data — TanStack Query or the framework loader.
# React 19
- Actions and use — forms and promises.
- ref as a prop — no forwardRef.
=== test
? When do you use useEffect?
* To sync with something external: subscriptions, timers, integrations
- To transform data
- To respond to a click
! The rest is computed in render or goes in the handler.
? A callback sees the old state. Cause and fix?
* Closure over an old value; use the functional form
- A key is missing
- It is a browser bug
! setX(prev => ...) always receives the current value.
? Which key do you use in lists that reorder?
- The index
* A stable id
- Math.random()
! The index mixes state between rows.
