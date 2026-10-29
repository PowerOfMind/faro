---
title: Riesgos del código generado con IA
desc: Qué falla de forma recurrente y cómo revisarlo antes de publicar.
---
El código generado **compila y parece correcto**. Eso es justo el riesgo: la IA optimiza que funcione en el ejemplo feliz, no que resista a un atacante.

## Fallos que se repiten
| Fallo | Ejemplo |
|---|---|
| Secretos en el cliente o en el repo | Clave de API en el JS del navegador, `.env` subido |
| Validación solo en el front | El botón está deshabilitado, pero el endpoint acepta cualquier cosa |
| Autorización ausente (IDOR) | `GET /api/pedidos/123` devuelve el pedido de otro usuario |
| Base de datos abierta | Reglas de Firebase/Supabase en modo prueba, RLS desactivado |
| Inyección | SQL concatenado, `innerHTML` con texto del usuario |
| Dependencias dudosas | Paquete inventado o abandonado |
| Mensajes de error con detalles internos | Stack traces al usuario |
| Sin límite de uso | Endpoint que llama al modelo sin rate limit: factura infinita |

## Revisión mínima (15 minutos)
1. **Busca secretos**: `git grep -nEi "api[_-]?key|secret|token|password"` y revisa el historial.
2. **Para cada endpoint**: ¿quién puede llamarlo? ¿Comprueba que el recurso es *suyo*? ¿Valida el cuerpo?
3. **Para cada consulta**: ¿parametrizada?
4. **Para cada `innerHTML`/`dangerouslySetInnerHTML`/`unsafeHTML`**: ¿de dónde viene el dato?
5. **Reglas de la BBDD** en producción, no en modo prueba.
6. `npm audit` y revisa las dependencias nuevas.
7. **Prueba como atacante**: abre otra sesión con otro usuario y pide los recursos del primero.

> [!AI] Pídeselo a la IA, pero no la tomes como única barrera
> "Revisa este endpoint como un pentester: lista accesos no autorizados posibles." Útil como segunda opinión. No sustituye pruebas reales ni una revisión humana de auth y pagos.

> [!SEC] Marco de referencia
> **OWASP Top 10** (aplicaciones web) y **OWASP Top 10 para LLM** (si tu app llama a modelos) son las listas a recorrer. Siguiente: [secretos](@/seguridad/secretos), [auth y datos](@/seguridad/auth-y-datos), [checklist](@/seguridad/checklist).
