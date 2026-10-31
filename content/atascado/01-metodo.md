---
title: Salir del bucle con la IA
desc: Depuración con IA para salir de intentos repetidos, reproducir errores, contrastar hipótesis y aportar contexto útil en una conversación nueva.
---
El patrón: la IA propone un arreglo, falla, propone otro parecido, falla. **Cada intento añade ruido al contexto.** Para.

## Método
1. **Reproduce en pequeño.** Un fichero mínimo que falle. Si no consigues reproducirlo, aún no entiendes el problema.
2. **Lee el error entero**, de abajo arriba en el stack: la primera línea *tuya* suele ser la causa.
3. **Una hipótesis, una prueba.** Cambia una cosa y observa. No apliques tres arreglos a la vez.
4. **Mide, no supongas.** `console.log` del valor real, `typeof`, Network del navegador, versión instalada (`npm ls paquete`).
5. **Busca el mensaje literal** entre comillas en el issue tracker del proyecto, no solo en un buscador.
6. **Reinicia la conversación** con: versión de todo, código mínimo, error exacto, y **lo que ya has descartado**.
7. **Cambia de ángulo**: pide a la IA que explique el concepto, no que arregle el fallo.

## Dónde buscar cuando la IA no sabe
| Fuente | Cuándo |
|---|---|
| Documentación oficial de **tu versión** | Primero siempre |
| Issues del repositorio (abiertos y cerrados) | Bugs y regresiones |
| Releases / CHANGELOG | "Antes funcionaba" |
| Discusiones del repo, Discord oficial | Casos raros |
| Stack Overflow | Errores clásicos; mira la fecha y la versión |
| Código fuente de la librería | Cuando la doc calla |

## Pregunta que sí obtiene respuesta (humana o IA)
```text
Quiero: <objetivo>
Entorno: Node 22, Vite 7, Windows 11
Código mínimo: <20 líneas>
Esperado: <...>  Obtenido: <error completo>
Ya probé: <1>, <2>
```

> [!TIP] Bisección
> Si "antes funcionaba": `git bisect` o vuelve al último commit bueno y reaplica los cambios de uno en uno.

=== esquema
# Método
- Reproducir en pequeño — un fichero mínimo que falle.
- Una hipótesis, una prueba — cambia una cosa a la vez.
- Medir — log del valor real y versión instalada.
# Si sigue
- Buscar el mensaje literal — en los issues del proyecto.
- Reiniciar la conversación — con versiones, código mínimo y lo descartado.
- git bisect — si antes funcionaba.
=== test
? ¿Qué haces antes de pedir otra solución a la IA?
- Pedir tres arreglos a la vez
* Reproducir el fallo en un ejemplo mínimo
- Cambiar de framework
! Si no puedes reproducirlo en pequeño, aún no entiendes el problema.
? En un stack trace, ¿qué línea suele indicar la causa?
* La primera línea de tu propio código
- La última de librerías
- La primera de todas
! Las líneas de librería suelen ser consecuencia de algo que llamaste tú.
? "Antes funcionaba": ¿qué herramienta ayuda?
- git blame sobre todo el repo
* git bisect
- npm audit
! Bisect encuentra el commit que rompió algo.
