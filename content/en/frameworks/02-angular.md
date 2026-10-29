---
title: Modern Angular
desc: Standalone, signals, control flow and what replaces the old way.
pkgs: "@angular/core", "@angular/cli"
---
## What changed (and the AI mixes up)
| Before | Now |
|---|---|
| `NgModule` | **Standalone** components (the default) |
| `*ngIf`, `*ngFor` | `@if`, `@for`, `@switch` in the template |
| `@Input()` / `@Output()` | `input()`, `output()`, `model()` |
| Constructor injection | `inject(Service)` |
| `BehaviorSubject` for local state | **Signals**: `signal()`, `computed()`, `effect()` |
| `zone.js` always | Zoneless change detection, increasingly used |
| `ngModel` / reactive forms | Reactive forms (and signal-based forms, evolving) |

## A current component
```ts
@Component({
  selector: 'app-counter',
  template: `
    <button (click)="inc()">{{ count() }} / {{ double() }}</button>
    @if (count() > 5) { <p>High!</p> }
    @for (n of list(); track n.id) { <li>{{ n.name }}</li> }
  `,
})
export class CounterComponent {
  count = signal(0);
  double = computed(() => this.count() * 2);
  list = input.required<Item[]>();
  inc() { this.count.update(v => v + 1); }
}
```

## Key points
- **Signals**: read with `()`, write with `set`/`update`. `computed` recalculates only if its dependencies change.
- `@for` requires `track` (identity). It is the equivalent of `key`.
- **HTTP**: `provideHttpClient()` and `HttpClient`; `httpResource` / `resource` for reactive data (an evolving API: check the docs for your version).
- **RxJS** is still useful for event streams; for simple state, signals.
- **Router**: routes with `loadComponent` (lazy loading), functional guards.
- CLI: `ng generate`, `ng update` (guided between versions), `ng build`.

## Typical errors
| Message | What to look at |
|---|---|
| `NG0100 ExpressionChanged...` | A value changes after detection; move the logic or use signals |
| `NG0303/NG0304 not a known element` | The component is not imported in the standalone `imports` |
| `No provider for X` | Missing `providedIn: 'root'` or the provider |
| Template does not update | `OnPush` + object mutation |

> [!AI] With AI
> Write "Angular standalone with signals and `@if/@for` control flow, no NgModules". If you see `*ngIf` or `@NgModule`, it is old code.

=== esquema
# Modern
- Standalone — no NgModules.
- Signals — signal, computed, effect.
- Control flow — @if, @for with track, @switch.
- input() and output() — instead of decorators.
- inject() — instead of the constructor.
# Errors
- NG0100 — a value changes after detection.
- Not a known element — the standalone import is missing.
=== test
? What replaces *ngFor?
* @for with track
- v-for
- map in the component
! track gives each element an identity.
? How do you read a signal?
- count.value
* count()
- count.get
! Signals are read by calling them.
? You see @NgModule and *ngIf in an AI answer. What does it indicate?
* Old code; ask for standalone with signals and control flow
- It is what is recommended today
- It is from React
! You must pin the paradigm when you ask.
