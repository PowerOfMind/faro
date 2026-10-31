---
title: React Native and Expo
desc: Practical foundations for returning to a mobile app with React Native and Expo.
pkgs: react-native, expo, expo-router
---
## Mental model: React without the DOM
Props, state and hooks work as in [React](@/frameworks/react), but on iOS and Android React Native renders native components, not a DOM: do not use `div`, `p` or browser CSS. React Native Web also exists, with platform differences.

Styles are JavaScript objects: `StyleSheet.create` groups them, using `backgroundColor` and numeric density-independent dimensions without writing `px`. Flexbox defaults to `flexDirection: 'column'`: `justifyContent` distributes along the vertical axis and `alignItems` along the horizontal axis, unless you change the direction.

## Screen building blocks
- `View` groups content; `Text` displays text; `Pressable` responds with `onPress`.
- `Image` displays images; specify dimensions for remote images.
- `ScrollView` mounts all its content: use it for bounded content. `FlatList` virtualises long lists; give it a `keyExtractor` with a stable id.
- `TextInput` accepts text with `value` and `onChangeText`.

```jsx
import {useState} from 'react';
import {FlatList, StyleSheet, Text, TextInput, View} from 'react-native';

const items = [{id: '1', name: 'Bread'}, {id: '2', name: 'Milk'}];
export default function List() {
  const [query, setQuery] = useState('');
  const filtered = items.filter(item => item.name.toLowerCase().includes(query.toLowerCase()));
  return <View style={styles.screen}>
    <TextInput value={query} onChangeText={setQuery} placeholder="Search" />
    <FlatList data={filtered} keyExtractor={item => item.id}
      renderItem={({item}) => <Text>{item.name}</Text>} />
  </View>;
}
const styles = StyleSheet.create({screen: {flex: 1, padding: 16}});
```

Use `Platform.OS` or `Platform.select` for justified differences between systems. To avoid notches and bars, use `SafeAreaView` from `react-native-safe-area-context` and set up its provider as required by the project; check both platforms and the keyboard.

## Expo: development and delivery
Expo brings together tools and modules for React Native. **Expo Go** gets you started quickly, but contains a fixed set of native code. A custom **development build** includes your project's native modules and configuration; rebuild it when native code or configuration changes. See the [development builds guide](https://docs.expo.dev/develop/development-builds/introduction/).

`app.json` or `app.config.js` defines app configuration, including its name and identifiers. Use `npx expo install package` to select a version compatible with the SDK. EAS Build produces binaries; EAS Update distributes compatible JavaScript and asset changes; EAS Submit sends binaries to store platforms. A native change needs a compatible build: Update does not replace every rebuild. See [EAS Update](https://docs.expo.dev/eas-update/introduction/).

## Expo Router
Routes come from files in the routes directory (`app/` or `src/app/`): `index.tsx` is the initial screen, `[id].tsx` accepts a parameter and `_layout.tsx` defines shared navigation. `Link` navigates; `useLocalSearchParams` reads the current route's parameters.

```tsx
// app/index.tsx
import {Link} from 'expo-router';
export default function Home() {
  return <Link href="/product/42">View product</Link>;
}
// app/product/[id].tsx
import {useLocalSearchParams} from 'expo-router';
import {Text} from 'react-native';
export default function Product() {
  const {id} = useLocalSearchParams<{id: string}>();
  return <Text>Product: {id}</Text>;
}
```

## Data, device and security
Use React state for local interaction and `fetch` for networking: handle loading, errors and cancellation where appropriate. TanStack Query helps with caching, refreshes and remote data states. AsyncStorage persists data **unencrypted**; Expo SecureStore keeps sensitive values in platform-protected storage.

> [!SEC] Secrets
> The app bundle and public configuration can be inspected: never include server secrets or private keys. Store session tokens in SecureStore where appropriate and keep server secrets on the backend.

For camera, location or notifications, install the relevant Expo module and check its configuration and availability by platform and environment. Request permissions in context, explain why and handle denial; some changes require a new build. See the [permissions guide](https://docs.expo.dev/guides/permissions/).

## Performance and debugging
Measure before optimising: inspect rows, stable keys and `extraData` if a `FlatList` depends on external data. Reduce image sizes and avoid loading oversized images. Hermes is a JavaScript engine optimised for React Native; it does not replace measurement. Use React Native DevTools, Metro logs and device tools; also reproduce issues in a production build and on real devices.

## Common errors
| Symptom | Cause or check |
|---|---|
| Text fails outside `Text` | Wrap text in `Text`, not directly in `View` |
| A native module is missing in Expo Go | Check whether it is included; it may need a development build |
| Content sits under the notch | Check the provider and safe areas |
| The list shows stale rows | Check immutable data, stable keys and `extraData` |
| An update does not reach the app | Check the channel and runtime version compatibility |
| A permission does not work | Check native configuration, platform and authorisation status |

> [!AI] With AI
> Ask for “React Native with my Expo SDK version and Expo Router, for iOS and Android; include installation, native configuration, permissions, and loading and error states”. Provide the complete error and environment (Expo Go or development build); check the APIs against the official documentation.

=== esquema
# Interface
- React Native — native components, not the DOM.
- Flexbox — column by default; numeric dimensions without px.
- FlatList — long lists and stable keys.
# Expo
- Expo Go — included, limited native code.
- Development build — project-specific modules and configuration.
- EAS — Build compiles, Update distributes compatible changes, Submit sends binaries.
# Real app
- Router — files, layouts and parameters.
- Data — fetch, caching and storage according to sensitivity.
- Device — permissions, safe areas and real-device testing.
=== test
? Which component displays text on a native screen?
* Text
- div
- View directly
! Text must be inside Text.
? What is the default Flexbox direction?
- row
* column
- grid
! The main axis is vertical by default.
? When do you need a development build?
* When you need native code that Expo Go does not include
- To use any Text component
- To write JavaScript
! Expo Go contains a fixed set of native modules.
? What does EAS Update do?
- Compiles any native change
* Distributes compatible JavaScript and asset changes
- Stores server secrets
! Native changes need a compatible build.
? Where do you read the current route's parameters in Expo Router?
* useLocalSearchParams
- keyExtractor
- StyleSheet.create
! The hook returns the route parameters.
? Where should you store a sensitive session token?
- In source code
- In unencrypted AsyncStorage
* In SecureStore where appropriate
! SecureStore uses platform-protected storage.
