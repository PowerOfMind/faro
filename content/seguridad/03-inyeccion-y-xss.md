---
title: Inyección y XSS
desc: SQL, HTML, comandos y cabeceras que cierran la puerta.
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
