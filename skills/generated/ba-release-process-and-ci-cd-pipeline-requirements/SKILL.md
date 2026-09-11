---
name: ba-release-process-and-ci-cd-pipeline-requirements
description: Use when the user is working on environment access & devops enablement and needs release process definitions, pipeline requirements. Define release governance and CI/CD pipeline requirements that balance delivery speed with public-sector change control. Produces a reviewable first draft for devops engineers (implementation) and change governance (approval).
license: CC-BY-4.0
---

# Release Process & CI/CD Pipeline Requirements

Derived from `TB-01-D2` in the BA Prompt Forge library
(Technical BA / Environment Access & DevOps Enablement, scored 20/20
against the CARE + G.E.T. rubric).

## When to use this

The user is doing environment access & devops enablement work and needs one of:
- Release process definitions
- pipeline requirements

The audience for whatever you produce is: **DevOps engineers (implementation) and change governance (approval)**.

## Before you start

The user's work must respect the user's organisation's privacy, information-security and data-residency obligations. Everything the user pastes is de-identified or synthetic — if any input appears to contain real personal or sensitive data, stop and alert them before proceeding.

Collect these inputs from the user. Do not guess them:

1. `[PROJECT NAME AND ONE-LINE DESCRIPTION]`
2. `[E.G. FORTNIGHTLY / ON-DEMAND]`
3. `[CAB, CHANGE WINDOWS, SEGREGATION RULES]`
4. `[E.G. AZURE DEVOPS, GITHUB — OR 'TBD']`

Then ask up to 5 clarifying questions about anything still
missing, and **wait for the answers** before drafting.

## What to produce

- Define release governance and CI/CD pipeline requirements that balance delivery speed with public-sector change control. Draft both. Note where a requirement trades speed against control and offer the option.

Format the output exactly as follows:

> Release process: stages from commit to production; entry/exit criteria per stage; approval points and who approves; rollback triggers and expectations; emergency release path. Pipeline requirements: numbered, tool-agnostic ('The pipeline shall block deployment when critical vulnerabilities are detected'), covering build, automated testing gates, security scanning, artefact integrity, deployment automation, audit logging.

Keep the language professional, plain-English and appropriate for a business audience.

## Rules

- Do not invent facts or figures: mark anything you could not verify from the user's inputs as [TBC] and any value you propose yourself as [PROPOSED — VALIDATE].
- Treat the output as a first draft for the user's review, not a finished artefact.
- Do not ask the user to paste real personal or sensitive data.

## Worked example to imitate

Example pipeline requirement: "PL-06: The pipeline shall block promotion to UAT when critical or high vulnerabilities are detected in dependency scanning, with an auditable override requiring security approval. PL-09: Every production deployment shall be traceable to an approved change record."

## Before you hand it back

1. **Explain** - break down, step by step, the logic you used: how you interpreted
   each input and why you structured the output the way you did.
2. **Test** - list the sources you drew on (the user's inputs, earlier turns, or
   your own general knowledge; label which is which), cross-reference the key facts
   against them, flag anything that does not trace back to a source, and list every
   assumption you made so the user can verify or correct it.
