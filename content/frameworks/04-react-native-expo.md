---
title: React Native y Expo
desc: Bases prácticas para retomar una aplicación móvil con React Native y Expo.
pkgs: react-native, expo, expo-router
---
## Modelo mental: React sin DOM
Props, estado y hooks funcionan como en [React](@/frameworks/react), pero en iOS y Android React Native representa componentes nativos, no un DOM: no uses `div`, `p` ni CSS de navegador. En web existe React Native Web, con diferencias de plataforma.

Los estilos son objetos JavaScript: `StyleSheet.create` los agrupa, usa `backgroundColor` y dimensiones numéricas independientes de la densidad, sin escribir `px`. Flexbox tiene `flexDirection: 'column'` por defecto: `justifyContent` distribuye en el eje vertical y `alignItems` en el horizontal, salvo que cambies la dirección.

## Piezas de una pantalla
- `View` agrupa; `Text` muestra texto; `Pressable` responde con `onPress`.
- `Image` muestra imágenes; para imágenes remotas indica sus dimensiones.
- `ScrollView` monta todo su contenido: sirve para contenido acotado. `FlatList` virtualiza listas largas; dale un `keyExtractor` con un id estable.
- `TextInput` recibe texto con `value` y `onChangeText`.

```jsx
import {useState} from 'react';
import {FlatList, StyleSheet, Text, TextInput, View} from 'react-native';

const items = [{id: '1', name: 'Pan'}, {id: '2', name: 'Leche'}];
export default function Lista() {
  const [query, setQuery] = useState('');
  const filtered = items.filter(item => item.name.toLowerCase().includes(query.toLowerCase()));
  return <View style={styles.screen}>
    <TextInput value={query} onChangeText={setQuery} placeholder="Buscar" />
    <FlatList data={filtered} keyExtractor={item => item.id}
      renderItem={({item}) => <Text>{item.name}</Text>} />
  </View>;
}
const styles = StyleSheet.create({screen: {flex: 1, padding: 16}});
```

Usa `Platform.OS` o `Platform.select` para diferencias justificadas entre sistemas. Para evitar muescas y barras, usa `SafeAreaView` de `react-native-safe-area-context` y configura su proveedor según el proyecto; comprueba ambas plataformas y el teclado.

