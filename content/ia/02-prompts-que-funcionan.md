---
title: Prompts que funcionan
desc: Estructura corta para pedir código y análisis sin ida y vuelta.
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
