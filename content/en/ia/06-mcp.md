---
title: MCP: connecting tools
desc: MCP connects AI agents to tools and data through a shared protocol. Learn about servers, setup, useful cases and security trade-offs.
pkgs: "@modelcontextprotocol/sdk"
---
**MCP** (Model Context Protocol) is an open standard that lets an agent use external tools and data (GitHub, databases, browser, calendar) through a common interface. An MCP server exposes *tools*, *resources* and *prompts*.

## Add one (Claude Code)
```bash
claude mcp add name -- npx -y server-package
claude mcp list
```

## When it pays off
- Access to a system the agent cannot reach with files and a terminal.
- The same server reusable from several applications.

## When it does not
- If there is a reliable CLI (`gh`, `psql`), the agent uses it with less context cost than a server with 30 tools.
- Every described tool takes up context. Enable only the ones you use.

> [!SEC] An MCP server is code you run
> - Install only servers from authors you know; check which permissions it asks for.
> - Minimum-scope credentials (a read-only token if that is enough).
> - The data a tool returns can contain malicious instructions: see [prompt injection](@/seguridad/prompt-injection).
> - Do not leave a server with production access in the session where you experiment.

## Build your own
Official SDKs in TypeScript and Python. Define each tool with a clear name, a description of when to use it and a validated input schema.

=== esquema
# What it is
- MCP — an open standard to connect tools and data to an agent.
- MCP server — exposes tools, resources and prompts.
# Care
- It is code you run — install only from authors you know.
- Minimal credentials — a read-only token if that is enough.
- Every tool takes context — enable only the ones you use.
=== test
? What is an MCP server?
* A program that exposes tools and data to an agent through a common protocol
- A type of database
- A new AI model
! It is the standard interface between the agent and external systems.
? Why be careful when installing one?
- Because they are slow
* Because it runs code with the permissions you give it
- Because they expire weekly
! Treat it like any dependency with access to your data.
? If a reliable CLI exists (gh, psql), what usually makes sense?
* Use it: it takes less context than a server with many tools
- Always install the server
- Write your own protocol
! Every described tool consumes context.