## Expo: desarrollo y entrega
Expo reúne herramientas y módulos para React Native. **Expo Go** permite empezar rápido, pero contiene un conjunto fijo de código nativo. Una **development build** propia incluye los módulos y la configuración nativa del proyecto; recompílala al cambiar código o configuración nativos. Consulta la [guía de development builds](https://docs.expo.dev/develop/development-builds/introduction/).

`app.json` o `app.config.js` definen la configuración de la app, incluidos nombre e identificadores. Usa `npx expo install paquete` para elegir una versión compatible con el SDK. EAS Build genera binarios; EAS Update distribuye cambios compatibles de JavaScript y recursos; EAS Submit los envía a las plataformas de las tiendas. Un cambio nativo necesita una build compatible: Update no sustituye toda recompilación. Consulta [EAS Update](https://docs.expo.dev/eas-update/introduction/).

## Expo Router
Las rutas se crean con archivos en el directorio de rutas (`app/` o `src/app/`): `index.tsx` es la pantalla inicial, `[id].tsx` recibe un parámetro y `_layout.tsx` define la navegación compartida. `Link` navega; `useLocalSearchParams` lee los parámetros de la ruta actual.

```tsx
// app/index.tsx
import {Link} from 'expo-router';
export default function Inicio() {
  return <Link href="/producto/42">Ver producto</Link>;
}
// app/producto/[id].tsx
import {useLocalSearchParams} from 'expo-router';
import {Text} from 'react-native';
export default function Producto() {
  const {id} = useLocalSearchParams<{id: string}>();
  return <Text>Producto: {id}</Text>;
}
```

## Datos, dispositivo y seguridad
Usa estado de React para la interacción local y `fetch` para la red: contempla carga, error y cancelación cuando corresponda. TanStack Query ayuda con la caché, la actualización y los estados de datos remotos. AsyncStorage persiste datos **sin cifrar**; Expo SecureStore guarda valores sensibles en almacenamiento protegido de la plataforma.

> [!SEC] Secretos
> El bundle y la configuración pública de la app pueden inspeccionarse: nunca incluyas secretos de servidor ni claves privadas. Guarda tokens de sesión en SecureStore cuando corresponda y mantén los secretos de servidor en el backend.

Para cámara, ubicación o notificaciones, instala el módulo Expo correspondiente y revisa su configuración y disponibilidad por plataforma y entorno. Solicita permisos en contexto, explica el motivo y gestiona la denegación; algunos cambios requieren una nueva build. Consulta la [guía de permisos](https://docs.expo.dev/guides/permissions/).

## Rendimiento y depuración
Mide antes de optimizar: revisa filas, claves estables y `extraData` si una `FlatList` depende de datos externos. Reduce el tamaño de las imágenes y evita cargar imágenes enormes. Hermes es un motor JavaScript optimizado para React Native; no sustituye la medición. Usa React Native DevTools, los registros de Metro y las herramientas del dispositivo; reproduce también en una build de producción y en dispositivos reales.

## Errores frecuentes
| Síntoma | Causa o comprobación |
|---|---|
| El texto falla fuera de `Text` | Envuelve el texto en `Text`, no directamente en `View` |
| Un módulo nativo no aparece en Expo Go | Comprueba si está incluido; puede requerir una development build |
| El contenido queda bajo la muesca | Revisa proveedor y áreas seguras |
| La lista muestra filas desactualizadas | Comprueba datos inmutables, claves estables y `extraData` |
| Una actualización no llega a la app | Comprueba canal y compatibilidad de la versión de runtime |
| El permiso no funciona | Revisa configuración nativa, plataforma y estado de autorización |

> [!AI] Con IA
> Pide «React Native con mi versión de Expo SDK y Expo Router, para iOS y Android; indica instalación, configuración nativa, permisos y estados de carga y error». Dale el error completo y el entorno (Expo Go o development build); contrasta las APIs con la documentación oficial.

=== esquema
# Interfaz
- React Native — componentes nativos, no DOM.
- Flexbox — columna por defecto; dimensiones numéricas sin px.
- FlatList — listas largas y claves estables.
# Expo
- Expo Go — código nativo incluido y limitado.
- Development build — módulos y configuración propios.
- EAS — Build compila, Update distribuye cambios compatibles, Submit envía binarios.
# App real
- Router — archivos, layouts y parámetros.
- Datos — fetch, caché y almacenamiento según sensibilidad.
- Dispositivo — permisos, áreas seguras y pruebas reales.
=== test
? ¿Qué componente muestra texto en una pantalla nativa?
* Text
- div
- View directamente
! El texto debe estar dentro de Text.
? ¿Cuál es la dirección predeterminada de Flexbox?
- row
* column
- grid
! El eje principal es vertical por defecto.
? ¿Cuándo necesitas una development build?
* Cuando necesitas código nativo que Expo Go no incluye
- Para usar cualquier componente Text
- Para escribir JavaScript
! Expo Go contiene un conjunto fijo de módulos nativos.
? ¿Qué hace EAS Update?
- Compila cualquier cambio nativo
* Distribuye cambios compatibles de JavaScript y recursos
- Guarda secretos de servidor
! Los cambios nativos necesitan una build compatible.
? ¿Dónde lees los parámetros de la ruta actual en Expo Router?
* useLocalSearchParams
- keyExtractor
- StyleSheet.create
! El hook devuelve los parámetros de la ruta.
? ¿Dónde guardas un token de sesión sensible?
- En el código fuente
- En AsyncStorage sin cifrar
* En SecureStore cuando corresponda
! SecureStore usa almacenamiento protegido de la plataforma.
