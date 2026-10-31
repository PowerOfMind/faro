---
title: Formularios y estado global
desc: Guía práctica de formularios y estado global, errores frecuentes, decisiones y comprobaciones para resolver problemas con criterio.
pkgs: react, react-dom
---
## Campos y Actions
Un campo controlado recibe `value` y actualiza el estado con `onChange`. En React 19, una función en `action` recibe `FormData`; `useActionState` permite representar resultado y estado pendiente. Valida también en el servidor.

## Reducer y Context
`useReducer` concentra transiciones en una función pura; Context distribuye estado y `dispatch` a descendientes. Mantén local el estado que solo necesita una pantalla.

## Elegir herramienta
Para estado compartido complejo considera Zustand o Redux; para datos remotos, caché y sincronización considera TanStack Query o la carga de datos del framework. Son problemas distintos: evita duplicar datos derivados.

## Decisiones rápidas
| Pregunta | Respuesta |
|---|---|
| ¿Qué controla un input controlado? | El estado de React |
| ¿Qué recibe una form action? | FormData |
| ¿Qué hace un reducer? | Calcula el siguiente estado |

> [!AI] Con IA
> Indica la versión, el entorno, el resultado esperado y real, y una reproducción mínima. Pide una explicación comprobable y referencias a la documentación oficial.

Documentación: [guía oficial](https://react.dev/reference/react-dom/components/form).

Relacionado: [continúa con otra guía](@/react/hooks-propios-y-rendimiento).

=== esquema
# Ideas clave
- Campos y Actions — Un campo controlado recibe `value` y actualiza el estado con `onChange`.
- Reducer y Context — `useReducer` concentra transiciones en una función pura; Context distribuye estado y `dispatch` a descendientes.
- Elegir herramienta — Para estado compartido complejo considera Zustand o Redux; para datos remotos, caché y sincronización considera TanStack Query o la carga de datos del framework.
=== test
? ¿Qué controla un input controlado?
* El estado de React
- FormData
- Calcula el siguiente estado
! El estado de React.
? ¿Qué recibe una form action?
* FormData
- Calcula el siguiente estado
- Distribuir valores a descendientes
! FormData.
? ¿Qué hace un reducer?
* Calcula el siguiente estado
- Distribuir valores a descendientes
- Datos remotos y su caché
! Calcula el siguiente estado.
? ¿Para qué sirve Context?
* Distribuir valores a descendientes
- Datos remotos y su caché
- El estado de React
! Distribuir valores a descendientes.
? ¿Qué problema aborda TanStack Query?
* Datos remotos y su caché
- El estado de React
- FormData
! Datos remotos y su caché.
=== prueba

## Campo controlado
```jsx
import {useState} from 'react';
import {createRoot} from 'react-dom/client';
function App() {
  const [name, setName] = useState('');
  return <><label>Name <input value={name} onChange={e => setName(e.target.value)} /></label><p>Hello, {name || 'visitor'}</p></>;
}
createRoot(document.getElementById('app')).render(<App />);
```
Reto: cambia un valor y observa el resultado.

## Action de formulario
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
Reto: cambia un valor y observa el resultado.
