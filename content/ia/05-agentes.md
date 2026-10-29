---
title: Crear agentes
desc: Qué es un agente, el bucle básico y cómo no perder el control.
pkgs: "@anthropic-ai/sdk", "@modelcontextprotocol/sdk"
---
## Qué es
Un agente es un **modelo en bucle con herramientas**: decide, llama a una herramienta, lee el resultado y vuelve a decidir hasta terminar.

```text
objetivo → el modelo elige acción → herramienta (leer, buscar, ejecutar) → resultado → ¿terminado? → no: repetir
```

## Esqueleto (TypeScript)
```ts
import Anthropic from '@anthropic-ai/sdk';
const client = new Anthropic();           // lee ANTHROPIC_API_KEY del entorno
const messages = [{role: 'user', content: 'Resume los TODO de src/'}];

for (let paso = 0; paso < 10; paso++) {    // tope de pasos
  const r = await client.messages.create({
    model: MODELO, max_tokens: 1024, tools, messages,
  });
  messages.push({role: 'assistant', content: r.content});
  if (r.stop_reason !== 'tool_use') break;
  const resultados = await ejecutarHerramientas(r.content);   // tu código, con validación
  messages.push({role: 'user', content: resultados});
}
```

## Cómo no perder el control
- **Tope de pasos y de gasto** siempre.
- **Mínimo privilegio**: herramientas de solo lectura por defecto; escritura y red con confirmación.
- **Valida los argumentos** de cada herramienta como si vinieran de un usuario hostil (pueden venir de una inyección; ver [prompt injection](@/seguridad/prompt-injection)).
- **Registra** cada llamada para poder reproducir fallos.
- **Evalúa**: 10 casos reales con resultado esperado, repetidos tras cada cambio.

## Cuándo NO usar un agente
Si los pasos son fijos, un script o un flujo con una sola llamada al modelo es más barato, rápido y predecible. Usa agente cuando el camino depende de lo que se vaya encontrando.

> [!TIP] Subagentes
> Para investigar o leer mucho, lanza un subagente: gasta su propio contexto y devuelve solo el resumen.

=== esquema
# Concepto
- Agente — un modelo en bucle con herramientas.
- Bucle — decide, usa una herramienta, lee el resultado, repite.
# Control
- Tope de pasos y gasto — siempre.
- Mínimo privilegio — herramientas de lectura por defecto.
- Validar argumentos — como si vinieran de un usuario hostil.
- Evaluar — casos reales repetidos tras cada cambio.
=== test
? ¿Cuándo NO usar un agente?
- Cuando el camino depende de lo que encuentres
* Cuando los pasos son fijos y conocidos
- Nunca; siempre conviene
! Un script o una sola llamada al modelo es más barato y predecible si el flujo es fijo.
? ¿Qué limitas siempre en un agente?
* El número de pasos y el gasto
- Solo el color de la UI
- Nada, para que sea libre
! Un bucle sin tope puede gastar sin control.
? ¿Cómo tratas los argumentos que el modelo pasa a una herramienta?
- Como datos de confianza
* Como entrada no fiable que hay que validar
- No hace falta mirarlos
! Pueden venir de una inyección de prompt.
