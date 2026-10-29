---
title: Web Components y qué añade Lit
desc: Los 4 estándares del navegador y la capa fina de Lit encima.
pkgs: lit
---
## Los 4 estándares
- **Custom Elements**: `customElements.define('mi-tag', Clase)`. El nombre **debe llevar guion**.
- **Shadow DOM**: DOM y CSS encapsulados.
- **`<template>` y `<slot>`**: plantillas inertes y proyección de contenido.
- **ES Modules**: cómo se distribuyen.

Callbacks nativos: `constructor`, `connectedCallback`, `disconnectedCallback`, `attributeChangedCallback` (solo para `observedAttributes`), `adoptedCallback`.

> [!NOTE] Atributo vs propiedad
> El atributo es siempre string y vive en el HTML. La propiedad es JS y puede ser de cualquier tipo. Lit sincroniza ambos.

## Qué es Lit
Librería de ~5 KB (min+gzip) de Google. `lit` lo trae todo; `lit-html` es el motor de plantillas; `LitElement` es la clase base (extiende `ReactiveElement`).

- **Sin virtual DOM**: parsea la plantilla una vez y en cada render solo actualiza los huecos `${}`.
- Los componentes son **nativos**: funcionan en React, Angular, Vue o sin framework.
- No exige build; los decoradores son opcionales.

## Componente mínimo
```ts
import {LitElement, html, css} from 'lit';
import {customElement, property} from 'lit/decorators.js';

@customElement('simple-greeting')
export class SimpleGreeting extends LitElement {
  static styles = css`p { color: blue; }`;
  @property() name = 'Somebody';
  render() { return html`<p>Hello, ${this.name}!</p>`; }
}
```

Sin decoradores (JS puro):
```js
class SimpleGreeting extends LitElement {
  static properties = { name: {} };
  constructor() { super(); this.name = 'Somebody'; }
  render() { return html`<p>Hello, ${this.name}!</p>`; }
}
customElements.define('simple-greeting', SimpleGreeting);
```

## Frente a React
React vuelve a ejecutar el componente y compara un VDOM. Lit toca solo los bindings. Un elemento Lit expone la API estándar del DOM (propiedades, atributos, eventos), por eso se integra en cualquier sitio.

> [!AI] Dónde suele fallar la IA
> Mezcla sintaxis de Lit 1/2 (`lit-element`, `UpdatingElement`) con Lit 3, o genera componentes React con nombres de evento de React (`onClick`) en un elemento Lit. Pide siempre "Lit 3, paquete `lit`".
