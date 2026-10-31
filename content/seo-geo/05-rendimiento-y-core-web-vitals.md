---
title: Rendimiento y Core Web Vitals
desc: Guía práctica de rendimiento y core web vitals, errores frecuentes, decisiones y comprobaciones para resolver problemas con criterio.
---
## Métricas
LCP mide cuándo se pinta el mayor contenido visible; INP mide la capacidad de respuesta durante las interacciones; CLS mide desplazamientos inesperados de diseño. Los umbrales buenos son LCP ≤ 2,5 s, INP ≤ 200 ms y CLS ≤ 0,1, evaluados en el percentil 75 por dispositivo.

## Imágenes y fuentes
Ajusta dimensiones y formato de imágenes, reserva espacio con anchura y altura y prioriza la imagen principal cuando corresponda. Evita cargar de forma diferida el recurso LCP. Reduce variantes de fuentes y reserva espacio para limitar saltos.

## JavaScript y medición
Reduce trabajo en el hilo principal y divide tareas largas para mejorar respuesta. Compara datos reales de campo (CrUX o medición propia) con diagnósticos de Lighthouse y DevTools; INP requiere interacciones reales, mientras Lighthouse usa TBT como indicador de laboratorio.

## Decisiones rápidas
| Pregunta | Respuesta |
|---|---|
| ¿Qué mide LCP? | El pintado del mayor contenido visible |
| ¿Qué mide INP? | La respuesta a interacciones |
| ¿Qué mide CLS? | Desplazamientos inesperados |

> [!AI] Con IA
> Indica la versión, el entorno, el resultado esperado y real, y una reproducción mínima. Pide una explicación comprobable y referencias a la documentación oficial.

Documentación: [guía oficial](https://web.dev/articles/vitals).

Relacionado: [continúa con otra guía](@/react/hooks-propios-y-rendimiento).

=== esquema
# Ideas clave
- Métricas — LCP mide cuándo se pinta el mayor contenido visible; INP mide la capacidad de respuesta durante las interacciones; CLS mide desplazamientos inesperados de diseño.
- Imágenes y fuentes — Ajusta dimensiones y formato de imágenes, reserva espacio con anchura y altura y prioriza la imagen principal cuando corresponda.
- JavaScript y medición — Reduce trabajo en el hilo principal y divide tareas largas para mejorar respuesta.
=== test
? ¿Qué mide LCP?
* El pintado del mayor contenido visible
- La respuesta a interacciones
- Desplazamientos inesperados
! El pintado del mayor contenido visible.
? ¿Qué mide INP?
* La respuesta a interacciones
- Desplazamientos inesperados
- El 75
! La respuesta a interacciones.
? ¿Qué mide CLS?
* Desplazamientos inesperados
- El 75
- Diagnósticos de laboratorio
! Desplazamientos inesperados.
? ¿Qué percentil se usa para los umbrales?
* El 75
- Diagnósticos de laboratorio
- El pintado del mayor contenido visible
! El 75.
? ¿Qué aporta Lighthouse?
* Diagnósticos de laboratorio
- El pintado del mayor contenido visible
- La respuesta a interacciones
! Diagnósticos de laboratorio.
