---
title: React Native: listas, estilos y rendimiento
desc: Guía práctica de react native: listas, estilos y rendimiento, errores frecuentes, decisiones y comprobaciones para resolver problemas con criterio.
pkgs: react-native, react, react-native-safe-area-context
---
## Listas
`FlatList` virtualiza filas; `SectionList` agrupa elementos por secciones. Usa identificadores estables con `keyExtractor`, datos inmutables y `extraData` si la representación depende de estado externo a `data`.

## Estilos y plataforma
Flexbox usa columna por defecto. `StyleSheet.create` organiza estilos y `Platform.select` permite diferencias justificadas. Usa `SafeAreaView` de `react-native-safe-area-context` con su proveedor para áreas seguras.

## Medir antes de optimizar
Reduce dimensiones y peso de imágenes; especifica dimensiones para imágenes remotas. Mide en una build de producción y dispositivos reales. `memo` puede ayudar con filas costosas si las props son estables; no arregla datos mutados.

## Decisiones rápidas
| Pregunta | Respuesta |
|---|---|
| ¿Qué lista agrupa secciones? | SectionList |
| ¿Qué identifica filas? | Una clave estable |
| ¿Qué se pasa si el render depende de estado externo? | extraData |

> [!AI] Con IA
> Indica la versión, el entorno, el resultado esperado y real, y una reproducción mínima. Pide una explicación comprobable y referencias a la documentación oficial.

Documentación: [guía oficial](https://reactnative.dev/docs/flatlist).

Relacionado: [continúa con otra guía](@/react-native/expo-router-y-navegacion).

=== esquema
# Ideas clave
- Listas — `FlatList` virtualiza filas; `SectionList` agrupa elementos por secciones.
- Estilos y plataforma — Flexbox usa columna por defecto.
- Medir antes de optimizar — Reduce dimensiones y peso de imágenes; especifica dimensiones para imágenes remotas.
=== test
? ¿Qué lista agrupa secciones?
* SectionList
- Una clave estable
- extraData
! SectionList.
? ¿Qué identifica filas?
* Una clave estable
- extraData
- column
! Una clave estable.
? ¿Qué se pasa si el render depende de estado externo?
* extraData
- column
- En dispositivos y una build de producción
! extraData.
? ¿Cuál es la dirección Flexbox predeterminada?
* column
- En dispositivos y una build de producción
- SectionList
! column.
? ¿Dónde se mide rendimiento real?
* En dispositivos y una build de producción
- SectionList
- Una clave estable
! En dispositivos y una build de producción.
=== prueba

> [!NOTE] Estos ejemplos usan React Native Web en el navegador; comprueba el comportamiento nativo en dispositivos.

## Lista filtrada
```jsx
import {useState} from 'react';
import {FlatList, Text, TextInput, View} from 'react-native';
import {createRoot} from 'react-dom/client';
const items = [{id: '1', name: 'Sun'}, {id: '2', name: 'Moon'}];
function App() {
  const [query, setQuery] = useState('');
  return <View><TextInput accessibilityLabel="Search" value={query} onChangeText={setQuery} /><FlatList data={items.filter(item => item.name.toLowerCase().includes(query.toLowerCase()))} keyExtractor={item => item.id} renderItem={({item}) => <Text>{item.name}</Text>} /></View>;
}
createRoot(document.getElementById('app')).render(<App />);
```
Reto: cambia un valor y observa el resultado.

## Flexbox
```jsx
import {useState} from 'react';
import {View, Text, Pressable} from 'react-native';
import {createRoot} from 'react-dom/client';
function App() {
  const [row, setRow] = useState(true);
  return <View><Pressable accessibilityRole="button" onPress={() => setRow(!row)}><Text>Change direction</Text></Pressable><View style={{flexDirection: row ? 'row' : 'column', gap: 12}}><Text>One</Text><Text>Two</Text></View></View>;
}
createRoot(document.getElementById('app')).render(<App />);
```
Reto: cambia un valor y observa el resultado.
