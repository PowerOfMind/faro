---
title: Async, promises and errors
desc: await in loops, Promise.all, cancellation, timeouts and error handling.
---
## Parallel vs sequential
```js
// sequential (slow): one after another
for (const id of ids) results.push(await getUser(id));
// parallel
const results = await Promise.all(ids.map(getUser));
// parallel and failure-tolerant
const r = await Promise.allSettled(ids.map(getUser));   // [{status, value|reason}]
```
`Promise.all` rejects as soon as one fails. `Promise.race` returns the first to finish. `Promise.any` returns the first that **fulfils**.
With many requests, limit concurrency (`p-limit`) so you do not saturate.

## `forEach` does not wait
`arr.forEach(async x => await f(x))` waits for nobody. Use `for...of` or `Promise.all(arr.map(...))`.

## Cancellation and timeout
```js
const ctrl = new AbortController();
const t = setTimeout(() => ctrl.abort(), 8000);
try { const r = await fetch(url, {signal: ctrl.signal}); }
finally { clearTimeout(t); }
// shortcut: fetch(url, {signal: AbortSignal.timeout(8000)})
```

## `fetch` does not throw on 404/500
```js
const r = await fetch(url);
if (!r.ok) throw new Error(`HTTP ${r.status}`);
const data = await r.json();
```

## Errors
- `try/catch` around `await`, not around the promise without `await`.
- A rejected promise with no `catch` ends in `unhandledrejection`.
- Rethrow with a cause: `throw new Error('Could not save', {cause: err})`.
- In TS `catch (e)` is `unknown`: check `e instanceof Error`.

## Race conditions
If the user types fast and responses arrive out of order, abort the previous request or compare a counter/id before applying the result.

## Top-level await
Available in ES modules (`<script type="module">`, Node ESM). Not in CommonJS.

=== esquema
# Parallel
- Promise.all — rejects as soon as one fails.
- allSettled — waits for all and gives each status.
- race and any — first finished or first fulfilled.
# Safety
- AbortController — cancellation and timeout.
- fetch does not throw on 404/500 — check r.ok.
- forEach does not wait — use for...of or Promise.all.
=== test
? Does fetch throw on a 404?
- Yes
* No: you must check r.ok
- Only on 500
! fetch only fails on network errors.
? Does arr.forEach(async ...) wait?
- Yes
* No
- Only with an outer await
! Use for...of or Promise.all(arr.map(...)).
? How do you put a timeout on a fetch?
* AbortSignal.timeout(ms)
- A bare setTimeout
- With try/catch
! The signal aborts the request.
