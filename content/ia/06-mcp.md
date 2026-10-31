---
title: MCP: conectar herramientas
desc: MCP para conectar agentes con herramientas y datos externos, con instrucciones de instalación y criterios para evaluar coste y seguridad.
pkgs: "@modelcontextprotocol/sdk"
---
**MCP** (Model Context Protocol) es un estándar abierto para que un agente use herramientas y datos externos (GitHub, bases de datos, navegador, calendario) con una interfaz común. Un servidor MCP expone *herramientas*, *recursos* y *prompts*.

## Añadir uno (Claude Code)
```bash
claude mcp add nombre -- npx -y paquete-servidor
claude mcp list
```

## Cuándo compensa
- Acceso a un sistema que el agente no alcanza con ficheros y terminal.
- Mismo servidor reutilizable desde varias aplicaciones.

## Cuándo no
- Si hay una CLI fiable (`gh`, `psql`), el agente la usa con menos coste de contexto que un servidor con 30 herramientas.
- Cada herramienta descrita ocupa contexto. Activa solo las que usas.

> [!SEC] Un servidor MCP es código que ejecutas
> - Instala solo servidores de autores que conoces; revisa qué permisos pide.
> - Credenciales con el mínimo alcance (token de solo lectura si basta).
> - Los datos que devuelve una herramienta pueden contener instrucciones maliciosas: ver [prompt injection](@/seguridad/prompt-injection).
> - No dejes un servidor con acceso a producción en la sesión donde pruebas cosas.

## Crear el tuyo
SDK oficial en TypeScript y Python. Define cada herramienta con nombre claro, descripción de cuándo usarla y esquema de entrada validado.

=== esquema
# Qué es
- MCP — estándar abierto para conectar herramientas y datos a un agente.
- Servidor MCP — expone herramientas, recursos y prompts.
# Cuidado
- Es código que ejecutas — instala solo de autores que conoces.
- Credenciales mínimas — token de solo lectura si basta.
- Cada herramienta ocupa contexto — activa solo las que usas.
=== test
? ¿Qué es un servidor MCP?
* Un programa que expone herramientas y datos a un agente por un protocolo común
- Un tipo de base de datos
- Un modelo de IA nuevo
! Es la interfaz estándar entre el agente y los sistemas externos.
? ¿Por qué ser prudente al instalar uno?
- Porque son lentos
* Porque ejecuta código con los permisos que le des
- Porque caducan cada semana
! Trátalo como cualquier dependencia con acceso a tus datos.
? Si existe una CLI fiable (gh, psql), ¿qué suele convenir?
* Usarla: ocupa menos contexto que un servidor con muchas herramientas
- Instalar siempre el servidor
- Escribir tu propio protocolo
! Cada herramienta descrita consume contexto.
