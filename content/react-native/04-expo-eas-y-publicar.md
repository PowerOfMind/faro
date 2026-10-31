---
title: Expo EAS y publicación
desc: Guía práctica de expo eas y publicación, errores frecuentes, decisiones y comprobaciones para resolver problemas con criterio.
pkgs: expo, expo-updates
---
## De desarrollo a producción
Una development build incorpora el código y configuración nativos del proyecto. Expo Go tiene módulos nativos limitados. Cambios nativos requieren una nueva build compatible.

## Build, Update y Submit
EAS Build genera binarios; EAS Update entrega JavaScript y recursos compatibles; EAS Submit envía binarios a las plataformas de las tiendas. El envío no garantiza la aprobación ni la publicación automática en todas las tiendas.

## Canales y versiones
Una build apunta a un canal; la actualización debe coincidir en plataforma y `runtimeVersion` con su código nativo. Cambia la versión de runtime cuando cambie la compatibilidad nativa o usa una política adecuada. Comprueba identificadores, versión visible y número de build para cada tienda, y prueba antes de publicar.

## Decisiones rápidas
| Pregunta | Respuesta |
|---|---|
| ¿Qué genera EAS Build? | Binarios |
| ¿Qué distribuye EAS Update? | JavaScript y recursos compatibles |
| ¿Qué hace EAS Submit? | Envía binarios a plataformas de tiendas |

> [!AI] Con IA
> Indica la versión, el entorno, el resultado esperado y real, y una reproducción mínima. Pide una explicación comprobable y referencias a la documentación oficial.

Documentación: [guía oficial](https://docs.expo.dev/eas-update/runtime-versions/).

Relacionado: [continúa con otra guía](@/react-native/expo-router-y-navegacion).

=== esquema
# Ideas clave
- De desarrollo a producción — Una development build incorpora el código y configuración nativos del proyecto.
- Build, Update y Submit — EAS Build genera binarios; EAS Update entrega JavaScript y recursos compatibles; EAS Submit envía binarios a las plataformas de las tiendas.
- Canales y versiones — Una build apunta a un canal; la actualización debe coincidir en plataforma y `runtimeVersion` con su código nativo.
=== test
? ¿Qué genera EAS Build?
* Binarios
- JavaScript y recursos compatibles
- Envía binarios a plataformas de tiendas
! Binarios.
? ¿Qué distribuye EAS Update?
* JavaScript y recursos compatibles
- Envía binarios a plataformas de tiendas
- Compatibilidad con el código nativo
! JavaScript y recursos compatibles.
? ¿Qué hace EAS Submit?
* Envía binarios a plataformas de tiendas
- Compatibilidad con el código nativo
- Una nueva build compatible
! Envía binarios a plataformas de tiendas.
? ¿Qué comprueba runtimeVersion?
* Compatibilidad con el código nativo
- Una nueva build compatible
- Binarios
! Compatibilidad con el código nativo.
? ¿Qué requiere un cambio nativo?
* Una nueva build compatible
- Binarios
- JavaScript y recursos compatibles
! Una nueva build compatible.
