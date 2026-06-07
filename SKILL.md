---
name: trpg-core-rulebook-reviewer
description: Review tabletop roleplaying game core rulebooks through design-first specialist critique. Use when assessing full or scoped RPG core books, SRDs, player handbooks, GM guides, ashcans, quickstart-to-core expansions, or rulebook drafts for play experience, rules architecture, character creation, advancement, GM procedures, setting integration, teaching path, reference usability, contradictions, safety risks, and visual flow.
---

# TRPG Core Rulebook Reviewer

## Core Principle

Use design critique as the first lens. A core rulebook must not only contain rules, it must teach a playable game, define a repeatable play loop, support character creation and advancement, guide the GM, and remain usable as a reference after learning.

The central question is: what experience does this game promise, and do the rules, procedures, examples, book structure, character options, GM tools, setting material, and presentation reliably produce that experience?

## Workflow

1. Identify source, scope, draft stage, audience, system lineage or rule-set if supplied, intended play experience, and whether this is a full-book or section review.
2. If the intended play experience is unstated, infer a provisional intent from the text. For full manuscripts or serious design reviews, ask the user to confirm or correct it before running the full pass set.
3. Define review scope before spawning agents:
   - **Full core book**: review architecture, teaching path, rules engine, character creation, advancement, GM procedures, reference usability, and visual flow if visible.
   - **Scoped section**: review the named section in context and flag dependencies on unseen chapters.
   - **Early draft**: challenge premise, play loop, procedures, incentives, advancement, and book architecture.
   - **Near-final**: focus on contradictions, missing procedures, examples, usability, presentation, and remaining structural faults.
4. Spawn independent subagents for the relevant review passes. Use `references/subagent-briefs.md` for role briefs.
   - If subagents are available but require user permission, ask for permission before continuing. Show the planned pass list and explain that the fallback is a lower-independence sequential review.
   - If permission is denied, run the passes sequentially with strict separation and record that limitation in the recommendations document.
5. If the environment limits active subagents, run the passes as a queue:
   - Build the complete pass list before starting.
   - Spawn only up to the available or approved maximum.
   - When the maximum is reached, wait for one active subagent to finish before spawning the next queued pass.
   - Capture the completed pass output immediately, then close that subagent if the environment requires closure to free capacity.
   - Repeat until every planned pass has completed.
6. Keep subagent outputs isolated until all passes return. Do not let one pass anchor another.
7. Synthesise findings in a neutral, evidence-led voice. Preserve important disagreement and uncertainty.
8. Save a Markdown recommendations document when a writable workspace exists. Use `outputs/core-rulebook-review-{source-slug}-{date}.md` where practical. Summarise the top findings in chat.

If no subagent tool is available, state that limitation and run the passes sequentially with strict separation. Do not treat a permission prompt as unavailability.

## Default Passes

Run these passes by default for a full or substantial core rulebook review:

- **Core design architect**: Assess promised play experience, core loop, procedures, incentive structure, player choices, GM workload, and whether the book's design elements reinforce each other.
- **Adversarial critic**: Stress-test structural claims, false assumptions, dominant strategies, hidden GM repair work, unearned genre promises, broken learning path, and places where the game may fail at the table.
- **Rules engine and probability reviewer**: Check core mechanic clarity, resolution flow, edge cases, scale, difficulty, odds, resource cycles, advancement pressure, and whether examples match rules.
- **Character creation and advancement reviewer**: Check chargen sequence, option balance, archetype support, onboarding, prerequisites, advancement loops, long-term incentives, and whether player choices remain meaningful.
- **GM procedure and play-support reviewer**: Check session structure, adjudication guidance, scenario creation, encounter or scene tools, NPC guidance, reward cycles, downtime, safety tools, and failure states.
- **Continuity and contradiction reader**: Check internal consistency, terminology, chapter-to-chapter contradictions, broken cross-references, stat block mismatches, and missing definitions.
- **Teaching path and reference usability reader**: Check whether the book teaches well on first read and works as a table reference after learning.

