---
title: MCP: conectar herramientas
desc: Qué es el Model Context Protocol y qué cuidar al instalar servidores.
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
