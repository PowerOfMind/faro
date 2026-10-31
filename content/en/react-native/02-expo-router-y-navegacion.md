---
title: Expo Router and navigation
desc: A practical guide to expo router and navigation, common mistakes, decisions, and checks to help you solve problems with confidence.
pkgs: expo, expo-router, react-native
---
## File routes
In `app/` or `src/app/`, `index.tsx` is an index and `[id].tsx` defines a dynamic segment. A parenthesized group organizes routes without adding its name to the URL.

## Layouts and navigation
`_layout.tsx` configures a shared navigator: `Stack` for stacked screens or `Tabs` for tabs. Use `Link` to navigate and `useLocalSearchParams` to read local parameters.

## Deep links
Configure a URL scheme in Expo configuration and test the link on a device and suitable build. iOS universal links and Android App Links also require domain and platform configuration.

## Quick decisions
| Question | Answer |
|---|---|
| Which file defines a layout? | _layout.tsx |
| What does [id] indicate? | A dynamic segment |
| Which hook reads local parameters? | useLocalSearchParams |

> [!AI] With AI
> Describe your version, environment, expected and actual results, and a minimal reproduction. Ask for a testable explanation and references to the official documentation.

Documentation: [official guide](https://docs.expo.dev/router/introduction/).

Related: [continue with a related guide](@/react-native/expo-eas-y-publicar).

=== esquema
# Key ideas
- File routes — In `app/` or `src/app/`, `index.tsx` is an index and `[id].tsx` defines a dynamic segment.
- Layouts and navigation — `_layout.tsx` configures a shared navigator: `Stack` for stacked screens or `Tabs` for tabs.
- Deep links — Configure a URL scheme in Expo configuration and test the link on a device and suitable build.
=== test
? Which file defines a layout?
* _layout.tsx
- A dynamic segment
- useLocalSearchParams
! _layout.tsx.
? What does [id] indicate?
* A dynamic segment
- useLocalSearchParams
- Tabs
! A dynamic segment.
? Which hook reads local parameters?
* useLocalSearchParams
- Tabs
- Domain and platform configuration
! useLocalSearchParams.
? Which navigator presents tabs?
* Tabs
- Domain and platform configuration
- _layout.tsx
! Tabs.
? What does a universal link require?
* Domain and platform configuration
- _layout.tsx
- A dynamic segment
! Domain and platform configuration.
