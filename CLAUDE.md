# a'mie marketing workspace

This repo is the marketing brain for a'mie (amie-sa.com, Zid store). It holds no app code.

- Brand, products, categories, keywords and hard rules: `.claude/product-marketing.md` — read it before any marketing task.
- Agents (`.claude/agents/`): `amie-seo`, `amie-geo`, `amie-writer`, `amie-cro`, `amie-reviewer`.
- Skills (`.claude/skills/`): the marketingskills library (MIT, coreyhaines31/marketingskills).
- Workflows (`.claude/workflows/`): `amie-seo-geo-categories.js` — writers → reviewers pipeline for category copy.

## Pipeline (always in this order)
1. Specialist agent drafts (writer / SEO / GEO / CRO).
2. `amie-reviewer` checks facts, forbidden claims, limits, links, voice.
3. A human approves or edits.
4. Only then is anything changed on the Zid store, and only what was approved.

## Store rules
- Never publish, delete or rename anything on Zid without explicit approval in the conversation.
- Renaming a category or product in Zid changes its URL — don't rename.
- Updating a category description through the Zid API resets its SEO title to the category name: write descriptions first, set SEO titles last (in the Zid dashboard).
- Take a backup (list/export) before bulk edits.
