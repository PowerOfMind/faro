---
title: Dependencies that do not add up
desc: Dependency conflicts can block a project. Resolve peer version errors and duplicate packages while understanding lockfiles and ESM.
---
## ERESOLVE / peer dependency
`npm` says A needs React 18 and you have 19.
1. Read **which package** asks for which version; is there a newer release of that package that supports it?
2. Update that package or wait for its release; check its issues.
3. `--legacy-peer-deps` or `overrides` are patches: document why you use them.

```json
{ "overrides": { "old-package": { "react": "$react" } } }
```

## Two copies of the same package
Symptoms: `instanceof` fails, an empty React context, **Lit "already defined"** (`customElements.define` twice), invalid hooks.
```bash
npm ls lit react            # look for "deduped" or several versions
npm dedupe
```
In monorepos, declare the library as a `peerDependency` in the shared package.

## Lockfile
- Commit it (`package-lock.json`, `pnpm-lock.yaml`).
- In CI use `npm ci`, which respects the lock and fails if it does not match.
- Deleting `node_modules` and the lock "to fix it" changes the versions of everything: last resort.

## ESM vs CommonJS
`require() of ES Module not supported` / `Cannot use import statement outside a module`:
- Set `"type": "module"` in `package.json` or use the `.mjs` extension.
- In TS, align `module` and `moduleResolution` (`NodeNext` or `Bundler`) with what your runtime runs.
- Relative imports in native ESM carry the extension (`./util.js`).

## Before adding a dependency
`npm view <pkg>`: last publish, maintainers, size. If the AI suggested it, confirm it exists and is the package you think (see [slopsquatting](@/seguridad/dependencias)).

=== esquema
# Conflicts
- ERESOLVE — a package asks for another version of a peer.
- Two copies — instanceof fails or Lit defines twice.
- overrides — a documented patch, not a solution.
# Discipline
- Committed lockfile — npm ci in CI.
- ESM vs CJS — type module or .mjs; extension in relative imports.
=== test
? What does npm ci do in CI?
* Installs exactly what the lockfile says and fails if it does not match
- Updates everything to latest
- Deletes node_modules without installing
! It gives reproducible builds.
? "Cannot use import statement outside a module". Usual fix?
- Change IDE
* "type": "module" or the .mjs extension
- Remove the import
! Align the module type with what your runtime runs.
? Deleting node_modules and the lockfile "to fix it" is...
- The first recommended solution
* A last resort: it changes versions of everything
- Essential every week
! Better to understand which package asks for which version.
