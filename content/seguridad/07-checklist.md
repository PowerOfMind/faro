---
title: Checklist antes de publicar
desc: 20 comprobaciones de seguridad, privacidad y calidad para una app hecha con IA.
---
## Secretos y configuración
1. Ninguna clave en el cliente ni en el historial de git.
2. `.env` ignorado; `.env.example` sin valores.
3. Límites de gasto y alertas en el proveedor de IA y de nube.
4. Modo debug apagado; errores genéricos al usuario.

## Acceso y datos
5. Cada endpoint comprueba sesión **y** propiedad del recurso.
6. Reglas de BBDD (RLS/Firestore/Storage) activas y probadas con dos usuarios.
7. Entradas validadas en servidor con esquema (Zod, Valibot...).
8. Consultas parametrizadas.
9. Rate limit en login, registro, recuperación y endpoints que cuestan dinero.
10. Webhooks de pago con firma verificada.

## Navegador
11. HTTPS y HSTS.
12. CSP, `nosniff`, `Referrer-Policy`.
13. Cookies `HttpOnly; Secure; SameSite`.
14. Sin `innerHTML` con datos sin sanear.

## Dependencias
15. `npm audit` sin críticas; lockfile commiteado.
16. Cada dependencia nueva comprobada (existe, mantenida, no sospechosa).

## Legal y privacidad
17. Aviso legal, política de privacidad y cookies si procede (RGPD en la UE).
18. Consentimiento antes de cookies no esenciales.
19. Copias de seguridad y forma de borrar los datos de un usuario.

## Calidad
20. Prueba en móvil, teclado y lector de pantalla básico; Lighthouse sin errores graves.

> [!TIP] Automatiza lo que puedas
> Gitleaks en pre-commit, Dependabot, `npm audit` en CI, y un agente de auditoría previa al lanzamiento para recorrer esta lista contra el código real.

=== esquema
# Antes de publicar
- Secretos — ninguna clave en cliente ni en el historial.
- Acceso — sesión y propiedad del recurso en cada endpoint.
- Datos — RLS/reglas activas y probadas con dos usuarios.
- Límites — rate limit y gasto máximo.
- Navegador — HTTPS, HSTS, CSP, cookies seguras.
- Legal — privacidad y cookies si procede.
=== test
? Antes de publicar, ¿cómo pruebas el control de acceso?
* Con dos usuarios intentando acceder a recursos del otro
- Con un solo usuario admin
- Mirando el código por encima
! Es la forma más directa de detectar IDOR.
? ¿Qué pones en pagos y endpoints que cuestan dinero?
- Nada
* Rate limit y límites de gasto
- Más animaciones
! Evita abusos y facturas inesperadas.
? ¿Qué automatizas en CI?
* npm audit y escáner de secretos
- El diseño
- Los textos legales
! Detectan fallos recurrentes sin esfuerzo manual.
