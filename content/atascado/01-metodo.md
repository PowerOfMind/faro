---
title: Salir del bucle con la IA
desc: Qué hacer cuando llevas tres intentos y el error sigue igual.
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
