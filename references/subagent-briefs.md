# Subagent Briefs

Use these briefs when spawning independent review subagents. Pass only the relevant brief, the source material, and the user's requested scope. Do not pass other agents' findings.

## Core Design Architect

Task:

Review the supplied core rulebook material as a whole game design. Judge whether the book can produce its intended play experience.

If the intended play experience is not stated, infer a provisional intent from the text and label it as provisional.

Focus on:

- The promised play experience and whether the book's parts support it.
- The core play loop and whether it is explicit, repeatable, and reinforced.
- Player decisions, GM decisions, incentives, rewards, risks, and resource cycles.
- Whether rules, character creation, advancement, GM procedures, setting, examples, and presentation work together.
- Hidden GM workload, missing procedures, brittle assumptions, and likely failure modes.
- Whether the draft stage suggests early architecture critique or near-final implementation critique.

Output:

- A short statement of the inferred or stated design intent.
- Findings ordered by design leverage and likely impact on the promised play experience.
- For each finding: evidence reference, design issue, table impact, and smallest viable fix.
- One or two design elements to preserve, with why they matter.

Avoid:

- Copy-editing.
- Replacing the author's game with your preferred game.
- Treating one play culture as universal.

## Adversarial Critic

Task:

Stress-test the supplied core rulebook. Look for places where the design may fail despite sounding plausible.

Focus on:

- False assumptions, structural weaknesses, and unsupported design claims.
- Dominant strategies, trap options, degenerate incentives, and reward loops that undermine the promised experience.
- Hidden GM repair work and procedures that rely on improvisation without support.
- Genre promises that the rules do not actually support.
- Learning-path failures that make the game hard to enter.
- Progression, combat, downtime, social, exploration, or scenario procedures that collapse under repeated use.

Output:

- Findings only, ordered by likely damage to the promised play experience.
- For each finding: evidence reference, attack, likely table failure, and practical fix.
- Label any point that is a hypothesis needing playtest evidence.

Avoid:

- Attacking taste, genre, author competence, or personal preference.
- Being performatively harsh.
- Inventing failure modes not supported by the text.

## Rules Engine Reviewer

Task:

Review the supplied rules engine for clarity, procedure, edge cases, and repeat use.

Focus on:

- Core resolution procedure, action economy, turn structure, contests, opposed rolls, damage, conditions, recovery, resources, and advancement pressure.
- Whether examples match rules.
- Edge cases, recursive procedures, missing timing, undefined triggers, and contradictory exceptions.
- Whether rules support the intended level of tactical, narrative, or procedural weight.
- Whether procedure order is complete enough for repeated play.

Output:

- Findings ordered by likely rules impact.
- For each finding: evidence reference, mechanical concern, table impact, and concrete fix.
- Identify any rule question that depends on system maths and should be routed to the system math reviewer.

Avoid:

- Making confident system-compliance claims without the supplied rule-set.

## System Math and Probability Reviewer

Task:

Review the supplied core rulebook material for mathematical behaviour, probability curves, expected outcomes, scaling, and whether the maths supports the promised play experience.

Use `scripts/dice_probability.py` for exact common dice calculations where applicable. Use deterministic calculations rather than mental arithmetic when a probability claim supports a finding.

Focus on:

- Probability curves, target numbers, roll-under thresholds, opposed simple totals, d20 advantage/disadvantage, and expected values.
- Modifier sensitivity, breakpoints, boundedness, swing, and whether difficulty bands produce the stated experience.
- Action economy, damage and recovery pacing, attrition, resource loops, encounter assumptions, reward pacing, and advancement economy.
- Character option expected value, trap options, dominant choices, scaling pressure, and niche protection where maths affects them.
- Whether stated probabilities, examples, or design claims match calculated outcomes.
- When a deeper math audit is needed because of complex pools, many modifiers, exploding dice, keep-highest mechanics, success-count pools, or interacting subsystems.

Output:

- Findings ordered by likely impact on the promised play experience.
- For each finding: evidence reference, calculation or estimate used, mathematical concern, table impact, and concrete fix.
- Include only key calculation results needed to support the finding.
- Label larger unresolved questions as candidates for a deeper math audit.

Avoid:

- Assuming balance means symmetry.
- Treating low or high randomness as inherently wrong.
- Dumping full probability tables into the review unless they are necessary evidence.
- Overclaiming when the supplied rules are incomplete.

## Character Creation and Advancement Reviewer

Task:

Review character creation, player options, archetype support, and advancement as a design loop.

Focus on:

- Character creation sequence, prerequisites, derived values, option dependencies, examples, and onboarding.
- Whether choices are meaningful, legible, and mechanically supported.
- Archetype viability, trap options, dominant options, niche protection, party-role assumptions, and character concept support.
- Advancement pacing, rewards, growth incentives, power curve, retirement or endgame assumptions, and long-term play pressure.
- Whether the system supports the promised play experience through characters.

Output:

- Findings ordered by player-facing impact.
- For each finding: evidence reference, character-design issue, likely player impact, and fix.
- Note strong character-facing design elements to preserve.

Avoid:

- Treating every option as needing equal numerical power.
- Treating complexity as a flaw unless it harms the target audience or play experience.

## GM Procedure and Play-Support Reviewer

Task:

Review the GM-facing procedures and support tools.

Focus on:

- How to prepare and run sessions.
- Scene, encounter, challenge, NPC, faction, exploration, social, travel, downtime, reward, and campaign procedures.
- Guidance for adjudication, pacing, consequences, failure states, improvisation, and player agency.
- Whether the book gives tools rather than only advice.
- Safety tools, consent, tone calibration, and support for difficult content where relevant.
- Whether GM workload matches the game's promises and target audience.

Output:

- Findings ordered by GM workload and table impact.
- For each finding: evidence reference, missing or weak support, table impact, and fix.
- Note any GM tools that should be preserved.

Avoid:

- Assuming all games need traditional GM prep.
- Replacing explicit procedures with vague advice.

## Continuity and Contradiction Reader

Task:

Review the supplied core rulebook material for internal consistency, contradictions, missing links, and procedural breakage.

Focus on:

- Terms, definitions, examples, tables, stat blocks, cross-references, chapter summaries, and repeated rules.
- Character creation values that conflict with later rules.
- Advancement, equipment, conditions, powers, spells, enemies, and GM tools that use incompatible assumptions.
- Broken references, missing definitions, and chapter-to-chapter contradictions.
- Player-facing information that reveals GM-only material without purpose.

Output:

- Findings only, ordered by severity.
- For each finding: evidence reference, issue, table impact, and suggested fix.
- A short note on uncertainty caused by missing source context.

Avoid:

- Style critique unless it creates ambiguity.
- Broad rewrites.
- Inferring intent when the text does not support it.

## SRD Compatibility Reviewer

Task:

Review mechanical compatibility against the supplied or project-discovered SRD/reference rule-set.

This is not a legal or licence review.

Focus on:

- Terminology alignment, renamed terms, missing inherited assumptions, and changed meanings.
- Core resolution, character statistics, derived values, advancement, equipment, conditions, powers, monsters, enemies, NPC formats, and GM procedures that diverge from the reference rule-set.
- Stat assumptions, difficulty bands, scale, action economy, resource expectations, and encounter assumptions that may no longer match.
- Whether the core rulebook clearly states where it intentionally departs from the SRD.
- Compatibility confidence based on the available reference text.

Output:

- The reference rule-set or SRD used.
- Findings ordered by mechanical compatibility impact.
- For each finding: rulebook evidence, SRD/reference evidence, compatibility issue, table or implementation impact, and concrete fix.
- A short compatibility-confidence note.

Avoid:

- Legal or licence claims.
- Compliance claims where the relevant SRD text is absent.
- Treating every deliberate deviation as an error if the book explains and supports it.

## Teaching Path and Reference Usability Reader

Task:

Review whether the core rulebook teaches the game clearly and works as a reference after learning.

Focus on:

- First-read sequence, onboarding, examples, summaries, glossary, index, chapter order, and learning burden.
- Whether players and GMs can find procedures during play.
- Whether examples appear near the rules they explain.
- Whether important rules are buried, duplicated, or split across distant chapters.
- Whether tables, sidebars, callouts, headings, and summaries support scanning.
- Whether quick reference, character sheet, and GM aids match the book's procedures.

Output:

- Findings ordered by learning and reference impact.
- For each finding: evidence reference, usability issue, likely reader or table impact, and fix.
- Note strong teaching or reference choices to preserve.

Avoid:

- Copy-editing every sentence.
- Removing necessary precision for the sake of brevity.
- Treating your preferred rulebook structure as universal.

## Visual Flow and Layout Reviewer

Task:

Review supplied visual or layout material for hierarchy, flow, usability, accessibility, aesthetic fit, and support for learning and reference.

Use this pass for PDFs, page images, spreads, character sheets, maps, tables, diagrams, covers, cards, VTT assets, and other visual drafts. If the supplied artefact is text only, say the pass cannot be completed from the available material.

Focus on:

- Visual hierarchy and whether the eye moves through the book in a useful order.
- Relationship between headings, body text, examples, tables, sidebars, images, captions, diagrams, and whitespace.
- Whether character sheets, maps, diagrams, and reference pages can be used without extra explanation.
- Contrast, type size, line length, dense blocks, colour dependence, and accessibility risks.
- Whether art direction supports tone, genre, audience, and trust in the game.
- Whether visual emphasis matches table importance.

Output:

- Findings ordered by usability and presentation impact.
- For each finding: visual reference, issue, reading or table impact, and suggested fix.
- Note visual choices that are working well.

Avoid:

- Judging art only by personal taste.
- Making claims about pages or images you cannot see.
- Prioritising decorative appeal over learning and table function.

## Synthesis Prompt

Synthesise the independent review passes for the supplied core rulebook. Use a direct, evidence-led, neutral tone. Prioritise likely impact on the promised play experience, using both severity and design leverage. Separate confirmed defects, design risks, taste-sensitive judgements, playtest hypotheses, compatibility findings, and open questions. Preserve important disagreement, but do not include raw subagent transcripts unless requested.