Run this pass by default when visual or laid-out material is supplied:

- **Visual flow and layout reviewer**: Check page hierarchy, spread flow, table usability, examples, sidebars, diagrams, character sheets, maps, accessibility, and whether presentation supports learning and reference use.

Mention these optional passes when relevant, but do not run them by default unless the user asks or the material clearly requires them: sensitivity, accessibility, safety tools, publisher fit, compatibility/licence review, setting canon fit, and combat math deep dive.

Safety and sensitive-content review should trigger automatically only when the material clearly includes safety-relevant content, such as horror, abuse, sexual content, self-harm, torture, coercion, bigotry, colonial themes, slavery, child harm, or bleed-heavy emotional play.

## Review Boundaries

- Use only supplied material unless the user provides a rule-set, names a public SRD, or asks for a rule-set-specific review.
- Use a named RPG design framework only when the user or material states it, or when the text is clearly supported by a particular rule-set.
- Flag system-compliance uncertainty when the underlying rules are implied but unavailable.
- Do not assume every core rulebook needs the same play culture, tactical weight, fiction-first procedure, or advancement model.
- Do not rewrite problem sections by default. Diagnose and record recommendations. Rewrite only when the user asks.
- Recommend redesign only when smaller fixes would mislead the author. Say plainly when a problem is structural rather than editorial, then offer the smallest viable redesign path.

## Evidence And Priority

- Rank findings by likely impact on the promised play experience, using both severity and design leverage.
- Cite evidence for every problem where possible: page, section, heading, paragraph, table, example, stat block, character option, visual location, or short quoted phrase.
- Keep broad impressions in summaries only, labelled as impressions rather than defects.
- Include positive findings sparingly and functionally. Explain what to preserve because it supports a specific play behaviour or learning need.
- Cap final findings by default. Include the top issues that materially affect the design, then note if minor editorial issues need a separate pass.
- Describe playtest predictions cautiously as "likely at the table" or "risk to test". Do not present them as facts.

Severity labels:

- **Critical**: Likely to break core play, block comprehension, invalidate the promised experience, or make the book unusable for its stated audience.
- **Major**: Likely to cause confusion, slow play, weaken the rules architecture, distort advancement, or require GM repair.
- **Moderate**: Noticeable weakness with a contained fix.
- **Minor**: Polish issue, preference-sensitive concern, or low-risk improvement.

## Recommendations Document

Create a Markdown recommendations document by default when possible:

```markdown
# Core Rulebook Review Recommendations: [Source]
Date: [date]

## Review Context
- Source:
- Scope:
- Draft stage:
- Audience:
- System lineage or rule-set:
- Intended play experience:
- Intent status: confirmed/provisional/inferred
- Sections reviewed:
- Sections unavailable:

## Review Method
- Passes run:
- Passes skipped:
- Permission or tooling limitations:
- Source limitations:

## Executive Judgement
[Readiness, main design risk, and whether the book currently teaches and supports its promised game.]

## Recommendation Register
| Priority | Area | Evidence | Issue | Impact | Recommendation | Owner/Status |
| --- | --- | --- | --- | --- | --- | --- |

## Core Architecture Notes
[Only when book structure, core loop, rules engine, or GM procedure needs structural redesign.]

## What To Preserve
- [Working design element, and why it matters.]

## Playtest Risks
[Only when text review cannot settle the issue.]

## Pass Summaries
- **Core design architect**:
- **Adversarial critic**:
- **Rules engine and probability**:
- **Character creation and advancement**:
- **GM procedure and play support**:
- **Continuity and contradiction**:
- **Teaching path and reference usability**:
- **Visual flow and layout**:

## Disagreements Or Uncertainties
- [Important disagreement, missing context, or question for the author.]
```

Do not include raw subagent transcripts unless the user asks for them.
