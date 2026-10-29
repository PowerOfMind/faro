---
title: Entorno, CORS y variables
desc: Fallos que no están en tu código: CORS, env vars, puertos, rutas de Windows, versiones de Node.
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
