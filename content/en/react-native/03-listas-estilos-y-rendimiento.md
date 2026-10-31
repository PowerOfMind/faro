---
title: React Native: lists, styling and performance
desc: A practical guide to react native: lists, styling and performance, common mistakes, decisions, and checks to help you solve problems with confidence.
pkgs: react-native, react, react-native-safe-area-context
---
## Lists
`FlatList` virtualizes rows; `SectionList` groups items into sections. Use stable IDs with `keyExtractor`, immutable data and `extraData` when rendering depends on state outside `data`.

## Styles and platform
Flexbox defaults to a column. `StyleSheet.create` organizes styles and `Platform.select` allows justified differences. Use `SafeAreaView` from `react-native-safe-area-context` with its provider for safe areas.

## Measure before optimizing
Reduce image dimensions and weight; specify dimensions for remote images. Measure in a production build and on real devices. `memo` can help expensive rows when props are stable; it does not fix mutated data.

## Quick decisions
| Question | Answer |
|---|---|
| Which list groups sections? | SectionList |
| What identifies rows? | A stable key |
| What is passed when rendering depends on external state? | extraData |

> [!AI] With AI
> Describe your version, environment, expected and actual results, and a minimal reproduction. Ask for a testable explanation and references to the official documentation.

Documentation: [official guide](https://reactnative.dev/docs/flatlist).

Related: [continue with a related guide](@/react-native/expo-router-y-navegacion).

=== esquema
# Key ideas
- Lists — `FlatList` virtualizes rows; `SectionList` groups items into sections.
- Styles and platform — Flexbox defaults to a column.
- Measure before optimizing — Reduce image dimensions and weight; specify dimensions for remote images.
=== test
? Which list groups sections?
* SectionList
- A stable key
- extraData
! SectionList.
? What identifies rows?
* A stable key
- extraData
- column
! A stable key.
? What is passed when rendering depends on external state?
* extraData
- column
- On devices and in a production build
! extraData.
? What is the default Flexbox direction?
* column
- On devices and in a production build
- SectionList
! column.
? Where should real performance be measured?
* On devices and in a production build
- SectionList
- A stable key
! On devices and in a production build.
=== prueba

> [!NOTE] These examples use React Native Web in the browser; test native behavior on devices.

## Filtered list
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
Reto: change a value and observe the result.

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
Reto: change a value and observe the result.
