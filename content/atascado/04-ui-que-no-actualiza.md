---
title: La UI no se actualiza o parpadea
desc: Estado obsoleto, hydration mismatch, keys, efectos en bucle y mutaciones.
---
## Estado obsoleto (stale closure)
Un callback capturó el valor viejo.
```jsx
// mal: siempre usa count del primer render
useEffect(() => { const id = setInterval(() => setCount(count + 1), 1000); return () => clearInterval(id); }, []);
// bien: forma funcional
setCount(c => c + 1);
```

## No re-renderiza
| Marco | Causa típica |
|---|---|
| React | Mutaste el estado en sitio (`arr.push`) en vez de crear uno nuevo |
| Lit | Mutaste objeto/array, o un class field sombrea el accessor (ver [reactividad](@/lit/reactividad)) |
| Angular | `OnPush` con mutación; usa signals o referencias nuevas |
| Vue | Reasignar un `reactive` completo pierde la reactividad |

## Efectos que se disparan sin parar
- Objeto o función creado en cada render dentro de las dependencias del efecto.
- Efecto que cambia lo que él mismo escucha.
- Solución: dependencias primitivas, `useMemo` / `useCallback` si hace falta, o mover la lógica a un manejador de evento (muchos `useEffect` sobran).

## Hydration mismatch (SSR)
El HTML del servidor difiere del primer render en cliente.
- Causas: `Date.now()`, `Math.random()`, `window`/`localStorage` en el render, zonas horarias, extensiones del navegador.
- Arreglo: calcular esos valores tras montar (`useEffect`) o marcarlos como solo cliente.

## Keys en listas
`key={index}` con listas que se reordenan mezcla estado entre filas (inputs que "saltan"). Usa un id estable.

## Si nada cambia aun así
1. ¿Edita el fichero correcto? (¿hay `dist/` o copia generada?)
2. ¿Caché de service worker o del bundler? Reinicia el servidor de desarrollo.
3. ¿Estás probando la URL de producción mientras cambias el local?

> [!TIP] Depurar en 2 minutos
> React DevTools / Angular DevTools: mira qué estado hay realmente, no el que crees.

=== esquema
# Causas
- Mutación — arr.push en vez de crear un array nuevo.
- Stale closure — un callback capturó el valor viejo.
- Dependencia inestable — objeto nuevo en cada render dentro de un efecto.
# SSR
- Hydration mismatch — Date.now() o window durante el render.
- key={index} — mezcla estado entre filas al reordenar.
=== test
? Mutas un array del estado y la UI no cambia. ¿Por qué?
* La referencia es la misma, no se detecta el cambio
- El navegador lo cachea
- Falta un return
! Crea una copia nueva: [...items, x].
? setCount(count + 1) dentro de un setInterval con deps [] siempre pone 1. ¿Solución?
- Quitar el intervalo
* Forma funcional: setCount(c => c + 1)
- Usar var
! La función recibe siempre el valor actual.
? ¿Qué provoca un "hydration mismatch"?
* HTML de servidor distinto al primer render en cliente
- Falta de CSS
- Un puerto ocupado
! Pasa con valores que dependen de la hora, aleatorios o de window.
