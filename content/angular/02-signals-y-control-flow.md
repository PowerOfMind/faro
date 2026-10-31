---
title: Angular: signals y control de flujo
desc: Guía práctica de angular: signals y control de flujo, errores frecuentes, decisiones y comprobaciones para resolver problemas con criterio.
pkgs: @angular/core
---
## Signals
`signal` contiene un valor que se lee llamándolo: `count()`. Actualiza con `set` o `update`; `computed` deriva un valor y sigue sus dependencias. No mutar objetos internamente evita cambios que no se notifiquen.

## Effect
`effect` ejecuta lógica al cambiar las señales que lee; úsalo para sincronizar con sistemas externos, no para copiar estado derivado. Normalmente se crea en un contexto de inyección, como el constructor de un componente.

## Plantillas y standalone
`@if` representa condiciones; `@for (item of items; track item.id)` identifica filas con una clave estable y admite `@empty`. Un componente standalone importa directamente las dependencias de su plantilla.

## Decisiones rápidas
| Pregunta | Respuesta |
|---|---|
| ¿Cómo lees una signal? | Llamándola como función |
| ¿Cómo derivas un valor? | Con computed |
| ¿Para qué sirve effect? | Para sincronizar con sistemas externos |

> [!AI] Con IA
> Indica la versión, el entorno, el resultado esperado y real, y una reproducción mínima. Pide una explicación comprobable y referencias a la documentación oficial.

Documentación: [guía oficial](https://angular.dev/guide/signals).

Relacionado: [continúa con otra guía](@/angular/formularios-http-y-rxjs).

=== esquema
# Ideas clave
- Signals — `signal` contiene un valor que se lee llamándolo: `count()`.
- Effect — `effect` ejecuta lógica al cambiar las señales que lee; úsalo para sincronizar con sistemas externos, no para copiar estado derivado.
- Plantillas y standalone — `@if` representa condiciones; `@for (item of items; track item.id)` identifica filas con una clave estable y admite `@empty`.
=== test
? ¿Cómo lees una signal?
* Llamándola como función
- Con computed
- Para sincronizar con sistemas externos
! Llamándola como función.
? ¿Cómo derivas un valor?
* Con computed
- Para sincronizar con sistemas externos
- track con una clave estable
! Con computed.
? ¿Para qué sirve effect?
* Para sincronizar con sistemas externos
- track con una clave estable
- En sus imports
! Para sincronizar con sistemas externos.
? ¿Qué identifica filas en @for?
* track con una clave estable
- En sus imports
- Llamándola como función
! track con una clave estable.
? ¿Dónde importa dependencias un componente standalone?
* En sus imports
- Llamándola como función
- Con computed
! En sus imports.
