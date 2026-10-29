---
title: Secretos y claves de API
desc: Dónde nunca pueden estar y qué hacer si se filtran.
---
## Regla
Todo lo que llega al navegador es público: JS, HTML, variables `VITE_*` / `NEXT_PUBLIC_*`, mapas de fuentes. **Una clave en el cliente es una clave publicada.**

## Dónde van
| Tipo | Dónde |
|---|---|
| Clave de servidor (modelo de IA, Stripe secret, DB) | Variables de entorno **en el servidor** o gestor de secretos |
| Clave "pública" (Stripe publishable, Maps con restricción de dominio) | Cliente, pero **restringida** por dominio/API |
| Token de usuario | Cookie `HttpOnly; Secure; SameSite` mejor que `localStorage` |

Si el navegador necesita usar un modelo de IA o una API de pago, crea **un endpoint propio** que haga la llamada con la clave, autentique al usuario y limite el uso.

## Evitar el accidente
```bash
echo ".env*" >> .gitignore && echo "!.env.example" >> .gitignore
```
- Un hook `pre-commit` con un escáner (gitleaks, trufflehog) bloquea claves antes del commit.
- Activa el escaneo de secretos del proveedor (GitHub secret scanning y push protection).
- No pegues claves en el chat con la IA; usa valores falsos.
- Agentes: que **no puedan leer** `.env` (reglas de permisos del agente).

## Si se filtró
1. **Revoca y rota** la clave ya. Es lo único que importa en la primera hora.
2. Revisa el uso/facturación del proveedor por actividad extraña.
3. Limpia el historial (`git filter-repo`) solo después, y asume que sigue comprometida.
4. Añade límites de gasto y alertas.

> [!WARN] Bots
> Hay bots que rastrean repos públicos y claves en minutos. Un repositorio "privado un ratito" no es seguro.

=== esquema
# Regla
- Todo lo que llega al navegador es público — incluidas VITE_* y NEXT_PUBLIC_*.
- Clave de servidor — solo en el servidor.
# Si se filtró
- Revocar y rotar — primero, ya.
- Revisar el uso del proveedor — actividad extraña.
- Límites de gasto — y alertas.
=== test
? Tu navegador necesita llamar a un modelo de IA de pago. ¿Cómo lo haces?
- Pones la clave en una variable VITE_
* Creas un endpoint propio que usa la clave, autentica y limita el uso
- La ofuscas en el JS
! La clave solo puede vivir en el servidor.
? Subiste una clave a un repo público. ¿Qué haces primero?
* Revocarla y crear otra
- Borrar el commit
- Hacer el repo privado
! Los bots la copian en minutos; el historial es secundario.
? ¿Qué evita el accidente antes del commit?
- Un linter de CSS
* Un escáner de secretos (gitleaks) en pre-commit
- Reiniciar el equipo
! Bloquea claves antes de que salgan de tu máquina.
