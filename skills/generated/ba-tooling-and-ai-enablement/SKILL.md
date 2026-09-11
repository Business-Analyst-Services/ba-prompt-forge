---
name: ba-tooling-and-ai-enablement
description: 'Use when the user is working on tooling & ai enablement and needs tool evaluations, tooling standards, ai adoption guidelines & guardrails. Evaluate and embed analysis tooling and AI-enabled ways of working across the practice: tool evaluations, tooling standards, and AI adoption guidelines with guardrails that keep use safe and consistent — including the practice prompt library and G. Produces a reviewable first draft for practice bas (guidelines), it/security (alignment), sponsor (investment).'
license: CC-BY-4.0
---

# Master – Tooling & AI Enablement

Derived from `PL-07-M` in the BA Prompt Forge library
(Practice Lead / Tooling & AI Enablement, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing tooling & ai enablement work and needs one of:
- Tool Evaluations
- Tooling Standards
- AI Adoption Guidelines & Guardrails

The audience for whatever you produce is: **Practice BAs (guidelines), IT/security (alignment), sponsor (investment)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[PRACTICE SIZE, MIX OF PERMANENT/CONTRACT, DELIVERY PORTFOLIO SHAPE]`
3. `[CURRENT TOOLS — e.g. Jira, Confluence, Copilot, modelling tools]`
4. `[WHAT'S APPROVED, WHAT'S BEING PILOTED]`
5. `[PRODUCTIVITY TARGETS, RISK CONCERNS]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- tool/AI capability evaluation (use cases served, evaluation criteria, trial design, cost model, recommendation)
- tooling standards (which tool for which job, data rules per tool)
- AI adoption guidelines (approved uses by task type, prohibited uses, data rules — de-identified inputs only, validation duty via Generate→Explain→Test, prompt library usage, quality scorecard for new prompts)
- adoption plan with capability building (training, champions, office hours) and success measures

Format the output exactly as follows:

> Structured, evidence-based business analysis writing aligned to BABOK good practice. Use clear headings, numbered requirements and tables where they aid scanning. Plain English; expand every acronym on first use; no marketing language. Tool evaluations against BA use cases from the L3 catalogue, not feature lists; AI guidelines pair every capability with its guardrail (approved uses / prohibited uses / validation duty); adoption measured by outcome (time saved, quality) not licence counts.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example approved-use pairing: "Approved: AI-drafting UAT scenarios from requirements. Guardrail: tester reviews every scenario against the requirement before use; coverage gaps remain the BA's accountability; synthetic test data only."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
