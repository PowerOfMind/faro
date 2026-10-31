---
title: Forms and global state
desc: A practical guide to forms and global state, common mistakes, decisions, and checks to help you solve problems with confidence.
pkgs: react, react-dom
---
## Inputs and Actions
A controlled input receives `value` and updates state via `onChange`. In React 19, a function passed to `action` receives `FormData`; `useActionState` represents the result and pending state. Validate on the server too.

## Reducer and Context
`useReducer` centralizes transitions in a pure function; Context distributes state and `dispatch` to descendants. Keep state local when only one screen needs it.

## Choosing a tool
For complex shared state consider Zustand or Redux; for remote data, caching and synchronization consider TanStack Query or the framework data loader. These solve different problems: avoid duplicating derived data.

## Quick decisions
| Question | Answer |
|---|---|
| What controls a controlled input? | React state |
| What does a form action receive? | FormData |
| What does a reducer do? | Calculates the next state |

> [!AI] With AI
> Describe your version, environment, expected and actual results, and a minimal reproduction. Ask for a testable explanation and references to the official documentation.

Documentation: [official guide](https://react.dev/reference/react-dom/components/form).

Related: [continue with a related guide](@/react/hooks-propios-y-rendimiento).

=== esquema
# Key ideas
- Inputs and Actions — A controlled input receives `value` and updates state via `onChange`.
- Reducer and Context — `useReducer` centralizes transitions in a pure function; Context distributes state and `dispatch` to descendants.
- Choosing a tool — For complex shared state consider Zustand or Redux; for remote data, caching and synchronization consider TanStack Query or the framework data loader.
=== test
? What controls a controlled input?
* React state
- FormData
- Calculates the next state
! React state.
? What does a form action receive?
* FormData
- Calculates the next state
- Distributes values to descendants
! FormData.
? What does a reducer do?
* Calculates the next state
- Distributes values to descendants
- Remote data and its cache
! Calculates the next state.
? What does Context do?
* Distributes values to descendants
- Remote data and its cache
- React state
! Distributes values to descendants.
? What does TanStack Query address?
* Remote data and its cache
- React state
- FormData
! Remote data and its cache.
=== prueba

## Controlled input
```jsx
import {useState} from 'react';
import {createRoot} from 'react-dom/client';
function App() {
  const [name, setName] = useState('');
  return <><label>Name <input value={name} onChange={e => setName(e.target.value)} /></label><p>Hello, {name || 'visitor'}</p></>;
}
createRoot(document.getElementById('app')).render(<App />);
```
Reto: change a value and observe the result.

## Form action
```jsx
import {useActionState} from 'react';
import {createRoot} from 'react-dom/client';
function App() {
  const [message, submit, pending] = useActionState(async (_previous, data) => {
    const name = String(data.get('name') || '').trim();
    return name ? 'Hello, ' + name : 'Enter a name';
  }, '');
  return <form action={submit}><label>Name <input name="name" /></label><button disabled={pending}>Send</button><p>{message}</p></form>;
}
createRoot(document.getElementById('app')).render(<App />);
```
Reto: change a value and observe the result.
