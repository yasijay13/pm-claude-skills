---
name: metric-definition-checker
description: >
  Validate any metric before it goes into an external or high-stakes document. Use this skill whenever a number is being claimed — adoption percentages, growth figures, "X% of customers," ARR/MRR figures, time savings, NPS — in a CV, investor material, board deck, case study, sales collateral, blog post, or press-facing text. Trigger on phrases like "check these metrics," "is this number defensible," or whenever drafting content that contains a statistic. Also use to build or maintain a metric evidence bank.
---

# Metric Definition Checker

A metric without a definition is an anecdote with a percent sign. Before any number leaves the building, it must survive five questions.

---

## The five required fields

Every externally used metric needs all five. A missing field means the metric is not usable yet — the output is the question that fills the gap, not a softened version of the claim.

1. **Definition** — what exactly counts? "Adoption" must name the action: activated the feature once? used it in the last 30 days? configured and running?
2. **Denominator** — percentage of what? All customers, active customers, customers on the plan that includes the feature, seats, accounts?
3. **Time window** — as of when, measured over what period? A point-in-time snapshot and a trailing average are different claims.
4. **Source** — where does the number come from, and could you re-derive it? Analytics query, CRM report, finance system, someone's slide?
5. **Last verified** — when did you last check it was still true? Numbers rot.

---

## Confidence labels

Attach one to every metric:

- **MEASURED** — you can re-run the query and get the number.
- **REPORTED** — someone else measured it; you're relaying. Name who.
- **ESTIMATE** — derived or extrapolated. State the method in one line.

Never present a REPORTED or ESTIMATE figure with MEASURED confidence. "Reported adoption reached 70%" and "adoption is 70%" are different claims — the first survives due diligence, the second might not.

---

## Core rules

1. **Percentages travel with their base.** "85% of customers" needs the n. 85% of 40 and 85% of 4,000 are different facts wearing the same clothes.
2. **Compound claims need both parts defined.** "70% increase in enterprise AI adoption" needs a definition of "enterprise," of "adoption," and of the baseline the increase is measured against.
3. **Targets are not results.** A programme carrying a $100M target did not generate $100M. Say "target," and past-tense verbs stay away from future numbers.
4. **Round honestly.** 68% is not "70%+". "~70%" and "70%+" are different claims — pick the one the data supports.
5. **Causation needs its own evidence.** "Adoption rose 70% after the release" is a sequence. "Because of the release" is a causal claim that needs more than a calendar. When in doubt, write "following," not "driven by."
6. **If a field is unknown, the metric waits.** The correct output is "unusable until we confirm the denominator — ask [who/where]," not a hedged version of the same claim.

---

## Worked example

Claim as drafted: **"85% adoption of our automation engine."**

| Field | Status |
|---|---|
| Definition | Missing — adopted = ran at least one automation? has one configured? |
| Denominator | Missing — all customers, or customers on plans that include it? |
| Time window | Missing — as of when? |
| Source | Missing — product analytics? which query? |
| Last verified | Missing |

Usable version after checking: "85% of active customers (n=~120) had at least one automation running in the 90 days to March — MEASURED, product analytics, verified March 28."

---

## Final check

- Does every number in the document have all five fields answered somewhere you can point to?
- Is every label (MEASURED / REPORTED / ESTIMATE) honest?
- Could you defend each number in a due-diligence meeting without looking anything up?
- If a journalist quoted the number stripped of context, would it still be true?
