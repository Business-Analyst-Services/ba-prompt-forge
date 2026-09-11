---
name: ba-privacy-impact-assessment-pia-input-pack
description: Use when the user is working on security, privacy & compliance and needs privacy assessments, information classification assessments. Assemble the structured inputs a privacy officer needs to complete a PIA efficiently. Produces a reviewable first draft for privacy officer (assessment), project (remediation planning).
license: CC-BY-4.0
---

# Privacy Impact Assessment (PIA) Input Pack

Derived from `TB-05-D2` in the BA Prompt Forge library
(Technical BA / Security, Privacy & Compliance, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing security, privacy & compliance work and needs one of:
- Privacy assessments
- information classification assessments

The audience for whatever you produce is: **Privacy officer (assessment), project (remediation planning)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE WHAT PERSONAL/HEALTH INFORMATION IS COLLECTED, USED, STORED, DISCLOSED]`
3. `[PASTE OR 'NONE']`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Assemble the structured inputs a privacy officer needs to complete a PIA efficiently. Draft the pack. List the questions only the privacy officer or legal can answer, separately from factual gaps I can close.

Format the output exactly as follows:

> Sections: data inventory (element, classification incl. health information flag, source, purpose); data flow narrative (collection → use → storage → disclosure → disposal) with a Mermaid data-flow diagram; purposes and legal basis as understood (marked for privacy officer confirmation); retention and disposal; disclosures and third parties (including cloud/vendor access, offshore support); individual rights handling (access, correction); risks identified with proposed mitigations.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example inventory row: "Element: professional assessment report | Classification: sensitive personal information | Source: third-party professional, supplied by the individual | Purpose: eligibility assessment for payments | Storage: case management system, contracted region | Disclosure: authorised delivery partners; other parties see a summary only | Retention: [RECORDS SCHEDULE REF] | Risk: the full report is visible to all parties in the current design — proposed mitigation: summary-only view."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
