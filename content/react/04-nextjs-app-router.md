---
title: Next.js App Router
desc: Guía práctica de next.js app router, errores frecuentes, decisiones y comprobaciones para resolver problemas con criterio.
pkgs: next, react, react-dom
---
## Servidor y cliente
En App Router, páginas y layouts son Server Components por defecto. Usa `"use client"` para estado, eventos o APIs del navegador; no expongas secretos mediante props enviadas al cliente.

## Rutas y estados
`app/page.tsx` define una página; carpetas y segmentos `[id]` definen rutas. `layout.tsx` comparte interfaz, `loading.tsx` muestra espera y `error.tsx` gestiona errores del segmento como Client Component.

## Datos e hidratación
Obtén datos en un Server Component asíncrono y comprueba los errores. La caché y sus valores predeterminados dependen de la versión y configuración: consulta la documentación de tu versión. Para evitar errores de hidratación, el primer render cliente debe coincidir con el HTML del servidor; evita fechas aleatorias o `window` en ese render.

## Decisiones rápidas
| Pregunta | Respuesta |
|---|---|
| ¿Qué son las páginas por defecto? | Server Components |
| ¿Dónde van eventos y estado? | En un Client Component |
| ¿Qué archivo muestra espera? | loading.tsx |

> [!AI] Con IA
> Indica la versión, el entorno, el resultado esperado y real, y una reproducción mínima. Pide una explicación comprobable y referencias a la documentación oficial.

Documentación: [guía oficial](https://nextjs.org/docs/app/getting-started/server-and-client-components).

Relacionado: [continúa con otra guía](@/react/hooks-propios-y-rendimiento).

=== esquema
# Ideas clave
- Servidor y cliente — En App Router, páginas y layouts son Server Components por defecto.
- Rutas y estados — `app/page.tsx` define una página; carpetas y segmentos `[id]` definen rutas.
- Datos e hidratación — Obtén datos en un Server Component asíncrono y comprueba los errores.
=== test
? ¿Qué son las páginas por defecto?
* Server Components
- En un Client Component
- loading.tsx
! Server Components.
? ¿Dónde van eventos y estado?
* En un Client Component
- loading.tsx
- Un segmento dinámico
! En un Client Component.
? ¿Qué archivo muestra espera?
* loading.tsx
- Un segmento dinámico
- HTML inicial distinto entre servidor y cliente
! loading.tsx.
? ¿Qué define [id]?
* Un segmento dinámico
- HTML inicial distinto entre servidor y cliente
- Server Components
! Un segmento dinámico.
? ¿Qué causa una hidratación incorrecta?
* HTML inicial distinto entre servidor y cliente
- Server Components
- En un Client Component
! HTML inicial distinto entre servidor y cliente.
