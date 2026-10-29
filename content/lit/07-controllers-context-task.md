---
title: Controllers, Context y Task
desc: Reutilizar lógica, evitar prop drilling y manejar async con estados.
pkgs: lit, @lit/context, @lit/task
---
## Reactive Controllers
Objeto que se engancha al ciclo de vida del host.
```ts
class ClockController implements ReactiveController {
  value = new Date(); private t?: number;
  constructor(private host: ReactiveControllerHost) { host.addController(this); }
  hostConnected() { this.t = setInterval(() => { this.value = new Date(); this.host.requestUpdate(); }, 1000); }
  hostDisconnected() { clearInterval(this.t); }
}
// en el componente: private clock = new ClockController(this);
```
**Frente a mixins**: tiene estado propio, no toca el prototipo, puedes tener varios por host y no hay colisiones de nombres. Casos: observers, eventos externos, tareas async.

## Context (`@lit/context`)
```ts
export const userContext = createContext<User>('user');
// proveedor
@provide({context: userContext}) user = {...};
// consumidor
@consume({context: userContext, subscribe: true}) user!: User;
```
- Sin `subscribe: true` el consumidor recibe el valor **una sola vez**.
- Usa eventos DOM (`context-request`): interopera con otras librerías.
- Casos: usuario actual, idioma, servicios, tema.

## Task (`@lit/task`)
```ts
private _user = new Task(this, {
  task: async ([id], {signal}) => (await fetch(`/u/${id}`, {signal})).json(),
  args: () => [this.id] as const,
});
render() {
  return this._user.render({
    pending: () => html`Cargando…`,
    complete: u => html`${u.name}`,
    error: e => html`Error: ${e}`,
  });
}
```
Estados `INITIAL`, `PENDING`, `COMPLETE`, `ERROR`. Se reejecuta al cambiar `args`; la ejecución anterior recibe un `AbortSignal` (pásalo a `fetch`). `autoRun: false` + `run()` para modo manual.
