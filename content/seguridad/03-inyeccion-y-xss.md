---
title: Inyección y XSS
desc: Inyección y XSS en aplicaciones web, con medidas para proteger consultas SQL, contenido HTML y comandos frente a entradas no fiables.
---
## SQL
```ts
// mal
db.query(`SELECT * FROM users WHERE email = '${email}'`);
// bien: parametrizada
db.query('SELECT * FROM users WHERE email = $1', [email]);
```
Los ORMs parametrizan, salvo en sus funciones "raw". Revísalas.

## XSS
Insertar texto del usuario como HTML permite ejecutar scripts en el navegador de otros.
- **Por defecto** React, Angular, Vue y Lit escapan lo que interpolas.
- El peligro está en: `innerHTML`, `dangerouslySetInnerHTML`, `v-html`, `[innerHTML]`, `unsafeHTML`, `href="javascript:..."`.
- Si necesitas HTML del usuario (editor, markdown), **sanitiza** con DOMPurify y una lista blanca de etiquetas.
- Valida las URLs: solo `https:` y `mailto:`.

## Comandos del sistema
Nunca concatenes entrada del usuario en `exec`. Usa `execFile` con argumentos en array y valida los valores.

## Cabeceras que importan
```text
Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'none'
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```
Empieza con la CSP en modo `Content-Security-Policy-Report-Only`, mira qué rompe y endurécela. Las comprobaciones gratuitas: securityheaders.com y el panel de seguridad de DevTools.

## Subidas de ficheros
Valida tipo por contenido (no solo extensión), limita tamaño, guarda fuera de la raíz pública y sirve con `Content-Disposition: attachment` si no es imagen.

## CSRF
Cookies de sesión + peticiones que cambian datos: usa `SameSite=Lax` o `Strict` y token CSRF si hay formularios entre sitios.

> [!AI] Frase de revisión
> "Lista todos los puntos donde un dato del usuario llega a SQL, HTML, URL, comando o fichero, y di cómo se sanea cada uno."

=== esquema
# Inyección
- Consultas parametrizadas — nunca concatenes entrada en SQL.
- execFile con array — nunca entrada del usuario en exec.
# XSS
- Escape por defecto — React, Angular, Vue y Lit escapan lo que interpolas.
- Zonas peligrosas — innerHTML, dangerouslySetInnerHTML, v-html, unsafeHTML.
- DOMPurify — si necesitas HTML del usuario.
- CSP — empieza en modo Report-Only.
=== test
? ¿Cómo evitas la inyección SQL?
* Consultas parametrizadas
- Quitando las comillas a mano
- Usando mayúsculas
! El motor separa código y datos.
? ¿Cuándo es peligroso renderizar texto del usuario?
- Con la interpolación normal
* Al insertarlo como HTML sin sanear
- Con textContent
! innerHTML y equivalentes ejecutan lo que reciben.
? ¿Para qué sirve una CSP?
* Limita qué scripts y recursos puede cargar la página
- Acelera la carga
- Cifra las cookies
! Reduce el daño si llega un XSS.
