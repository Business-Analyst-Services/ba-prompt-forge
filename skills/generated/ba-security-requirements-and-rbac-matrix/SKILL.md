---
name: ba-security-requirements-and-rbac-matrix
description: Use when the user is working on security, privacy & compliance and needs security requirements, rbac/iam inputs. Draft the security requirements and role-based access matrix for the solution. Produces a reviewable first draft for security architects (review), engineers (build), business owners (role sign-off).
license: CC-BY-4.0
---

# Security Requirements & RBAC Matrix

Derived from `TB-05-D1` in the BA Prompt Forge library
(Technical BA / Security, Privacy & Compliance, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing security, privacy & compliance work and needs one of:
- Security requirements
- RBAC/IAM inputs

The audience for whatever you produce is: **Security architects (review), engineers (build), business owners (role sign-off)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE — INTERNAL, AGENTS, EXTERNAL USERS]`
3. `[LIST KEY FUNCTIONS]`
4. `[E.G. ENTRA ID SSO, MFA POLICY — OR 'TBD']`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Draft the security requirements and role-based access matrix for the solution. Draft requirements and matrix. Flag every place where the user's function list was too coarse to set permissions safely.

Format the output exactly as follows:

> Security requirements numbered by domain: identity and authentication (SSO, MFA, session rules); authorisation; data protection (encryption at rest/in transit, masking); auditability (who did what when, tamper resistance); vulnerability and patching expectations. RBAC matrix: role vs function with permission (none/view/create/update/approve); least-privilege justification per elevated permission; segregation-of-duties conflicts flagged (e.g. same role raising and approving).

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example SoD flag: "Conflict: 'Finance Officer' role can both create and approve a payee bank detail change — fraud risk. Recommendation: split into maintain-payee and approve-payee roles; approval requires different user; both actions audit-logged."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
