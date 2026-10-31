---
title: Angular: formularios, HTTP y RxJS
desc: Guía práctica de angular: formularios, http y rxjs, errores frecuentes, decisiones y comprobaciones para resolver problemas con criterio.
pkgs: @angular/core, @angular/forms, @angular/common, rxjs
---
## Formularios reactivos
`FormControl` representa un campo y `FormGroup` agrupa controles. Importa `ReactiveFormsModule`, aplica validadores y muestra errores cuando el campo se haya tocado o enviado. No confíes solo en la validación del cliente.

## HTTP
Configura `provideHttpClient()` y usa `HttpClient` desde un servicio. Sus métodos devuelven observables: cada suscripción a una petición HTTP puede iniciar otra petición. Gestiona errores y estados de carga.

## RxJS y plantilla
`map` transforma emisiones, `switchMap` cambia al observable más reciente y `catchError` permite gestionar fallos. La pipe `async` se suscribe y libera la suscripción al destruirse la vista; evita suscripciones manuales sin limpieza.

## Decisiones rápidas
| Pregunta | Respuesta |
|---|---|
| ¿Qué representa FormControl? | Un campo |
| ¿Cómo se configura HttpClient? | Con provideHttpClient |
| ¿Qué puede provocar suscribirse dos veces a HTTP? | Dos peticiones |

> [!AI] Con IA
> Indica la versión, el entorno, el resultado esperado y real, y una reproducción mínima. Pide una explicación comprobable y referencias a la documentación oficial.

Documentación: [guía oficial](https://angular.dev/guide/forms/reactive-forms).

Relacionado: [continúa con otra guía](@/angular/signals-y-control-flow).

=== esquema
# Ideas clave
- Formularios reactivos — `FormControl` representa un campo y `FormGroup` agrupa controles.
- HTTP — Configura `provideHttpClient()` y usa `HttpClient` desde un servicio.
- RxJS y plantilla — `map` transforma emisiones, `switchMap` cambia al observable más reciente y `catchError` permite gestionar fallos.
=== test
? ¿Qué representa FormControl?
* Un campo
- Con provideHttpClient
- Dos peticiones
! Un campo.
? ¿Cómo se configura HttpClient?
* Con provideHttpClient
- Dos peticiones
- Cambia al observable más reciente
! Con provideHttpClient.
? ¿Qué puede provocar suscribirse dos veces a HTTP?
* Dos peticiones
- Cambia al observable más reciente
- La pipe al destruirse la vista
! Dos peticiones.
? ¿Qué hace switchMap?
* Cambia al observable más reciente
- La pipe al destruirse la vista
- Un campo
! Cambia al observable más reciente.
? ¿Quién libera la suscripción de async?
* La pipe al destruirse la vista
- Un campo
- Con provideHttpClient
! La pipe al destruirse la vista.
