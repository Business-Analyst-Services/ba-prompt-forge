---
name: ba-ai-adoption-guidelines-and-guardrails-practice
description: 'Use when the user is working on tooling & ai enablement and needs tooling standards, ai adoption guidelines & guardrails. Draft the practice''s AI adoption guidelines: what BAs may use AI for, what they must never do, and the validation discipline that makes outputs trustworthy. Produces a reviewable first draft for all practice bas.'
license: CC-BY-4.0
---

# AI Adoption Guidelines & Guardrails (Practice)

Derived from `PL-07-D2` in the BA Prompt Forge library
(Practice Lead / Tooling & AI Enablement, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing tooling & ai enablement work and needs one of:
- Tooling Standards
- AI Adoption Guidelines & Guardrails

The audience for whatever you produce is: **All practice BAs; endorsed by security/privacy and the sponsor**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PRACTICE SIZE, MIX OF PERMANENT/CONTRACT, DELIVERY PORTFOLIO SHAPE]`
3. `[LIST]`
4. `[PASTE OR REFERENCE]`
5. `[ANY]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Draft the practice's AI adoption guidelines: what BAs may use AI for, what they must never do, and the validation discipline that makes outputs trustworthy. Draft the guidelines. Where the user's organisational policy is stricter than these defaults, follow the policy and note it; where it is silent, mark the gap for the policy owner.

Format the output exactly as follows:

> Guidelines: approved uses by task type (drafting, summarising, analysis support, test scenario generation — each with its guardrail); prohibited uses (decisions about individuals, unreviewed outputs into governance artefacts, real personal or sensitive data as input — de-identified or synthetic only); the validation duty (Generate→Explain→Test on every substantive output, human accountable always); prompt quality expectations (use the practice prompt library; new prompts scored on the 10-criterion scorecard before sharing); transparency rule (when to disclose AI assistance); escalation path for uncertainty. Aligned to the user's pasted policy with conflicts flagged for resolution.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example prohibited-use line: "Prohibited: entering real customer, employee or other identifying information, or sensitive personal information, into any AI tool — approved or not. Use de-identified or synthetic data. No AI-generated content enters a governance artefact without named-human review recorded."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
