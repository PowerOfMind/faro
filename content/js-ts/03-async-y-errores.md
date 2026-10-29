---
title: Async, promesas y errores
desc: await en bucles, Promise.all, cancelación, timeouts y manejo de errores.
---
## Paralelo vs secuencial
```js
// secuencial (lento): una tras otra
for (const id of ids) results.push(await getUser(id));
// paralelo
const results = await Promise.all(ids.map(getUser));
// paralelo tolerante a fallos
const r = await Promise.allSettled(ids.map(getUser));   // [{status, value|reason}]
```
`Promise.all` rechaza en cuanto falla una. `Promise.race` devuelve la primera. `Promise.any` la primera que **cumple**.
Con muchas peticiones, limita la concurrencia (`p-limit`) para no saturar.

## `forEach` no espera
`arr.forEach(async x => await f(x))` no espera a nadie. Usa `for...of` o `Promise.all(arr.map(...))`.

## Cancelación y timeout
```js
const ctrl = new AbortController();
const t = setTimeout(() => ctrl.abort(), 8000);
try { const r = await fetch(url, {signal: ctrl.signal}); }
finally { clearTimeout(t); }
// atajo: fetch(url, {signal: AbortSignal.timeout(8000)})
```

## `fetch` no lanza en 404/500
```js
const r = await fetch(url);
if (!r.ok) throw new Error(`HTTP ${r.status}`);
const data = await r.json();
```

## Errores
- `try/catch` alrededor de `await`, no de la promesa sin `await`.
- Una promesa rechazada sin `catch` termina en `unhandledrejection`.
- Relanza con causa: `throw new Error('No se pudo guardar', {cause: err})`.
- En TS el `catch (e)` es `unknown`: comprueba `e instanceof Error`.

## Carreras de condiciones
Si el usuario escribe rápido y llegan respuestas desordenadas, aborta la petición anterior o compara un contador/id antes de aplicar el resultado.

## Top-level await
Disponible en módulos ES (`<script type="module">`, Node ESM). No en CommonJS.
