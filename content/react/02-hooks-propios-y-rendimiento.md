---
title: Hooks propios y rendimiento
desc: Guía práctica de hooks propios y rendimiento, errores frecuentes, decisiones y comprobaciones para resolver problemas con criterio.
pkgs: react, react-dom
---
## Memorizar con criterio
`useMemo` guarda el resultado de un cálculo puro; `useCallback`, una función. `memo` permite omitir renders del hijo si sus props no cambian. Mide con el Profiler antes de optimizar: un cálculo barato o una prop siempre nueva pueden hacer inútil la memorización.

## Hooks propios
Extrae lógica reutilizable a una función `use...`; cada llamada mantiene su propio estado. Llama los hooks siempre al nivel superior e incluye todas las dependencias reactivas.

## Compiler y límites
React Compiler, cuando está instalado y activado, automatiza buena parte de la memorización. No uses la caché para corregir errores de lógica: el componente debe funcionar también sin ella.

## Decisiones rápidas
| Pregunta | Respuesta |
|---|---|
| ¿Qué guarda useMemo? | El resultado de un cálculo |
| ¿Qué guarda useCallback? | Una función |
| ¿Qué comparte un hook propio? | Lógica, no el estado entre llamadas |

> [!AI] Con IA
> Indica la versión, el entorno, el resultado esperado y real, y una reproducción mínima. Pide una explicación comprobable y referencias a la documentación oficial.

Documentación: [guía oficial](https://react.dev/reference/react/useMemo).

Relacionado: [continúa con otra guía](@/react/formularios-y-estado-global).

=== esquema
# Ideas clave
- Memorizar con criterio — `useMemo` guarda el resultado de un cálculo puro; `useCallback`, una función.
- Hooks propios — Extrae lógica reutilizable a una función `use...`; cada llamada mantiene su propio estado.
- Compiler y límites — React Compiler, cuando está instalado y activado, automatiza buena parte de la memorización.
=== test
? ¿Qué guarda useMemo?
* El resultado de un cálculo
- Una función
- Lógica, no el estado entre llamadas
! El resultado de un cálculo.
? ¿Qué guarda useCallback?
* Una función
- Lógica, no el estado entre llamadas
- Tras medir un problema
! Una función.
? ¿Qué comparte un hook propio?
* Lógica, no el estado entre llamadas
- Tras medir un problema
- Automatiza parte de la memorización
! Lógica, no el estado entre llamadas.
? ¿Cuándo conviene optimizar?
* Tras medir un problema
- Automatiza parte de la memorización
- El resultado de un cálculo
! Tras medir un problema.
? ¿Qué hace React Compiler activado?
* Automatiza parte de la memorización
- El resultado de un cálculo
- Una función
! Automatiza parte de la memorización.
=== prueba

## Cálculo derivado
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
Reto: cambia un valor y observa el resultado.

## Hook propio
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
Reto: cambia un valor y observa el resultado.
