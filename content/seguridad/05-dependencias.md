---
title: Dependencias y slopsquatting
desc: Paquetes inventados por la IA, cadena de suministro y cómo reducir superficie.
---
## Slopsquatting
Los modelos a veces **recomiendan paquetes que no existen**. Un atacante registra ese nombre con código malicioso; quien copia el `npm install` sin mirar lo instala. También pasa con typosquatting (`reqeusts`).

## Antes de instalar
```bash
npm view <paquete>            # ¿existe? ¿quién lo mantiene? ¿cuándo se publicó?
npm view <paquete> time.created repository.url dist.unpackedSize
```
Señales de alarma: creado hace días, pocas descargas, sin repositorio, nombre casi igual a uno famoso, scripts `postinstall` que descargan cosas.

## Reducir riesgo
- **Menos dependencias**: si son 10 líneas, escríbelas.
- Commitea el lockfile; `npm ci` en CI.
- `npm audit` (o `osv-scanner`) y Dependabot/Renovate con revisión.
- `npm install --ignore-scripts` para paquetes nuevos y revisa qué scripts tienen.
- Fija versiones críticas; evita `latest` y rangos amplios en producción.
- Para CDN: usa `integrity` (SRI) y versión exacta.
- Activa 2FA en tu cuenta de npm/GitHub; publica con *provenance*.

## Agentes y herramientas
Los agentes también instalan paquetes y ejecutan scripts. Configura que **pidan confirmación** para `npm install`, `curl | sh` y cualquier comando destructivo.

> [!AI] Pregunta útil
> "¿Hay una forma sin dependencia nueva? Si no, dame 3 candidatas con enlace al repositorio y fecha de último release." Y compruébalas tú.
