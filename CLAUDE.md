# a'mie marketing workspace

This repo is the marketing brain for a'mie (amie-sa.com, Zid store). It holds no app code.

- Brand, products, categories, keywords and hard rules: `.claude/product-marketing.md` — read it before any marketing task.
- What each product and the packaging look like (label text, colours, scale, the real shopping bag): `.claude/product-visual-library.md`, with official photos in `content/brand/product-refs/` — read it before any image prompt or image review.
- Agents (`.claude/agents/`): core team `amie-seo`, `amie-geo`, `amie-writer`, `amie-cro`, `amie-reviewer`, `amie-visual-qa` (checks every generated image), plus 34 specialists from agency-agents (MIT, msitarzewski/agency-agents), each with an a'mie preamble and no access to Zid or live accounts:
  - Performance / paid: `paid-media-auditor`, `paid-media-ppc-strategist`, `paid-media-paid-social-strategist`, `paid-media-creative-strategist`, `paid-media-search-query-analyst`, `paid-media-tracking-specialist`, `marketing-growth-hacker`
  - Analysis / BI (Power BI-ready): `support-analytics-reporter`, `engineering-data-visualization-engineer`, `engineering-data-engineer`, `finance-financial-analyst`, `finance-fpa-analyst`, `product-feedback-synthesizer`, `product-trend-researcher`, `business-strategist`, `specialized-pricing-analyst`, `support-executive-summary-generator`, `research-synthesist`
  - SEO / AI search / content: `marketing-seo-specialist`, `marketing-ai-citation-strategist`, `marketing-aeo-foundations`, `marketing-content-creator`, `marketing-email-strategist`, `marketing-pr-communications-manager`, `marketing-instagram-curator` (also Saudi-dialect captions), `marketing-tiktok-strategist`
  - Images / video / brand: `design-image-prompt-engineer`, `design-visual-storyteller` (also campaign director: concept, shot list, timeline), `design-brand-guardian`, `marketing-short-video-editing-coach`, `marketing-video-optimization-specialist`, `design-persona-walkthrough`
  - Quality / output: `support-legal-compliance-checker`, `specialized-document-generator`
  - Every specialist's output still goes through `amie-reviewer`.
- Skills (`.claude/skills/`): the marketingskills library (MIT, coreyhaines31/marketingskills).
- Workflows (`.claude/workflows/`): `amie-seo-geo-categories.js` — writers → reviewers pipeline for category copy.

## Pipeline (always in this order)
1. Specialist agent drafts (writer / SEO / GEO / CRO).
2. `amie-reviewer` checks facts, forbidden claims, limits, links, voice.
3. A human approves or edits.
4. Only then is anything changed on the Zid store, and only what was approved.

## Image pipeline
1. `design-visual-storyteller` plans the campaign and shot list.
2. `design-image-prompt-engineer` writes prompts from `.claude/product-visual-library.md` and attaches the reference photos.
3. Generate a draft at quality medium, 1K (0.5 credits), with one image per request.
4. `amie-visual-qa` checks the draft, and free local fixes come first.
5. A human approves.
6. The final is generated at high, 2K (2.75 credits).
- Tell the user the credit cost before generating.

## Store rules
- Never publish, delete or rename anything on Zid without explicit approval in the conversation.
- Renaming a category or product in Zid changes its URL — don't rename.
- Updating a category description through the Zid API resets its SEO title to the category name: write descriptions first, set SEO titles last (in the Zid dashboard).
- Take a backup (list/export) before bulk edits.
