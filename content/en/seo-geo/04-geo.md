---
title: GEO: getting cited by AI models
desc: Generative Engine Optimization: what is known and what is hype.
---
**GEO** aims to get AI search tools (AI Overviews, ChatGPT with search, Perplexity, Copilot) to use you as a **cited source**. It is SEO with nuances: you no longer compete only for a click but for appearing inside the answer.

## What has a basis
1. **Solid SEO first.** Search-enabled systems start from web results; if you are not indexed and reachable, you do not exist.
2. **HTML readable without JS.** AI bots often do not run JavaScript (so server-side or static rendering matters).
3. **Direct answers.** A question-style heading, the answer in 1-2 sentences, then the detail.
4. **Citable facts.** Figures with sources, clear definitions, dates, tables. Vague claims do not get cited.
5. **Visible authorship and date.** Trust signals (E-E-A-T): who writes, when it was updated, sources.
6. **Structured data** consistent with the content.
7. **External mentions**: being cited or linked by reliable sites matters.
8. **Update** what expires (versions, prices) and show the review date.

## Controlling bots
`robots.txt` can tell training bots from search bots. Example agents: `GPTBot` (OpenAI training), `OAI-SearchBot` (search), `ClaudeBot`, `PerplexityBot`, `Google-Extended` (Gemini usage control). Blocking the training bot does not have to remove you from search results. Check current names in each company's docs.
```text
User-agent: GPTBot
Disallow: /
User-agent: OAI-SearchBot
Allow: /
```

## `llms.txt`
A proposed Markdown file at the site root that summarises the site and links the key pages for models. It is cheap to generate (this site does it). **There is no solid evidence it improves citations**, and the big search engines have not adopted it as a standard: treat it as an extra, not a strategy.

## What to avoid
- Promising to "rank in ChatGPT" with tricks. There is no trick.
- Generic mass-produced text: it adds little and erodes trust.
- Measuring only clicks: also measure mentions and referral traffic from AI tools.

=== esquema
# What works
- Solid SEO first — if you are not indexed, you do not exist.
- HTML readable without JS — AI bots often do not run it.
- Direct answer — a question and 1-2 sentences of answer.
- Citable facts — figures with sources, dates, tables.
- Authorship and date — trust signals.
# Caution
- llms.txt — cheap, no solid evidence of effect.
- AI bots — separate training from search in robots.txt.
=== test
? What is GEO?
* Optimising so AI search tools cite you as a source
- An image format
- A type of server
! It is SEO focused on appearing inside the generated answer.
? Does llms.txt improve citations, per current evidence?
- Yes, clearly
* There is no solid evidence: it is an extra, not a strategy
- It is mandatory
! The big search engines have not adopted it as a standard.
? Which content gets cited most?
* Concrete facts with visible source and date
- Mass-produced generic text
- Vague phrases
! Models cite verifiable claims.
