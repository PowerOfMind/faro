---
title: SSR, testing e integración con frameworks
desc: Probar Lit, renderizar en servidor, usarlo en React y migrar de Lit 1/2.
pkgs: lit, "@lit/react", "@lit-labs/ssr", "@web/test-runner"
---
## Testing
En navegador real: Web Test Runner (+ `@open-wc/testing`, `fixture`) o Playwright. Siempre `await el.updateComplete` antes de las aserciones.
```ts
const el = await fixture<MyEl>(html`<my-el name="Ana"></my-el>`);
expect(el.shadowRoot!.textContent).to.contain('Ana');
```

## SSR (`@lit-labs/ssr`, experimental)
Genera HTML con **Declarative Shadow DOM** y se hidrata en cliente (`@lit-labs/ssr-client`). Solo corren `willUpdate` y `render`. Integraciones: Eleventy, Astro, Next (pages), Nuxt.

## En React
```tsx
import {createComponent} from '@lit/react';
export const MyEl = createComponent({tagName: 'my-el', elementClass: MyElement, react: React, events: {onSelect: 'item-selected'}});
```
React 19 ya pasa propiedades y eventos a custom elements; en React < 19 todo llegaba como atributo string, por eso existe el wrapper.

## En Angular
Añade `CUSTOM_ELEMENTS_SCHEMA` y enlaza propiedades con `[prop]` y eventos con `(evento)`.

## Otros
- **Localización**: `@lit/localize`.
- **Publicar**: ES modules; `lit` como dependencia, no empaquetado dentro.
- `lit-analyzer` / plugin de IDE detecta errores de plantilla.

## Lit 1/2 → 3
- `lit-element` + `lit-html` → paquete único `lit`. `UpdatingElement` → `ReactiveElement`.
- Decoradores en `lit/decorators.js`; Lit 3 admite los estándar (`accessor`).
- Lit 3: ES2021, sin IE11. Libs pueden declarar `"^2.7.0 || ^3.0.0"`.
