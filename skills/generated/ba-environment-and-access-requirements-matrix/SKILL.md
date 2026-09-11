---
name: ba-environment-and-access-requirements-matrix
description: Use when the user is working on environment access & devops enablement and needs environment requirements, access requirements. Define the environment set and the role-based access matrix with approval and audit requirements. Produces a reviewable first draft for platform engineers and security reviewers.
license: CC-BY-4.0
---

# Environment & Access Requirements Matrix

Derived from `TB-01-D1` in the BA Prompt Forge library
(Technical BA / Environment Access & DevOps Enablement, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing environment access & devops enablement work and needs one of:
- Environment requirements
- access requirements

The audience for whatever you produce is: **Platform engineers and security reviewers**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[LIST OR 'PROPOSE STANDARD SET']`
3. `[LIST — INCLUDE VENDORS/CONTRACTORS]`
4. `[WHAT DATA APPEARS IN WHICH ENVIRONMENT]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Define the environment set and the role-based access matrix with approval and audit requirements. Draft both tables. Flag risky patterns explicitly (shared accounts, vendor admin access, prod data in test).

Format the output exactly as follows:

> Environment table: name; purpose; test types supported; data class permitted (flag: no unmasked personal/health data outside production); refresh cadence; prod-likeness. Access matrix: role vs environment with permission level (none/read/deploy/admin); justification; approval required; review cadence; segregation-of-duties conflicts flagged.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example environment row: "SIT | Purpose: system integration testing | Test types: interface, regression | Data: masked production subset (no unmasked personal or sensitive data) | Refresh: monthly | Prod-likeness: same integrations, 50% capacity."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
