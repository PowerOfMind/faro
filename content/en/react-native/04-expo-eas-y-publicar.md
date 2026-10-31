---
title: Expo EAS and publishing
desc: A practical guide to expo eas and publishing, common mistakes, decisions, and checks to help you solve problems with confidence.
pkgs: expo, expo-updates
---
## From development to production
A development build includes the project's native code and configuration. Expo Go has a limited native module set. Native changes require a new compatible build.

## Build, Update and Submit
EAS Build produces binaries; EAS Update delivers compatible JavaScript and assets; EAS Submit uploads binaries to store platforms. Submission does not guarantee approval or automatic publication in every store.

## Channels and versions
A build points to a channel; an update must match its platform and `runtimeVersion` for native compatibility. Change the runtime version when native compatibility changes or use a suitable policy. Check identifiers, visible version and build number for each store and test before release.

## Quick decisions
| Question | Answer |
|---|---|
| What does EAS Build produce? | Binaries |
| What does EAS Update deliver? | Compatible JavaScript and assets |
| What does EAS Submit do? | Uploads binaries to store platforms |

> [!AI] With AI
> Describe your version, environment, expected and actual results, and a minimal reproduction. Ask for a testable explanation and references to the official documentation.

Documentation: [official guide](https://docs.expo.dev/eas-update/runtime-versions/).

Related: [continue with a related guide](@/react-native/expo-router-y-navegacion).

=== esquema
# Key ideas
- From development to production — A development build includes the project's native code and configuration.
- Build, Update and Submit — EAS Build produces binaries; EAS Update delivers compatible JavaScript and assets; EAS Submit uploads binaries to store platforms.
- Channels and versions — A build points to a channel; an update must match its platform and `runtimeVersion` for native compatibility.
=== test
? What does EAS Build produce?
* Binaries
- Compatible JavaScript and assets
- Uploads binaries to store platforms
! Binaries.
? What does EAS Update deliver?
* Compatible JavaScript and assets
- Uploads binaries to store platforms
- Compatibility with native code
! Compatible JavaScript and assets.
? What does EAS Submit do?
* Uploads binaries to store platforms
- Compatibility with native code
- A new compatible build
! Uploads binaries to store platforms.
? What does runtimeVersion check?
* Compatibility with native code
- A new compatible build
- Binaries
! Compatibility with native code.
? What does a native change require?
* A new compatible build
- Binaries
- Compatible JavaScript and assets
! A new compatible build.
