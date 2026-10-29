---
title: SPA, SSR and SSG for SEO
desc: What the crawler sees depending on how you render.
---
## What each crawler sees
Google runs JavaScript, but in a second phase, with delay and limits. Many other crawlers, social previews and **AI bots** do not run JS or do so in a limited way. What is not in the initial HTML may not exist for them.

| Strategy | Initial HTML | SEO | When |
|---|---|---|---|
| SPA (CSR) | Almost empty | Worse | Apps behind login |
| **SSG** (static) | Complete, prerendered | Excellent | Docs, blogs, marketing, this site |
| **SSR** | Complete, on every request | Very good | Dynamic and personalised content |
| ISR / revalidation | Static that refreshes | Very good | Catalogues, news |
| Prerender for bots only | Complete for bots | Acceptable | A patch for an existing SPA |

## Metadata per route
In an SPA, `<title>` and `meta` must change per route **and be in the served HTML**. Use the framework's APIs: `generateMetadata` (Next), `Title`/`Meta` (Angular), `@unhead/vue` (Nuxt/Vue), `<svelte:head>`.

## Check what a bot sees
```bash
curl -s https://your-site.com/route | head -50        # is the content and the title there?
```
If `curl` does not show your text, a crawler without JS will not either.

## Navigation
- Real `<a href>` links; `onClick` with `navigate()` is not crawled.
- Do not use `#` for routes (`/#/page`): use the History API.
- Pagination and filters with their own URLs if you want them indexed.

## Languages
`hreflang` between versions and `x-default`. Truly translated content, not just the menu.

> [!TIP] For content sites
> A static generator (Astro, Eleventy, Next with export, or your own like this one) gives complete, fast HTML that is cheap to host.

=== esquema
# Strategies
- SPA — almost empty HTML; worse for SEO.
- SSG — complete prerendered HTML; ideal for content.
- SSR — complete HTML on every request.
# Rules
- Metadata per route — in the served HTML.
- Real a href links — not just onClick.
- hreflang — between language versions.
=== test
? Do AI bots run JavaScript?
- Always
* Many do not, or only in a limited way
- They never see HTML
! What is not in the initial HTML may not exist for them.
? What is best for a documentation site?
* Static generation (SSG)
- An SPA without SSR
- iframes
! Complete, fast HTML that is cheap to host.
? How do you check what a bot sees?
- With the inspector
* curl to the URL
- With Lighthouse only
! If curl does not show your text, a crawler without JS will not either.
