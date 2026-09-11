---
name: ba-environment-access-and-devops-enablement
description: Use when the user is working on environment access & devops enablement and needs environment requirements, deployment requirements, access requirements, release process definitions. Define the requirements for environments, access, deployment and release processes and CI/CD enablement — answering who can access which environment, how the solution is deployed, and how releases are governed. Produces a reviewable first draft for platform/devops engineers (build), security (approval), delivery teams (consumers).
license: CC-BY-4.0
---

# Master – Environment Access & DevOps Enablement

Derived from `TB-01-M` in the BA Prompt Forge library
(Technical BA / Environment Access & DevOps Enablement, scored 19/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing environment access & devops enablement work and needs one of:
- Environment requirements
- deployment requirements
- access requirements
- release process definitions
- pipeline requirements

The audience for whatever you produce is: **Platform/DevOps engineers (build), security (approval), delivery teams (consumers)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[DESCRIBE]`
3. `[DEV, TEST, VENDOR, SUPPORT]`
4. `[DESCRIBE OR 'UNKNOWN']`
5. `[CHANGE FREEZE WINDOWS, CAB REQUIREMENTS]`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- environment requirements (environment, purpose, users, data class allowed — e.g. masked only outside prod, prod-likeness, availability window)
- access matrix (role vs environment vs permission level, with approval workflow and audit needs)
- deployment and runtime topology requirements
- release process definition (stages, entry/exit criteria, approvals, rollback expectations)
- CI/CD pipeline requirements (build, test gates, security scanning, deployment automation)

Format the output exactly as follows:

> Structured technical-BA writing: requirements numbered and testable, expressed as needs and constraints rather than design decisions (pre-solution) or as precise specifications (post-solution). Tables over prose where possible; expand acronyms on first use. Access requirements honour least privilege and segregation of duties; release requirements distinguish governance needs from tooling implementation.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example access row: "Role: Vendor developer | DEV: deploy | SIT: read | UAT: none | PROD: none | Justification: build responsibilities only | Approval: platform owner + security | Review: quarterly. Flag: vendor requested UAT deploy — segregation conflict with test independence, escalated."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
