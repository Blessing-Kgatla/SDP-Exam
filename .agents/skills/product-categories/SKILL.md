---
name: product-categories
description: Category reference for the 40 product types (e-commerce, marketplace, SaaS, ERP, fintech, LMS, social, healthcare, fitness, games, maps, creative editors, AI tools, desktop utilities and more). Use it after classifying a product, before choosing its art direction, palette, stack or repository structure, or when reviewing category-specific risks.
---

# Product categories: design briefs, palettes, stacks, risks

Use this after you have classified the product (AGENTS.md §4). Look up the **primary** category number (01–40) in each file below. Secondary categories only add requirements; they don't replace the primary category's layout or stack.

| Need | Read | What it holds |
|---|---|---|
| Visual character, primary screens, distinctive patterns, clichés to avoid | `design-briefs.md` | 40 design briefs grouped A–G |
| Starting colour tokens and whether they are accessible | `palettes.md` | 40 six-colour suites, a computed WCAG contrast audit, and fixed primaries for #19 and #39 |
| Minimal stack, feature modules, repository structure letter | `stacks.md` | 40 stack recommendations with notes (payments by country, AI features) |
| What usually goes wrong in this category | `risks.md` | Category risk table and AI-feature documentation checklist |

Read files with `read_skill_file`. Load only the files you need for the current step.

## How to apply

1. Treat briefs and palettes as **starting points**. Adapt them to the real brand, audience, market and content. Never apply them wholesale or copy another product's identity.
2. Check the palette's row in the contrast audit **before** assigning roles. Accent colours are mostly fill-only, and secondary colours are mostly not for body text.
3. Take the stack from `stacks.md`, then confirm it against the actual requirements (AGENTS.md §6). Deviate when the requirements justify it, and record why.
4. Turn every risk that applies to the category into a requirement, test or open question. Don't just list it.
5. For the structure letter (A–H) and setup commands, load the `project-scaffolds` skill.
