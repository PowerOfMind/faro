---
title: Git y despliegue
desc: Conflictos, commits mal hechos, 404 en producción y builds que fallan solo en CI.
---
## Git: situaciones frecuentes
| Quiero | Comando |
|---|---|
| Deshacer el último commit conservando cambios | `git reset --soft HEAD~1` |
| Descartar cambios de un fichero | `git restore fichero` |
| Guardar cambios a medias | `git stash -u` / `git stash pop` |
| Ver qué commit rompió algo | `git bisect start` |
| Recuperar algo "perdido" | `git reflog` |
| Quitar del repo un fichero ya subido sin borrarlo | `git rm --cached fichero` |

- **Secreto subido por error**: revócalo **primero** (cambiar la clave); reescribir el historial es secundario.
- No uses `push --force` en ramas compartidas; `--force-with-lease` si es imprescindible.
- Conflictos: lee ambos lados, no aceptes "todo lo mío" sin mirar.

## Funciona en local, falla en producción
1. **404 en rutas**: SPA sin *fallback* a `index.html`, o carpeta ignorada por `.gitignore` (un patrón mayúsculas/minúsculas en Windows puede ocultar carpetas).
2. **Rutas relativas vs base**: GitHub Pages sirve bajo `/repo/`; configura `base` del bundler.
3. **Mayúsculas**: Windows/macOS no distinguen; Linux (CI, hosting) sí. `Logo.png` ≠ `logo.png`.
4. **Variables de entorno** no definidas en el hosting.
5. **Build en CI**: Node distinto, `npm ci` con lock desactualizado, advertencias tratadas como errores.
6. **Caché del CDN**: purga o cambia el nombre del fichero (hash).

## Antes de empujar
```bash
git status && git diff --stat
npm run build && npm test
```
Mensajes de commit con el *por qué*; commits pequeños son más fáciles de revertir.

> [!NOTE] Ficheros generados
> Si el repo contiene salida de build, decide si se versiona. Si no, `.gitignore` y que lo genere el CI.

=== esquema
# Git
- reset --soft HEAD~1 — deshace el commit y conserva cambios.
- stash -u — guarda cambios a medias.
- reflog — recupera lo "perdido".
- Secreto subido — revócalo primero.
# Producción
- Mayúsculas — Linux distingue Logo.png de logo.png.
- Base path — GitHub Pages sirve bajo /repo/.
- Variables — definidas en el hosting, no solo en .env local.
=== test
? Subiste una clave a git por error. ¿Qué haces primero?
- Reescribir el historial
* Revocar y rotar la clave
- Borrar el repo
! Si se filtró, ya es pública; limpiar el historial es secundario.
? Funciona en tu Windows y da 404 de una imagen en producción. ¿Sospecha?
* Diferencia de mayúsculas/minúsculas en el nombre del fichero
- Falta de RAM
- El tema oscuro
! Linux distingue mayúsculas; Windows no.
? ¿Cómo deshaces el último commit sin perder los cambios?
- git reset --hard HEAD~1
* git reset --soft HEAD~1
- git revert --hard
! --soft deja los cambios preparados.
