---
title: Reactive properties
desc: "@property, @state, when it re-renders and the class fields trap."
pkgs: lit
---
## Public or internal
- `@property()` / `static properties`: the component's input API.
- `@state()`: internal state, no attribute, private.

`@property` options: `attribute` (name or `false`), `type`, `converter`, `reflect`, `hasChanged` (default `!==`), `noAccessor`, `state`.

## Flow
setter → `requestUpdate()` → compare with `hasChanged` → if changed, **batched async update (microtask)** → `update()` → `render()`.

## Mutating does not trigger a render
Same reference, same value, no render.
```ts
// bad: this.items.push(x)
this.items = [...this.items, x];          // preferred (immutable)
// or, if you mutate:
this.items.push(x); this.requestUpdate();
```

## The class fields trap
A JS class field shadows the prototype accessor and stops being reactive.

| Environment | Fix |
|---|---|
| TypeScript with experimental decorators | `"useDefineForClassFields": false` |
| Without that option | `declare name: string;` |
| Standard decorators (TS 5.2+) | the `accessor` keyword |

```ts
@property() accessor name = 'x';   // standard decorators
```

## Attributes
- Default name = the property in lowercase (`fooBar` → `foobar`).
- Booleans: start at `false` so they can be set in markup.
- `reflect: true` only if you need it in CSS (`:host([active])`). Never with objects or arrays.
- Derived values: `willUpdate`, not a hand-written setter.

> [!WARN] Classic symptom
> "I change the data and the UI does not update": almost always in-place mutation or a class field shadowing the accessor.

=== esquema
# Declaration
- @property — declares an input visible from outside, like the name typed into a tag.
- @state — declares internal data, like whether a menu is open; it creates no HTML attribute.
- static properties — the equivalent of decorators without a compiler.
# Options
- attribute — sets the attribute name, or false for none.
- type and converter — convert the HTML text into a JS value, like "3" to 3.
- reflect — copies the property back to the attribute.
- hasChanged — decides whether there is a change; by default compares with !==.
# Updating
- Setter — calls requestUpdate().
- Multiple changes — give a single render per microtask.
- Mutating arrays — needs a new list or requestUpdate(): changing a page of the notebook without changing the notebook is not detected.
# Traps
- Class fields — shadow prototype accessors and remove reactivity.
- Booleans — must start at false so they can be set from markup.
- Reflecting objects — avoid it; it only makes sense with simple types.
=== test
? Declare _abierto as internal state that triggers render but creates NO HTML attribute:
```js
static properties = {
  _abierto: { ___: true }
};
```
* state
- internal
- private
- noAttribute
! state: true defines a private reactive property that syncs with no HTML attribute.
? Make the attribute in the DOM update when the property changes in JS (<mi-tag activo>):
```js
static properties = {
  activo: { type: Boolean, ___: true }
};
```
* reflect
- sync
- attribute
- mirror
! reflect: true writes property changes back to the HTML attribute.
? Say that items is a complex Array and must not be read from an HTML attribute:
```js
static properties = {
  items: { ___: false }
};
```
* attribute
- reflect
- type
- converter
! attribute: false turns off reading from HTML attributes, ideal for objects and complex arrays.
? Add an element to the list guaranteeing a new reference so Lit detects the change:
```js
añadir(nuevo) {
  this.items = ___
}
```
* [...this.items, nuevo];
- this.items.push(nuevo);
- this.items.concat();
- Object.assign(this.items, nuevo);
! Lit uses a !== check. Mutating with .push() keeps the same memory reference and does not trigger the render.
? Configure a custom hasChanged that only triggers a render when the value is greater than zero:
```js
static properties = {
  puntos: {
    type: Number,
    ___: (nuevo, viejo) => nuevo > 0 && nuevo !== viejo
  }
};
```
* hasChanged
- shouldChange
- isDifferent
- compare
! hasChanged defines the function that decides whether a value change should trigger an update.
=== prueba
## Attribute ↔ property, type and reflect
The `valor` property is a Number and is reflected to the attribute. Compare what happens when you change the property or the attribute.
Reto: remove `reflect: true` and check that changing the property no longer updates the HTML attribute.
Clave: The attribute is a string; `type: Number` converts it to a property. `reflect` copies property → attribute (use it sparingly).
## Mutating an array does not re-render
Three buttons: mutate with push, create a new reference (the right way) and push + requestUpdate().
Reto: press "bad" three times: nothing happens. Then press "good": they all appear at once (the render reads the current array).
Clave: Lit compares by reference (!==). Mutating does not change the reference: reassign (immutable) or call requestUpdate().
