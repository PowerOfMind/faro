---
title: Angular moderno
desc: Standalone, signals, control flow y lo que sustituye a lo antiguo.
pkgs: "@angular/core", "@angular/cli"
---
## Lo que cambió (y la IA mezcla)
| Antes | Ahora |
|---|---|
| `NgModule` | Componentes **standalone** (por defecto) |
| `*ngIf`, `*ngFor` | `@if`, `@for`, `@switch` en la plantilla |
| `@Input()` / `@Output()` | `input()`, `output()`, `model()` |
| Constructor para inyectar | `inject(Servicio)` |
| `BehaviorSubject` para estado local | **Signals**: `signal()`, `computed()`, `effect()` |
| `zone.js` siempre | Detección sin zonas (*zoneless*) cada vez más usada |
| `ngModel` / reactive forms | Reactive forms (y formularios con signals, en evolución) |

## Componente actual
```ts
@Component({
  selector: 'app-contador',
  template: `
    <button (click)="inc()">{{ cuenta() }} / {{ doble() }}</button>
    @if (cuenta() > 5) { <p>¡Alto!</p> }
    @for (n of lista(); track n.id) { <li>{{ n.name }}</li> }
  `,
})
export class ContadorComponent {
  cuenta = signal(0);
  doble = computed(() => this.cuenta() * 2);
  lista = input.required<Item[]>();
  inc() { this.cuenta.update(v => v + 1); }
}
```

## Claves
- **Signals**: lee con `()`, escribe con `set`/`update`. `computed` se recalcula solo si cambian sus dependencias.
- `@for` exige `track` (identidad). Es el equivalente de `key`.
- **HTTP**: `provideHttpClient()` y `HttpClient`; `httpResource` / `resource` para datos reactivos (API en evolución: revisa la doc de tu versión).
- **RxJS** sigue siendo útil para flujos de eventos; para estado simple, signals.
- **Router**: rutas con `loadComponent` (carga diferida), guards funcionales.
- CLI: `ng generate`, `ng update` (guiado entre versiones), `ng build`.

## Errores típicos
| Mensaje | Qué mirar |
|---|---|
| `NG0100 ExpressionChanged...` | Valor cambia tras la detección; mueve la lógica o usa signals |
| `NG0303/NG0304 not a known element` | Falta importar el componente en `imports` del standalone |
| `No provider for X` | Falta `providedIn: 'root'` o el provider |
| Plantilla no se actualiza | `OnPush` + mutación de objeto |

> [!AI] Con IA
> Escribe "Angular standalone con signals y control flow `@if/@for`, sin NgModules". Si ves `*ngIf` o `@NgModule`, es código antiguo.

=== esquema
# Moderno
- Standalone — sin NgModules.
- Signals — signal, computed, effect.
- Control flow — @if, @for con track, @switch.
- input() y output() — en lugar de decoradores.
- inject() — en lugar del constructor.
# Errores
- NG0100 — valor cambia tras la detección.
- Not a known element — falta el import del standalone.
=== test
? ¿Qué sustituye a *ngFor?
* @for con track
- v-for
- map en el componente
! track da identidad a cada elemento.
? ¿Cómo lees una signal?
- cuenta.value
* cuenta()
- cuenta.get
! Las signals se leen llamándolas.
? Ves @NgModule y *ngIf en una respuesta de IA. ¿Qué indica?
* Código antiguo; pide standalone con signals y control flow
- Es lo recomendado hoy
- Es de React
! Hay que fijar el paradigma al pedir.
