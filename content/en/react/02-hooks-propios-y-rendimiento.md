---
title: Custom hooks and performance
desc: A practical guide to custom hooks and performance, common mistakes, decisions, and checks to help you solve problems with confidence.
pkgs: react, react-dom
---
## Memoize deliberately
`useMemo` caches a pure calculation; `useCallback` caches a function. `memo` can skip child renders when props do not change. Measure with the Profiler first: a cheap calculation or an always-new prop can make memoization pointless.

## Custom hooks
Extract reusable logic into a `use...` function; each call has its own state. Call hooks at the top level and include all reactive dependencies.

## Compiler and limits
React Compiler, when installed and enabled, automates much of the memoization. Do not use caching to fix logic errors: the component should work without it.

## Quick decisions
| Question | Answer |
|---|---|
| What does useMemo cache? | A calculation result |
| What does useCallback cache? | A function |
| What does a custom hook share? | Logic, not state between calls |

> [!AI] With AI
> Describe your version, environment, expected and actual results, and a minimal reproduction. Ask for a testable explanation and references to the official documentation.

Documentation: [official guide](https://react.dev/reference/react/useMemo).

Related: [continue with a related guide](@/react/formularios-y-estado-global).

=== esquema
# Key ideas
- Memoize deliberately — `useMemo` caches a pure calculation; `useCallback` caches a function.
- Custom hooks — Extract reusable logic into a `use...` function; each call has its own state.
- Compiler and limits — React Compiler, when installed and enabled, automates much of the memoization.
=== test
? What does useMemo cache?
* A calculation result
- A function
- Logic, not state between calls
! A calculation result.
? What does useCallback cache?
* A function
- Logic, not state between calls
- After measuring a problem
! A function.
? What does a custom hook share?
* Logic, not state between calls
- After measuring a problem
- Automates some memoization
! Logic, not state between calls.
? When should you optimize?
* After measuring a problem
- Automates some memoization
- A calculation result
! After measuring a problem.
? What does an enabled React Compiler do?
* Automates some memoization
- A calculation result
- A function
! Automates some memoization.
=== prueba

## Derived calculation
```jsx
import {useState, useMemo} from 'react';
import {createRoot} from 'react-dom/client';
const names = ['Ada', 'Lin', 'Sam'];
function App() {
  const [query, setQuery] = useState('');
  const visible = useMemo(() => names.filter(name => name.toLowerCase().includes(query.toLowerCase())), [query]);
  return <><input aria-label="Search" value={query} onChange={e => setQuery(e.target.value)} /><p>{visible.join(', ')}</p></>;
}
createRoot(document.getElementById('app')).render(<App />);
```
Reto: change a value and observe the result.

## Custom hook
```jsx
import {useState} from 'react';
import {createRoot} from 'react-dom/client';
function useCounter() {
  const [count, setCount] = useState(0);
  return [count, () => setCount(n => n + 1)];
}
function App() {
  const [count, increment] = useCounter();
  return <button onClick={increment}>Count: {count}</button>;
}
createRoot(document.getElementById('app')).render(<App />);
```
Reto: change a value and observe the result.
