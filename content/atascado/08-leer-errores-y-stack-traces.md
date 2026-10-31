---
title: Leer errores y stack traces
desc: Guía práctica de leer errores y stack traces, errores frecuentes, decisiones y comprobaciones para resolver problemas con criterio.
---
## Leer el mensaje
Empieza por el tipo y el mensaje exacto; identifica archivo y línea relevantes de tu código. La primera línea de la pila no siempre es la causa raíz: sigue llamadas y causas encadenadas hasta el origen.

## Aislar y reproducir
Anota pasos, resultado esperado y real, versiones y entorno. Reduce el ejemplo quitando piezas sin perder el fallo; compara el último estado que funcionaba y cambia una hipótesis cada vez.

## Pedir ayuda útil
Entrega a la IA el mensaje completo, la pila, el ejemplo mínimo y lo ya intentado, sin secretos ni datos personales. Pide una hipótesis comprobable, una prueba que la descarte y la fuente oficial correspondiente.

## Decisiones rápidas
| Pregunta | Respuesta |
|---|---|
| ¿Por dónde empiezas? | Por el tipo y mensaje exactos |
| ¿Qué contiene una reproducción mínima? | Solo lo necesario para conservar el fallo |
| ¿Qué comparas? | El último estado que funcionaba |

> [!AI] Con IA
> Indica la versión, el entorno, el resultado esperado y real, y una reproducción mínima. Pide una explicación comprobable y referencias a la documentación oficial.

Documentación: [guía oficial](https://react.dev/learn/react-developer-tools).

Relacionado: [continúa con otra guía](@/js-ts/testing-con-vitest-y-playwright).

=== esquema
# Ideas clave
- Leer el mensaje — Empieza por el tipo y el mensaje exacto; identifica archivo y línea relevantes de tu código.
- Aislar y reproducir — Anota pasos, resultado esperado y real, versiones y entorno.
- Pedir ayuda útil — Entrega a la IA el mensaje completo, la pila, el ejemplo mínimo y lo ya intentado, sin secretos ni datos personales.
=== test
? ¿Por dónde empiezas?
* Por el tipo y mensaje exactos
- Solo lo necesario para conservar el fallo
- El último estado que funcionaba
! Por el tipo y mensaje exactos.
? ¿Qué contiene una reproducción mínima?
* Solo lo necesario para conservar el fallo
- El último estado que funcionaba
- Una cada vez
! Solo lo necesario para conservar el fallo.
? ¿Qué comparas?
* El último estado que funcionaba
- Una cada vez
- Secretos y datos personales
! El último estado que funcionaba.
? ¿Cómo pruebas hipótesis?
* Una cada vez
- Secretos y datos personales
- Por el tipo y mensaje exactos
! Una cada vez.
? ¿Qué eliminas antes de compartir registros?
* Secretos y datos personales
- Por el tipo y mensaje exactos
- Solo lo necesario para conservar el fallo
! Secretos y datos personales.

=== prueba

## Leer un error
```js
function parseCount(value) {
  const count = Number(value);
  if (!Number.isFinite(count)) throw new Error('Invalid count');
  return count;
}
try {
  console.log(parseCount('many'));
} catch (error) {
  console.error(error.name, error.message, error.stack);
}
```
Reto: cambia la entrada y compara el resultado.

## Conservar la causa
```js
try {
  try {
    throw new Error('Connection failed');
  } catch (error) {
    throw new Error('Could not load data', {cause: error});
  }
} catch (error) {
  console.error(error.message, error.cause.message);
}
```
Reto: inspecciona la causa además del mensaje.
