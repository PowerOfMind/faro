---
title: Environment, CORS and variables
desc: Failures that are not in your code: CORS, env vars, ports, Windows paths, Node versions.
---
## CORS
The browser blocks the response; the server did receive it.
- It is fixed **on the server** (`Access-Control-Allow-Origin` headers, and answering `OPTIONS` for preflighted requests). Not from the client.
- In development, a bundler proxy (`server.proxy` in Vite) avoids CORS.
- `Access-Control-Allow-Origin: *` does not work with cookies (`credentials`).
- A "CORS error" is sometimes a 500 or 404 from the server without headers. Check the Network tab.

## Environment variables
- On the client only those the bundler exposes with a prefix exist (`VITE_`, `NEXT_PUBLIC_`). And they **are visible to anyone**: no secrets there.
- Many bundlers read them **at build time**, not at runtime: changing the value requires a rebuild.
- `.env` is not committed; a `.env.example` without values is.
- On the host you must define them in the dashboard; the local `.env` is not enough.

## Ports and processes
```bash
# Windows: who is using port 3000
netstat -ano | findstr :3000
# macOS / Linux
lsof -i :3000
```
- `localhost` vs `127.0.0.1` vs `::1`: some servers listen on only one. Inside Docker, listen on `0.0.0.0`.

## Windows
- Paths with `\` break scripts: use `path.join` and `/` in configuration.
- Line endings: `git config core.autocrlf` and a `.gitattributes` with `* text=auto`. If a `.sh` script fails with `\r`, it is CRLF.
- Long paths and synced folders (OneDrive) cause odd errors with `node_modules`.

## Node versions
```bash
node -v
echo "22" > .nvmrc      # and "engines" in package.json
```
"Works on my machine" is usually a different Node, an ignored lockfile or a variable not defined in CI.

## Caches
Service workers, the browser cache and CDNs show you old code. Unregister the SW and hard-reload before saying "it does not change".

=== esquema
# CORS
- Fixed on the server — Allow-Origin headers and answering OPTIONS.
- Dev proxy — avoids CORS without touching the server.
# Environment
- VITE_ / NEXT_PUBLIC_ variables — reach the browser and are public.
- Build-time variables — changing them requires a rebuild.
- Different Node — .nvmrc and engines.
=== test
? Where is a CORS error fixed?
- On the client with fetch
* On the server, with the right headers
- In the CSS
! The browser blocks the response based on the headers the server sends.
? Can a secret go in a VITE_API_KEY variable?
- Yes, if it is private
* No: it reaches the browser and is public
- Only in production
! Everything the bundler exposes is visible to anyone.
? On Windows a .sh script fails with \r. Probable cause?
* CRLF line endings
- Lack of RAM
- Node version
! Set .gitattributes with text=auto.
