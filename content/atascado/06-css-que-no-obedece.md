---
title: CSS que no obedece
desc: z-index, scroll horizontal, 100vh móvil, flex que desborda, Safari.
---
## z-index no funciona
Crea un **contexto de apilamiento** el ancestro con `position`+`z-index`, `transform`, `opacity<1`, `filter`, `isolation`. Un hijo nunca sale de él. Soluciona subiendo el ancestro, o sacando el elemento (modales: `<dialog>` + `showModal()` o un portal).

## Scroll horizontal inesperado
1. Inspecciona: `document.querySelectorAll('*').forEach(e => e.scrollWidth > innerWidth && console.log(e))`.
2. Causas: `100vw` (incluye la barra de scroll), imágenes sin `max-width:100%`, `pre` o tablas anchas, márgenes negativos.
3. No lo tapes con `overflow-x:hidden` en `body` sin encontrar el origen.

## Flex/Grid que desborda
Los hijos flex tienen `min-width:auto`: un texto largo o `pre` empuja. Solución: `min-width:0` en el hijo y `overflow:auto`. En grid: `minmax(0,1fr)` en vez de `1fr`.

## 100vh en móvil
La barra del navegador lo rompe. Usa `100dvh` (o `svh`/`lvh` según el caso).

## Posiciones y alturas
- `position:sticky` no pega si un ancestro tiene `overflow` distinto de `visible`.
- `height:100%` exige que el padre tenga altura definida.
- `margin` colapsa entre hermanos y padre-hijo; usa `gap` en flex/grid.

## Móvil y táctil
- Objetivos táctiles de **44×44 px** mínimo.
- `font-size` < 16px en `input` hace que iOS haga zoom al enfocar.
- `:hover` no existe en táctil: no escondas funciones tras él.

## Modo oscuro
Define colores como variables (`--bg`, `--text`), cambia el conjunto bajo `prefers-color-scheme: dark` y permite forzar con un atributo. Revisa contraste en ambos (WCAG AA: 4.5:1).

> [!AI] Para pedir CSS a una IA
> Dale el HTML real y el contenedor padre; sin ellos inventa estructura. Pídele la causa, no solo un `!important`.

=== esquema
# Capas y desbordes
- Contexto de apilamiento — position+z-index, transform, opacity<1.
- 100vw — incluye la barra de scroll y desborda.
- min-width:0 — para hijos flex con texto o pre largos.
# Móvil
- 100dvh — en vez de 100vh.
- 44×44 px — objetivo táctil mínimo.
- font-size 16px — evita el zoom de iOS en inputs.
=== test
? Un z-index enorme no pone tu modal delante. ¿Por qué?
* Un ancestro crea otro contexto de apilamiento
- El navegador ignora z-index
- Falta !important
! El hijo no sale del contexto de su ancestro.
? Un hijo flex con texto largo empuja el ancho. ¿Arreglo?
- width:100vw
* min-width:0 y overflow adecuado
- display:block en el body
! Los hijos flex tienen min-width:auto por defecto.
? ¿Qué unidad usas para altura de pantalla completa en móvil?
- 100vh
* 100dvh
- 100%
! dvh se ajusta a la barra del navegador.
