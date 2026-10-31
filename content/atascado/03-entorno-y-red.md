---
title: Entorno, CORS y variables
desc: CORS y entorno de desarrollo para diagnosticar errores de red, variables, puertos y rutas, con comprobaciones útiles para el navegador y servidor.
---
## CORS
El navegador bloquea la respuesta; el servidor sí la recibió.
- Se arregla **en el servidor** (cabeceras `Access-Control-Allow-Origin`, y respuesta a `OPTIONS` en peticiones con preflight). No desde el cliente.
- En desarrollo, un proxy del bundler (`server.proxy` en Vite) evita CORS.
- `Access-Control-Allow-Origin: *` no vale con cookies (`credentials`).
- Un "error CORS" a veces es un 500 o un 404 del servidor sin cabeceras. Mira Network.

## Variables de entorno
- En el cliente solo existen las que el bundler expone con prefijo (`VITE_`, `NEXT_PUBLIC_`). Y **quedan visibles para cualquiera**: ahí no van secretos.
- Se leen **en build**, no en ejecución, en muchos bundlers: cambiar el valor exige reconstruir.
- `.env` no se sube a git; sí un `.env.example` sin valores.
- En el hosting hay que definirlas en el panel, no basta con el `.env` local.

## Puertos y procesos
```bash
# Windows: quién usa el puerto 3000
netstat -ano | findstr :3000
# macOS / Linux
lsof -i :3000
```
- `localhost` vs `127.0.0.1` vs `::1`: algunos servidores solo escuchan en uno. Dentro de Docker, escucha en `0.0.0.0`.

## Windows
- Rutas con `\` rompen scripts: usa `path.join` y `/` en configuraciones.
- Fin de línea: `git config core.autocrlf` y un `.gitattributes` con `* text=auto`. Si un script `.sh` falla con `\r`, es CRLF.
- Rutas largas y carpetas sincronizadas (OneDrive) dan errores raros con `node_modules`.

## Versiones de Node
```bash
node -v
echo "22" > .nvmrc      # y "engines" en package.json
```
"Funciona en mi máquina" suele ser Node distinto, lockfile ignorado o variable no definida en CI.

## Cachés
Service worker, caché del navegador y CDN te muestran código viejo. Desregistra el SW y haz recarga forzada antes de decir "no cambia".

=== esquema
# CORS
- Se arregla en el servidor — cabeceras Allow-Origin y respuesta a OPTIONS.
- Proxy en desarrollo — evita CORS sin tocar el servidor.
# Entorno
- Variables VITE_ / NEXT_PUBLIC_ — llegan al navegador y son públicas.
- Variables en build — cambiarlas exige reconstruir.
- Node distinto — .nvmrc y engines.
=== test
? ¿Dónde se arregla un error de CORS?
- En el cliente con fetch
* En el servidor, con las cabeceras adecuadas
- En el CSS
! El navegador bloquea la respuesta según las cabeceras que envía el servidor.
? ¿Puede ir un secreto en una variable VITE_API_KEY?
- Sí, si es privado
* No: llega al navegador y es pública
- Solo en producción
! Todo lo que expone el bundler es visible para cualquiera.
? En Windows falla un script .sh con \r. ¿Causa probable?
* Finales de línea CRLF
- Falta de RAM
- Versión de Node
! Configura .gitattributes con text=auto.
