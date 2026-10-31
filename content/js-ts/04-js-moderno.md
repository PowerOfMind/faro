---
title: JavaScript moderno que conviene conocer
desc: JavaScript moderno para reducir dependencias y evitar errores comunes, con utilidades nativas para arrays, objetos, fechas y navegador.
---
## Que ya no necesitan librería
| Antes | Ahora |
|---|---|
| lodash `cloneDeep` | `structuredClone(obj)` |
| lodash `groupBy` | `Object.groupBy(arr, fn)` / `Map.groupBy` |
| lodash `last`, `at` | `arr.at(-1)` |
| Copiar y ordenar sin mutar | `toSorted()`, `toReversed()`, `with()`, `toSpliced()` |
| `Array.from(new Set(a))` | `[...new Set(a)]` |
| axios básico | `fetch` |
| uuid | `crypto.randomUUID()` |
| Debounce de eventos de scroll | `IntersectionObserver`, `ResizeObserver` |
| Selector CSS en JS para modales | `<dialog>`, `popover` |

```js
const ultimo = lista.at(-1);
const ordenada = lista.toSorted((a, b) => a.n - b.n);   // no muta
const copia = structuredClone(estado);
```

## Operadores
- `??` solo para `null`/`undefined`; `||` también para `0` y `''`.
- `?.` evita errores en cadenas; `a?.b ?? 'x'`.
- `??=`, `||=`, `&&=` asignaciones lógicas.

## Trampas clásicas
| Trampa | Realidad |
|---|---|
| `0.1 + 0.2 !== 0.3` | Coma flotante: para dinero usa enteros (céntimos) o `Intl.NumberFormat` |
| `typeof null === 'object'` | Comprueba `=== null` |
| `[1,10,2].sort()` | Ordena como texto: pasa comparador numérico |
| `parseInt('08abc')` | Acepta basura: usa `Number()` y valida |
| `Date` y zonas horarias | `new Date('2026-10-29')` es UTC, no local |
| Igualdad de objetos | `{} === {}` es `false`: compara por valor o por id |
| `this` en callbacks | Usa arrow functions o `.bind` |

## Fechas e internacionalización
`Intl.DateTimeFormat`, `Intl.NumberFormat`, `Intl.RelativeTimeFormat` formatean sin librerías. **Temporal** es la API moderna de fechas: está llegando a los navegadores; comprueba soporte en caniuse y usa un polyfill si lo necesitas.

## Módulos
`import`/`export` nativos, `import()` dinámico para cargar bajo demanda, `import.meta.url`. Mira la sección de dependencias en [Dependencias que no cuadran](@/atascado/dependencias) para ESM vs CJS.

=== esquema
# Nativo
- structuredClone — copia profunda.
- toSorted y at — ordenar sin mutar, índice negativo.
- crypto.randomUUID — ids.
- Intl — formatos de fecha y número.
# Trampas
- ?? frente a || — ?? solo para null/undefined.
- Coma flotante — dinero en céntimos.
- sort() — ordena como texto por defecto.
=== test
? ¿Qué copia profunda es nativa?
* structuredClone
- Object.copy
- JSON.deepCopy
! Está disponible en navegadores y Node actuales.
? Diferencia entre ?? y ||:
* ?? solo actúa con null o undefined
- Son iguales
- ?? actúa con 0 y ''
! || también considera falsos 0 y la cadena vacía.
? [1, 10, 2].sort() ordena…
- Numéricamente
* Como texto
- Aleatoriamente
! Pasa un comparador numérico.
