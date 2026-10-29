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

=== esquema
# Estándares
- Custom Elements — se registran con customElements.define('mi-tag', Clase). El nombre debe contener un guion.
- Shadow DOM — aporta encapsulación de DOM y de estilos.
- Template y slot — permiten plantillas inertes y proyectar hijos en huecos con <slot>.
# Ciclo nativo
- constructor — se llama al crear o mejorar (upgrade) el elemento.
- connectedCallback / disconnectedCallback — se llaman al entrar y salir del DOM.
- attributeChangedCallback — reacciona a cambios en los observedAttributes.
- adoptedCallback — se llama al mover el elemento a otro documento.
# Atributos y propiedades
- Atributo — es siempre un string; está en el HTML.
- Propiedad — es un valor JS de cualquier tipo.
- Upgrade — ocurre cuando la definición del elemento llega después de que ya esté en el DOM.
# Piezas
- lit — es el paquete que lo agrupa todo.
- lit-html — es el motor de plantillas con html``.
- LitElement — es la clase base para crear componentes Lit con reactividad y plantillas.
# Por qué Lit
- Componentes nativos — implican funcionan en cualquier framework o sin él.
- Design systems — se benefician de un componente escrito una vez que sirve a varios stacks.

=== test
? Completa la llamada nativa para registrar el elemento con un nombre válido:
```js
customElements.define('___', MiEtiqueta);
```
* mi-etiqueta
- mietiqueta
- MiEtiqueta
- mi_etiqueta
! Los nombres de custom elements deben contener obligatoriamente un guión para no colisionar con etiquetas nativas.

? Declara el getter estático para observar cambios en el atributo 'texto':
```js
class MiEtiqueta extends HTMLElement {
  static get ___() { return ['texto']; }
}
```
* observedAttributes
- watchedAttributes
- attributes
- observed
! observedAttributes es la única lista estática que el navegador consulta para disparar attributeChangedCallback.

? Adjunta el Shadow DOM accesible en this.shadowRoot:
```js
constructor() {
  super();
  this.attachShadow({ mode: '___' });
}
```
* open
- closed
- true
- isolated
! mode: 'open' permite leer y manipular element.shadowRoot desde JavaScript externo.

? Extiende de la clase base de Lit para crear un componente con Shadow DOM:
```js
class MiSaludo extends ___ {
  render() { return html`<p>Hola</p>`; }
}
```
* LitElement
- HTMLElement
- ReactiveElement
- Component
! LitElement combina ReactiveElement y lit-html aportando reactividad y renderizado eficiente.

? Declara la propiedad reactiva en JavaScript estándar sin decoradores:
```js
class MiSaludo extends LitElement {
  static ___ = {
    nombre: { type: String }
  };
}
```
* properties
- props
- state
- observedAttributes
! En JavaScript estándar sin decoradores, las propiedades reactivas se declaran en el campo estático properties.

? Genera el TemplateResult en render con la tagged template de Lit:
```js
render() {
  return ___`<p>Hola, <b>${this.nombre}</b></p>`;
}
```
* html
- css
- template
- vdom
! html marca la plantilla de Lit; sus huecos dinámicos se explican en el tema de plantillas.

=== prueba

## Un custom element nativo (sin Lit)
Fíjate en el orden de los logs: el elemento ya estaba en el HTML y se «mejora» (upgrade) al registrar la clase.
```html
<mi-saludo nombre="Juan"></mi-saludo>
<p><button onclick="document.querySelector('mi-saludo').setAttribute('nombre','Ana')">Cambiar atributo</button>
<button onclick="document.querySelector('mi-saludo').remove()">Quitar del DOM</button></p>
```
```js
class MiSaludo extends HTMLElement {
  static observedAttributes = ['nombre'];
  constructor() {
    super();
    console.log('constructor');
    this.attachShadow({mode: 'open'});
  }
  connectedCallback() { console.log('connectedCallback'); this.pintar(); }
  disconnectedCallback() { console.log('disconnectedCallback'); }
  attributeChangedCallback(nombre, antes, ahora) {
    console.log(`attributeChangedCallback: ${nombre}  ${antes} -> ${ahora}`);
    if (this.isConnected) this.pintar();
  }
  pintar() {
    this.shadowRoot.innerHTML =
      `<style>p{color:var(--primary);font-weight:700}</style><p>Hola, ${this.getAttribute('nombre')}</p>`;
  }
}
customElements.define('mi-saludo', MiSaludo);
```
Reto: quita `static observedAttributes` y comprueba que attributeChangedCallback deja de llamarse.
Clave: El nombre lleva guion; attributeChangedCallback solo salta para observedAttributes; un elemento ya presente se mejora (upgrade) al registrarse.

## Shadow DOM y slots: encapsulación
El CSS global pinta de rojo el párrafo de fuera; el del interior del shadow DOM no se ve afectado.
```html
<style>p{color:crimson}</style>
<p>Párrafo de fuera: le afecta el CSS global.</p>
<mi-caja><span slot="titulo">Título proyectado</span>Contenido por defecto</mi-caja>
```
```js
class MiCaja extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({mode: 'open'}).innerHTML = `
      <style>
        p { color: seagreen }                      /* solo dentro del shadow */
        h4 { margin: 0; border-bottom: 1px solid #888 }
      </style>
      <h4><slot name="titulo">Sin título</slot></h4>
      <p><slot></slot></p>`;
  }
}
customElements.define('mi-caja', MiCaja);
```
Reto: borra el span con slot="titulo" del HTML y mira aparecer el contenido fallback «Sin título».
Clave: Shadow DOM encapsula DOM y estilos; los <slot> proyectan los hijos sin moverlos de sitio.

## Tu primer componente Lit
Propiedad reactiva + plantilla + evento. Sin build: JavaScript estándar.
```html
<mi-contador></mi-contador>
```
```js
import {LitElement, html, css} from 'lit';

class MiContador extends LitElement {
  static properties = { cuenta: {type: Number} };
  static styles = css`button { padding: 8px 14px; font-size: 15px; }`;

  constructor() {
    super();
    this.cuenta = 0;
  }
  render() {
    return html`<button @click=${() => this.cuenta++}>
      Pulsado ${this.cuenta} veces
    </button>`;
  }
}
customElements.define('mi-contador', MiContador);
```
Reto: añade `?disabled=${this.cuenta >= 5}` al botón para bloquearlo al llegar a 5.
Clave: Cambia una propiedad reactiva → Lit programa un render asíncrono → solo se actualiza el hueco ${} afectado.
