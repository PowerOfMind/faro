---
title: Testing con Vitest y Playwright
desc: Guía práctica de testing con vitest y playwright, errores frecuentes, decisiones y comprobaciones para resolver problemas con criterio.
pkgs: vitest, @playwright/test, @testing-library/react
---
## Elegir pruebas
Prueba reglas y casos límite con Vitest; usa React Testing Library para comportamiento observable de componentes y Playwright para recorridos completos en navegador. Prioriza lo que puede fallar y afecta al usuario.

## Mocks
Simula límites externos cuando sea necesario, por ejemplo una petición o un reloj, y restablece los mocks entre pruebas. No simules la función cuya lógica quieres verificar: perderías la señal de la prueba.

## E2E sin flakiness
Usa localizadores por rol y nombre, datos aislados y aserciones que esperan el estado esperado. Evita tiempos fijos y dependencias entre pruebas. Investiga trazas y causa del fallo antes de repetir o ampliar timeouts.

## Decisiones rápidas
| Pregunta | Respuesta |
|---|---|
| ¿Qué comprueba una prueba E2E? | Un recorrido completo en navegador |
| ¿Qué conviene simular? | Un límite externo cuando sea necesario |
| ¿Qué localizador suele reflejar la interfaz accesible? | Rol y nombre |

> [!AI] Con IA
> Indica la versión, el entorno, el resultado esperado y real, y una reproducción mínima. Pide una explicación comprobable y referencias a la documentación oficial.

Documentación: [guía oficial](https://playwright.dev/docs/best-practices).

Relacionado: [continúa con otra guía](@/js-ts/modulos-y-bundlers).

=== esquema
# Ideas clave
- Elegir pruebas — Prueba reglas y casos límite con Vitest; usa React Testing Library para comportamiento observable de componentes y Playwright para recorridos completos en navegador.
- Mocks — Simula límites externos cuando sea necesario, por ejemplo una petición o un reloj, y restablece los mocks entre pruebas.
- E2E sin flakiness — Usa localizadores por rol y nombre, datos aislados y aserciones que esperan el estado esperado.
=== test
? ¿Qué comprueba una prueba E2E?
* Un recorrido completo en navegador
- Un límite externo cuando sea necesario
- Rol y nombre
! Un recorrido completo en navegador.
? ¿Qué conviene simular?
* Un límite externo cuando sea necesario
- Rol y nombre
- Datos aislados
! Un límite externo cuando sea necesario.
? ¿Qué localizador suele reflejar la interfaz accesible?
* Rol y nombre
- Datos aislados
- Investigar su causa y las trazas
! Rol y nombre.
? ¿Qué reduce interferencias entre pruebas?
* Datos aislados
- Investigar su causa y las trazas
- Un recorrido completo en navegador
! Datos aislados.
? ¿Qué hacer ante un fallo intermitente?
* Investigar su causa y las trazas
- Un recorrido completo en navegador
- Un límite externo cuando sea necesario
! Investigar su causa y las trazas.
