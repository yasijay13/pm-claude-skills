---
name: feature-request-triage
description: >
  Triage inbound feature requests before they become roadmap items. Use this skill whenever the task involves evaluating a feature request, a customer ask, or a list of requests — phrases like "customers want X," "we got a request for," "should we build," "triage these FRs," or when a request is pasted for assessment. Also use when summarising feature request themes for a roadmap discussion or a weekly report. The skill applies whether the request comes from a customer call, a support ticket, a sales deal, or an internal stakeholder.
---

# Feature Request Triage

A feature request is a proposed solution, not a problem statement. The job of triage is to recover the problem before anyone commits to the solution.

---

## Before triaging, answer these

- Who asked, in what words? (verbatim if available)
- What were they trying to do when they hit this?
- How many distinct customers or users have raised this, over what period?
- What happens to them today without it — workaround, abandonment, or nothing?

If the record can't answer these, the output of triage is the list of questions to ask, not a guess dressed up as an assessment.

---

## Core rules

1. **Separate the ask from the outcome.** "We want bulk export" is an ask. "Finance re-keys 400 rows into their ERP every month-end" is an outcome gap. Triage is not done until the outcome is stated in the customer's terms, or explicitly marked unknown.
2. **One loud customer is not a pattern.** Record who asked and how often. Weight by breadth (distinct accounts), frequency (repeat mentions), and stakes (revenue, churn risk, seniority of the person asking) — in that order. Never let volume of noise from one account substitute for breadth.
3. **Never invent the outcome.** If the source material doesn't say why the customer wants it, say so. "Assumed outcome:" is an acceptable label; an unlabelled guess is not.
4. **Distinguish gap from symptom.** Many requests are workarounds for something else that's broken. Ask what the request would let the customer stop doing. If the answer points at an existing broken flow, the request is a symptom — triage the underlying flow instead.
5. **A request can be valid and still declined.** Fit with product direction is a separate judgement from whether the pain is real. Keep the two assessments visibly separate so a "no" doesn't require pretending the pain isn't real.

---

## Classify every request as one of

| Class | Meaning | Typical next step |
|---|---|---|
| Outcome gap | A real job the product can't do | Size it, find more evidence |
| Workaround symptom | Papering over a broken existing flow | Fix or investigate the flow |
| Preference | Works today, they'd like it differently | Log, watch for pattern |
| Parity ask | "Competitor X has it" with no stated job | Recover the underlying job first |
| One-off customisation | Real need, one account, low generality | Solve outside the roadmap or decline |

---

## Output format

For each triaged request:

- **Request (as received):** the ask in the requester's words
- **Underlying outcome:** stated, or "ASSUMED:" with reasoning, or "UNKNOWN — ask [who]: [question]"
- **Evidence:** who, how many accounts, over what period, stakes
- **Class:** one of the five above
- **Recommendation:** build / investigate / watch / decline — with a one-line reason
- **Open questions:** max three, each naming who to ask

---

## Rewrite patterns

| Instead of | Write |
|---|---|
| "Multiple customers want an API." | "3 accounts (2 enterprise) asked in the last quarter; all three are exporting CSVs weekly to sync data into their own systems." |
| "Customer requested dark mode — low priority." | "One account, one mention, no stated job. Class: preference. Watch." |
| "This would improve the user experience." | "This removes the double data entry the ops team does at every month-end close." |
| "Competitor has this feature so we should too." | "Parity ask. The job behind it is unstated — ask the prospect what they'd use it for before sizing." |

---

## Final check

- Is every stated outcome traceable to something a customer actually said?
- Is every assumption labelled as one?
- Could a reader tell the difference between "widely felt" and "loudly felt"?
- Does every "decline" acknowledge the pain honestly rather than minimising it?
