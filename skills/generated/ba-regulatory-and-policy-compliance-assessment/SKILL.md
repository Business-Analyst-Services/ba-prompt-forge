---
name: ba-regulatory-and-policy-compliance-assessment
description: Use when the user is working on solution analysis & design support and needs regulatory & policy compliance assessments, business rules. Assess the solution against each obligation and derive the business rules and requirements needed for compliance. Produces a reviewable first draft for design team (remediation), legal/privacy advisors (confirmation), governance (assurance).
license: CC-BY-4.0
---

# Regulatory & Policy Compliance Assessment

Derived from `BT-07-D2` in the BA Prompt Forge library
(Business/Tech BA / Solution Analysis & Design Support, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing solution analysis & design support work and needs one of:
- Regulatory & Policy Compliance Assessments
- Business Rules

The audience for whatever you produce is: **Design team (remediation), legal/privacy advisors (confirmation), governance (assurance)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE WHAT THE SOLUTION DOES, DATA IT TOUCHES]`
3. `[LIST — e.g. privacy legislation, legislation covering health or other sensitive information, information security standards, sector regulation, records legislation]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Assess the solution against each obligation and derive the business rules and requirements needed for compliance. Draft the assessment and rules. Mark every interpretation that needs legal/privacy confirmation.

Format the output exactly as follows:

> Assessment table: obligation (with clause/standard reference where I supply it); requirement it creates; current/proposed solution behaviour; compliant / gap / unclear; remediation requirement. Then derived business rules, categorised. Do not give legal advice — frame findings as analysis for legal/privacy team confirmation.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example compliance row: "Obligation: the security principle in our applicable privacy legislation — reasonable security of personal information | Requirement created: role-based access to case documents with audit logging | Proposed behaviour: all users can open any case document | Finding: GAP | Remediation: restrict document access to assigned officers + audit trail [LEGAL/PRIVACY TO CONFIRM interpretation]."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
