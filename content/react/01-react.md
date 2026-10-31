---
title: React: modelo mental y trampas
desc: React para entender el renderizado y evitar errores de estado, con reglas de hooks, efectos, listas y novedades de React 19.
pkgs: react, react-dom, next
---
## Modelo mental
Un componente es una **función de (props, estado) → UI**. React lo vuelve a llamar cuando cambia el estado; el resultado se compara y se actualiza el DOM. Las funciones deben ser puras: nada de efectos al renderizar.

## Reglas
- Estado **inmutable**: `setItems([...items, x])`, nunca `items.push(x)`.
- Hooks solo al nivel superior de componentes y hooks propios; nunca en condiciones ni bucles.
- `key` estable en listas (id, no índice si se reordena).
- Estado derivado se **calcula**, no se guarda (`const total = items.length`).
- Levanta el estado al ancestro común; Context para datos globales poco cambiantes.

## `useEffect`: para sincronizar con lo externo
Necesario para suscripciones, timers, fetch inicial o integrar librerías. **No** para transformar datos ni responder a un clic (eso va en el manejador).
```jsx
useEffect(() => {
  const c = new AbortController();
  fetch(`/api/u/${id}`, {signal: c.signal}).then(r => r.json()).then(setUser);
  return () => c.abort();          // limpieza
}, [id]);
```
Para datos de servidor usa **TanStack Query** (o la carga de datos de tu framework), no `useEffect` a mano.

## Novedades de React 19 (resumen)
- **Actions** y hooks `useActionState`, `useFormStatus`, `useOptimistic` para formularios.
- **`use(promise | context)`** para leer promesas y contexto con Suspense.
- `ref` como prop normal (sin `forwardRef` en componentes nuevos).
- **Custom elements** soportados de forma nativa (propiedades y eventos).
- **Server Components** y Server Actions (en frameworks como Next); el **React Compiler** memoriza automáticamente cuando está activado.

## Errores que se repiten
| Síntoma | Causa |
|---|---|
| Bucle infinito de renders | `setState` dentro del render o dependencia inestable en `useEffect` |
| Valor viejo en callback | Cierre sobre estado antiguo (ver [UI que no actualiza](@/atascado/ui-que-no-actualiza)) |
| `Hydration failed` | Contenido distinto servidor/cliente |
| `Too many re-renders` | `onClick={fn()}` en vez de `onClick={fn}` |
| Estado que "se pierde" | El componente cambia de posición/`key` y se remonta |

> [!AI] Con IA
> Pide "React 19, componentes de función, sin `useEffect` salvo que sea imprescindible". Sin eso tiende a abusar de efectos y de `useMemo`.

=== esquema
# Modelo
- Componente — función de props y estado a UI.
- Estado inmutable — copias nuevas, nunca push.
- Estado derivado — se calcula, no se guarda.
# Efectos
- useEffect — para sincronizar con lo externo.
- Limpieza — return en el efecto.
- Datos de servidor — TanStack Query o loader del framework.
# React 19
- Actions y use — formularios y promesas.
- ref como prop — sin forwardRef.
=== test
? ¿Cuándo se usa useEffect?
* Para sincronizar con algo externo: suscripciones, timers, integraciones
- Para transformar datos
- Para responder a un clic
! Lo demás se calcula en render o va en el manejador.
? Un callback ve el estado antiguo. ¿Causa y arreglo?
* Cierre sobre valor viejo; usa la forma funcional
- Falta un key
- Es un bug del navegador
! setX(prev => ...) recibe siempre el valor actual.
? ¿Qué key usas en listas que se reordenan?
- El índice
* Un id estable
- Math.random()
! El índice mezcla estado entre filas.
