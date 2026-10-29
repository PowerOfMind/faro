---
title: Autenticación, autorización y base de datos
desc: Quién eres no es lo mismo que qué puedes hacer; IDOR, RLS y sesiones.
---
## No lo escribas tú
Para login usa una solución probada (proveedor gestionado o librería madura: Auth.js, Better Auth, Clerk, Supabase Auth, Firebase Auth). Hashes con **Argon2id** o **bcrypt** si guardas contraseñas. Una IA puede generar un login que "funciona" con fallos sutiles (comparación no constante, tokens sin caducidad, sin límite de intentos).

## Autenticación ≠ autorización
- **Autenticación**: ¿quién eres?
- **Autorización**: ¿puedes hacer **esto** sobre **este recurso**?

El fallo clásico (IDOR): el servidor solo mira que haya sesión.
```ts
// mal
const pedido = await db.pedido.findById(req.params.id);
// bien: acota por dueño
const pedido = await db.pedido.findFirst({ where: { id, userId: session.userId } });
if (!pedido) return res.status(404).end();
```
Autoriza **en el servidor, en cada petición**. Esconder un botón no es control de acceso.

## Bases de datos expuestas al cliente
Con Supabase/Firebase el cliente habla directo con la BBDD, así que **las reglas son tu backend**.
- Supabase: activa **Row Level Security** en cada tabla y crea políticas (`auth.uid() = user_id`). Sin políticas, nadie accede; con RLS apagado, **cualquiera**.
- Firebase: reglas de Firestore/Storage nunca en `allow read, write: if true`.
- La `service_role` key salta RLS: solo en servidor.

## Sesiones y tokens
- Cookies `HttpOnly`, `Secure`, `SameSite`; caducidad razonable y rotación al login.
- JWT: verifica firma y `exp`, fija el algoritmo esperado; no guardes datos sensibles dentro.
- Limita intentos de login y de recuperación de contraseña.

## Pagos
Nunca confíes en el precio o el "pagado" que envía el cliente. Confirma por **webhook firmado** del proveedor y valida la firma.

> [!SEC] Prueba rápida
> Entra con el usuario A, copia una petición de la pestaña Network, repítela con el id de un recurso del usuario B. Si responde, tienes un IDOR.

=== esquema
# Conceptos
- Autenticación — quién eres.
- Autorización — qué puedes hacer sobre qué recurso.
- IDOR — acceso a recursos ajenos por cambiar un id.
# Datos
- RLS (Supabase) — políticas por fila; sin ellas, nadie o todos.
- Reglas de Firebase — nunca allow read, write: if true.
- service_role — salta RLS, solo en servidor.
=== test
? ¿Cómo evitas un IDOR?
- Ocultando el botón
* Acotando la consulta por dueño en el servidor
- Con un id más largo
! La autorización se comprueba en cada petición.
? Tabla de Supabase con RLS desactivado y clave pública en el cliente. ¿Riesgo?
* Cualquiera puede leer y escribir
- Ninguno
- Solo lectura
! Sin RLS el cliente tiene acceso total.
? ¿Cómo confirmas un pago?
- Con el "pagado" que envía el cliente
* Con un webhook firmado del proveedor
- Con una cookie
! El cliente puede mentir.
