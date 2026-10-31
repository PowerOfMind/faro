---
title: Expo Router y navegación
desc: Guía práctica de expo router y navegación, errores frecuentes, decisiones y comprobaciones para resolver problemas con criterio.
pkgs: expo, expo-router, react-native
---
## Rutas por archivos
En `app/` o `src/app/`, `index.tsx` es el índice y `[id].tsx` define un segmento dinámico. Un grupo entre paréntesis organiza rutas sin añadir su nombre a la URL.

## Layouts y navegación
`_layout.tsx` configura un navegador compartido: `Stack` para pantallas apiladas o `Tabs` para pestañas. Usa `Link` para navegar y `useLocalSearchParams` para leer parámetros locales.

## Enlaces profundos
Configura un esquema de URL en la configuración de Expo y prueba el enlace en dispositivo y en la build adecuada. Los enlaces universales de iOS y App Links de Android requieren además configuración de dominio y plataforma.

## Decisiones rápidas
| Pregunta | Respuesta |
|---|---|
| ¿Qué archivo define el layout? | _layout.tsx |
| ¿Qué indica [id]? | Un segmento dinámico |
| ¿Qué hook lee parámetros locales? | useLocalSearchParams |

> [!AI] Con IA
> Indica la versión, el entorno, el resultado esperado y real, y una reproducción mínima. Pide una explicación comprobable y referencias a la documentación oficial.

Documentación: [guía oficial](https://docs.expo.dev/router/introduction/).

Relacionado: [continúa con otra guía](@/react-native/expo-eas-y-publicar).

=== esquema
# Ideas clave
- Rutas por archivos — En `app/` o `src/app/`, `index.tsx` es el índice y `[id].tsx` define un segmento dinámico.
- Layouts y navegación — `_layout.tsx` configura un navegador compartido: `Stack` para pantallas apiladas o `Tabs` para pestañas.
- Enlaces profundos — Configura un esquema de URL en la configuración de Expo y prueba el enlace en dispositivo y en la build adecuada.
=== test
? ¿Qué archivo define el layout?
* _layout.tsx
- Un segmento dinámico
- useLocalSearchParams
! _layout.tsx.
? ¿Qué indica [id]?
* Un segmento dinámico
- useLocalSearchParams
- Tabs
! Un segmento dinámico.
? ¿Qué hook lee parámetros locales?
* useLocalSearchParams
- Tabs
- Configuración de dominio y plataforma
! useLocalSearchParams.
? ¿Qué navegador presenta pestañas?
* Tabs
- Configuración de dominio y plataforma
- _layout.tsx
! Tabs.
? ¿Qué requiere un enlace universal?
* Configuración de dominio y plataforma
- _layout.tsx
- Un segmento dinámico
! Configuración de dominio y plataforma.
