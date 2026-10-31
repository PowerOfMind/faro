---
title: Prompts que funcionan
desc: Prompts para programar con IA que ayudan a obtener respuestas útiles, con una plantilla de contexto, objetivo, restricciones y comprobación.
---
## Plantilla
```text
Contexto: Lit 3 + TypeScript, Vite, sin framework.
Objetivo: un <app-tabs> accesible con teclado.
Restricciones: sin dependencias nuevas; no toques src/legacy/.
Salida: solo el diff de los ficheros que cambian.
Comprobación: cómo verificar que funciona (comando o pasos).
```

## Qué mejora el resultado
- **Versiones explícitas** (`React 19`, `Angular 22`, `Node 22`).
- **Criterio de "hecho"**: "pasa `npm test`", "no hay errores en consola".
- **El error completo**, no la paráfrasis: mensaje, stack y la línea de código.
- **Ejemplo de entrada y salida** cuando el formato importa.
- **Pedir alternativas con trade-offs** antes de implementar algo grande.
- **Acotar el alcance**: "solo este fichero".

## Qué lo empeora
- Pedir varias cosas no relacionadas en un mensaje.
- Insistir tras 2 fallos sin cambiar nada: cambia el contexto (ver [salir del bucle](@/atascado/metodo)).
- Prompts con órdenes contradictorias ("hazlo simple y que cubra todos los casos").

> [!AI] Patrones útiles
> - "Antes de escribir código, dime qué dudas tienes."
> - "Explica por qué falla con una hipótesis y cómo comprobarla."
> - "¿Qué supuestos has hecho que yo no te haya dicho?"
> - "Revisa tu respuesta buscando APIs que podrían no existir en la versión indicada."

=== esquema
# Plantilla
- Contexto — versiones y stack (Lit 3, Node 22).
- Objetivo — una sola cosa concreta.
- Restricciones — qué no tocar y qué no añadir.
- Comprobación — cómo saber que funciona.
# Evitar
- Pedir varias cosas a la vez — mezcla el contexto.
- Insistir sin cambiar nada — cambia el contexto tras dos fallos.
- Órdenes contradictorias — "simple" y "cubre todo".
=== test
? ¿Qué mejora más un prompt de código?
* Indicar versiones y un criterio de "hecho"
- Hacerlo más largo
- Escribirlo en mayúsculas
! Versiones y criterio de éxito evitan APIs equivocadas y respuestas a medias.
? Tras dos intentos fallidos con el mismo error, ¿qué haces?
- Repetir el mismo prompt
* Cambiar el contexto: error completo, código mínimo y lo ya descartado
- Pedir lo mismo con más insistencia
! Insistir añade ruido; un contexto nuevo y mejor da otra respuesta.
? ¿Cómo pides el error a la IA?
* Con el mensaje y el stack completos y la línea de código
- Con tu resumen de qué crees que pasa
- Solo con "no funciona"
! La paráfrasis pierde los detalles que delatan la causa.
