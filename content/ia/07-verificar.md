---
title: Verificar lo que dice la IA
desc: Alucinaciones típicas en código y comprobaciones rápidas.
---
## Lo que más se inventa
| Qué | Cómo se nota |
|---|---|
| Funciones o parámetros que no existen | "is not a function", opción ignorada sin error |
| API de otra versión | Funciona en el ejemplo, falla en tu proyecto |
| Paquetes inexistentes | `npm install` falla... o instala uno **malicioso** con ese nombre (ver [slopsquatting](@/seguridad/dependencias)) |
| Flags de CLI | `unknown option` |
| Datos con apariencia exacta | Versiones, fechas, límites, precios |

## Comprobación en 60 segundos
1. **Busca el símbolo en la doc oficial** de la versión que usas.
2. `npm view <paquete> version time.modified` (¿existe? ¿se mantiene?).
3. **Ejecútalo**: un test mínimo vale más que releer el código.
4. Pregunta a la IA: "¿en qué versión se añadió esto y dónde está documentado?" Si duda, desconfía.
5. Abre el changelog si la API cambió hace poco.

## Si no te convence
- Pega la **documentación real** en el chat y pide que se ciña a ella.
- Pide que cite el fragmento de doc en el que se apoya.
- Cambia de modelo o usa búsqueda web.

> [!WARN] Confianza
> Una respuesta segura y fluida no es una respuesta correcta. El tono no mide la fiabilidad.

=== esquema
# Se inventa
- APIs y parámetros — funciones que no existen.
- Versiones — API de otra versión de la librería.
- Paquetes — nombres inexistentes (o maliciosos).
# Comprobar
- Doc oficial — busca el símbolo en tu versión.
- npm view — ¿existe y se mantiene?
- Ejecutarlo — un test mínimo vale más que releer.
=== test
? Una respuesta segura y fluida, ¿es fiable por eso?
- Sí, el tono lo indica
* No: el tono no mide la corrección
- Solo si es larga
! Los modelos suenan seguros incluso cuando inventan.
? ¿Cuál es la comprobación más rápida de una función desconocida?
* Buscarla en la documentación de tu versión
- Preguntar de nuevo al mismo modelo
- Copiarla y esperar
! La doc oficial de tu versión es la fuente de verdad.
? Antes de instalar un paquete sugerido por la IA…
- Instalarlo y mirar si falla
* Comprobar con npm view que existe, quién lo mantiene y cuándo se publicó
- Fiarte del nombre
! Puede ser inexistente o un paquete malicioso con ese nombre.
